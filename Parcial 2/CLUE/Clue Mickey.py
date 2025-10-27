import tkinter as tk
import random

# ---------------------------
# Datos del juego
# ---------------------------
personajes = ["Mickey Mouse","Minnie Mouse","Goofy","Donald","Daisy"]
locaciones = ["Cocina","Jardín","Sala Principal","Estudio de Fotografía","Taller de Modas"]
armas = ["Sartén","Tijeras","Regadera","Micrófono","Cámara fotográfica"]

colores_personajes = {
    "Mickey Mouse":"#d62828",   # rojo
    "Minnie Mouse":"#ff6bcb",   # rosa
    "Goofy":"#2a9d8f",          # verde
    "Donald":"#0077b6",         # azul
    "Daisy":"#7b2cbf"           # morado
}

historias = {
    "Mickey Mouse":{
        "arma":"Micrófono",
        "lugar":"Sala Principal",
        "narrativa":"Mickey estaba practicando su discurso para la fiesta. Nervioso, tropieza con el micrófono y derriba el pastel en la Sala Principal.",
        "pistas":["Parecía muy nervioso con el micrófono.","Había migajas cerca del micrófono.","Comentó que quería impresionar a todos."]
    },
    "Minnie Mouse":{
        "arma":"Tijeras",
        "lugar":"Taller de Modas",
        "narrativa":"Minnie estaba diseñando un vestido nuevo. Distraída, deja caer sus tijeras sobre el pastel mientras cortaba telas en su taller.",
        "pistas":["Tenía unas tijeras nuevas muy filosas.","Hablaba sobre su próximo vestido de gala.","Se la vio molesta cortando telas."]
    },
    "Goofy":{
        "arma":"Regadera",
        "lugar":"Jardín",
        "narrativa":"Goofy regaba las plantas, pero un descuido hizo que la regadera chocara con la mesa donde estaba el pastel, arruinándolo en el jardín.",
        "pistas":["Regaba el jardín y mojó todo.","Llevaba la regadera vacía corriendo.","Comentó que escuchó un golpe fuerte."]
    },
    "Donald":{
        "arma":"Sartén",
        "lugar":"Cocina",
        "narrativa":"Donald intentaba preparar el pastel él mismo. Se enfada porque se quema, y sin querer lo lanza con la sartén dentro de la cocina.",
        "pistas":["Se le vio con la sartén en la mano.","Estaba cocinando todo el tiempo.","Se enojó porque el pastel no estaba listo."]
    },
    "Daisy":{
        "arma":"Cámara fotográfica",
        "lugar":"Estudio de Fotografía",
        "narrativa":"Daisy estaba haciendo fotos del evento. Al mover la cámara para capturar la mejor toma, accidentalmente golpea el pastel en el estudio.",
        "pistas":["Su cámara se cayó al suelo.","Tomaba fotos del evento.","Se quejaba de que el flash no funcionaba."]
    }
}

# ---------------------------
# Estado del juego
# ---------------------------
def init_game_state():
    return {
        "culpable": random.choice(personajes),
        "cuaderno": []
    }

state = init_game_state()

# ---------------------------
# Helpers UI
# ---------------------------
def animar_texto(widget, texto, delay=30):
    """Efecto máquina de escribir."""
    widget.config(state="normal")
    widget.delete(1.0, tk.END)
    def escribir(i=0):
        if i < len(texto):
            widget.insert(tk.END, texto[i])
            widget.see(tk.END)
            widget.after(delay, escribir, i+1)
        else:
            widget.config(state="disabled")
    escribir()

def show_dialogo_animado(titulo, texto):
    """Ventana con texto animado."""
    modal = tk.Toplevel(root)
    modal.title(titulo)
    modal.configure(bg="black")
    modal.geometry("480x260+" + str(root.winfo_x()+40) + "+" + str(root.winfo_y()+40))
    tk.Label(modal, text=titulo, bg="black", fg="white", font=("Arial", 14, "bold")).pack(pady=(10,6))
    texto_box = tk.Text(modal, bg="#111", fg="white", wrap="word", height=8, width=50, font=("Consolas", 11))
    texto_box.pack(padx=12, pady=(0,8))
    animar_texto(texto_box, texto)
    tk.Button(modal, text="Continuar", width=12, bg="#222", fg="white", command=modal.destroy).pack(pady=(4,10))
    modal.transient(root)
    modal.grab_set()
    root.wait_window(modal)

