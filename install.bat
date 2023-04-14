@echo off

REM Create a virtual environment in a subdirectory called "venv"
echo Creating virtual environment...
python -m venv venv

REM Activate the virtual environment
echo Activating virtual environment...
venv\Scripts\activate.bat

REM Check if pip package is installed
python -m pip > NUL 2>&1
if %errorlevel% == 1 (
    echo Upgrading pip...
    python -m ensurepip --upgrade
)

REM Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

echo Done!
