materiales = {
    "Acero AISI 1045": {"limite_elastico": 530, "modulo_rigidez": 80_000},
    "Aluminio 6061-T6": {"limite_elastico": 275, "modulo_rigidez": 26_000},
    "Bronce SAE 660": {"limite_elastico": 240, "modulo_rigidez": 44_000},
    "Titanio Grado 5": {"limite_elastico": 895, "modulo_rigidez": 44_000},
    "Nylon PA66": {"limite_elastico": 90, "modulo_rigidez": 1_200},
    # ...agrega los demás materiales
}
materials_other = {

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

# Valores constantes recomendados

# Factores de seguridad típicos para ejes de transmisión
FACT_S_MIN = 1.5   # Mínimo recomendado para aplicaciones generales
FACT_S_MAX = 2.5   # Máximo recomendado para aplicaciones críticas

# Módulo de rigidez (GPa) por defecto para materiales no listados (puedes ajustar según el material)
MODULO_RIGIDEZ_DEFAULT = 80.0  # GPa (valor típico para aceros)

# Paso mínimo recomendado para el barrido de diámetros
PASO_MIN = 0.5  # mm

# Diámetro mínimo y máximo recomendados para ejes pequeños/medianos
DIAMETRO_MIN_DEFAULT = 10.0  # mm
DIAMETRO_MAX_DEFAULT = 100.0 # mm

# Tensión máxima permisible por defecto (ajusta según el caso)
TENSION_MAX_DEFAULT = 100.0  # MPa

# Longitud de eje por defecto
LONGITUD_DEFAULT = 100.0  # mm

# Potencia y velocidad por defecto
POTENCIA_DEFAULT = 10.0   # W
VELOCIDAD_DEFAULT = 100.0 # rpm
