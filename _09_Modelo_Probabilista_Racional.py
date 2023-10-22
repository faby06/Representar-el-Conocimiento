import numpy as np

# Definir las probabilidades de dos opciones
probabilidad_opcion_A = 0.7
probabilidad_opcion_B = 0.3

# Generar una decisi�n basada en las probabilidades
decision = np.random.choice(['Opcion A', 'Opcion B'], p=[probabilidad_opcion_A, probabilidad_opcion_B])

# Mostrar la decisi�n tomada
print(f"Decisi�n tomada: {decision}")
