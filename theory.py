theory_text = """
# Teoría de Torsión en Ejes

La torsión es el esfuerzo que se produce cuando se aplica un momento de fuerza (torque) a un eje. Los conceptos clave son:

- **Torque (T):** Es la fuerza que hace girar el eje. Se calcula como:
  $$
  T = \\frac{P \\cdot 60}{2\\pi N}
  $$
  donde $P$ es la potencia (W) y $N$ la velocidad (rpm).

- **Momento polar de inercia (J):**
  $$
  J = \\frac{\\pi d^4}{32}
  $$
  donde $d$ es el diámetro del eje.

- **Tensión cortante máxima ($\\tau_{max}$):**
  $$
  \\tau_{max} = \\frac{T \\cdot r}{J}
  $$
  donde $r$ es el radio del eje.

- **Deformación angular ($\\theta$):**
  $$
  \\theta = \\frac{T \\cdot L}{J \\cdot G}
  $$
  donde $L$ es la longitud del eje y $G$ el módulo de rigidez.

- **Factor de seguridad (FS):**
  $$
  FS = \\frac{\\text{Límite elástico}}{\\tau_{max}}
  $$

## ¿Por qué es importante?

Un diseño seguro y eficiente de ejes garantiza la transmisión de potencia sin fallas mecánicas, evitando accidentes y pérdidas económicas.

---
"""