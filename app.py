import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from logic import *
from materials import materiales
from theory import theory_text
import pandas as pd

st.set_page_config(page_title="Resistencia de Materiales", layout="wide")
st.title("⚙️ Proyecto Resistencia de Materiales ⚙️")
st.markdown(theory_text)

st.sidebar.header("🔩 Parámetros de cálculo")
pot = st.sidebar.number_input("Potencia (W)", min_value=0.01, value=10.0, step=1.0)
vel = st.sidebar.number_input("Velocidad de rotación (rpm)", min_value=0.01, value=100.0, step=1.0)
longitud = st.sidebar.number_input("Longitud del eje (mm)", min_value=0.01, value=100.0, step=1.0)
material_usar = st.sidebar.selectbox("Material", list(materiales.keys()))
fs_objetivo = st.sidebar.number_input("FS objetivo", min_value=1.0, value=2.0)
tension_max = st.sidebar.number_input("Tensión máxima permitida (MPa)", min_value=0.01, value=100.0)
diametro_min = st.sidebar.number_input("Diámetro mínimo (mm)", min_value=0.01, value=10.0)
diametro_max = st.sidebar.number_input("Diámetro máximo (mm)", min_value=0.01, value=100.0)
paso = st.sidebar.number_input("Paso (mm)", min_value=0.01, value=1.0)

# Validaciones adicionales
if diametro_min > diametro_max:
    st.sidebar.error("El diámetro mínimo no puede ser mayor que el máximo.")
    st.stop()
if pot <= 0 or vel <= 0 or longitud <= 0 or tension_max <= 0 or diametro_min <= 0 or diametro_max <= 0 or paso <= 0:
    st.sidebar.error("Todos los valores deben ser mayores que cero.")
    st.stop()
if paso > (diametro_max - diametro_min):
    st.sidebar.error("El paso es demasiado grande para el rango de diámetros.")
    st.stop()

if st.sidebar.button("🔢 Calcular y Graficar"):
    props = materiales[material_usar]
    diametros = np.arange(diametro_min, diametro_max + paso, paso)
    torques = cal_torque(pot, vel)
    fs_list = []
    tensiones = []
    deformaciones = []

    for d in diametros:
        radio = d / 2
        J = polar_moment_iner(d)
        tau = ten_cortante_fun(torques, radio, J)
        theta = angular_deformation(torques, longitud, J, props["modulo_rigidez"])
        fs = fact_security(props["limite_elastico"], tau)
        fs_list.append(fs)
        tensiones.append(tau)
        deformaciones.append(theta)

    fig, ax = plt.subplots(1, 3, figsize=(18, 5))
    ax[0].plot(diametros, fs_list, label="FS")
    ax[0].axhline(fs_objetivo, color='r', linestyle='--', label="FS objetivo")
    ax[0].set_xlabel("Diámetro (mm)")
    ax[0].set_ylabel("Factor de Seguridad")
    ax[0].legend()
    ax[0].set_title("FS vs Diámetro")

    ax[1].plot(diametros, tensiones, label="Tensión cortante")
    ax[1].axhline(tension_max, color='r', linestyle='--', label="Tensión máxima")
    ax[1].set_xlabel("Diámetro (mm)")
    ax[1].set_ylabel("Tensión (MPa)")
    ax[1].legend()
    ax[1].set_title("Tensión cortante vs Diámetro")

    ax[2].plot(diametros, deformaciones, label="Deformación angular")
    ax[2].set_xlabel("Diámetro (mm)")
    ax[2].set_ylabel("Deformación angular (rad)")
    ax[2].legend()
    ax[2].set_title("Deformación angular vs Diámetro")

    st.pyplot(fig)

    # Mostrar resultados para el diámetro mínimo
    st.subheader("Resultados para el diámetro mínimo")
    st.markdown(f"- **Torque:** {torques:.2f} Nm")
    st.markdown(f"- **Tensión cortante:** {tensiones[0]:.2f} MPa")
    st.markdown(f"- **Deformación angular:** {deformaciones[0]:.6f} rad")
    st.markdown(f"- **Factor de seguridad:** {fs_list[0]:.2f}")

    st.info("Puedes ajustar los parámetros para ver cómo cambian los resultados y las gráficas.")

    # Tabla de comparación de materiales
    st.subheader("Comparación de materiales (para diámetro mínimo)")
    data = []
    for nombre, props in materiales.items():
        J = polar_moment_iner(diametro_min)
        radio = diametro_min / 2
        tau = ten_cortante_fun(torques, radio, J)
        fs = fact_security(props["limite_elastico"], tau)
        data.append({
            "Material": nombre,
            "FS": round(fs, 2),
            "Tensión (MPa)": round(tau, 2),
            "Límite elástico (MPa)": props["limite_elastico"]
        })
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Plot de comparación de materiales
    st.subheader("Gráfico: FS de materiales para diámetro mínimo")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.bar(df["Material"], df["FS"], color='skyblue')
    ax2.axhline(fs_objetivo, color='r', linestyle='--', label="FS objetivo")
    ax2.set_ylabel("Factor de Seguridad")
    ax2.set_xlabel("Material")
    ax2.set_title("FS de materiales para diámetro mínimo")
    ax2.legend()
    plt.xticks(rotation=30, ha='right')
    st.pyplot(fig2)

st.sidebar.markdown("---")