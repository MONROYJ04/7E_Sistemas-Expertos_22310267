Adivina Quién - Naruto Edition
===============================

Versión empaquetada para Windows

Archivos incluidos
- AdivinaQuien.exe -> ejecutable (Windows)
- personajes.json -> lista editable de personajes (puedes editar este JSON para añadir o cambiar personajes sin recompilar)
- README.txt -> instrucciones rápidas

Cómo ejecutar
1. Extrae el ZIP en una carpeta.
2. Ejecuta `AdivinaQuien.exe` (doble clic) para iniciar el juego.

Notas técnicas
- El juego está hecho en Python + Tkinter. La lista por defecto de personajes está embebida en el exe, pero si el archivo `personajes.json` existe en la misma carpeta que el exe, el juego lo cargará en lugar de la lista interna.
- Si el juego no abre o se cierra inmediatamente, recompila en modo consola para ver errores: `pyinstaller --onefile --console "Adivina quien.py"`.

Problemas y soluciones comunes
- Windows SmartScreen o antivirus pueden advertir sobre el exe. Explica a los usuarios que pueden permitirlo en la ventana de advertencia o en la configuración del antivirus.
- Para añadir personajes, edita `personajes.json` (UTF-8) y mantén la estructura de array de objetos con las mismas claves que en el archivo.

Contacto
- Autor: MONROYJ04
- Repositorio: incluye código fuente en la distribución original (si quieres, subo el repo o pongo un enlace en la página de itch.io).