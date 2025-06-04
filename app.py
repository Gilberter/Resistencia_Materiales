import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from logic import *
from materials import materiales
from theory import theory_text
import requests
import pandas as pd


st.set_page_config(page_title="Resistencia de Materiales", layout="wide")
st.title("⚙️ Proyecto Resistencia de Materiales ⚙️")
st.markdown(theory_text)

<<<<<<< HEAD
st.sidebar.header("🔩 Parámetros de cálculo")
pot = st.sidebar.number_input("Potencia (W)", min_value=0.1)
vel = st.sidebar.number_input("Velocidad de rotación (rpm)", min_value=0.1)
longitud = st.sidebar.number_input("Longitud del eje (mm)", min_value=1.0)
material_usar = st.sidebar.selectbox("Material", list(materiales.keys()))
fs_objetivo = st.sidebar.number_input("FS objetivo", min_value=1.0, value=2.0)
tension_max = st.sidebar.number_input("Tensión máxima permitida (MPa)", min_value=1.0, value=100.0)
diametro_min = st.sidebar.number_input("Diámetro mínimo (mm)", min_value=1.0, value=10.0)
diametro_max = st.sidebar.number_input("Diámetro máximo (mm)", min_value=diametro_min, value=100.0)
paso = st.sidebar.number_input("Paso (mm)", min_value=0.1, value=1.0)
=======

    st.title("⚙️Proyecto Resistencia de Materiales⚙️")
>>>>>>> 6ebe0e9c38e427fb48ca40b0239c353b24cdc47c

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

    # Mostrar resultados para el diámetro seleccionado
    st.subheader("Resultados para el diámetro mínimo")
    st.markdown(f"- **Torque:** {torques:.2f} Nm")
    st.markdown(f"- **Tensión cortante:** {tensiones[0]:.2f} MPa")
    st.markdown(f"- **Deformación angular:** {deformaciones[0]:.6f} rad")
    st.markdown(f"- **Factor de seguridad:** {fs_list[0]:.2f}")

    # Animación (opcional, requiere instalar streamlit-lottie y un archivo .json de animación)
    # from streamlit_lottie import st_lottie
    # import requests
    # lottie_url = "https://assets10.lottiefiles.com/packages/lf20_2ks3pjua.json"
    # lottie_json = requests.get(lottie_url).json()
    # st_lottie(lottie_json, height=200, key="torsion_anim")

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

st.sidebar.markdown("---")
