import os
import re
import csv
import datetime
from typing import Dict, List, Optional, Tuple

# Expresiones regulares precompiladas para eficiencia.

# Patrón 1: El formato más completo y esperado.
# Hace la 's' de 'Nodes' opcional para aceptar 'Node' y 'Nodes'.
PATH_REGEX_FULL = re.compile(
    r"nb(?P<NB>\d+)_n(?P<N>\d+)/"
    r"P(?P<P>\d+)_Q(?P<Q>\d+)_"
    r"Nodes?(?P<Nodes>\d+)_"  # 's' es opcional
    r"Ntask(?P<Tasks>\d+)"
)

# Patrón 2: Un formato más simple observado en los logs de error.
# Extrae N, NB y Nodes, pero P, Q y Tasks no están presentes.
PATH_REGEX_SIMPLE = re.compile(
    r"nb(?P<NB>\d+)_n(?P<N>\d+)/"
    r".*_(?P<Nodes>\d+)nodos"
)

# Extrae el Nro de Job del nombre del archivo (e.g., hpl_1668.out -> 1668)
JOB_ID_REGEX = re.compile(r"hpl_(\d+)\.out")

# Extrae la línea de resultados de HPL, que usualmente comienza con 'WR'
# Captura los dos últimos valores numéricos: Tiempo y Gflops.
HPL_RESULT_REGEX = re.compile(
    r"^WR\w+\s+\d+\s+\d+\s+\d+\s+\d+\s+([\d.eE+-]+)\s+([\d.eE+-]+)$"
)


def seconds_to_human_readable(seconds: float) -> str:
    """
    Convierte un tiempo en segundos a un formato HH:MM:SS.micros.

    Args:
        seconds: El número de segundos a convertir.

    Returns:
        Una cadena de texto con el tiempo en formato legible.
    """
    return str(datetime.timedelta(seconds=seconds))


def parse_hpl_output(file_path: str) -> Optional[Dict[str, any]]:
    """
    Analiza un único archivo de salida HPL y extrae todos los datos relevantes.

    Combina la información de la ruta del archivo con el contenido del mismo.

    Args:
        file_path: La ruta completa al archivo hpl_*.out.

    Returns:
        Un diccionario con los datos extraídos o None si no se pudo procesar.
    """
    # Intenta primero con el patrón más específico y completo.
    path_match = PATH_REGEX_FULL.search(file_path)
    if not path_match:
        # Si falla, intenta con el patrón más simple.
        path_match = PATH_REGEX_SIMPLE.search(file_path)

    if not path_match:
        print(f"ADVERTENCIA: La estructura de la ruta no coincide con ningún patrón conocido: {file_path}")
        return None

    data = path_match.groupdict()
    # Aseguramos que los campos opcionales existan para evitar errores.
    data.setdefault("P", "N/A")
    data.setdefault("Q", "N/A")
    data.setdefault("Tasks", "N/A")

    filename = os.path.basename(file_path)
    job_id_match = JOB_ID_REGEX.match(filename)
    data["Nro Job"] = job_id_match.group(1) if job_id_match else "N/A"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                result_match = HPL_RESULT_REGEX.search(line)
                if result_match:
                    time_str, gflops_str = result_match.groups()
                    time_val = float(time_str)
                    data["Time"] = time_val
                    data["Time Humanamente legible"] = seconds_to_human_readable(time_val)
                    data["Gflops"] = float(gflops_str)
                    # Renombramos 'Tasks' a como lo pide el CSV
                    data["Task per Node"] = data.pop("Tasks")
                    return data
    except (IOError, ValueError) as e:
        print(f"ERROR: No se pudo leer o procesar el archivo {file_path}: {e}")

    return None


def find_and_process_files(root_dir: str) -> List[Dict[str, any]]:
    """
    Busca recursivamente archivos hpl_*.out en un directorio y los procesa.

    Args:
        root_dir: El directorio raíz desde donde empezar la búsqueda.

    Returns:
        Una lista de diccionarios, donde cada uno representa una fila del futuro CSV.
    """
    results = []
    print(f"Iniciando búsqueda de archivos en: {os.path.abspath(root_dir)}")
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if JOB_ID_REGEX.match(filename):
                full_path = os.path.join(dirpath, filename)
                print(f"  -> Procesando: {full_path}")
                parsed_data = parse_hpl_output(full_path)
                if parsed_data:
                    results.append(parsed_data)
    return results


def write_to_csv(data: List[Dict[str, any]], output_filename: str = "hpl_summary.csv"):
    """
    Escribe los datos extraídos en un archivo CSV.

    Args:
        data: La lista de diccionarios con los datos.
        output_filename: El nombre del archivo CSV de salida.
    """
    if not data:
        print("No se encontraron datos para escribir en el CSV.")
        return

    # Aseguramos el orden de las columnas según lo solicitado.
    headers = [
        "Nro Job", "N", "NB", "P", "Q", "Nodes", "Task per Node",
        "Time", "Time Humanamente legible", "Gflops"
    ]

    try:
        with open(output_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=';')
            writer.writeheader()
            for row in data:
                # Convertir valores numéricos a string y reemplazar '.' por ','
                processed_row = {
                    k: str(v).replace('.', ',') if isinstance(v, (float, int)) else v
                    for k, v in row.items()
                }
                writer.writerow(processed_row)
        print(f"\n¡Éxito! Se ha generado el archivo '{output_filename}' con {len(data)} registros.")
    except IOError as e:
        print(f"ERROR: No se pudo escribir el archivo CSV: {e}")


def main():
    """
    Función principal que orquesta la búsqueda, procesamiento y escritura.
    """
    # El script buscará en el directorio 'CACIC_2025' relativo a su ubicación.
    # Puedes cambiarlo a '.' para que busque desde donde se ejecuta.
    target_directory = "CACIC_2025"
    if not os.path.isdir(target_directory):
        print(f"ERROR: El directorio '{target_directory}' no existe. Buscando en el directorio actual ('.').")
        target_directory = "."
        
    processed_data = find_and_process_files(target_directory)
    write_to_csv(processed_data)


if __name__ == "__main__":
    main()