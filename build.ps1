<# Wrapper build.ps1 - Delegates to Parcial 2\ADIVINA\build.ps1

Este archivo en la raíz ahora delega la ejecución al script específico dentro de
`Parcial 2\ADIVINA` para mantener todo el material del juego organizado.

Uso:
  .\build.ps1 [<args>]

Ejemplo: .\build.ps1 -OneFile -Name "AdivinaQuien"
#>

Write-Host "Delegando a Parcial 2\ADIVINA\build.ps1"
$delegate = Join-Path $PSScriptRoot "Parcial 2\ADIVINA\build.ps1"
if (-Not (Test-Path $delegate)) {
    Write-Error "No se encontró el script delegado: $delegate"
    exit 1
}

# Forward all arguments to the delegated script
& powershell -NoProfile -ExecutionPolicy Bypass -File $delegate @args
exit $LASTEXITCODE
