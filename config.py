import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_NAME = os.environ.get("BOT_NAME")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
	UPDATES_CH = os.environ.get("UPDATES_CH")
	SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
	UPDATES_NAME = os.environ.get("UPDATES_NAME")
	SUPPORT_NAME = os.environ.get("SUPPORT_NAME")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(853393439)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[☠️](https://telegra.ph/file/ac48f2037d79b1763d089.jpg) **FORCE SUBSCRIBE :**\n\nhey,i'm {BOT_NAME} can Force Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "[☠️](https://telegra.ph/file/83c970d7130ead36a8b72.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n☠️ Note: Only Creator Of The Group Can Setup Me.",
        
        "[☠️](https://telegra.ph/file/fe1111b216042f2cfb883.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[☠️](https://telegra.ph/file/ac48f2037d79b1763d089.jpg) **DEVELOPED BY {OWNER_USERNAME}**"
      ]

      START_MSG = "**Hey! [☠️](https://telegra.ph/file/ac48f2037d79b1763d089.jpg) [{}](tg://user?id={})**\n\nmy name is {BOT_NAME},I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help"
