import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="PCA", page_icon="📉")

df = pd.read_csv("data/processed/streaming_users_clean.csv")

st.title("📉 Reducción de Dimensionalidad (PCA)")

st.write("""
En esta sección se presenta el Análisis de Componentes Principales (PCA), técnica utilizada para reducir la dimensionalidad del conjunto de datos conservando la mayor cantidad posible de información.
""")

st.markdown("---")

st.header("📌 Variables utilizadas")

st.write("""
Para aplicar el PCA se utilizaron únicamente las variables numéricas:

- age
- monthly_watch_time_mins
- customer_support_tickets
""")

st.markdown("---")

st.header("⚙️ Escalamiento de los datos")

st.info("""
Antes de aplicar el PCA, las variables numéricas fueron estandarizadas mediante **StandardScaler**.

Este paso fue necesario porque las variables presentan escalas diferentes y el PCA es sensible a dichas diferencias.
""")

st.markdown("---")

# ==========================================================
# Aplicación del PCA
# ==========================================================

variables = [
    "age",
    "monthly_watch_time_mins",
    "customer_support_tickets"
]

X = df[variables]

scaler = StandardScaler()
X_escalado = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_escalado)

# ==========================================================
# Varianza explicada
# ==========================================================

import numpy as np

st.header("📊 Varianza explicada")

varianza = pd.DataFrame({

    "Componente":
        [f"PC{i+1}" for i in range(len(pca.explained_variance_ratio_))],

    "Varianza explicada":
        pca.explained_variance_ratio_,

    "Varianza acumulada":
        np.cumsum(pca.explained_variance_ratio_)

})

st.dataframe(
    varianza.style.format({
        "Varianza explicada": "{:.3f}",
        "Varianza acumulada": "{:.3f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.success("""
**Interpretación**

La primera componente principal explica aproximadamente el **33,8 %** de la variabilidad del conjunto de datos. Con las dos primeras componentes se alcanza cerca del **66,9 %**, mientras que las tres componentes explican el **100 %** de la variabilidad disponible, ya que el análisis se realizó sobre tres variables numéricas.
""")

st.markdown("---")

# ==========================================================
# Gráfico de varianza explicada acumulada
# ==========================================================

st.header("📈 Varianza explicada acumulada")

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(

    range(1, len(pca.explained_variance_ratio_) + 1),

    np.cumsum(pca.explained_variance_ratio_),

    marker="o"

)

ax.set_xlabel("Número de Componentes")
ax.set_ylabel("Varianza acumulada")
ax.set_title("Varianza explicada acumulada")

ax.grid(True)

st.pyplot(fig)

st.success("""
**Interpretación**

La varianza explicada acumulada aumenta de forma progresiva a medida que se incorporan nuevas componentes principales. Las dos primeras componentes conservan aproximadamente el **66,9 %** de la información original, mientras que las tres componentes alcanzan el **100 %** de la varianza, ya que el análisis se realizó sobre tres variables numéricas.
""")

st.markdown("---")

# ==========================================================
# Proyección sobre las dos primeras componentes
# ==========================================================

st.header("📊 Proyección de los datos sobre las dos primeras componentes principales")

pca_2 = PCA(n_components=2)

componentes = pca_2.fit_transform(X_escalado)

df_pca = pd.DataFrame(
    componentes,
    columns=["PC1", "PC2"]
)

fig, ax = plt.subplots(figsize=(8,6))

sns.scatterplot(
    data=df_pca,
    x="PC1",
    y="PC2",
    alpha=0.6,
    ax=ax
)

ax.set_title("Proyección de los datos sobre las dos primeras componentes principales")
ax.set_xlabel("Componente Principal 1")
ax.set_ylabel("Componente Principal 2")

st.pyplot(fig)

st.success("""
**Interpretación**

La proyección de los datos sobre las dos primeras componentes principales permite representar el conjunto de datos en un espacio bidimensional conservando aproximadamente el **66,9 %** de la variabilidad original. No se observan agrupamientos claramente definidos, lo que indica que el PCA fue utilizado principalmente como una técnica de reducción de dimensionalidad y exploración visual de los datos.
""")

st.markdown("---")

# ==========================================================
# Conclusión
# ==========================================================

st.header("📌 Conclusión del PCA")

st.info("""
El Análisis de Componentes Principales permitió reducir la dimensionalidad del conjunto de datos y facilitar su representación gráfica.

Los principales resultados obtenidos fueron:

- Se trabajó con tres variables numéricas previamente estandarizadas.
- La primera componente principal explicó aproximadamente el **33,8 %** de la variabilidad.
- Las dos primeras componentes principales conservaron cerca del **66,9 %** de la información del conjunto de datos.
- No se identificaron agrupamientos claramente diferenciados en la proyección bidimensional.
- El Análisis de Componentes Principales (PCA) fue útil como técnica de exploración y visualización, aunque la baja correlación entre las variables limitó una reducción más significativa de la dimensionalidad.""")
