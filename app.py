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
    n_conducido = st.sidebar.number_input("n conducido", min_value = 1)
    n_conductor = st.sidebar.number_input("n conductor", min_value =  1)

    st.sidebar.subheader("🔧 Calculo de torque")
    pot = st.sidebar.number_input("Potencia(W)", min_value = 0.1)
    vel = st.sidebar.number_input("Velocidad de rotación (rpm)", min_value = 0.1)
    
    st.sidebar.subheader("🍎 Calculo del momento polar de incercia")
    diametro = st.sidebar.number_input("Diametro(m)", min_value = 1.0)

    st.sidebar.subheader("Calculo de la tensión cortante")
    radio = st.sidebar.number_input("Radio(m)", min_value = 1.0)

    st.sidebar.subheader("📐 Calculo de la deformación angular")
    longitud = st.sidebar.number_input("Longitud(m)", min_value= 1.0)
    modulo_rigidez = st.sidebar.number_input("Rigidez(MPa)", min_value = 1.0)

    st.sidebar.subheader(" Seleccione el valor de la tensión maxima")
    tension_max = st.sidebar.number_input("Tensión maxima(MPa)", min_value = 1.0)

    st.sidebar.subheader("Seleccione el material que vamos a usar")
    material_usar = st.sidebar.selectbox("Material(Limite elastico)", list(materiales.keys()))
    elastic_limit = materiales[material_usar]

    



    if st.sidebar.button("🔢 Realizar calculos"):
        
        st.subheader("Valores de los calculos")

        eje_transmision_value = eje_transmision(n_conducido, n_conductor)
        torque = cal_torque(pot, vel)
        momento_polar = polar_moment_iner(diametro)
        tension_cor = ten_cortante_fun(torque, radio, momento_polar)
        deformacion_angular = angular_deformation(torque, longitud, momento_polar, modulo_rigidez)
        fs = fact_security(elastic_limit, tension_max)

        st.markdown(f"Eje de transmisión = {eje_transmision_value}")
        st.markdown(f"Torque = {torque:.4f}")
        st.markdown(f"Momento Polar = {momento_polar:.4f}")
        st.markdown(f"Tensión Cortante = {tension_cor:.4f}")
        st.markdown(f"Deformación Angular = {deformacion_angular:.4f}")
        
        if fs >= fact_s_min and fs <= fact_s_max:
            st.info(f"✅ El material seleccionado de acuerdo a los calculos realizados es {materiales} su factor de seguridad es {fs}")
        else: 
            st.error(f"⚠️ El material {material_usar} seleccionado NO cumple con el factor de seguridad mínimo ni maximo.")


if __name__ == "__main__":
    main()