import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from logic import *
from materials import materiales, materials_other, FACT_S_MIN, FACT_S_MAX, MODULO_RIGIDEZ_DEFAULT, PASO_MIN, DIAMETRO_MIN_DEFAULT, DIAMETRO_MAX_DEFAULT, TENSION_MAX_DEFAULT, LONGITUD_DEFAULT, POTENCIA_DEFAULT, VELOCIDAD_DEFAULT 
from theory import theory_text
import pandas as pd
from gears import generar_gif_engranajes


st.set_page_config(page_title="Resistencia de Materiales", layout="wide")
st.title("⚙️ Proyecto Resistencia de Materiales ⚙️")
st.subheader("Estudiantes: Nichol Jimenez - Lia Gomez - Laura Corzo")
st.subheader("Análisis de Transmision de piñones")

st.write("""Imagina que estas diseñando un sistema de transmisión para una bicileta electrica. Este sistema utiliza un motor que transmite potencia a la rueda trasera mediante un conjunto de piñones y engranajes. Es crucial analizar como la relación entre piñones afecta la velocidad, el torque y la resistencia de los materiales.""")

st.subheader("Objetivos del Proyecto")
st.write("""1. Análizar la relación entre piñones y su impacto en la velocidad y torque del sistema. """)
st.write("""2. Calcular las tensiones y deformaciones en los ejes y engranjes debido a las cargas aplicadas. """)
st.write("""3. Determine la resistencia de los materiales utilizados en lo piñones y ejes para asegurar la durabilidad del sistema.""")

st.subheader("Teoría de Torsión en Ejes")
st.write(
    "La torsión es el esfuerzo que se produce cuando se aplica un momento de fuerza (torque) a un eje. "
    "Los conceptos clave son:"
)

st.markdown("---")
st.subheader("1. Relación de transmisión entre piñones")
st.write(
    "La relación de transmisión entre dos piñones se define como:"
)
st.latex(r"\text{Relación de Transmisión} = \frac{N_{\text{conducido}}}{N_{\text{conductor}}}")
st.write(
    "donde $N_{\\text{conducido}}$ es el número de dientes del piñón conducido y "
    "$N_{\\text{conductor}}$ es el número de dientes del piñón conductor."
)
# --- Parámetros de cálculo en la barra lateral ---
st.sidebar.header("🔩 Parámetros de cálculo")
st.sidebar.subheader("Eje de transmisión")
n_conducido = st.sidebar.number_input("n conducido", min_value=1, value=1, step=1)
n_conductor = st.sidebar.number_input("n conductor", min_value=1, value=1, step=1)

if st.sidebar.button("🎞️ Generar animación de engranajes"):
    generar_gif_engranajes(n_conductor, n_conducido, filename="gears.gif")
    with open("gears.gif", "rb") as f:
        st.image(f.read(), caption="Simulación de engranajes")

st.markdown("---")
st.subheader("2. Torque (T)")
st.write(
    "Es la fuerza que hace girar el eje. Se calcula como:"
)
st.latex(r"T = \frac{P \cdot 60}{2\pi N}")
st.write(
    "donde $P$ es la potencia (W) y $N$ la velocidad (rpm)."
)

st.markdown("---")
st.subheader("3. Momento polar de inercia (J)")
st.latex(r"J = \frac{\pi d^4}{32}")
st.write(
    "donde $d$ es el diámetro del eje."
)

st.markdown("---")
st.subheader("4. Tensión cortante máxima ($\\tau_{max}$)")
st.latex(r"\tau_{max} = \frac{T \cdot r}{J}")
st.write(
    "donde $r$ es el radio del eje."
)

st.markdown("---")
st.subheader("5. Deformación angular ($\\theta$)")
st.latex(r"\theta = \frac{T \cdot L}{J \cdot G}")
st.write(
    "donde $L$ es la longitud del eje y $G$ el módulo de rigidez."
)

st.markdown("---")
st.subheader("6. Factor de seguridad (FS)")
st.latex(r"FS = \frac{\text{Límite elástico}}{\tau_{max}}")

st.markdown("---")
st.subheader("¿Por qué es importante?")
st.write(
    "Un diseño seguro y eficiente de ejes garantiza la transmisión de potencia sin fallas mecánicas, "
    "evitando accidentes y pérdidas económicas."
)
st.markdown("---")



st.sidebar.subheader("🔧 Cálculo de torque")
pot = st.sidebar.number_input("Potencia (W)", min_value=0.1, value=POTENCIA_DEFAULT, step=50.0)
vel = st.sidebar.number_input("Velocidad de rotación (rpm)", min_value=0.1, value=VELOCIDAD_DEFAULT, step=20.)

