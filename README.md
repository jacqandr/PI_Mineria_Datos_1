# Proyecto Integrador - Minería de Datos I

## Análisis Exploratorio y Reducción de Dimensionalidad de un Dataset de Usuarios de una Plataforma de Streaming

## Información general

Este proyecto fue desarrollado como parte de la asignatura **Minería de Datos I**.
El proyecto consiste en realizar un análisis reproducible sobre un conjunto de datos de usuarios de una plataforma de streaming, siguiendo las etapas propuestas por la cátedra: inspección inicial, preparación y limpieza de datos, análisis exploratorio (EDA), reducción de dimensionalidad mediante Análisis de Componentes Principales (PCA) y comunicación de resultados.
Todas las decisiones adoptadas durante el proyecto fueron documentadas y justificadas con base en la evidencia obtenida durante el análisis.

## Objetivo del proyecto

El objetivo del proyecto es analizar un conjunto de datos de usuarios de una plataforma de streaming para comprender sus características, mejorar la calidad de la información mediante un proceso de limpieza documentado y explorar relaciones entre las variables. Además, se aplica el Análisis de Componentes Principales (PCA) para evaluar la posibilidad de reducir la dimensionalidad del conjunto de datos, garantizando un proceso reproducible y correctamente documentado.

## Dataset

El conjunto de datos corresponde a usuarios de una plataforma de streaming e incluye información demográfica, hábitos de visualización, tipo de suscripción, género favorito, país de residencia, actividad reciente y cantidad de tickets de soporte.
El dataset original fue proporcionado en formato JSON por la cátedra y se conservó sin modificaciones en la carpeta `data/raw`. Durante el proceso de preparación se generó un dataset procesado, almacenado en `data/processed`, que fue utilizado para el análisis exploratorio y la aplicación del PCA.
El conjunto de datos contiene variables numéricas, categóricas y temporales, lo que permitió realizar distintos análisis y aplicar técnicas de preparación y reducción de dimensionalidad.

## Estructura del repositorio

```text
PI_Mineria_Datos_1
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
├── notebooks/
├── reports/
├── README.md
└── requirements.txt
```

## Preparación y calidad de los datos

El proceso de preparación comenzó con una inspección del dataset para identificar registros duplicados, valores faltantes, inconsistencias en variables categóricas, fechas inválidas, edades fuera del rango esperado y valores extremos.
Las acciones de limpieza fueron aplicadas únicamente cuando existía evidencia que justificara la decisión. Entre ellas se incluyeron la eliminación de registros duplicados, la imputación de valores faltantes, la normalización de categorías equivalentes, la validación de fechas, la corrección de edades inconsistentes y el tratamiento de valores extremos mediante winsorización cuando fue necesario.
Todas las transformaciones realizadas fueron registradas en el archivo `logs/pipeline_log.csv`, permitiendo mantener la trazabilidad y la reproducibilidad del proceso.

## Resumen del análisis exploratorio

El análisis exploratorio se desarrolló mediante visualizaciones univariadas, bivariadas y multivariadas con el objetivo de responder preguntas definidas durante la inspección inicial.
Se observó que el plan **Básico** es el más utilizado por los usuarios y que la mayor parte del tiempo mensual de visualización se concentra entre aproximadamente **500 y 1000 minutos**. Además, los usuarios con plan **Premium** presentan, en general, un mayor tiempo de visualización.
También se analizó la relación entre la edad y el tiempo de visualización, sin evidenciar una relación lineal clara. Finalmente, la matriz de correlación mostró asociaciones débiles entre las variables numéricas analizadas.

## Reducción de dimensionalidad

Se aplicó el Análisis de Componentes Principales (PCA) sobre las variables numéricas previamente escaladas mediante `StandardScaler`.
Los resultados mostraron que la varianza se distribuye de manera relativamente uniforme entre las tres componentes principales, por lo que fue necesario conservarlas para representar la totalidad de la información.
Este comportamiento es consistente con las bajas correlaciones observadas durante el análisis exploratorio y evidencia que la reducción de dimensionalidad resulta limitada para este conjunto de datos.

## Visualización interactiva

El proyecto incluye una aplicación desarrollada con **Streamlit**, diseñada para presentar de forma interactiva los principales resultados obtenidos durante el análisis. La aplicación permite explorar el dataset, visualizar los resultados del análisis exploratorio, interpretar el Análisis de Componentes Principales (PCA) y consultar las conclusiones del proyecto mediante una interfaz orientada a usuarios no técnicos.

**Aplicación en Streamlit Cloud:** https://pimineriadatos1-fukp7mrgj4aki72zap3skp.streamlit.app/


## Cómo ejecutar localmente

1. Clonar el repositorio:

```bash
git clone <https://github.com/jacqandr/PI_Mineria_Datos_1>
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
streamlit run app/Home.py
```

## Conclusiones

El proyecto permitió aplicar las principales etapas del proceso de minería de datos, desde la inspección inicial hasta la reducción de dimensionalidad mediante PCA. Las decisiones de limpieza fueron justificadas mediante evidencia observada en el conjunto de datos y documentadas durante todo el proceso. Los resultados obtenidos permitieron comprender el comportamiento general del dataset, identificar relaciones entre las variables y evaluar el comportamiento de las componentes principales dentro del conjunto de datos, garantizando un proyecto reproducible y correctamente documentado.

## Enlaces

Repositorio GitHub: https://github.com/jacqandr/PI_Mineria_Datos_1

Aplicación Streamlit: https://pimineriadatos1-fukp7mrgj4aki72zap3skp.streamlit.app/