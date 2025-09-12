# ------------------------------------------------------------------------------------
# CÓDIGO EXPLICATIVO: ENCADENAMIENTO HACIA ADELANTE Y HACIA ATRÁS EN LÓGICA PROPOSICIONAL
# ------------------------------------------------------------------------------------
# Este programa implementa dos algoritmos fundamentales en lógica proposicional:
# 1. Encadenamiento hacia adelante: Deriva nuevos hechos a partir de hechos iniciales y reglas.
# 2. Encadenamiento hacia atrás: Verifica si un objetivo puede ser derivado a partir de hechos y reglas.

# ------------------------------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LAS REGLAS Y HECHOS INICIALES
# ------------------------------------------------------------------------------------
# - Las reglas son representadas como una lista de tuplas (condiciones, conclusión).
# - Cada regla tiene una lista de condiciones que deben cumplirse para derivar la conclusión.
# - Los hechos iniciales son los datos conocidos como verdaderos al inicio del proceso.

reglas = [
    (["A", "B"], "C"),  # Si A y B son verdaderos, entonces C es verdadero.
    (["C"], "D"),       # Si C es verdadero, entonces D es verdadero.
    (["D"], "E")        # Si D es verdadero, entonces E es verdadero.
]

hechos_iniciales = ["A", "B"]  # Hechos iniciales conocidos como verdaderos.

# ------------------------------------------------------------------------------------
# PASO 2: FUNCIÓN PARA EL ENCADENAMIENTO HACIA ADELANTE
# ------------------------------------------------------------------------------------
# - Esta función deriva nuevos hechos a partir de los hechos iniciales y las reglas.
# - Utiliza un conjunto para almacenar los hechos derivados y evitar duplicados.
# - Itera sobre las reglas hasta que no se puedan derivar más hechos nuevos.

def encadenamiento_hacia_adelante(hechos, reglas):
    """
    Realiza el encadenamiento hacia adelante para derivar nuevos hechos.
    :param hechos: Lista de hechos iniciales.
    :param reglas: Lista de reglas (condiciones, conclusión).
    :return: Lista de todos los hechos derivados.
    """
    hechos_derivados = set(hechos)  # Usamos un conjunto para evitar duplicados.
    cambio = True  # Variable para rastrear si se derivaron nuevos hechos.

    while cambio:
        cambio = False
        for condiciones, conclusion in reglas:
            # Verificamos si todas las condiciones de la regla son verdaderas.
            if all(condicion in hechos_derivados for condicion in condiciones):
                if conclusion not in hechos_derivados:
                    hechos_derivados.add(conclusion)  # Agregamos la conclusión como un nuevo hecho.
                    cambio = True  # Indicamos que hubo un cambio.
    return list(hechos_derivados)

# ------------------------------------------------------------------------------------
# PASO 3: FUNCIÓN PARA EL ENCADENAMIENTO HACIA ATRÁS
# ------------------------------------------------------------------------------------
# - Esta función verifica si un objetivo puede ser derivado a partir de los hechos y reglas.
# - Parte del objetivo y busca si puede ser derivado mediante las reglas.
# - Si el objetivo depende de otros hechos, verifica recursivamente si estos pueden ser derivados.

def encadenamiento_hacia_atras(objetivo, hechos, reglas):
    """
    Realiza el encadenamiento hacia atrás para verificar si un objetivo puede ser derivado.
    :param objetivo: El hecho que queremos verificar.
    :param hechos: Lista de hechos iniciales.
    :param reglas: Lista de reglas (condiciones, conclusión).
    :return: True si el objetivo puede ser derivado, False en caso contrario.
    """
    if objetivo in hechos:
        return True  # El objetivo ya es un hecho conocido.

    for condiciones, conclusion in reglas:
        if conclusion == objetivo:
            # Verificamos si todas las condiciones de la regla pueden ser derivadas.
            if all(encadenamiento_hacia_atras(condicion, hechos, reglas) for condicion in condiciones):
                return True
    return False

# ------------------------------------------------------------------------------------
# PASO 4: EJEMPLO PRÁCTICO
# ------------------------------------------------------------------------------------
# - Este ejemplo muestra cómo funcionan ambos algoritmos con un conjunto de reglas y hechos iniciales.
# - Encadenamiento hacia adelante: Deriva todos los hechos posibles.
# - Encadenamiento hacia atrás: Verifica si un objetivo específico puede ser derivado.

if __name__ == "__main__":
    # Encadenamiento hacia adelante
    print("Encadenamiento hacia adelante:")
    hechos_finales = encadenamiento_hacia_adelante(hechos_iniciales, reglas)
    print("Hechos derivados:", hechos_finales)

    # Encadenamiento hacia atrás
    print("\nEncadenamiento hacia atrás:")
    objetivo = "E"  # Queremos verificar si E puede ser derivado.
    puede_derivarse = encadenamiento_hacia_atras(objetivo, hechos_iniciales, reglas)
    print(f"¿El objetivo '{objetivo}' puede ser derivado?:", puede_derivarse)

# ------------------------------------------------------------------------------------
# EXPLICACIÓN DETALLADA DEL ALGORITMO
# ------------------------------------------------------------------------------------
# 1. Encadenamiento hacia adelante:
#    - Parte de los hechos iniciales y aplica las reglas para derivar nuevos hechos.
#    - Se detiene cuando no se pueden derivar más hechos nuevos.
#    - Ventaja: Útil para descubrir todos los hechos posibles a partir de un conjunto inicial.
#
# 2. Encadenamiento hacia atrás:
#    - Parte de un objetivo y verifica si puede ser derivado mediante las reglas.
#    - Utiliza recursión para verificar las dependencias de las condiciones.
#    - Ventaja: Útil para responder preguntas específicas sobre si un hecho puede ser derivado.
#
# Suposiciones clave:
# - Las reglas son determinísticas (si las condiciones se cumplen, la conclusión es verdadera).
# - Los hechos iniciales son correctos y completos.
#
# Ventajas:
# - Ambos algoritmos son simples y efectivos para sistemas basados en reglas.
# Limitaciones:
# - No manejan incertidumbre ni conflictos entre reglas.