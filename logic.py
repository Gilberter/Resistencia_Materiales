import numpy as np

#CONSTANTES
fact_s_min = 1.5
fact_s_max = 2.5

#FUNCIONES

import numpy as np

def eje_transmision(n_conducido, n_conductor):
    return n_conducido / n_conductor

def cal_torque(pot, vel):
    return (pot * 60) / (2 * np.pi * vel)

def polar_moment_iner(diametro):
    return (np.pi * (diametro ** 4)) / 32

def ten_cortante_fun(torque, radio, polar_moment):
    torque_nmm = torque * 1000  # Convertir Nm a Nmm
    return (torque_nmm * radio) / polar_moment

def angular_deformation(torque, longitud, polar_moment, rigidez):
    torque_nmm = torque * 1000  # Convertir Nm a Nmm
    return (torque_nmm * longitud) / (polar_moment * rigidez)

def fact_security(limite_elastico, tension_max):
    return limite_elastico / tension_max

def select_material(materiales, tension_max, fs_min, fs_max):
    for nombre, props in materiales.items():
        fs = fact_security(props["limite_elastico"], tension_max)
        if fs_min <= fs <= fs_max:
            return nombre, fs
    return None, None