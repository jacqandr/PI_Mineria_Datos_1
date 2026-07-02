import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# Encabezado
# ==========================================

st.title("📊 Proyecto Integrador - Minería de Datos I")

st.subheader(
    "Análisis Exploratorio de Datos y Reducción de Dimensionalidad mediante PCA"
)

st.markdown("---")

# ==========================================
# Presentación
# ==========================================

st.header("📌 Presentación")

st.write("""
Bienvenido a la aplicación desarrollada para el **Proyecto Integrador de la asignatura Minería de Datos I**.

En este trabajo se realizó un proceso completo de análisis sobre un conjunto de datos de usuarios de una plataforma de streaming, aplicando técnicas de inspección inicial, limpieza y preparación de datos, análisis exploratorio (EDA) y reducción de dimensionalidad mediante Análisis de Componentes Principales (PCA).

La aplicación resume los principales resultados obtenidos durante cada etapa del proyecto de forma clara e interactiva.
""")

st.markdown("---")

st.header("🎯 Objetivo del proyecto")

st.write("""
Analizar un conjunto de datos de usuarios de una plataforma de streaming mediante técnicas de inspección inicial, preparación de datos, análisis exploratorio y reducción de dimensionalidad, con el propósito de obtener información relevante y desarrollar un proceso reproducible de minería de datos.
""")

st.markdown("---")

st.header("🛠️ Etapas desarrolladas")

st.success("✔ Inspección inicial del dataset")

st.success("✔ Limpieza y preparación de datos")

st.success("✔ Análisis Exploratorio (EDA)")

st.success("✔ Reducción de dimensionalidad mediante PCA")

st.success("✔ Elaboración de conclusiones")

st.markdown("---")

st.header("👤 Información del proyecto")

col1, col2 = st.columns(2)

with col1:
    st.write("**Autor**")
    st.write("Lourdes Jacqueline Andrada")

    st.write("**Asignatura**")
    st.write("Minería de Datos I")

with col2:
    st.write("**Fecha**")
    st.write("Julio 2026")

    st.write("**Repositorio GitHub**")
    st.write("Se agregará al publicar el proyecto.")