st.sidebar.subheader("🍎 Cálculo del momento polar de inercia")
diametro_min = st.sidebar.number_input("Diámetro (mm)", min_value=0.01, value=DIAMETRO_MIN_DEFAULT, step=10.0)


st.sidebar.subheader("📐 Cálculo de la deformación angular")
longitud = st.sidebar.number_input("Longitud del eje (mm)", min_value=0.01, value=LONGITUD_DEFAULT, step=10.0)
modulo_rigidez = st.sidebar.number_input("Rigidez(MPa)", min_value = 1.0)

st.sidebar.subheader("Seleccione el valor de la tensión máxima")
tension_max = st.sidebar.number_input("Tensión máxima permitida (MPa)", min_value=1.0, value=TENSION_MAX_DEFAULT, step=10.0)

st.sidebar.subheader("Seleccione el material que vamos a usar")
materiales_principales = list(materiales.keys())
materiales_opciones = materiales_principales + ["Otros materiales..."]

material_usar = st.sidebar.selectbox("Seleccione el material", materiales_opciones)

if material_usar == "Otros materiales...":
    material_otro = st.sidebar.selectbox("Seleccione otro material", list(materials_other.keys()))

    material_seleccionado = material_otro
    modulo_rigidez_sel = st.sidebar.number_input(
        "Módulo de rigidez (MPa) para el material seleccionado",
        min_value=1.0, value=80.0, step=5.0
    )
    modulo_rigidez_sel_mpa = modulo_rigidez_sel  # MPa ya está en MPa
    elastic_limit = st.sidebar.number_input(
        "Límite elástico (MPa) para el material seleccionado",
        min_value=1.0, value=200.0, step=10.0
    )
    
else:
    elastic_limit = materiales[material_usar]["limite_elastico"]
    material_seleccionado = material_usar
    modulo_rigidez_sel_mpa = materiales[material_usar]["modulo_rigidez"]  # Ya está en MPa
    st.sidebar.markdown(f"**Limite elastico (MPa):** {elastic_limit}")
    st.sidebar.markdown(f"**Módulo de rigidez (MPa):** {modulo_rigidez_sel_mpa}")

fs_objetivo = st.sidebar.number_input("FS objetivo", min_value=1.0, value=2.0, step=10.0)

diametro_max = 1000  # Valor por defecto, se puede ajustar según el contexto

# --- Validaciones ---
if diametro_min > diametro_max:
    st.sidebar.error("El diámetro mínimo no puede ser mayor que el máximo.")
    st.stop()
if pot <= 0 or vel <= 0 or longitud <= 0 or tension_max <= 0 or diametro_min <= 0 or diametro_max <= 0:
    st.sidebar.error("Todos los valores deben ser mayores que cero.")
    st.stop()



if st.sidebar.button("🔢 Calcular y Graficar"):
    diametros = np.arange(diametro_min, diametro_max + 1, 1)
    torques = cal_torque(pot, vel)
    fs_list = []
    tensiones = []
    deformaciones = []

    for d in diametros:
        radio = d / 2
        J = polar_moment_iner(d)
        tau = ten_cortante_fun(torques, radio, J)
        theta = angular_deformation(torques, longitud, J, modulo_rigidez_sel_mpa)
        fs = fact_security(elastic_limit, tau)
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

    # Mostrar resultados para el material seleccionado
    st.subheader(f"Resultados para el material seleccionado: {material_seleccionado}")
    st.markdown(f"- **Torque:** {torques:.2f} Nm")
    st.markdown(f"- **Tensión cortante:** {tensiones[0]:.2f} MPa")
    st.markdown(f"- **Deformación angular:** {deformaciones[0]:.6f} rad")
    st.markdown(f"- **Factor de seguridad:** {fs_list[0]:.2f}")

    st.info("Puedes ajustar los parámetros para ver cómo cambian los resultados y las gráficas.")

    # Tabla de comparación de materiales
    st.subheader("Comparación de materiales")
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
    st.subheader("Gráfico: FS de materiales ")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.bar(df["Material"], df["FS"], color='skyblue')
    ax2.axhline(fs_objetivo, color='r', linestyle='--', label="FS objetivo")
    ax2.set_ylabel("Factor de Seguridad")
    ax2.set_xlabel("Material")
    ax2.set_title("FS de materiales")
    ax2.legend()
    plt.xticks(rotation=30, ha='right')
    st.pyplot(fig2)

    

    

st.sidebar.markdown("---")