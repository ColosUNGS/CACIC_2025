# Análisis de rendimiento y eficiencia energética en el clúster Raspberry Pi Cronos
Este repositorio acompaña al artículo presentado en CACIC 2025. Contiene el material experimental, scripts, gráficos y documentación complementaria al trabajo.

## 📂 Contenido
- [**Análisis de rendimiento y eficiencia energética en el clúster Raspberry Pi Cronos** (PDF)](Análisis_de_rendimiento_y_eficiencia_energética_en_el_clúster_Raspberry_Pi_Cronos.pdf): Informe principal del proyecto, con metodología, resultados y conclusiones.

- [**3_HPL_Linpack**](3_HPL_Linpack/README.md): Ejecución y análisis de pruebas HPL Linpack sobre el clúster. Incluye scripts, configuraciones (`HPL.dat`), resultados de rendimiento y gráficos.
  _Ver [README de la carpeta](3_HPL_Linpack/README.md) para detalles de cada experimento y archivos generados._

- [**3.2_Medición_Energética**](3.2_Medición_Energética/README.md): Medición y análisis del consumo energético durante la ejecución de HPL.
  _Incluye datos crudos, gráficos y explicación de la metodología de medición. Ver [README de la carpeta](3.2_Medición_Energética/README.md)._

- [**4_Calculo_Pi_en_paralelo**](4_Calculo_Pi_en_paralelo/README.md): Experimentos de cálculo de Pi usando paralelismo (MPI y hibrido).
  _Contiene código fuente, scripts de ejecución, resultados y análisis de eficiencia. Ver [README de la carpeta](4_Calculo_Pi_en_paralelo/README.md)._

## 🧪 Requisitos
- Raspbian con Slurm, OpenMPI, y HPL instalado.
- El entorno fue ejecutado en 6 nodos Raspberry Pi 4.

## 🔁 Reproducibilidad
Se proveen los archivos necesarios para reproducir la ejecución de HPL Linpack y las condiciones de medición energética.

## 📄 Cita sugerida
Vargas, M. et al. (2025). Análisis de rendimiento y eficiencia energética en el clúster Raspberry Pi Cronos. CACIC 2025.



