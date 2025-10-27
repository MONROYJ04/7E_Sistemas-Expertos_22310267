<#
ADIVINA\build.ps1 - Build helper for Adivina Quién located in Parcial 2\ADIVINA

This script is intended to be run from either:
 - the repo root: .\Parcial 2\ADIVINA\build.ps1
 - from the ADIVINA folder directly

It locates the repo root relative to its location and uses the virtualenv at repoRoot\env\Scripts\python.exe when present.

Options: same as the root build.ps1 wrapper (OneFile, Name, IconPath).
#>

param(
    [switch]$OneFile = $true,
    [string]$Name = "AdivinaQuien",
    [string]$IconPath = ""
)

$ErrorActionPreference = 'Stop'
# Directory where this script lives (Parcial 2\ADIVINA)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
# Repo root is two levels up from ADIVINA
$repoRoot = Resolve-Path (Join-Path $scriptDir "..\..")
$repoRoot = $repoRoot.Path
Write-Host "Repo root: $repoRoot"
Write-Host "ADIVINA folder: $scriptDir"

# Prefer virtualenv python in repo root
$pythonEnv = Join-Path $repoRoot "env\Scripts\python.exe"
if (-Not (Test-Path $pythonEnv)) {
    Write-Warning "No se encontró el virtualenv en '$pythonEnv'. Se utilizará 'python' del PATH. Asegúrate de que PyInstaller esté instalado." 
    $pythonEnv = "python"
}

# Main script inside ADIVINA
$mainScript = Join-Path $scriptDir "Adivina quien.py"
if (-Not (Test-Path $mainScript)) {
    Write-Error "No se encontró el archivo principal: $mainScript"
    exit 1
}

# Build options (relative outputs will be created inside ADIVINA)
$pyArgs = @("-m", "PyInstaller", "--noconfirm")
if ($OneFile) { $pyArgs += "--onefile" } else { $pyArgs += "--onedir" }
$pyArgs += "--name"; $pyArgs += $Name
$pyArgs += "--console"  # Change to --windowed if you want no console
if ($IconPath -and (Test-Path $IconPath)) { $pyArgs += "--icon"; $pyArgs += $IconPath }
$pyArgs += $mainScript

Write-Host "Ejecutando PyInstaller desde: $pythonEnv";
& $pythonEnv @pyArgs

# Prepare output folders inside ADIVINA
$buildRoot = Join-Path $scriptDir "builds"
if (-Not (Test-Path $buildRoot)) { New-Item -ItemType Directory -Path $buildRoot | Out-Null }
$newFolder = Join-Path $buildRoot "$Name-Windows"
if (Test-Path $newFolder) { Remove-Item $newFolder -Recurse -Force }
New-Item -ItemType Directory -Path $newFolder | Out-Null

# Copy exe/result from dist
$distPath = Join-Path $scriptDir "dist"
if ($OneFile) {
    $exePath = Join-Path $distPath ("$Name.exe")
    if (-Not (Test-Path $exePath)) {
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

# Copy personajes.json and common assets from ADIVINA
$patterns = @('*.json')
foreach ($pattern in $patterns) {
    $items = Get-ChildItem -Path $scriptDir -Recurse -Include $pattern -File -ErrorAction SilentlyContinue
    foreach ($it in $items) { Copy-Item -Path $it.FullName -Destination $newFolder -Force }
}

$assetDirs = @('assets','data','images','sounds')
foreach ($d in $assetDirs) {
    $p = Join-Path $scriptDir $d
    if (Test-Path $p) { Copy-Item -Path $p -Destination (Join-Path $newFolder $d) -Recurse -Force }
}

# Create README inside the build
$readme = @()
$readme += "Adivina Quién - Naruto Edition (Windows)"
$readme += "======================================"
$readme += "Instrucciones:"
$readme += "1) Extrae el ZIP en una carpeta."
$readme += "2) Ejecuta $Name.exe para iniciar el juego."
$readme += "3) Asegúrate de que cualquier archivo .json esté en la misma carpeta que el exe si el juego lo requiere."
$readmePath = Join-Path $newFolder "README.txt"
$readme | Out-File -FilePath $readmePath -Encoding UTF8

# Create ZIP
$zipPath = Join-Path $buildRoot ("$Name-Windows.zip")
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $newFolder '*') -DestinationPath $zipPath -Force

Write-Host "Build completado. Carpeta: $newFolder"
Write-Host "ZIP creado en: $zipPath"
Write-Host "Listo para subir a itch.io"
