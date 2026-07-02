import streamlit as st
import pandas as pd

# ==========================================
# Configuración
# ==========================================

st.set_page_config(page_title="Dataset", page_icon="📊")

# ==========================================
# Carga del dataset
# ==========================================

df = pd.read_csv("data/processed/streaming_users_clean.csv")

# ==========================================
# Título
# ==========================================

st.title("📊 Dataset")

st.write("""
En esta sección se presenta una descripción general del conjunto de datos utilizado durante el proyecto, junto con un resumen de su calidad y las principales transformaciones realizadas durante la etapa de preparación.
""")

st.markdown("---")

st.header("📌 Información general")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Registros", df.shape[0])

with col2:
    st.metric("Variables", df.shape[1])

with col3:
    st.metric(
        "Numéricas",
        len(df.select_dtypes(include="number").columns)
    )

with col4:
    st.metric(
        "Categóricas",
        len(df.select_dtypes(include="object").columns)
    )

st.markdown("---")

st.header("📝 Descripción de las variables")

# Descripciones de cada variable
descripciones = {
    "user_id": "Identificador único del usuario.",
    "age": "Edad del usuario.",
    "subscription_plan": "Plan de suscripción contratado.",
    "monthly_watch_time_mins": "Tiempo mensual de visualización en minutos.",
    "country": "País de residencia del usuario.",
    "favorite_genre": "Género audiovisual favorito.",
    "last_login_date": "Fecha del último acceso a la plataforma.",
    "customer_support_tickets": "Cantidad de tickets de soporte realizados."
}

# Crear la tabla automáticamente
descripcion = pd.DataFrame({
    "Variable": df.columns,
    "Descripción": [descripciones[col] for col in df.columns],
    "Tipo de dato": df.dtypes.astype(str).values
})

st.dataframe(
    descripcion,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.header("👀 Vista previa del dataset")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

st.info("""
**Resumen de calidad**

- Registros: 8034
- Variables: 8
- Registros duplicados: 0
- Valores negativos: 0
- Fechas futuras: 0
- Valores faltantes: solo en `last_login_date`
""")

st.markdown("---")

st.header("📋 Calidad del dataset")

calidad = pd.DataFrame({
    "Valores faltantes": df.isnull().sum(),
    "Porcentaje (%)": round(df.isnull().mean()*100,2)
})

st.dataframe(calidad, use_container_width=True)

st.markdown("---")

st.header("🧹 Transformaciones realizadas")

transformaciones = pd.DataFrame({
    "Transformación": [
        "Eliminación de registros duplicados",
        "Tratamiento de valores faltantes",
        "Normalización de categorías",
        "Corrección de edades",
        "Validación de fechas",
        "Tratamiento de valores extremos",
        "Generación del dataset limpio"
    ],
    "Estado": [
        "✅",
        "✅",
        "✅",
        "✅",
        "✅",
        "✅",
        "✅"
    ]
})

st.dataframe(transformaciones, use_container_width=True, hide_index=True)
