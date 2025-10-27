# Clue: Misterio en la Casa de Mickey — Paquete para itch.io

Este repositorio contiene un pequeño juego hecho en Python con interfaz gráfica (tkinter).

Contenido a incluir en el ZIP (recomendado):
- `Clue Mickey.py` — archivo principal del juego.
- `requirements.txt` — dependencias / notas.
- `build_windows.ps1` — script opcional para crear un EXE (Windows) usando PyInstaller.

Opciones para subir a itch.io:

1) Subir el ZIP de código fuente ("Kind: Other" o "Source")
   - Incluye los archivos listados arriba.
   - El jugador deberá tener Python 3.8+ instalado y ejecutar:

     ```powershell
     python "Clue Mickey.py"
     ```

   - Nota: tkinter suele venir con la instalación de Python en Windows.

2) Subir un build Windows (recomendado para usuarios no técnicos)
   - Genera un ejecutable único (.exe) usando PyInstaller y sube el ZIP resultante como "Windows".
   - Puedes usar el script `build_windows.ps1` incluido para generar el EXE y el ZIP.

Cómo crear el ejecutable (Windows, desde PowerShell) — ejemplo:

1. Activa tu entorno virtual o asegúrate de tener PyInstaller instalado.
   - Si usas el entorno incluido en este repositorio (carpeta `env`), en PowerShell desde la raíz del repo:

     ```powershell
     .\env\Scripts\Activate.ps1
     ```

2. Ejecuta el script de construcción desde la carpeta `Parcial 2\CLUE`:

   ```powershell
   .\build_windows.ps1
   ```

Resultado esperado:
- Carpeta `builds\ClueMickey-Windows` con el EXE (y otros artefactos), y un ZIP `builds\ClueMickey-Windows.zip` listo para subir.

Notas importantes:
- No hay dependencias pip en este proyecto: solo se usa `tkinter` y `random` de la stdlib.
- Si planeas publicar en itch.io como juego nativo para navegador (HTML5), necesitarías portar a JS/Web o usar herramientas que exporten a HTML (no está incluido aquí).

Contacto rápido:
- Si quieres, puedo crear el ZIP de código fuente ahora y/o intentar construir el EXE en tu entorno y crear el ZIP final para subir a itch.io.
