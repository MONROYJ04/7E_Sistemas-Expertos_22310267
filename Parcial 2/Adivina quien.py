#------------------------------------------------------
#Sistema experto: "Adivina quien-Naruto"
#Se emplea Encadenamiento hacia adelante usando la libreria experta 
#------------------------------------------------------

from experta import *

#------------------------------------------------------
#Definiciion de los hechos
#------------------------------------------------------

class Personajes(Fact):
    """Hechos de los personajes"""
    pass

#------------------------------------------------------
#Motor de inferencia
#------------------------------------------------------

class AdivinaNaruto(KnowledgeEngine):

    @Rule(Personaje(pelo="rubio", aldea="Konoha", lider=True))
    def naruto(self):
        print("\nTu personaje es: NARUTO UZUMAKI")

    @Rule(Personaje(pelo="negro", clan="Uchiha", sharingan=True))
    def sasuke(self):
        print("\nTu personaje es: SASUKE UCHIHA")

    @Rule(Personaje(pelo="rosa", aldea="Konoha", genero="femenino"))
    def sakura(self):
        print("\nTu personaje es: SAKURA HARUNO")

    @Rule(Personaje(pelo="blanco", mascara=True))
    def kakashi(self):
        print("\nTu personaje es: KAKASHI HATAKE")

    @Rule(Personaje(pelo="negro", clan="Hyuga", byakugan=True))
    def hinata(self):
        print("\nTu personaje es: HINATA HYUGA")

    @Rule(Personaje(pelo="negro", clan="Uchiha", sharingan=True, akatsuki=True))
    def itachi(self):
        print("\nTu personaje es: ITACHI UCHIHA")

    @Rule(Personaje(pelo="blanco", sannin=True))
    def jiraiya(self):
        print("\nTu personaje es: JIRAIYA")

    @Rule(Personaje(pelo="rubio", sannin=True, genero="femenino"))
    def tsunade(self):
        print("\nTu personaje es: TSUNADE")

    @Rule(Personaje(pelo="rojo", aldea="Suna", lider=True))
    def gaara(self):
        print("\nTu personaje es: GAARA DEL DESIERTO")

    @Rule(Personaje(pelo="negro", inteligente=True, aldea="Konoha"))
    def shikamaru(self):
        print("\nTu personaje es: SHIKAMARU NARA")


#------------------------------------------------------
#Funcion auxiliar: Validar las respuestas 
#------------------------------------------------------

def preguntar(pregunta, opciones):
    """Hace una pregunta y valida la respuesta"""
    while True:
        resp = input(pregunta + f" {opciones}: ").strip().lower()
        if resp in opciones:
            return resp
        else:
            print("Por favor responde una opción válida:", opciones)

def preguntar_bool(pregunta):
    """Pregunta si/no"""
    while True:
        resp = input(pregunta + " (si/no): ").strip().lower()
        if resp in ["si", "no"]:
            return resp == "si"
        else:
            print("Escribe 'si' o 'no'.")

#------------------------------------------------------
#Programa principal
#------------------------------------------------------

if __name__ == "__main__":
    print("===============================================")
    print("  Sistema Experto: Adivina Quién - Naruto Edition")
    print("===============================================\n")

    engine = AdivinaNaruto()
    engine.reset()

    # Recolección de datos
    pelo = preguntar("¿De qué color tiene el pelo tu personaje?", 
                     ["rubio", "negro", "blanco", "rosa", "rojo"])
    aldea = preguntar("¿A qué aldea pertenece?", 
                      ["konoha", "suna", "akatsuki", "otra"])
    clan = preguntar("¿A qué clan pertenece?", 
                     ["uchiha", "hyuga", "ninguno"])
    genero = preguntar("¿Tu personaje es masculino o femenino?", 
                       ["masculino", "femenino"])
    lider = preguntar_bool("¿Es líder o Hokage?")
    mascara = preguntar_bool("¿Usa máscara?")
    sharingan = preguntar_bool("¿Tiene Sharingan?")
    byakugan = preguntar_bool("¿Tiene Byakugan?")
    sannin = preguntar_bool("¿Es uno de los Sannin?")
    inteligente = preguntar_bool("¿Destaca por su inteligencia?")
    akatsuki = preguntar_bool("¿Pertenece a la organización Akatsuki?")

    # Declarar hechos
    engine.declare(Personaje(
        pelo=pelo,
        aldea=aldea,
        clan=clan,
        genero=genero,
        lider=lider,
        mascara=mascara,
        sharingan=sharingan,
        byakugan=byakugan,
        sannin=sannin,
        inteligente=inteligente,
        akatsuki=akatsuki
    ))

    print("\nAnalizando tu personaje...\n")
    engine.run()
    print("\nFin del razonamiento.\n")

