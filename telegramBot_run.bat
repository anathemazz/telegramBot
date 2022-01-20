@echo off

call %~dp0telegramBot\venv\Scripts\activate

cd %~dp0telegramBot

set TOKEN=5021941924:AAGwoickulSzKu3mk0ZQlkI93rbHBGudopM

python telegramBot.py

pause