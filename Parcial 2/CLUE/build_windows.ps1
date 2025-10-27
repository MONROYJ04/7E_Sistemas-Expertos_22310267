# Script para crear un ejecutable Windows y zippearlo (usa el Python del entorno 'env' del repo si existe)
Set-StrictMode -Version Latest

# PY apunta al Python dentro de la carpeta env del repo (ajusta si usas un entorno diferente)
$PY = "..\..\env\Scripts\python.exe"
if (!(Test-Path $PY)) {
    Write-Host "No se encontró $PY. Activa tu entorno virtual o ajusta la variable `$PY`." -ForegroundColor Yellow
    exit 1
}

Write-Host "Usando Python en: $PY"

$distDir = "..\builds\ClueMickey-Windows"
if (!(Test-Path $distDir)) { New-Item -ItemType Directory -Path $distDir | Out-Null }

# Ejecutar PyInstaller
& $PY -m PyInstaller --onefile --noconfirm --name "ClueMickey" --distpath $distDir "Clue Mickey.py"

if ($LASTEXITCODE -ne 0) {
    Write-Host "PyInstaller falló con código $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

# Crear ZIP del contenido del build
$zipOut = "..\builds\ClueMickey-Windows.zip"
if (Test-Path $zipOut) { Remove-Item $zipOut -Force }
Compress-Archive -Path "$distDir\*" -DestinationPath $zipOut -Force
Write-Host "ZIP creado en: $zipOut" -ForegroundColor Green