def show_modal(title, text):
    modal = tk.Toplevel(root)
    modal.title(title)
    modal.configure(bg="black")
    modal.geometry("460x200+" + str(root.winfo_x()+40) + "+" + str(root.winfo_y()+40))
    tk.Label(modal, text=title, bg="black", fg="white", font=("Arial", 14, "bold")).pack(pady=(10,6))
    tk.Label(modal, text=text, bg="black", fg="white", wraplength=420, justify="left", font=("Arial", 11)).pack(padx=10)
    tk.Button(modal, text="OK", width=10, bg="#222", fg="white", command=modal.destroy).pack(pady=8)
    modal.transient(root)
    modal.grab_set()
    root.wait_window(modal)

def show_result_modal(title, text):
    modal = tk.Toplevel(root)
    modal.title(title)
    modal.configure(bg="black")
    modal.geometry("520x260+" + str(root.winfo_x()+20) + "+" + str(root.winfo_y()+20))
    tk.Label(modal, text=title, bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=(12,6))
    tk.Label(modal, text=text, bg="black", fg="white", wraplength=480, justify="left", font=("Arial", 11)).pack(padx=12, pady=6)
    frame = tk.Frame(modal, bg="black")
    frame.pack(pady=12)
    def jugar_otra():
        modal.destroy()
        reset_game()
    tk.Button(frame, text="Jugar otra vez", width=16, bg="#1b9aaa", fg="white", command=jugar_otra).pack(side="left", padx=8)
    tk.Button(frame, text="Salir", width=12, bg="#b00020", fg="white", command=root.destroy).pack(side="left", padx=8)
    modal.transient(root)
    modal.grab_set()
    root.wait_window(modal)

# ---------------------------
# Cuaderno
# ---------------------------
def actualizar_cuaderno(tipo, texto):
    state["cuaderno"].append((tipo, texto))
    texto_cuaderno.config(state="normal")
    texto_cuaderno.delete(1.0, tk.END)
    for t, linea in state["cuaderno"]:
        if t=="personaje":
            icono = "👤"
            color = colores_personajes.get(linea.split(":")[0], "white")
        elif t=="arma":
            icono = "🔧"
            color = "orange"
        elif t=="lugar":
            icono = "🏠"
            color = "lightblue"
        else:
            icono = "📝"
            color = "white"
        texto_cuaderno.insert(tk.END, f"{icono} {linea}\n", t)
        texto_cuaderno.tag_config(t, foreground=color)
    texto_cuaderno.config(state="disabled")

# ---------------------------
# Acciones del juego
# ---------------------------
def manejar_personaje(personaje):
    pista = random.choice(historias[personaje]["pistas"])
    extra = " 🤔 Parece nervioso..." if personaje == state["culpable"] else ""
    mensaje = f"{personaje}: {pista}{extra}"
    show_dialogo_animado("Interrogatorio", mensaje)
    actualizar_cuaderno("personaje", mensaje)

def manejar_arma(arma):
    if arma == historias[state["culpable"]]["arma"]:
        mensaje = "🩸 Tiene rastros del pastel y parece haber sido usada recientemente."
    else:
        mensaje = "Está limpia y bien guardada."
    show_modal("Examen de arma", f"Inspeccionas {arma}.\n\n{mensaje}")
    actualizar_cuaderno("arma", f"Arma: {arma} - {mensaje}")

def manejar_lugar(lugar):
    if lugar == historias[state["culpable"]]["lugar"]:
        mensaje = "❗ Hay señales de que algo ocurrió aquí... ¡una pista importante!"
    else:
        mensaje = "No parece haber nada extraño por ahora."
    show_modal("Visita al lugar", f"Visitas {lugar}.\n\n{mensaje}")
    actualizar_cuaderno("lugar", f"Lugar: {lugar} - {mensaje}")

