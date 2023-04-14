# Activate virtual environment
$envPath = Join-Path $PSScriptRoot ".venv\Scripts\activate"
& $envPath

# Run Python script
$mainPath = Join-Path $PSScriptRoot "src\main.py"
python $mainPath

# Deactivate virtual environment
$deactivatePath = Join-Path $PSScriptRoot ".venv\Scripts\deactivate"
& $deactivatePath
