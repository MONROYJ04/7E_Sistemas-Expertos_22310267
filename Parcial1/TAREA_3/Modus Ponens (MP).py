# ------------------------------------------------------------------------------------
# CÓDIGO EDUCATIVO: MODUS PONENS (MP) – DIAGNÓSTICO DE PLANTA INDUSTRIAL
# ------------------------------------------------------------------------------------
# Escenario: Planta de producción con varias máquinas
# Objetivo: Diagnosticar fallas y efectos encadenados usando Modus Ponens
# ------------------------------------------------------------------------------------

# ---------------------------------------------
# REGLAS: Condición → Consecuencia (con descripciones realistas)
# ---------------------------------------------
reglas = [
    # Fallas en máquinas
    (["vibracion_alta_maquina1"], "husillo_danado_maquina1"),  # Si la máquina 1 vibra mucho, el husillo puede estar dañado
    (["vibracion_alta_maquina2"], "husillo_danado_maquina2"),
    (["ruido_extraño_maquina1"], "husillo_danado_maquina1"),   # Ruidos extraños también indican daño
    (["ruido_extraño_maquina2"], "husillo_danado_maquina2"),
    # Consecuencias de fallas
    (["husillo_danado_maquina1"], "produccion_maquina1_detenerse"),  # Si el husillo está dañado, la máquina se detiene
    (["husillo_danado_maquina2"], "produccion_maquina2_detenerse"),
    # Efecto en la línea de producción
    (["produccion_maquina1_detenerse", "produccion_maquina2_detenerse"], "linea_produccion_detenerse"),  # Si ambas máquinas se detienen, la línea para
    (["linea_produccion_detenerse"], "alerta_supervisor_encendida"),  # Se enciende una alerta para el supervisor
    # Otros problemas
    (["temperatura_elevada_maquina1"], "falla_refrigeracion_maquina1"),  # Temperatura alta indica falla en refrigeración
    (["falla_refrigeracion_maquina1"], "reduccion_velocidad_maquina1"),  # Si falla la refrigeración, se reduce la velocidad
    (["reduccion_velocidad_maquina1", "reduccion_velocidad_maquina2"], "linea_produccion_mas_lenta")  # Si ambas bajan velocidad, la línea es más lenta
]

# ---------------------------------------------
# HECHOS INICIALES CONOCIDOS (con descripciones)
# ---------------------------------------------
hechos_iniciales = [
    "vibracion_alta_maquina1",         # Sensor detecta vibración anormal en máquina 1
    "ruido_extraño_maquina2",         # Operador reporta ruido extraño en máquina 2
    "temperatura_elevada_maquina1"     # Sensor detecta temperatura elevada en máquina 1
]

# ---------------------------------------------
# FUNCION: Modus Ponens (MP)
# ---------------------------------------------
def modus_ponens(reglas, hechos):
    hechos_derivados = set(hechos)
    cambio = True
    paso = 1

    print("\n==============================================")
    print("=== PROCESO: MODUS PONENS (MP) – DIAGNÓSTICO DE PLANTA INDUSTRIAL ===")
    print("==============================================")
    print("Hechos iniciales (con descripciones):")
    for hecho in hechos:
        if hecho == "vibracion_alta_maquina1":
            print("- vibracion_alta_maquina1: Sensor detecta vibración anormal en máquina 1")
        elif hecho == "ruido_extraño_maquina2":
            print("- ruido_extraño_maquina2: Operador reporta ruido extraño en máquina 2")
        elif hecho == "temperatura_elevada_maquina1":
            print("- temperatura_elevada_maquina1: Sensor detecta temperatura elevada en máquina 1")
        else:
            print(f"- {hecho}")
    print("----------------------------------------------")

    while cambio:
        cambio = False
        for condiciones, consecuencia in reglas:
            if all(cond in hechos_derivados for cond in condiciones) and consecuencia not in hechos_derivados:
                # Mensaje más descriptivo para cada deducción
                print(f"\nPaso {paso}: Se cumplen {condiciones} → Se deduce '{consecuencia}'")
                if consecuencia == "husillo_danado_maquina1":
                    print("  [Diagnóstico] Husillo de máquina 1 probablemente dañado. Requiere inspección.")
                elif consecuencia == "husillo_danado_maquina2":
                    print("  [Diagnóstico] Husillo de máquina 2 probablemente dañado. Requiere inspección.")
                elif consecuencia == "produccion_maquina1_detenerse":
                    print("  [Acción] Producción de máquina 1 detenida automáticamente.")
                elif consecuencia == "produccion_maquina2_detenerse":
                    print("  [Acción] Producción de máquina 2 detenida automáticamente.")
                elif consecuencia == "linea_produccion_detenerse":
                    print("  [Impacto] Toda la línea de producción se detiene. Se requiere intervención.")
                elif consecuencia == "alerta_supervisor_encendida":
                    print("  [Alerta] Supervisor notificado por sistema de monitoreo.")
                elif consecuencia == "falla_refrigeracion_maquina1":
                    print("  [Diagnóstico] Falla en sistema de refrigeración de máquina 1. Revisar urgentemente.")
                elif consecuencia == "reduccion_velocidad_maquina1":
                    print("  [Acción] Velocidad de máquina 1 reducida para evitar daños mayores.")
                elif consecuencia == "linea_produccion_mas_lenta":
                    print("  [Impacto] La línea de producción opera a menor velocidad. Riesgo de retrasos.")
                hechos_derivados.add(consecuencia)
                print(f"  Hechos actuales: {sorted(list(hechos_derivados))}")
                cambio = True
                paso += 1

    print("\n----------------------------------------------")
    print("RESUMEN FINAL (MP):")
    print("Hechos derivados finales:", sorted(list(hechos_derivados)))
    print("==============================================\n")
    return list(hechos_derivados)

# ---------------------------------------------
# EJECUCIÓN DEL CÓDIGO
# ---------------------------------------------
if __name__ == "__main__":
    hechos_finales = modus_ponens(reglas, hechos_iniciales)
