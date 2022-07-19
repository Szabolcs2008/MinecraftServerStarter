#Minecraft Server Starter Discord bot

## Setup:

To run this, you need to have a discord application setup!

You have to run the bot on the same computer, as the server!

1. download the GitHub source code
2. Unzip the folder
3. Configure the bot in the config.yml file
     - Paste your discord bot's token after: TOKEN:
     - Write your IP after IP:
     - Write your server's port after PORT: 
     - Set a start command for your server after STARTCOMMAND: 
     - If you want set a prefix for the bot commands (default: !!)
     - If you want configure the langauge settings (default: Hungarian)
4. Run the bot.bat or the bot.sh file

if you can't run the bot.sh file:
```
sudo chmod +x bot.sh
```

### Dependencies:

- discord.py
- mcstatus
- pyyaml

Install the dependencies:
```
pip install discord
pip install pyyaml
pip instal mcststus
```

###My configuration (example):
```
botConfig:
  TOKEN: my-discord-token
  IP: my-ip(ex. 1.2.3.4)
  PORT: 25565
  STARTCOMMAND: ./start.sh
  COMMANDPREFIX: "!!" #default: !!
embedConfig:
  #Not finished

langSettings: #Customise the messages (DOESN'T SUPPORT NEW LINES)
  general:
    botOnline: "Bot elérhető" #Message to send when bot goes online (python console)
  statusCommand:
    onRun: "Információ lekérdezése" #Message to send on running the command
    online: "Igen" #Messsge to send if server online
    offline: "nem" #Message to send if server offline
    embedTitle: "Szerver info:" 
    playersOnline: "Játékosok online:" 
  startCommand:
    onRun: "Szerver ellenőrzése..."
    serverAlreadyRunning: "A szerver már fut!"
    startingServer: "Szerver indítása"
    serverOnline: "Szerver online" #Message to send when the server is online
```