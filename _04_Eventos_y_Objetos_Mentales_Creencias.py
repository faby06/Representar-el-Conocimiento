# Crear una estructura para representar creencias
creencias = {
    "Juan": {
        "cree_que": {
            "el cielo_es_azul": True,
            "los gatos_pueden_volar": False,
            "la pizza_es_deliciosa": True
        }
    },
    "Mar�a": {
        "cree_que": {
            "el cielo_es_azul": True,
            "los gatos_pueden_volar": True,
            "la pizza_es_deliciosa": False
        }
    }
}

# Mostrar las creencias de Juan
print("Creencias de Juan:")
for creencia, valor in creencias["Juan"]["cree_que"].items():
    print(f"{creencia}: {valor}")

# Mostrar las creencias de Mar�a
print("\nCreencias de Mar�a:")
for creencia, valor in creencias["Mar�a"]["cree_que"].items():
    print(f"{creencia}: {valor}")
