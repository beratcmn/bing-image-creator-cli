# Check if the venv module is available
if (-not(Get-Command -Name "python" -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python first." -ForegroundColor Red
    exit
}

if (-not(Get-Module -Name "venv" -ErrorAction SilentlyContinue)) {
    Write-Host "Installing venv module..." -ForegroundColor Yellow
    python -m pip install virtualenv
}

# Create a virtual environment
$envName = "venv"
if (Test-Path $envName) {
    Write-Host "$envName already exists." -ForegroundColor Yellow
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Green
    python -m venv $envName
}

# Activate the virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
& "$envName\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Done!" -ForegroundColor Green
