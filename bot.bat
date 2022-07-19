@echo off
cls
:bot
python DiscordBot.py
echo "The bot is going to restart in 10 seconds. Unless CTRL+C is pressed"
timeout 10
goto bot