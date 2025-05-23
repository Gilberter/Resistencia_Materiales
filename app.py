import streamlit as st
from logic import *
import io


def main():
    st.set_page_config(page_title="Resistencia de Materiales", layout="wide")

    st.title("⚙️Proyecto Resistencia de Materiales⚙️")

    st.subheader("Estudiantes: Nichol Jimenez - Lia Gomez - Laura Corzo")

    st.write("""Textpppp""")

    # --- Barra Desplegable ---
    st.sidebar.header("🔩 Parametros para realzar loz calculos")

    st.sidebar.subheader("Eje de transmisión")
    n_conducido = st.sidebar.number_input("n conducido", value = 0)
    n_conductor = st.sidebar.number_input("n conductor", value = 0)

    st.sidebar.subheader("🔧 Calculo de torque")
    pot = st.sidebar.number_input("Potencia(W)", value = 0.0)
    vel = st.sidebar.number_input("Velocidad de rotación (rpm)", value = 0.0)
    
if __name__ == "__main__":
    main()