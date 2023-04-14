@echo off

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run Python script
python src\main.py

REM Deactivate virtual environment
call .venv\Scripts\deactivate
