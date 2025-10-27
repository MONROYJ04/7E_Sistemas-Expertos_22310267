<#
build.ps1 - Script para construir y empaquetar "Adivina Quién" para Windows

Uso:
  .\build.ps1 [-OneFile] [-Name "AdivinaQuien"] [-IconPath "path\to\icon.ico"]

Qué hace:
 - Ejecuta PyInstaller (usa el python del virtualenv `env\Scripts\python.exe` si existe)
 - Crea un build (--onefile por defecto)
 - Copia el exe y cualquier archivo .json y carpetas de assets comunes a builds\Adivina-Windows
 - Crea builds\Adivina-Windows.zip listo para subir a itch.io
#>

param(
    [switch]$OneFile = $true,
    [string]$Name = "AdivinaQuien",
    [string]$IconPath = ""
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Write-Host "Proyecto root: $root"

$pythonEnv = Join-Path $root "env\Scripts\python.exe"
if (-Not (Test-Path $pythonEnv)) {
    Write-Warning "No se encontró el virtualenv en 'env\Scripts\python.exe'. Se utilizará 'python' del PATH. Asegúrate de que PyInstaller esté instalado." 
    $pythonEnv = "python"
}

# Archivo principal (con espacios en ruta)
$mainScript = Join-Path $root "Parcial 2\Adivina quien.py"
if (-Not (Test-Path $mainScript)) {
    Write-Error "No se encontró el archivo principal: $mainScript"
    exit 1
}

# Opciones de PyInstaller
$pyArgs = @("-m", "PyInstaller", "--noconfirm")
if ($OneFile) {
    $pyArgs += "--onefile"
} else {
    $pyArgs += "--onedir"
}
$pyArgs += "--name"; $pyArgs += $Name
$pyArgs += "--console"  # Cambiar por --windowed si quieres ocultar consola
if ($IconPath -and (Test-Path $IconPath)) {
    $pyArgs += "--icon"; $pyArgs += $IconPath
}
$pyArgs += $mainScript

Write-Host "Ejecutando PyInstaller... (esto puede tardar unos segundos/minutos dependiendo del proyecto)"
& $pythonEnv @pyArgs

# Preparar carpeta de salida
$buildRoot = Join-Path $root "builds"
$newFolder = Join-Path $buildRoot "$Name-Windows"
if (Test-Path $newFolder) { Remove-Item $newFolder -Recurse -Force }
New-Item -ItemType Directory -Path $newFolder | Out-Null

# Copiar resultado
$distPath = Join-Path $root "dist"
if ($OneFile) {
    $exePath = Join-Path $distPath ("$Name.exe")
    if (-Not (Test-Path $exePath)) {
        # A veces PyInstaller pone el exe en dist\<Name>\<Name>.exe cuando hay coincidencias
        $possible = Get-ChildItem -Path $distPath -Recurse -Filter "$Name.exe" -File -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -eq $possible) { Write-Error "No se encontró el exe en dist/"; exit 1 }
        $exePath = $possible.FullName
    }
    Copy-Item -Path $exePath -Destination $newFolder -Force
} else {
    $dirPath = Join-Path $distPath $Name
    if (-Not (Test-Path $dirPath)) { Write-Error "No se encontró la carpeta dist\$Name"; exit 1 }
    Copy-Item -Path (Join-Path $dirPath '*') -Destination $newFolder -Recurse -Force
}

# Copiar archivos .json del proyecto (raíz y subcarpetas), y carpetas comunes de assets si existen
$patterns = @('*.json')
foreach ($pattern in $patterns) {
    $items = Get-ChildItem -Path $root -Recurse -Include $pattern -File -ErrorAction SilentlyContinue
    foreach ($it in $items) {
        Copy-Item -Path $it.FullName -Destination $newFolder -Force
    }
}

# Carpetas comunes de assets para juegos
$assetDirs = @('assets','data','images','sounds')
foreach ($d in $assetDirs) {
    $p = Join-Path $root $d
    if (Test-Path $p) {
        Copy-Item -Path $p -Destination (Join-Path $newFolder $d) -Recurse -Force
    }
}

# Crear README simple dentro del build
$readme = @()
$readme += "Adivina Quién - Naruto Edition (Windows)"
$readme += "======================================"
$readme += "Instrucciones:"
$readme += "1) Extrae el ZIP en una carpeta."
$readme += "2) Ejecuta $Name.exe para iniciar el juego."
$readme += "3) Asegúrate de que cualquier archivo .json esté en la misma carpeta que el exe si el juego lo requiere."
$readmePath = Join-Path $newFolder "README.txt"
$readme | Out-File -FilePath $readmePath -Encoding UTF8

# Empaquetar a zip
$zipPath = Join-Path $buildRoot ("$Name-Windows.zip")
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $newFolder '*') -DestinationPath $zipPath -Force

Write-Host "Build completado. Carpeta: $newFolder"
Write-Host "ZIP creado en: $zipPath"
Write-Host "Listo para subir a itch.io"
