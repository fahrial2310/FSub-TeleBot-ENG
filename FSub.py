import logging
from pyrogram import Client
from config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "FSub-TeleBot-ENG",
        "help"
    ]
)

app = Client(
     'FSub-TeleBot-ENG',
      bot_token = Config.BOT_TOKEN,
      bot_name = Config.BOT_NAME,
      bot_username = Config.BOT_USERNAME,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      updates_ch = Config.UPDATES_CH,
      support_grp = Config.SUPPORT_GRP,
      updates_name = Config.UPDATES_NAME,
      support_name = Config.SUPPORT_NAME,
      owner_username = Config.OWNER_USERNAME
      plugins = plugins
)

app.run()
