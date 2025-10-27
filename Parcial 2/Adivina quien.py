# ------------------------------------------------------
# Adivina Quién - Naruto Edition (Tkinter)
# Flujo estilo Adivina Quién
# ------------------------------------------------------

import tkinter as tk
from tkinter import simpledialog
import json
import re
import unicodedata
import os

# -------------------------------
# Funciones de texto y keywords
# -------------------------------
STOPWORDS = {
    "el","la","los","las","un","una","unos","unas","y","o","de","del","que","es","en","por","con",
    "para","su","sus","al","se","lo","como","este","esta","estos","estas","ha","han","pero","no",
    "tu","tú","si","sí","fue","son"
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
    if not frase:
        return {"pregunta_canonica": "", "keywords": [], "regex": ""}
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
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return personajes_base[:]
    else:
        return personajes_base[:]

def guardar_personajes(lista):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# -------------------------------
# Personajes base (15)
# -------------------------------
personajes_base = [
    {"nombre": "Naruto Uzumaki", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": False,
     "pregunta_clave": "¿Es el protagonista rubio?", "pregunta_clave_regex": r"\b(?:protagonista|rubio)\b"},
    {"nombre": "Sasuke Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "lider": False, "mascara": False, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Tiene Sharingan y es del clan Uchiha?", "pregunta_clave_regex": r"\b(?:sharingan|uchiha)\b"},
    {"nombre": "Sakura Haruno", "pelo": "rosa", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Tiene cabello rosa y es muy inteligente?", "pregunta_clave_regex": r"\b(?:rosa|inteligente)\b"},
    {"nombre": "Kakashi Hatake", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": True, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Usa una máscara cubriendo su rostro?", "pregunta_clave_regex": r"\b(?:mascara|rostro)\b"},
    {"nombre": "Hinata Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": True,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Tiene Byakugan?", "pregunta_clave_regex": r"\b(?:byakugan)\b"},
    {"nombre": "Itachi Uchiha", "pelo": "negro", "aldea": "konoha", "clan": "uchiha",
     "lider": False, "mascara": False, "sharingan": True, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True,
     "pregunta_clave": "¿Es miembro de Akatsuki?", "pregunta_clave_regex": r"\b(?:akatsuki)\b"},
    {"nombre": "Jiraiya", "pelo": "blanco", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": True, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Es uno de los Sannin legendarios?", "pregunta_clave_regex": r"\b(?:sannin)\b"},
    {"nombre": "Tsunade", "pelo": "rubio", "aldea": "konoha", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": True, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Es mujer líder y Sannin?", "pregunta_clave_regex": r"\b(?:mujer|lider|sannin)\b"},
    {"nombre": "Gaara", "pelo": "rojo", "aldea": "suna", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Es de Suna y líder?", "pregunta_clave_regex": r"\b(?:suna|lider)\b"},
    {"nombre": "Shikamaru Nara", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Es estratega inteligente?", "pregunta_clave_regex": r"\b(?:estratega|inteligente)\b"},
    {"nombre": "Neji Hyuga", "pelo": "negro", "aldea": "konoha", "clan": "hyuga",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": True,
     "sannin": False, "inteligente": True, "akatsuki": False,
     "pregunta_clave": "¿Tiene Byakugan y es miembro del clan Hyuga?", "pregunta_clave_regex": r"\b(?:byakugan|hyuga)\b"},
    {"nombre": "Rock Lee", "pelo": "negro", "aldea": "konoha", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": False,
     "pregunta_clave": "¿Es experto en taijutsu sin habilidades oculares?", "pregunta_clave_regex": r"\b(?:taijutsu)\b"},
    {"nombre": "Pain", "pelo": "naranja", "aldea": "akatsuki", "clan": "ninguno",
     "lider": True, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True,
     "pregunta_clave": "¿Es líder de Akatsuki con cabello naranja?", "pregunta_clave_regex": r"\b(?:akatsuki|lider|naranja)\b"},
    {"nombre": "Konan", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": True, "akatsuki": True,
     "pregunta_clave": "¿Es mujer miembro de Akatsuki con cabello azul?", "pregunta_clave_regex": r"\b(?:akatsuki|mujer|azul)\b"},
    {"nombre": "Kisame Hoshigaki", "pelo": "azul", "aldea": "akatsuki", "clan": "ninguno",
     "lider": False, "mascara": False, "sharingan": False, "byakugan": False,
     "sannin": False, "inteligente": False, "akatsuki": True,
     "pregunta_clave": "¿Es miembro de Akatsuki con cabello azul y gran espada?", "pregunta_clave_regex": r"\b(?:akatsuki|azul|espada)\b"}
]

# -------------------------------
# Clase principal del juego
# -------------------------------
class AdivinaQuien:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina Quién - Naruto Edition")
        self.root.configure(bg="black")
        self.personajes = cargar_personajes()
        self.candidatos = []
        self.hechos = {}
        self.base_preguntas = [
            ("¿Es líder o Hokage?", "lider"),
            ("¿Usa máscara?", "mascara"),
            ("¿Tiene Sharingan?", "sharingan"),
            ("¿Tiene Byakugan?", "byakugan"),
            ("¿Es uno de los Sannin?", "sannin"),
            ("¿Es inteligente?", "inteligente"),
            ("¿Es miembro de Akatsuki?", "akatsuki")
        ]
        self.menu_inicial()

    # ---------------------------
    # Menú inicial
    # ---------------------------
    def menu_inicial(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="=== Adivina Quién - Naruto Edition ===", 
                 bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(self.root, text="Jugar", bg="blue", fg="white", width=20, command=self.jugar).pack(pady=5)
        tk.Button(self.root, text="Agregar Personaje", bg="green", fg="white", width=20, command=self.agregar_personaje).pack(pady=5)
        tk.Button(self.root, text="Salir", bg="red", fg="white", width=20, command=self.root.quit).pack(pady=5)

        tk.Label(self.root, text="Personajes disponibles:", bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
        lista = "\n".join([p["nombre"] for p in self.personajes])
        tk.Label(self.root, text=lista, bg="black", fg="white", justify="left").pack()

    # ---------------------------
    # Juego
    # ---------------------------
    def jugar(self):
        self.candidatos = self.personajes.copy()
        self.hechos = {}
        self.pregunta_idx = 0
        self.pregunta_clave_idx = 0
        self.preguntas_clave_usadas = []
        self.preguntar_base()

    def preguntar_base(self):
        if self.pregunta_idx < len(self.base_preguntas):
            texto, clave = self.base_preguntas[self.pregunta_idx]
            self.pregunta_idx += 1
            self.preguntar(texto, clave, self.preguntar_base)
        else:
            self.preguntar_siguiente_clave()

    def preguntar_siguiente_clave(self):
        candidatos_restantes = [p for p in self.candidatos if p not in self.preguntas_clave_usadas]
        if not candidatos_restantes:
            self.mostrar_no_encontrado()
            return
        self.actual = candidatos_restantes[0]
        self.preguntas_clave_usadas.append(self.actual)
        self.preguntar_clave(self.actual)

    def preguntar(self, texto, clave, callback_siguiente):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=texto, bg="black", fg="white", font=("Arial", 14)).pack(pady=20)
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=10)

        def responder(valor):
            if clave:
                self.hechos[clave] = valor
                # filtrar candidatos
                self.candidatos = [p for p in self.candidatos if (p.get(clave) == valor if valor is not None else True)]
            callback_siguiente()

        tk.Button(frame, text="Sí", bg="green", fg="white", width=10, command=lambda: responder(True)).pack(side="left", padx=5)
        tk.Button(frame, text="No", bg="red", fg="white", width=10, command=lambda: responder(False)).pack(side="left", padx=5)
        tk.Button(frame, text="No sé", bg="gray", fg="white", width=10, command=lambda: responder(None)).pack(side="left", padx=5)

    def preguntar_clave(self, candidato):
        texto = candidato["pregunta_clave"]
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=texto, bg="black", fg="white", font=("Arial", 14)).pack(pady=20)
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=10)

        tk.Button(frame, text="Sí", bg="green", fg="white", width=10, command=lambda: self.mostrar_adivinado(candidato)).pack(side="left", padx=5)
        tk.Button(frame, text="No", bg="red", fg="white", width=10, command=self.preguntar_siguiente_clave).pack(side="left", padx=5)
        tk.Button(frame, text="No sé", bg="gray", fg="white", width=10, command=self.preguntar_siguiente_clave).pack(side="left", padx=5)

    def mostrar_adivinado(self, candidato):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"¡Genial! Se adivinó a {candidato['nombre']}!", bg="black", fg="white", font=("Arial", 16)).pack(pady=20)
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=10)
        tk.Button(frame, text="Jugar de nuevo", bg="blue", fg="white", width=15, command=self.menu_inicial).pack(side="left", padx=5)
        tk.Button(frame, text="Salir", bg="red", fg="white", width=15, command=self.root.quit).pack(side="left", padx=5)

    def mostrar_no_encontrado(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="No se pudo encontrar tu personaje.", bg="black", fg="white", font=("Arial", 14)).pack(pady=20)
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=10)
        tk.Button(frame, text="Agregar Personaje", bg="green", fg="white", width=15, command=self.agregar_personaje).pack(side="left", padx=5)
        tk.Button(frame, text="Volver al menú", bg="blue", fg="white", width=15, command=self.menu_inicial).pack(side="left", padx=5)

    # ---------------------------
    # Agregar personaje
    # ---------------------------
    def agregar_personaje(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Agregar nuevo personaje", bg="black", fg="white", font=("Arial", 14)).pack(pady=20)
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=10)

        nombre = simpledialog.askstring("Nombre", "Nombre del personaje:", parent=self.root)
        if not nombre:
            self.menu_inicial()
            return
        pregunta_clave = simpledialog.askstring("Pregunta clave", "Pregunta clave para identificarlo:", parent=self.root)
        if not pregunta_clave:
            self.menu_inicial()
            return
        data = procesar_pregunta_clave(pregunta_clave)
        nuevo = {"nombre": nombre, "pregunta_clave": data["pregunta_canonica"], "pregunta_clave_regex": data["regex"]}
        self.personajes.append(nuevo)
        guardar_personajes(self.personajes)
        self.menu_inicial()

# -------------------------------
# Ejecutar aplicación
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaQuien(root)
    root.mainloop()
