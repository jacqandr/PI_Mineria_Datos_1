import streamlit as st

st.set_page_config(
    page_title="Conclusiones",
    page_icon="🏁"
)

st.title("🏁 Conclusiones")

st.write("""
En esta sección se presentan las principales conclusiones obtenidas durante el desarrollo del proyecto, resumiendo los resultados del análisis exploratorio, la preparación de los datos y la aplicación del Análisis de Componentes Principales (PCA).
""")

st.markdown("---")

st.header("📌 Calidad del conjunto de datos")

st.success("""
Durante la etapa de preparación se mejoró la calidad del conjunto de datos mediante diversas tareas de limpieza y validación.

Las principales acciones realizadas fueron:

- Eliminación de registros duplicados.
- Tratamiento de valores faltantes.
- Normalización de categorías.
- Corrección de edades fuera del rango esperado.
- Validación y conversión de fechas.
- Tratamiento de valores extremos mediante winsorización.

Estas transformaciones permitieron obtener un conjunto de datos consistente y adecuado para el análisis.
""")

st.markdown("---")

st.header("📊 Principales resultados del análisis exploratorio")

st.info("""
El análisis exploratorio permitió responder las preguntas planteadas al inicio del proyecto.

Los principales hallazgos fueron:

- El plan **Básico** fue el más utilizado.
- La mayor parte del tiempo de visualización se concentró entre **500 y 1000 minutos**.
- Los usuarios del plan **Premium** presentaron un mayor tiempo de visualización.
- No se observó una relación lineal clara entre la edad y el tiempo de visualización.
- Las variables numéricas mostraron correlaciones débiles entre sí.
""")

st.markdown("---")

st.header("📉 Principales resultados del PCA")

st.info("""
La aplicación del Análisis de Componentes Principales permitió reducir la dimensionalidad del conjunto de datos y facilitar su representación gráfica.

Se observó que:

- La primera componente principal explicó aproximadamente el **33,8 %** de la variabilidad.
- Las dos primeras componentes principales conservaron cerca del **66,9 %** de la información.
- No se identificaron agrupamientos claramente diferenciados.
- El Análisis de Componentes Principales (PCA) fue útil como técnica de exploración y visualización, aunque la baja correlación entre las variables limitó una reducción más significativa de la dimensionalidad.""")

st.markdown("---")

st.header("💡 Reflexión final")

st.write("""
Este proyecto permitió aplicar de forma práctica las principales etapas del proceso de minería de datos, desde la inspección inicial hasta el análisis exploratorio y la reducción de dimensionalidad mediante PCA.

La experiencia evidenció la importancia de una adecuada preparación de los datos antes de realizar cualquier análisis estadístico, así como el valor de las técnicas de visualización para interpretar los resultados obtenidos.
""")

st.markdown("---")

st.header("🚀 Trabajo futuro")

st.write("""
Como posibles líneas de trabajo futuro se propone:

- Incorporar nuevas variables relacionadas con el comportamiento de los usuarios.
- Aplicar técnicas de clustering para identificar perfiles de usuarios.
- Implementar modelos predictivos utilizando algoritmos de aprendizaje automático.
- Ampliar el análisis incorporando nuevos conjuntos de datos y variables relacionadas con el comportamiento de los usuarios.
""")
