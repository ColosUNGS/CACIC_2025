# Análisis de rendimiento y eficiencia energética en el clúster Raspberry Pi Cronos
Este repositorio acompaña al artículo presentado en CACIC 2025. Contiene el material experimental, scripts, gráficos y documentación complementaria al trabajo.

## 📂 Contenido
- [`3.2 - Medición Energética`](3.2_Medición_Energética/README.md): Cálculo detallado de eficiencia energética a partir de datos reales.
- `hpl.dat`: Archivo de configuración usado en las pruebas de HPL Linpack.
- `sbatch_hpl.sh`: Script utilizado para lanzar HPL con Slurm.
- `resultados_hpl.xlsx`: Tabla con los principales resultados de rendimiento.
- `corriente_durante_ejecucion.xlsx`: Datos medidos con pinza amperimétrica.
- `src/`: Carpeta con código fuente usado en la fase de desarrollo (aplicaciones paralelas, ejercicios educativos).

## 🧪 Requisitos
- Raspbian con Slurm, OpenMPI, y HPL instalado.
- El entorno fue ejecutado en 6 nodos Raspberry Pi 4.

## 🔁 Reproducibilidad
Se proveen los archivos necesarios para reproducir la ejecución de HPL Linpack y las condiciones de medición energética.

## 📄 Cita sugerida
Vargas, M. et al. (2025). Análisis de rendimiento y eficiencia energética en el clúster Raspberry Pi Cronos. CACIC 2025.



