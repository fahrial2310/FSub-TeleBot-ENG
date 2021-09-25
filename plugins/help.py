import logging
from config import Messages as tr
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

SUPPORT_NAME = Config.SUPPORT_NAME
OWNER_USERNAME = Config.OWNER_USERNAME
UPDATES_CH = Config.UPDATES_CH
UPDATES_NAME = Config.UPDATES_NAME
SUPPORT_GRP = Config.SUPPORT_GRP

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id, Config.BOT_NAME),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = "https://github.com/fahrial2310/FSub-Telebot-ENG"
        button = [
            [InlineKeyboardButton(text = '☠️ Creator ☠️', url=f"https://t.me{OWNER_USERNAME}")],
            [InlineKeyboardButton(text = f'☠️ {SUPPORT_NAME} ☠️', url=f"https://t.me/{SUPPORT_GRP}"),
             InlineKeyboardButton(text = f'☠️ {UPDATES_NAME} ☠️', url=f"https://t.me/{UPDATES_CH}")],
            [InlineKeyboardButton(text = '☠️ Source Code ☠️', url=url)],
            [InlineKeyboardButton(text = '◀️Back', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️Back', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Next▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
