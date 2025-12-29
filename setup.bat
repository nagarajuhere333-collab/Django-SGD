@echo off
echo ====================================
echo SGD Events - Setup Script
echo ====================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
echo Virtual environment created!
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate
echo Virtual environment activated!
echo.

echo Step 3: Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed!
echo.

echo Step 4: Running migrations...
python manage.py makemigrations
python manage.py migrate
echo Migrations completed!
echo.

echo ====================================
echo Setup completed successfully!
echo ====================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo To create an admin user, run:
echo   python manage.py createsuperuser
echo.
echo Access the site at: http://127.0.0.1:8000/
echo ====================================

pause
