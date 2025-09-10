@echo off
cd /d "%~dp0"

set "FILE=main.py"

if exist "%PYFILE%" (
    echo START %fILE%
    python "%FILE%"
) else (
    echo ERROR 404!
    echo :
    dir /b *.py
)

pause
