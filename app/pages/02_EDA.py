import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="📈")

df = pd.read_csv("data/processed/streaming_users_clean.csv")

st.title("📈 Análisis Exploratorio de Datos (EDA)")

st.write("""
En esta sección se presentan las principales visualizaciones realizadas durante el análisis exploratorio del conjunto de datos. El objetivo es comprender el comportamiento de las variables y responder las preguntas planteadas durante la etapa de inspección inicial.
""")

st.markdown("---")

# ==========================================================
# Pregunta 1
# ==========================================================

st.header("1️⃣ ¿Cuál es el plan de suscripción más utilizado por los usuarios?")

fig, ax = plt.subplots(figsize=(8,5))

sns.countplot(
    data=df,
    x="subscription_plan",
    order=df["subscription_plan"].value_counts().index,
    ax=ax
)

for container in ax.containers:
    ax.bar_label(container)

ax.set_title("Distribución de los planes de suscripción")
ax.set_xlabel("Plan de suscripción")
ax.set_ylabel("Cantidad de usuarios")

st.pyplot(fig)

st.success("""
**Interpretación**

Se observa que el **plan Básico** es el más utilizado por los usuarios, seguido por el plan **Estándar**.
El **plan Premium** presenta la menor cantidad de suscriptores, lo que indica una menor adopción de esta modalidad.
""")

st.markdown("---")

# ==========================================================
# Pregunta 2
# ==========================================================

st.header("2️⃣ ¿Cómo se distribuye el tiempo mensual de visualización?")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(
    df["monthly_watch_time_mins"],
    bins=30
)

ax.axvline(
    df["monthly_watch_time_mins"].mean(),
    color="red",
    linestyle="--",
    label="Media"
)

ax.set_title("Distribución del tiempo mensual de visualización")
ax.set_xlabel("Minutos")
ax.set_ylabel("Frecuencia")

ax.legend()

st.pyplot(fig)

st.success("""
**Interpretación**

La mayor parte del tiempo mensual de visualización se concentra entre aproximadamente **500 y 1000 minutos**. Además, la línea roja indica la **media** del tiempo de visualización, que se encuentra cercana al centro de la distribución, mostrando que la mayoría de los usuarios presenta un consumo intermedio y que existen pocos casos con tiempos muy bajos o muy altos.
""")

st.markdown("---")

# ==========================================================
# Pregunta 3
# ==========================================================

st.header("3️⃣ ¿Existen diferencias en el tiempo de visualización según el plan contratado?")

fig, ax = plt.subplots(figsize=(8,5))

sns.boxplot(
    data=df,
    x="subscription_plan",
    y="monthly_watch_time_mins",
    ax=ax
)

ax.set_title("Tiempo mensual de visualización según el plan de suscripción")
ax.set_xlabel("Plan de suscripción")
ax.set_ylabel("Minutos")

st.pyplot(fig)

st.success("""
**Interpretación**

Se observan diferencias en el tiempo mensual de visualización entre los distintos planes de suscripción. En general, los usuarios del **plan Premium** presentan una mediana de tiempo de visualización mayor que los usuarios de los planes **Estándar** y **Básico**. Además, se identifican algunos valores atípicos en los tres planes, aunque estos no modifican la tendencia general observada.
""")

st.markdown("---")

# ==========================================================
# Pregunta 4
# ==========================================================

st.header("4️⃣ ¿Existe relación entre la edad de los usuarios y el tiempo mensual de visualización?")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="age",
    y="monthly_watch_time_mins",
    alpha=0.5,
    ax=ax
)

ax.set_title("Relación entre la edad y el tiempo mensual de visualización")
ax.set_xlabel("Edad")
ax.set_ylabel("Minutos")

st.pyplot(fig)

st.success("""
**Interpretación**

El gráfico de dispersión no evidencia una relación lineal clara entre la edad de los usuarios y el tiempo mensual de visualización. Los puntos se encuentran distribuidos de manera dispersa a lo largo del gráfico, lo que indica que la edad, por sí sola, no explica el comportamiento del tiempo de visualización.
""")

st.markdown("---")

# ==========================================================
# Pregunta 5
# ==========================================================

st.header("5️⃣ ¿Qué relación presentan las variables numéricas del conjunto de datos?")

variables_numericas = [
    "age",
    "monthly_watch_time_mins",
    "customer_support_tickets"
]

correlacion = df[variables_numericas].corr()

fig, ax = plt.subplots(figsize=(7,6))

sns.heatmap(
    correlacion,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    ax=ax
)

ax.set_title("Matriz de correlación entre variables numéricas")

st.pyplot(fig)

st.success("""
**Interpretación**

La matriz de correlación muestra que las variables numéricas presentan **correlaciones débiles**, ya que los coeficientes se encuentran próximos a cero. Esto indica que no existe una relación lineal fuerte entre la edad, el tiempo mensual de visualización y la cantidad de tickets de soporte.
""")

st.markdown("---")

# ==========================================================
# Conclusión general
# ==========================================================

st.header("📌 Conclusión general del análisis exploratorio")

st.info("""
El análisis exploratorio permitió conocer el comportamiento general del conjunto de datos y responder las preguntas planteadas al inicio del proyecto.

Los principales hallazgos fueron:

- El plan **Básico** es el más utilizado por los usuarios.
- La mayor parte del tiempo mensual de visualización se concentra entre **500 y 1000 minutos**.
- Los usuarios del **plan Premium** presentan, en general, un mayor tiempo de visualización.
- No se observa una relación lineal clara entre la edad y el tiempo de visualización.
- Las variables numéricas presentan correlaciones débiles, por lo que existe poca dependencia lineal entre ellas.
""")
