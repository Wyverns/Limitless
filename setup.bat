@echo off
echo Starting setup...

python -m venv venv

echo Created virtual environment.

python tools\setup.py
echo Completed process, close this window and write execute venv\Scripts\activate then install the required packages.
PAUSE