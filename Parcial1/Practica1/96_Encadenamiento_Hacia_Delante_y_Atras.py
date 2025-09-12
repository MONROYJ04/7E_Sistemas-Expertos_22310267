# ------------------------------------------------------------------------------------
# CÓDIGO EDUCATIVO: ENCADENAMIENTO HACIA ADELANTE Y HACIA ATRÁS (APLICACIÓN EN INDUSTRIA)
# ------------------------------------------------------------------------------------
# Este programa simula un sistema de reglas aplicado a la industria de manufactura.
# Caso práctico: Diagnóstico de fallas en una máquina CNC.
#
# Reglas (si ... entonces ...):
# 1. Si la máquina presenta vibración (A) y ruido extraño (B), entonces el husillo está dañado (C).
# 2. Si el husillo está dañado (C), entonces la producción se detiene (D).
# 3. Si la producción se detiene (D), entonces se requiere mantenimiento urgente (E).
#
# Hechos iniciales: vibración (A) y ruido extraño (B).
#
# Encadenamiento hacia adelante → descubre todos los hechos posibles a partir de A y B.
# Encadenamiento hacia atrás → verifica si un objetivo (E = mantenimiento urgente) se puede derivar.
# ------------------------------------------------------------------------------------

# Definimos las reglas como pares: ([condiciones], conclusión)
reglas = [
    (["A", "B"], "C"),  # Si hay vibración y ruido extraño → husillo dañado.
    (["C"], "D"),       # Si husillo dañado → producción se detiene.
    (["D"], "E")        # Si producción detenida → mantenimiento urgente.
]

# Hechos iniciales conocidos
hechos_iniciales = ["A", "B"]  # Vibración y ruido extraño

# ------------------------------------------------------------------------------------
# FUNCIÓN: Encadenamiento hacia adelante
# ------------------------------------------------------------------------------------
def encadenamiento_hacia_adelante(hechos, reglas):
    """
    Deriva nuevos hechos a partir de los iniciales, mostrando cada paso.
    """
    hechos_derivados = set(hechos)  # Evitamos duplicados
    cambio = True
    paso = 1  # Contador de pasos para mostrar proceso

    print("\n==============================================")
    print("=== PROCESO: ENCADENAMIENTO HACIA ADELANTE ===")
    print("==============================================")
    print("Hechos iniciales:", hechos)
    print("----------------------------------------------")

    while cambio:
        cambio = False
        for condiciones, conclusion in reglas:
            # Verificamos si todas las condiciones se cumplen
            if all(condicion in hechos_derivados for condicion in condiciones):
                if conclusion not in hechos_derivados:
                    print(f"\nPaso {paso}: Se cumplen {condiciones} → Se añade '{conclusion}' a los hechos.")
                    hechos_derivados.add(conclusion)
                    print(f"  Hechos actuales: {sorted(list(hechos_derivados))}")
                    cambio = True
                    paso += 1
    print("\n----------------------------------------------")
    print("RESUMEN FINAL (Hacia Adelante):")
    print("Hechos derivados finales:", sorted(list(hechos_derivados)))
    print("==============================================\n")
    return list(hechos_derivados)

# ------------------------------------------------------------------------------------
# FUNCIÓN: Encadenamiento hacia atrás
# ------------------------------------------------------------------------------------
def encadenamiento_hacia_atras(objetivo, hechos, reglas, nivel=1):
    """
    Verifica si un objetivo puede derivarse, mostrando la recursión paso a paso.
    """
    indent = "  " * (nivel - 1)  # Sangría para ver recursión
    print(f"{indent}¿Podemos derivar '{objetivo}'?")

    # Caso base: el hecho ya está en los iniciales
    if objetivo in hechos:
        print(f"{indent}✔ '{objetivo}' es un hecho conocido (base de hechos).")
        return True

    # Recorremos reglas que concluyan el objetivo
    for condiciones, conclusion in reglas:
        if conclusion == objetivo:
            print(f"{indent}Regla encontrada: Si {condiciones} entonces {conclusion}")
            # Verificamos cada condición recursivamente
            todas_cumplen = True
            for cond in condiciones:
                if not encadenamiento_hacia_atras(cond, hechos, reglas, nivel + 1):
                    todas_cumplen = False
            if todas_cumplen:
                print(f"{indent}✔ '{objetivo}' puede derivarse (todas las condiciones se cumplen).")
                return True

    print(f"{indent}✘ '{objetivo}' NO puede derivarse (no se cumplen todas las condiciones o no hay regla).")
    return False

# ------------------------------------------------------------------------------------
# EJECUCIÓN DEL CÓDIGO
# ------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Hacia adelante
    hechos_finales = encadenamiento_hacia_adelante(hechos_iniciales, reglas)

    # Hacia atrás
    print("\n==============================================")
    print("=== PROCESO: ENCADENAMIENTO HACIA ATRÁS   ===")
    print("==============================================")
    objetivo = "E"  # Queremos verificar si se puede concluir "mantenimiento urgente"
    print(f"\nObjetivo a verificar: '{objetivo}' (¿Se puede derivar?)\n")
    resultado = encadenamiento_hacia_atras(objetivo, hechos_iniciales, reglas)
    print("\n----------------------------------------------")
    print("RESUMEN FINAL (Hacia Atrás):")
    if resultado:
        print(f"✔ El objetivo '{objetivo}' SÍ puede derivarse a partir de los hechos iniciales y las reglas.")
    else:
        print(f"✘ El objetivo '{objetivo}' NO puede derivarse a partir de los hechos iniciales y las reglas.")
    print("==============================================\n")
