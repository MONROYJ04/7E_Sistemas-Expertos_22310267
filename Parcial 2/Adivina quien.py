# ------------------------------------------------------
# Sistema Experto Mejorado "Adivina Quién - Naruto Edition"
# 32 personajes
# ------------------------------------------------------

# -------------------------------
# Definición de personajes
# -------------------------------
personajes = [
    {"nombre": "Naruto Uzumaki", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": False, "akatsuki": False},

    {"nombre": "Sasuke Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Sakura Haruno", "pelo": "rosa", "aldea": "konoha", "clan": "ninguno",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Kakashi Hatake", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": True, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Hinata Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": True, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Itachi Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": True},

    {"nombre": "Jiraiya", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": True, "inteligente": True, "akatsuki": False},

    {"nombre": "Tsunade", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "genero": "femenino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": True, "inteligente": True, "akatsuki": False},

    {"nombre": "Gaara", "pelo": "rojo", "aldea": "suna", "clan": "ninguno",
     "genero": "masculino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Shikamaru Nara", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Neji Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": True, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Rock Lee", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": False, "akatsuki": False},

    {"nombre": "Temari", "pelo": "rubio", "aldea": "suna", "clan": "ninguno",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Kankuro", "pelo": "negro", "aldea": "suna", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": True, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Pain", "pelo": "naranja", "aldea": "akatsuki", "clan": "ninguno",
     "genero": "masculino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": True},

    {"nombre": "Konan", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": True},

    {"nombre": "Kisame Hoshigaki", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": False, "akatsuki": True},

    {"nombre": "Obito Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "genero": "masculino", "lider": False, "mascara": True, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": True},

    {"nombre": "Madara Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Minato Namikaze", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Obito (Tobi)", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "genero": "masculino", "lider": False, "mascara": True, "sharingan": True,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": True},

    {"nombre": "Hiruzen Sarutobi", "pelo": "gris", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": True, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Shino Aburame", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": True, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Kiba Inuzuka", "pelo": "marron", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Akamaru", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": False, "akatsuki": False},

    {"nombre": "Sai", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Ino Yamanaka", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Choji Akimichi", "pelo": "marron", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Tenten", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "femenino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Haku", "pelo": "negro", "aldea": "otra", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Zabuza Momochi", "pelo": "negro", "aldea": "otra", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Orochimaru", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": True, "inteligente": True, "akatsuki": False},

    {"nombre": "Kabuto Yakushi", "pelo": "gris", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Saiyuki", "pelo": "blanco", "aldea": "otra", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Orochimaru joven", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": True, "inteligente": True, "akatsuki": False},

    {"nombre": "Yamato", "pelo": "marron", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False},

    {"nombre": "Sarutobi Asuma", "pelo": "marron", "aldea": "konoha", "clan": "ninguno",
     "genero": "masculino", "lider": False, "mascara": False, "sharingan": False,
     "byakugan": False, "sannin": False, "inteligente": True, "akatsuki": False}
]

# -------------------------------
# Funciones de entrada
# -------------------------------
def preguntar(opcion, opciones):
    while True:
        resp = input(opcion + f" {opciones}: ").strip().lower()
        if resp in opciones or resp == "no_se":
            return resp
        else:
            print("Responde una opción válida:", opciones, "o 'no_se' si no sabes.")

def preguntar_bool(opcion):
    while True:
        resp = input(opcion + " (si/no/no_se): ").strip().lower()
        if resp in ["si", "no"]:
            return resp == "si"
        elif resp == "no_se":
            return None
        else:
            print("Escribe 'si', 'no' o 'no_se'.")

# -------------------------------
# Recolección de hechos
# -------------------------------
def recolectar_hechos():
    hechos = {}
    hechos["pelo"] = preguntar("¿De qué color tiene el pelo tu personaje?", ["rubio","negro","blanco","rosa","rojo","gris","marron","azul","naranja"])
    hechos["aldea"] = preguntar("¿A qué aldea pertenece?", ["konoha","suna","akatsuki","otra"])
    hechos["clan"] = preguntar("¿A qué clan pertenece?", ["uchiha","hyuga","ninguno"])
    hechos["genero"] = preguntar("¿Tu personaje es masculino o femenino?", ["masculino","femenino"])
    hechos["lider"] = preguntar_bool("¿Es líder o Hokage?")
    hechos["mascara"] = preguntar_bool("¿Usa máscara?")
    hechos["sharingan"] = preguntar_bool("¿Tiene Sharingan?")
    hechos["byakugan"] = preguntar_bool("¿Tiene Byakugan?")
    hechos["sannin"] = preguntar_bool("¿Es uno de los Sannin?")
    hechos["inteligente"] = preguntar_bool("¿Destaca por su inteligencia?")
    hechos["akatsuki"] = preguntar_bool("¿Pertenece a la organización Akatsuki?")
    return hechos

# -------------------------------
# Motor de inferencia mejorado
# -------------------------------
def inferir(hechos):
    candidatos = personajes.copy()

    # 🔹 Filtrar por género y clan si se saben
    for attr in ["genero","clan"]:
        if hechos[attr] not in [None,"no_se"]:
            candidatos = [p for p in candidatos if p[attr]==hechos[attr]]

    # 🔹 Si no quedan candidatos
    if not candidatos:
        print("\n⚠️ No se encontró ningún personaje que coincida con género y clan.")
        return

    # 🔹 Puntuar coincidencias parciales
    puntajes = []
    for personaje in candidatos:
        score = 0
        total = 0
        for attr, valor in personaje.items():
            if attr == "nombre":
                continue
            if hechos[attr] is None:
                continue
            total += 1
            if hechos[attr] == valor:
                score += 1
        puntajes.append((score, personaje["nombre"]))

    # 🔹 Ordenar de mayor a menor
    puntajes.sort(reverse=True)
    mejor = puntajes[0]
    if mejor[0]==0:
        print("\nNo se encontró ningún personaje que coincida con los atributos dados.")
    else:
        print(f"\nEl personaje más probable es: {mejor[1]} (coincidencias: {mejor[0]})")

# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    print("Sistema Experto Mejorado: Adivina Quién - Naruto Edition (32 personajes)\n")
    
    while True:  # 🔹 Bucle principal hasta acertar
        hechos_usuario = recolectar_hechos()
        inferir(hechos_usuario)
        
        # Preguntar si el personaje adivinado fue correcto
        correcto = input("\n¿El personaje adivinado es correcto? (si/no): ").strip().lower()
        if correcto == "si":
            print("¡Genial! Me alegra haber adivinado tu personaje.")
            break  # 🔹 Salir del bucle
        else:
            print("\nOk, vamos a intentarlo de nuevo.\n")