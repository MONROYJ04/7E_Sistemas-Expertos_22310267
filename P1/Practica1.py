import sqlite3
from datetime import datetime

class ChatCNC:
    """Chat especializado para empresas de CNC y maquinados"""
    
    def __init__(self):
        self.conexion = sqlite3.connect('cnc_chat.db')
        self.crear_tabla()
        self.inicializar_conocimiento_cnc()
    
    def crear_tabla(self):
        """Crear tabla para almacenar el conocimiento"""
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conocimiento_cnc (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pregunta TEXT UNIQUE,
                respuesta TEXT,
                categoria TEXT DEFAULT 'CNC/Maquinados',
                fecha_creacion TEXT
            )
        ''')
        self.conexion.commit()
    
    def inicializar_conocimiento_cnc(self):
        """Inicializar con conocimiento específico de CNC"""
        cursor = self.conexion.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM conocimiento_cnc")
        if cursor.fetchone()[0] == 0:
            # Conocimiento específico para industria de maquinados
            datos_cnc = [
                ("hola", "Hola, soy asistente especializado en CNC. ¿En qué puedo ayudarte?", "Saludo"),
                ("que es cnc", "CNC significa Control Numérico Computarizado. Controla máquinas herramienta mediante computadoras.", "Definición"),
                ("que es un torno", "Máquina que mecaniza piezas giratorias mediante herramientas de corte.", "Máquinas"),
                ("que es una fresadora", "Máquina que realiza mecanizados por arranque de viruta con herramientas rotativas.", "Máquinas"),
                ("que es g-code", "Lenguaje de programación para controlar máquinas CNC.", "Programación"),
                ("que materiales trabajan", "Metales (acero, aluminio), plásticos, composites y maderas.", "Materiales"),
                ("que es tolerancia", "Margen de error permitido en las dimensiones de piezas mecanizadas.", "Calidad")
            ]
            
            for pregunta, respuesta, categoria in datos_cnc:
                cursor.execute(
                    "INSERT INTO conocimiento_cnc (pregunta, respuesta, categoria, fecha_creacion) VALUES (?, ?, ?, ?)",
                    (pregunta, respuesta, categoria, datetime.now().isoformat())
                )
            
            self.conexion.commit()
    
    def obtener_respuesta(self, pregunta):
        """Buscar respuesta en la base de conocimiento"""
        pregunta = pregunta.lower().strip()
        
        cursor = self.conexion.cursor()
        cursor.execute("SELECT respuesta FROM conocimiento_cnc WHERE pregunta = ?", (pregunta,))
        resultado = cursor.fetchone()
        
        return resultado[0] if resultado else None
    
    def agregar_conocimiento(self, pregunta, respuesta, categoria="CNC/Maquinados"):
        """Agregar nuevo conocimiento al sistema"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO conocimiento_cnc (pregunta, respuesta, categoria, fecha_creacion) VALUES (?, ?, ?, ?)",
                (pregunta.lower(), respuesta, categoria, datetime.now().isoformat())
            )
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            # Si ya existe, actualizamos
            cursor.execute(
                "UPDATE conocimiento_cnc SET respuesta = ?, categoria = ? WHERE pregunta = ?",
                (respuesta, categoria, pregunta.lower())
            )
            self.conexion.commit()
            return True
        except:
            return False

# Función principal del chat
def ejecutar_chat():
    chat = ChatCNC()
    
    print("=" * 50)
    print("CHAT ESPECIALIZADO EN CNC Y MAQUINADOS")
    print("=" * 50)
    print("Escribe 'salir' para terminar la conversación\n")
    
    while True:
        try:
            entrada_usuario = input("Tú: ").strip()
            
            if entrada_usuario.lower() == 'salir':
                print("Chat: ¡Hasta luego! Que tengas excelentes maquinados.")
                break
            
            if not entrada_usuario:
                continue
            
            # Buscar respuesta
            respuesta = chat.obtener_respuesta(entrada_usuario)
            
            if respuesta:
                print(f"Chat: {respuesta}")
            else:
                print(f"Chat: No tengo respuesta para '{entrada_usuario}'. ¿Podrías enseñarme?")
                nueva_respuesta = input("Por favor, ingresa la respuesta adecuada: ").strip()
                
                if nueva_respuesta:
                    if chat.agregar_conocimiento(entrada_usuario, nueva_respuesta):
                        print("Chat: ¡Gracias! He aprendido algo nuevo.")
                    else:
                        print("Chat: No pude guardar esa información.")
                else:
                    print("Chat: De acuerdo, continuemos.")
        
        except KeyboardInterrupt:
            print("\nChat: ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"Chat: Ocurrió un error: {e}")

if __name__ == "__main__":
    ejecutar_chat()