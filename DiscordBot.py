from discord.ext import commands
import discord
import socket
import subprocess
import time
from mcstatus import JavaServer
import yaml
with open("config.yml", 'r') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)
TOKEN = str(config['botConfig']['TOKEN'])
ip = str(config['botConfig']['IP'])
port = str(config['botConfig']['PORT'])
onStart = str(config['botConfig']['STARTCOMMAND'])
commandprefix = str(config['botConfig']['COMMANDPREFIX'])
botOnline = str(config['langSettings']['general']['botOnline'])

status_OnRun = str(config['langSettings']['statusCommand']['onRun'])
status_online = str(config['langSettings']['statusCommand']['online'])
status_offline = str(config['langSettings']['statusCommand']['offline'])
status_embedTitle = str(config['langSettings']['statusCommand']['embedTitle'])
status_playersOnline = str(config['langSettings']['statusCommand']['playersOnline'])

start_onRun = str(config['langSettings']['startCommand']['onRun'])
start_AlreadyRunning = str(config['langSettings']['startCommand']['serverAlreadyRunning'])
start_StartingServer = str(config['langSettings']['startCommand']['startingServer'])
start_serverOnline = str(config['langSettings']['startCommand']['serverOnline'])

mcserverip = (ip + ':' + port)
bot = commands.Bot(command_prefix=commandprefix)


@bot.event
async def on_ready():
    print(botOnline)


# !!status
@bot.command()
async def status(ctx):
    await ctx.send(status_OnRun)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.settimeout(1)
        s.shutdown(1)
        server = JavaServer.lookup(mcserverip)
        serverstatus = server.status()
        playerlist = serverstatus.players.online
        embedmsg = discord.Embed(title=status_embedTitle, color=0x40CD00)
        embedmsg.add_field(name="Online:", value=status_online, inline=False)
        embedmsg.add_field(name=status_playersOnline, value=playerlist, inline=False)
        await ctx.send(embed=embedmsg)
    except:
        playerlist = 'unknown'
        embedmsg = discord.Embed(title=status_embedTitle, color=0xBC0000)
        embedmsg.add_field(name="Online:", value=status_offline, inline=False)
        embedmsg.add_field(name=status_playersOnline, value=playerlist, inline=False)
        await ctx.send(embed=embedmsg)


# !!test:
@bot.command()
async def test(ctx):
    await ctx.send('The bot is working')


# !!start:
@bot.command()
async def start(ctx):
    await ctx.send(start_onRun)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.settimeout(1)
        s.shutdown(1)
        await ctx.send(start_AlreadyRunning)
    except:
        print(start_StartingServer)
        await ctx.send(start_StartingServer)
        subprocess.Popen(onStart)
        while True:
            try:
                JavaServer.lookup(mcserverip)
                await ctx.send(start_serverOnline)
                break
            except:
                time.sleep(5)
                pass


bot.run(TOKEN)
