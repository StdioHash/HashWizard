@echo off
echo loading...

:: checking if python installed in path
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed in PATH, please install it.
    pause
    exit /b
)

for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set PYVER=%%a

echo Found Python version %PYVER%

for /f "tokens=1,2 delims=." %%i in ("%PYVER%") do (
    set MAJOR=%%i
    set MINOR=%%j
)

if %MAJOR% LSS 3 (
    echo Python version is not compatible. Please install Python 3.7+.
    pause
    exit /b
)
if %MAJOR%==3 if %MINOR% LSS 7 (
    echo Python version is not compatible. Please install Python 3.7+.
    pause
    exit /b
)

echo Starting ui/python/main.py...
python ui/python/main.py
pause