def crear_ventana_interactiva(titulo, opciones, tipo):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)
    ventana.configure(bg="black")
    ventana.geometry("360x340+" + str(root.winfo_x()+40) + "+" + str(root.winfo_y()+40))
    tk.Label(ventana, text=titulo, bg="black", fg="white", font=("Arial",14,"bold")).pack(pady=8)
    frame = tk.Frame(ventana, bg="black")
    frame.pack(pady=6)
    for o in opciones:
        if tipo=="personaje":
            color_btn = colores_personajes.get(o, "gray")
            cmd = lambda opt=o: manejar_personaje(opt)
        elif tipo=="arma":
            color_btn = "#b86500"
            cmd = lambda opt=o: manejar_arma(opt)
        else:
            color_btn = "#2b6cb0"
            cmd = lambda opt=o: manejar_lugar(opt)
        tk.Button(frame, text=o, width=28, bg=color_btn, fg="white", command=cmd).pack(pady=6)
    tk.Button(ventana, text="Cerrar", width=12, bg="#333", fg="white", command=ventana.destroy).pack(pady=8)

# ---------------------------
# Ventana de acusación final
# ---------------------------
def ventana_acusacion():
    v = tk.Toplevel(root)
    v.title("Acusación final")
    v.configure(bg="black")
    v.geometry("520x420+" + str(root.winfo_x()+30) + "+" + str(root.winfo_y()+30))

    tk.Label(v, text="Acusación Final", bg="black", fg="white", font=("Arial",16,"bold")).pack(pady=(12,6))
    tk.Label(v, text="Elige quién, con qué y dónde:", bg="black", fg="white", font=("Arial",11)).pack(pady=(0,10))

    sel_personaje = tk.StringVar(value="Selecciona personaje")
    sel_arma = tk.StringVar(value="Selecciona arma")
    sel_lugar = tk.StringVar(value="Selecciona lugar")

    f = tk.Frame(v, bg="black")
    f.pack(pady=4, padx=8, fill="x")

    def crear_menu(label, opciones, variable, fila):
        tk.Label(f, text=label, bg="black", fg="white").grid(row=fila, column=0, sticky="w", padx=6, pady=6)
        menu = tk.OptionMenu(f, variable, *opciones)
        menu.configure(bg="#222", fg="white", width=28)
        menu["menu"].configure(bg="#111", fg="white")
        menu.grid(row=fila, column=1, padx=6, pady=6)

    crear_menu("Culpable:", personajes, sel_personaje, 0)
    crear_menu("Arma:", armas, sel_arma, 1)
    crear_menu("Lugar:", locaciones, sel_lugar, 2)

    def confirmar():
        p, a, l = sel_personaje.get(), sel_arma.get(), sel_lugar.get()
        if p not in personajes or a not in armas or l not in locaciones:
            show_modal("Atención", "Debes seleccionar personaje, arma y lugar válidos.")
            return
        actualizar_cuaderno("personaje", f"Acusación - {p}")
        actualizar_cuaderno("arma", f"Arma: {a}")
        actualizar_cuaderno("lugar", f"Lugar: {l}")
        if p == state["culpable"] and a == historias[p]["arma"] and l == historias[p]["lugar"]:
            texto = f"🎉 ¡Felicidades! Atinaste la acusación.\n\nHistoria:\n{historias[p]['narrativa']}"
            show_result_modal("¡Caso cerrado!", texto)
        else:
            texto = (f"❌ Fallaste.\nEl verdadero culpable fue {state['culpable']} con {historias[state['culpable']]['arma']} "
                     f"en {historias[state['culpable']]['lugar']}.\n\nHistoria:\n{historias[state['culpable']]['narrativa']}")
            show_result_modal("Caso abierto", texto)
        v.destroy()

    tk.Button(v, text="Confirmar acusación", width=22, bg="#1b9aaa", fg="white", command=confirmar).pack(pady=12)
    tk.Button(v, text="Cerrar", width=14, bg="#333", fg="white", command=v.destroy).pack()

