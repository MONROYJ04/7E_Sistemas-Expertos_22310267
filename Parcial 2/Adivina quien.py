# ------------------------------------------------------
# Adivina Quién - Naruto Edition (Interfaz Visual Final)
# 15 personajes completos
# ------------------------------------------------------

import PySimpleGUI as sg
import json
import re
import unicodedata
import os

# -------------------------------
# Funciones de texto y keywords
# -------------------------------
STOPWORDS = {
    "el","la","los","las","un","una","unos","unas","y","o","de","del","que","es","en","por","con",
    "para","su","sus","al","se","lo","como","su","este","esta","estos","estas","ha","han","pero","no",
    "una","uno","tu","tú","si","sí","fue","son","ser","esta","esta"
}

JSON_FILE = "personajes.json"

def quitar_acentos(texto: str) -> str:
    texto_norm = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto_norm if not unicodedata.combining(c))

def limpiar_texto(texto: str) -> str:
    t = texto.strip()
    t = re.sub(r'\s+', ' ', t)
    return t

def formar_pregunta_canonica(frase: str) -> str:
    frase = limpiar_texto(frase)
    if not frase:
        return frase
    frase = frase[0].upper() + frase[1:]
    if not frase.startswith('¿'):
        frase = '¿' + frase
    if not frase.endswith('?'):
        frase = frase + '?'
    return frase

def extraer_keywords(frase: str, max_keywords: int = 6) -> list:
    s = frase.lower()
    s = s.replace('¿', ' ').replace('?', ' ')
    s = re.sub(r'[^\w\s]', ' ', s)
    s = quitar_acentos(s)
    s = limpiar_texto(s)
    tokens = s.split(' ')
    keywords = []
    for t in tokens:
        if t and t not in STOPWORDS and len(t) > 1:
            if t not in keywords:
                keywords.append(t)
        if len(keywords) >= max_keywords:
            break
    return keywords

def generar_regex_keywords(keywords: list) -> str:
    if not keywords:
        return None
    esc = [re.escape(k) for k in keywords]
    pattern = r'\b(?:' + '|'.join(esc) + r')\b'
    return pattern

def procesar_pregunta_clave(raw: str):
    frase = limpiar_texto(raw)
    pregunta = formar_pregunta_canonica(frase)
    keywords = extraer_keywords(frase)
    regex = generar_regex_keywords(keywords)
    return {
        "pregunta_canonica": pregunta,
        "keywords": keywords,
        "regex": regex
    }

# -------------------------------
# Funciones de persistencia
# -------------------------------
def cargar_personajes():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return personajes_base.copy()

def guardar_personajes(lista):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# -------------------------------
# Funciones de GUI
# -------------------------------
def preguntar_bool_gui(pregunta):
    layout = [
        [sg.Text(pregunta)],
        [sg.Button("Sí"), sg.Button("No"), sg.Button("No sé")]
    ]
    window = sg.Window("Pregunta", layout)
    while True:
        event, _ = window.read()
        if event == "Sí":
            window.close()
            return True
        elif event == "No":
            window.close()
            return False
        elif event == "No sé" or event == sg.WIN_CLOSED:
            window.close()
            return None

def preguntar_clave_gui(p_personaje):
    pregunta = p_personaje.get("pregunta_clave", "")
    regex = p_personaje.get("pregunta_clave_regex", "")
    layout = [
        [sg.Text(pregunta)],
        [sg.Input(key="-RESP-")],
        [sg.Button("Enviar")]
    ]
    window = sg.Window("Pregunta Clave", layout)
    while True:
        event, values = window.read()
        if event == "Enviar":
            respuesta = values["-RESP-"].strip()
            low = respuesta.lower()
            if low in ["si", "sí"]:
                window.close()
                return True
            elif low == "no":
                window.close()
                return False
            elif low == "no_se":
                window.close()
                return None
            normalizada = quitar_acentos(low)
            if regex and re.search(regex, normalizada):
                window.close()
                return True
            else:
                window.close()
                return None
        if event == sg.WIN_CLOSED:
            window.close()
            return None

def jugar_gui():
    personajes = cargar_personajes()
    hechos = {}
    hechos["lider"] = preguntar_bool_gui("¿Es líder o Hokage?")
    hechos["mascara"] = preguntar_bool_gui("¿Usa máscara?")
    hechos["sharingan"] = preguntar_bool_gui("¿Tiene Sharingan?")
    hechos["byakugan"] = preguntar_bool_gui("¿Tiene Byakugan?")
    hechos["sannin"] = preguntar_bool_gui("¿Es uno de los Sannin?")
    hechos["inteligente"] = preguntar_bool_gui("¿Destaca por su inteligencia?")
    hechos["akatsuki"] = preguntar_bool_gui("¿Pertenece a la organización Akatsuki?")

    candidatos = personajes.copy()
    for attr in hechos:
        if hechos[attr] is not None:
            candidatos = [p for p in candidatos if p[attr] == hechos[attr]]

    if not candidatos:
        sg.popup("No se pudo determinar ningún personaje con esas respuestas.")
        if sg.popup_yes_no("¿Deseas agregar un nuevo personaje?") == "Yes":
            aprender_personaje_gui()
        return

    while candidatos:
        p = candidatos[0]
        if len(candidatos) == 1:
            if sg.popup_yes_no(f"¿Tu personaje es {p['nombre']}?") == "Yes":
                sg.popup(f"¡Genial! Se adivinó a {p['nombre']}")
                return
            else:
                candidatos.remove(p)
        else:
            res = preguntar_clave_gui(p)
            if res is True:
                sg.popup(f"¡Genial! Se adivinó a {p['nombre']}")
                return
            elif res is False:
                candidatos.remove(p)
            else:
                candidatos.remove(p)

    sg.popup("No se pudo adivinar el personaje. Considera agregar más información o preguntas.")
    if sg.popup_yes_no("¿Deseas agregar un nuevo personaje?") == "Yes":
        aprender_personaje_gui()

