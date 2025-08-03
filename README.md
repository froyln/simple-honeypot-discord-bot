# simple-honeypot-discord-bot
Simple honeypot bot, works only with one server (more easy code). 

> [!WARNING]
> The discord bot ONLY works with one server.
> Multiple servers require multiple settings.

## Dependencies
[Python ](https://www.python.org) versions 3.9+. Other versions and implementations may or may not work correctly.

[Discord.py](https://discordpy.readthedocs.io/en/stable/) ```pip install discord.py```

## Installation
Clone the github project
```
git clone https://github.com/froyln/simple-honeypot-discord-bot/
```
Open settings.json
```
cd simple-honeypot-discord-bot
nano settings.json
```
Set bot token and channel id.

## How works
When people send any message on #honeypot, bot bans the author message. 