# ---------------------------
# Ventana introductoria
# ---------------------------
def mostrar_intro():
    intro = tk.Toplevel(root)
    intro.title("Introducción al caso")
    intro.configure(bg="black")
    intro.geometry("540x300+" + str(root.winfo_x()+40) + "+" + str(root.winfo_y()+40))

    tk.Label(intro, text="🕵️ Misterio en la Casa de Mickey 🏠", bg="black", fg="white", font=("Arial", 16, "bold")).pack(pady=(12,6))
    texto_box = tk.Text(intro, bg="#111", fg="white", wrap="word", height=8, width=60, font=("Consolas", 11))
    texto_box.pack(padx=12, pady=(0,8))

    intro_text = (
        "En la casa del famoso Mickey Mouse se celebraba una gran fiesta.\n"
        "Todo iba bien… hasta que alguien arruinó el pastel principal del evento.\n\n"
        "Nadie sabe quién lo hizo, ni cómo ocurrió.\n"
        "Tu misión, detective, es descubrir al culpable:\n"
        "¿Quién fue? ¿Con qué objeto? ¿Y en qué lugar sucedió?"
    )

    animar_texto(texto_box, intro_text)

    tk.Button(intro, text="Comenzar investigación", width=20, bg="#1b9aaa", fg="white",
              command=intro.destroy).pack(pady=(6,10))

    intro.transient(root)
    intro.grab_set()
    root.wait_window(intro)

# ---------------------------
# Reset / reinicio
# ---------------------------
def reset_game():
    new_state = init_game_state()
    state["culpable"] = new_state["culpable"]
    state["cuaderno"].clear()
    texto_cuaderno.config(state="normal")
    texto_cuaderno.delete(1.0, tk.END)
    texto_cuaderno.config(state="disabled")
    print("Nuevo culpable:", state["culpable"])

# ---------------------------
# Interfaz principal
# ---------------------------
root = tk.Tk()
root.title("🕵️‍♂️ Clue: Misterio en la Casa de Mickey 🏠")
root.geometry("620x600")
root.configure(bg="black")

tk.Label(root, text="Bienvenido al Misterio en la Casa de Mickey!", bg="black", fg="white", font=("Arial",16,"bold")).pack(pady=(12,6))
tk.Label(root, text="Interroga, visita, examina y usa tu cuaderno para resolver el caso.", bg="black", fg="white", font=("Arial",11)).pack()

frame_btns = tk.Frame(root, bg="black")
frame_btns.pack(pady=12)

tk.Button(frame_btns, text="Interrogar a un personaje", width=24, bg="#a4161a", fg="white",
          command=lambda: crear_ventana_interactiva("Interrogar personaje", personajes, "personaje")).grid(row=0,column=0,padx=8,pady=6)
tk.Button(frame_btns, text="Visitar un lugar", width=24, bg="#1b3b8a", fg="white",
          command=lambda: crear_ventana_interactiva("Visitar lugar", locaciones, "lugar")).grid(row=0,column=1,padx=8,pady=6)
tk.Button(frame_btns, text="Examinar un arma", width=24, bg="#3a6b35", fg="white",
          command=lambda: crear_ventana_interactiva("Examinar arma", armas, "arma")).grid(row=1,column=0,padx=8,pady=6)
tk.Button(frame_btns, text="Hacer acusación final", width=24, bg="#6a3fb5", fg="white",
          command=ventana_acusacion).grid(row=1,column=1,padx=8,pady=6)

tk.Button(root, text="Reiniciar juego", width=18, bg="#3a3a3a", fg="white", command=reset_game).pack(pady=(6,4))
tk.Button(root, text="Salir", width=12, bg="#b00020", fg="white", command=root.destroy).pack(pady=(0,10))

tk.Label(root, text="📓 Cuaderno de detective:", bg="black", fg="white", font=("Arial",12,"bold")).pack(pady=(12,4))
texto_cuaderno = tk.Text(root, height=16, width=78, bg="#111213", fg="white", state="disabled", font=("Consolas",10))
texto_cuaderno.pack(padx=12)

# Mostrar introducción al iniciar
mostrar_intro()

print("Culpable inicial (debug):", state["culpable"])
root.mainloop()
