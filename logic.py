import numpy as np

#CONSTANTES
fact_s_min = 1.5
fact_s_max = 2.5

#FUNCIONES

def eje_transmision(n_conducido, n_conductor):
    return (
        n_conducido/n_conductor
    )

def cal_torque(pot, vel):
    return (pot*60) / (2*np.pi*vel)
    
def polar_moment_iner(diametro):
    return (np.pi * (diametro ** 4))/32
    
def ten_cortante_fun(torque, radio, polar_moment):
    return (torque * radio) / polar_moment

def angular_deformation(torque, longitud, polar_moment, rigidez):
    return (torque * longitud) / (polar_moment * rigidez)

def fact_security(limite_elastico, tension_max):
    return limite_elastico / tension_max

materiales = {
    "Acero AISI 1045": 530,
    "Aluminio 6061-T6": 275,
    "Bronce SAE 660": 240,
    "Titanio Grado 5": 895,
    "Nylon PA66": 90,
    "Acero 8620 cementado":500,
    "Acero 4140": 655,
    "Acero 4340": 850,
    "Acero al carbono 1045": 450,
    "Fundición nodular": 200,
    "Bronce al estaño (SAE 600)": 300,
    "Nylon 6/6 + fibra de vidrio": 180,  
    "Aleación de aluminio 7075-T6": 500,
    "Cobre-berilio": 600,
    "Aleación de aluminio 6061-T6": 240,
    "PEEK (Polietheretherketone)": 100
}

"""def select_material(tension_max):
    materiales_s = materiales;

    for material, limite in materiales_s.items():
        fs = fact_security(limite, tension_max)
        print (f'{material}: FS = {fs:.2f}')
        if fs >= fact_s_min & fs <= fact_s_max:
            print (f'Material adecuado: {material} (FS = {fs:.2f})')
            return material, fs
        else:
            print('Ninguno de los materiales dados cumple con el factor de seguridad mínimo.')
    return None, None           """