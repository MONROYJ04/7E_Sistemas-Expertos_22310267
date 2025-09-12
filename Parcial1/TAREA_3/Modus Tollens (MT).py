# ------------------------------------------------------------------------------------
# CÓDIGO EDUCATIVO: MODUS TOLLENS (MT) – DEDUCCIÓN POR NEGACIÓN
# ------------------------------------------------------------------------------------
# Caso práctico: Diagnóstico de fallas en máquina CNC
# Usamos Modus Tollens para deducir posibles causas a partir de resultados que no ocurren
# ------------------------------------------------------------------------------------


# Reglas: (condición, consecuencia) con descripciones
reglas = [
    ("husillo_danado", "produccion_detenerse"),  # Si el husillo está dañado, la producción se detiene
    ("produccion_detenerse", "mantenimiento_urgente"),  # Si la producción se detiene, se requiere mantenimiento urgente
    ("corriente_activa", "motor_encendido"),  # Si hay corriente, el motor está encendido
    ("presion_baja", "alarma_presion"),  # Si la presión es baja, se activa la alarma
    ("sensor_temperatura_falla", "alarma_temperatura"),  # Si el sensor de temperatura falla, se activa la alarma
]

# Hechos que NO ocurrieron (con descripciones)
hechos_no_ocurridos = [
    "produccion_detenerse",  # La producción NO se detuvo
    "alarma_presion"         # La alarma de presión NO se activó
]


# Función mejorada para aplicar Modus Tollens en cadena
def modus_tollens_cadena(reglas, hechos_no_ocurridos):
    conclusiones_negativas = set()
    hechos_no_ocurridos = set(hechos_no_ocurridos)
    paso = 1
    explicaciones = []

    print("\n==============================================")
    print("=== PROCESO: MODUS TOLLENS (MT) – DIAGNÓSTICO EN CADENA ===")
    print("==============================================")
    print("Hechos que NO ocurrieron (negados):")
    for hecho in hechos_no_ocurridos:
        if hecho == "produccion_detenerse":
            print("- produccion_detenerse: La producción NO se detuvo")
        elif hecho == "alarma_presion":
            print("- alarma_presion: La alarma de presión NO se activó")
        else:
            print(f"- {hecho}")
    print("----------------------------------------------")

    nuevos = True
    while nuevos:
        nuevos = False
        for condicion, consecuencia in reglas:
            if consecuencia in hechos_no_ocurridos and condicion not in conclusiones_negativas:
                print(f"\nPaso {paso}: '{consecuencia}' NO ocurrió → Por Modus Tollens, '{condicion}' tampoco ocurrió")
                explicacion = f"Si '{condicion}' entonces '{consecuencia}'. Como '{consecuencia}' NO ocurrió, se deduce que '{condicion}' tampoco ocurrió."
                print(f"  [Explicación] {explicacion}")
                conclusiones_negativas.add(condicion)
                hechos_no_ocurridos.add(condicion)
                nuevos = True
                paso += 1

    print("\n----------------------------------------------")
    print("RESUMEN FINAL (Modus Tollens en cadena):")
    if conclusiones_negativas:
        print("Conclusiones deducidas por negación:")
        for c in sorted(conclusiones_negativas):
            if c == "husillo_danado":
                print("- husillo_danado: El husillo NO está dañado")
            elif c == "presion_baja":
                print("- presion_baja: No hubo presión baja en el sistema")
            elif c == "sensor_temperatura_falla":
                print("- sensor_temperatura_falla: El sensor de temperatura NO falló")
            elif c == "corriente_activa":
                print("- corriente_activa: No hubo corriente activa")
            else:
                print(f"- {c}: No ocurrió")
    else:
        print("No se pudo deducir ninguna causa negada a partir de los hechos proporcionados.")
    print("==============================================\n")
    return list(conclusiones_negativas)

# ------------------------------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------------------------------
if __name__ == "__main__":
    resultado_negativo = modus_tollens_cadena(reglas, hechos_no_ocurridos)
