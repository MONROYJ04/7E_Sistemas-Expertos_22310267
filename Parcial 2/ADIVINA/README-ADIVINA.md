Carpeta ADIVINA — Adivina Quién (organización)
===============================================

Estructura dentro de `Parcial 2\ADIVINA`:

- `Adivina quien.py`         : Código fuente del juego (Python + Tkinter)
- `personajes.json`         : Lista editable de personajes (se carga si existe)
- `dist\`                   : Salida de PyInstaller (exe y archivos temporales)
- `builds\AdivinaQuien-Windows` : Carpeta con el exe final y recursos listos para distribuir
- `AdivinaQuien-Windows.zip` : ZIP listo para subir a itch.io
- `build.ps1`               : Script de construcción específico para ADIVINA
- `README-ADIVINA.md`       : Este archivo

Comandos útiles
---------------
# Ejecutar el juego desde esta carpeta (exe dentro de dist)
cd "Parcial 2\ADIVINA"
.\dist\Adivina` quien.exe

# Ejecutar el exe final empaquetado (si quieres probar la versión subida)
cd "Parcial 2\ADIVINA\builds\AdivinaQuien-Windows"
.\AdivinaQuien.exe

# Regenerar el ZIP y el build (usa el Python del virtualenv en la raíz del repo)
# Desde la raíz del repositorio:
cd "D:\Documentos\GitHub\7E_Sistemas-Expertos_22310267"
# Llama al script dentro de ADIVINA (usa ExecutionPolicy Bypass si tu PowerShell lo requiere)
powershell -NoProfile -ExecutionPolicy Bypass -File "Parcial 2\ADIVINA\build.ps1"

Notas
-----
- `build.ps1` usa el `python.exe` dentro de `env\Scripts` del repo si existe. Si no, intenta `python` del PATH.
- Si quieres mover todo a otra carpeta, actualiza las rutas dentro del script o usa el wrapper en la raíz que delega aquí.
- Para comodidad, `build.ps1` en la raíz delega automáticamente al script dentro de `ADIVINA` (puedes usar cualquiera de los dos).

Si quieres que haga un commit con estos cambios y mueva o elimine el `build.ps1` raíz, dímelo y lo hago.