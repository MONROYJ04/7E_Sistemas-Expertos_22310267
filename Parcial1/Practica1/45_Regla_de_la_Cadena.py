# Este algoritmo implementa la Regla de la Cadena en probabilidad.
# La Regla de la Cadena se utiliza para calcular la probabilidad conjunta de varios eventos
# en función de las probabilidades condicionales de los eventos.

# Definimos una función que calcula la probabilidad conjunta de una lista de eventos
# utilizando la Regla de la Cadena.
def regla_de_la_cadena(probabilidades_condicionales):
    """
    Calcula la probabilidad conjunta de una lista de eventos utilizando la Regla de la Cadena.

    :param probabilidades_condicionales: Lista de probabilidades condicionales en orden.
    :return: Probabilidad conjunta de los eventos.
    """
    # Inicializamos la probabilidad conjunta en 1 (neutro multiplicativo)
    probabilidad_conjunta = 1.0

    # Iteramos sobre las probabilidades condicionales y las multiplicamos
    for probabilidad in probabilidades_condicionales:
        probabilidad_conjunta *= probabilidad

    # Retornamos la probabilidad conjunta calculada
    return probabilidad_conjunta


# Ejemplo práctico:
# Supongamos que queremos calcular la probabilidad conjunta de tres eventos A, B y C:
# P(A ∩ B ∩ C) = P(A) * P(B | A) * P(C | A ∩ B)
# Donde:
# P(A) = 0.6 (probabilidad de que ocurra el evento A)
# P(B | A) = 0.5 (probabilidad de que ocurra B dado que ocurrió A)
# P(C | A ∩ B) = 0.4 (probabilidad de que ocurra C dado que ocurrieron A y B)

# Definimos las probabilidades condicionales en orden
probabilidades = [0.6, 0.5, 0.4]

# Calculamos la probabilidad conjunta utilizando la función
resultado = regla_de_la_cadena(probabilidades)

# Mostramos el resultado con un mensaje explicativo
print("La probabilidad conjunta de los eventos A, B y C es:", resultado)

# Explicación del resultado:
# En este caso, el algoritmo calcula P(A ∩ B ∩ C) = 0.6 * 0.5 * 0.4 = 0.12
# Esto significa que la probabilidad de que ocurran los tres eventos juntos es del 12%.