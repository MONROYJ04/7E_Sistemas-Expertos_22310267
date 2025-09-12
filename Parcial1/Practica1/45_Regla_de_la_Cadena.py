#Algoritmo Regla de la Cadena aplicado a la produccion de modulo electronicos 
#Joaquin Monroy Navarro_22310267
#Descripcion
#Este programa la probabilidad de que un modulo elecronico pase 
#todas las etapas de produccion (inspeccion, soldadura, pruebas)
#utilizando la Regla de Cadena en probabilidad 
#


# Algoritmo: Regla de la Cadena aplicado a la producción de módulos electrónicos
# Autor: Ejemplo educativo
# Descripción:
# Este programa calcula la probabilidad de que un módulo electrónico pase
# todas las etapas del proceso de producción (inspección, soldadura, pruebas)
# utilizando la Regla de la Cadena en probabilidad.

def regla_de_la_cadena(probabilidades_condicionales):
    """
    Calcula la probabilidad conjunta mostrando paso a paso cómo se aplica la
    Regla de la Cadena en probabilidad.

    :param probabilidades_condicionales: Lista de probabilidades condicionales en orden.
    :return: Probabilidad conjunta de los eventos.
    """
    probabilidad_conjunta = 1.0

    print("=== PROCESO DE CÁLCULO ===")
    for i, probabilidad in enumerate(probabilidades_condicionales, start=1):
        print(f"Etapa {i}: Multiplicamos {round(probabilidad_conjunta, 4)} x {probabilidad}")
        probabilidad_conjunta *= probabilidad
        print(f"  → Resultado parcial tras etapa {i}: {round(probabilidad_conjunta, 4)}\n")

    return probabilidad_conjunta


# Caso práctico en industria electrónica:
# Etapas de producción de un módulo:
# 1. Inspección de componentes: P(A) = 0.95
# 2. Soldadura automatizada: P(B|A) = 0.90
# 3. Prueba funcional intermedia: P(C|A∩B) = 0.85
# 4. Prueba de estrés térmico: P(D|A∩B∩C) = 0.80


# Nombres de las etapas para referencia
etapas = [
    "Inspección de componentes",
    "Soldadura automatizada",
    "Prueba funcional intermedia",
    "Prueba de estrés térmico"
]

probabilidades = [0.95, 0.90, 0.85, 0.80]

# Ejecutamos el cálculo paso a paso
resultado = regla_de_la_cadena(probabilidades)

# Identificar la etapa más débil
min_prob = min(probabilidades)
indice_min = probabilidades.index(min_prob)
etapa_mas_debil = etapas[indice_min]

print("===================================")
print("La probabilidad final de que un módulo pase TODAS las etapas es:", round(resultado, 4))
print("Esto equivale a", round(resultado*100, 2), "% de éxito en la producción.")
print()
print(f"La etapa más crítica a mejorar es: '{etapa_mas_debil}' con una probabilidad de {min_prob}.")
print("Se recomienda enfocar esfuerzos de mejora en esta área para aumentar el éxito global.")