def aprender_personaje_gui():
    personajes = cargar_personajes()
    layout = [
        [sg.Text("Nombre del personaje:"), sg.Input(key="-NOMBRE-")],
        [sg.Button("Continuar")]
    ]
    window = sg.Window("Agregar Personaje", layout)
    event, values = window.read()
    nombre = values["-NOMBRE-"].strip()
    window.close()

    nuevo = {"nombre": nombre}
    nuevo["lider"] = preguntar_bool_gui("¿Es líder o Hokage?")
    nuevo["mascara"] = preguntar_bool_gui("¿Usa máscara?")
    nuevo["sharingan"] = preguntar_bool_gui("¿Tiene Sharingan?")
    nuevo["byakugan"] = preguntar_bool_gui("¿Tiene Byakugan?")
    nuevo["sannin"] = preguntar_bool_gui("¿Es uno de los Sannin?")
    nuevo["inteligente"] = preguntar_bool_gui("¿Destaca por su inteligencia?")
    nuevo["akatsuki"] = preguntar_bool_gui("¿Pertenece a Akatsuki?")

    raw_clave = sg.popup_get_text("Ingresa la pregunta clave diferenciadora del personaje:")
    clave_procesada = procesar_pregunta_clave(raw_clave)
    nuevo.update({
        "pregunta_clave": clave_procesada["pregunta_canonica"],
        "pregunta_clave_regex": clave_procesada["regex"]
    })

    personajes.append(nuevo)
    guardar_personajes(personajes)
    sg.popup(f"Personaje '{nombre}' agregado con éxito.")

# -------------------------------
# Personajes base (15)
# -------------------------------
personajes_base = [
    {"nombre": "Naruto Uzumaki", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": False, "pregunta_clave": "¿Es el protagonista rubio?", "pregunta_clave_regex": "\\b(?:protagonista|rubio)\\b"},

    {"nombre": "Sasuke Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "lider": False, "mascara": False, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Tiene Sharingan y es del clan Uchiha?", "pregunta_clave_regex": "\\b(?:sharingan|uchiha)\\b"},

    {"nombre": "Sakura Haruno", "pelo": "rosa", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Tiene cabello rosa y es muy inteligente?", "pregunta_clave_regex": "\\b(?:rosa|inteligente)\\b"},

    {"nombre": "Kakashi Hatake", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": True, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Usa una máscara cubriendo su rostro?", "pregunta_clave_regex": "\\b(?:mascara|rostro)\\b"},

    {"nombre": "Hinata Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": True,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Tiene Byakugan?", "pregunta_clave_regex": "\\b(?:byakugan)\\b"},

    {"nombre": "Itachi Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "lider": False, "mascara": False, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True, "pregunta_clave": "¿Es miembro de Akatsuki?", "pregunta_clave_regex": "\\b(?:akatsuki)\\b"},

    {"nombre": "Jiraiya", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": True, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Es uno de los Sannin legendarios?", "pregunta_clave_regex": "\\b(?:sannin)\\b"},

    {"nombre": "Tsunade", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": True, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Es mujer líder y Sannin?", "pregunta_clave_regex": "\\b(?:mujer|lider|sannin)\\b"},

    {"nombre": "Gaara", "pelo": "rojo", "aldea": "suna", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Es de Suna y líder?", "pregunta_clave_regex": "\\b(?:suna|lider)\\b"},

    {"nombre": "Shikamaru Nara", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Es estratega inteligente?", "pregunta_clave_regex": "\\b(?:estratega|inteligente)\\b"},

    {"nombre": "Neji Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": True,
     "sannin": False, "inteligente": True, "akatsuki": False, "pregunta_clave": "¿Tiene Byakugan y es miembro del clan Hyuga?", "pregunta_clave_regex": "\\b(?:byakugan|hyuga)\\b"},

    {"nombre": "Rock Lee", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": False, "pregunta_clave": "¿Es experto en taijutsu sin habilidades oculares?", "pregunta_clave_regex": "\\b(?:taijutsu)\\b"},

    {"nombre": "Pain", "pelo": "naranja", "aldea": "akatsuki", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True, "pregunta_clave": "¿Es líder de Akatsuki con cabello naranja?", "pregunta_clave_regex": "\\b(?:akatsuki|lider|naranja)\\b"},

    {"nombre": "Konan", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True, "pregunta_clave": "¿Es mujer miembro de Akatsuki con cabello azul?", "pregunta_clave_regex": "\\b(?:akatsuki|mujer|azul)\\b"},

    {"nombre": "Kisame Hoshigaki", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": True, "pregunta_clave": "¿Es miembro de Akatsuki con cabello azul y gran espada?", "pregunta_clave_regex": "\\b(?:akatsuki|azul|espada)\\b"}
]

# -------------------------------
# Interfaz principal
# -------------------------------
def main():
    sg.theme("DarkBlue3")
    layout = [
        [sg.Text("=== Adivina Quién - Naruto Edition ===")],
        [sg.Button("Jugar"), sg.Button("Agregar Personaje"), sg.Button("Salir")]
    ]
    window = sg.Window("Adivina Quién", layout)
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
        elif event == "Jugar":
            jugar_gui()
        elif event == "Agregar Personaje":
            aprender_personaje_gui()
    window.close()

if __name__ == "__main__":
    main()
