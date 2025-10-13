import random
import time

# --- Datos del juego ---
personajes = [
    "Mickey Mouse",
    "Minnie Mouse",
    "Goofy",
    "Donald",
    "Daisy"
]

profesiones = {
    "Mickey Mouse": "Presentador de fiestas",
    "Minnie Mouse": "Diseñadora de modas",
    "Goofy": "Jardinero despistado",
    "Donald": "Chef del club",
    "Daisy": "Fotógrafa profesional"
}

locaciones = [
    "la Cocina",
    "el Jardín",
    "la Sala Principal",
    "el Estudio de Fotografía",
    "el Taller de Modas"
]

armas = [
    "una sartén",
    "unas tijeras",
    "una regadera",
    "un micrófono",
    "una cámara fotográfica"
]

# --- Generar combinación secreta ---
culpable = random.choice(personajes)
arma_usada = random.choice(armas)
lugar_crimen = random.choice(locaciones)

# --- Pistas ---
pistas = {
    "Mickey Mouse": [
        "Parecía muy nervioso por su discurso.",
        "Tenía algo de harina en las manos.",
        "Estaba practicando frente al micrófono."
    ],
    "Minnie Mouse": [
        "Se la pasó en su taller todo el día.",
        "Tenía unas tijeras nuevas muy filosas.",
        "Parecía molesta con alguien."
    ],
    "Goofy": [
        "Estaba regando el jardín pero mojó todo.",
        "Llevaba una regadera vacía corriendo por la casa.",
        "Decía que escuchó un golpe fuerte en la sala."
    ],
    "Donald": [
        "Estuvo cocinando en la cocina todo el tiempo.",
        "Se le vio con una sartén en la mano.",
        "Se enojó porque el pastel no estaba listo."
    ],
    "Daisy": [
        "Estaba tomando fotos del evento.",
        "Su cámara se cayó al suelo y se rompió algo.",
        "Se quejaba de que el flash no funcionaba bien."
    ]
}

# --- Funciones del juego ---
def mostrar_intro():
    print("🕵️‍♂️ BIENVENIDO AL MISTERIO EN LA CASA DE MICKEY 🏠\n")
    print("Durante la gran fiesta, el pastel principal fue destruido justo antes de servirlo.")
    print("Tu misión es descubrir QUIÉN lo hizo, CON QUÉ y EN DÓNDE.\n")
    input("Presiona ENTER para comenzar tu investigación...")

def menu_principal():
    print("\n🔍 ¿Qué deseas hacer ahora?")
    print("1. Interrogar a un personaje")
    print("2. Visitar una locación")
    print("3. Examinar un objeto (arma)")
    print("4. Hacer una acusación final")
    print("5. Salir del juego")
    opcion = input("Selecciona una opción (1-5): ")
    return opcion

def interrogar():
    sospechoso = random.choice(personajes)
    pista = random.choice(pistas[sospechoso])
    print(f"\n👤 Interrogas a {sospechoso} ({profesiones[sospechoso]}):")
    time.sleep(1)
    print(f"🗣️ {pista}")
    if sospechoso == culpable:
        print("🤔 Notas que parece un poco nervioso...")
    input("\nPresiona ENTER para continuar...")

def visitar_lugar():
    lugar = random.choice(locaciones)
    print(f"\n🏠 Visitas {lugar}...")
    time.sleep(1)
    if lugar == lugar_crimen:
        print("❗ Hay señales de que algo ocurrió aquí... ¡una pista importante!")
    else:
        print("No parece haber nada extraño por ahora.")
    input("\nPresiona ENTER para continuar...")

def examinar_arma():
    arma = random.choice(armas)
    print(f"\n🔧 Inspeccionas {arma}...")
    time.sleep(1)
    if arma == arma_usada:
        print("🩸 Tiene rastros del pastel y parece haber sido usada recientemente.")
    else:
        print("Está limpia y bien guardada.")
    input("\nPresiona ENTER para continuar...")

def acusar():
    print("\n⚖️ Es momento de hacer tu acusación final.")
    sospechoso = input("¿Quién crees que fue el culpable?: ")
    arma = input("¿Con qué arma lo hizo?: ")
    lugar = input("¿En qué lugar ocurrió?: ")

    print("\nRevisando tu acusación...")
    time.sleep(2)

    if (sospechoso == culpable and arma == arma_usada and lugar == lugar_crimen):
        print(f"\n🎉 ¡Felicidades! Has resuelto el misterio correctamente.")
    else:
        print(f"\n❌ Fallaste, detective. El verdadero culpable fue {culpable}, con {arma_usada} en {lugar_crimen}.")
    print("\n--- FIN DEL JUEGO ---")
    exit()

# --- Juego principal ---
def clue_mickey_interactivo():
    mostrar_intro()
    while True:
        opcion = menu_principal()
        if opcion == "1":
            interrogar()
        elif opcion == "2":
            visitar_lugar()
        elif opcion == "3":
            examinar_arma()
        elif opcion == "4":
            acusar()
        elif opcion == "5":
            print("\n👋 Gracias por jugar. ¡Hasta la próxima, detective!")
            break
        else:
            print("❗ Opción no válida, intenta de nuevo.")

# --- Iniciar juego ---
if __name__ == "__main__":
    clue_mickey_interactivo()
