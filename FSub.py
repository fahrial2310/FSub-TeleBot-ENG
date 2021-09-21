import logging
from pyrogram import Client
from config import Config

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = Config.BOT_TOKEN

APP_ID = Config.APP_ID
API_HASH = Config.API_HASH

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)


Client(
    "ForceSubscribe",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
).run()
