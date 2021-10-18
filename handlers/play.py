from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues
import aiohttp
from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import os
import json
import ffmpeg
import aiohttp
import aiofiles
import asyncio
import requests
import converter
from os import path
from asyncio.queues import QueueEmpty
from pyrogram import Client, filters
from typing import Callable
from helpers.channelmusic import get_chat_id
from callsmusic import callsmusic
from callsmusic.queues import queues
from helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from callsmusic.callsmusic import client as USER
from pyrogram.errors import UserAlreadyParticipant
from downloaders import youtube

from config import que, THUMB_IMG, DURATION_LIMIT, BOT_USERNAME, BOT_NAME, UPDATES_CHANNEL, GROUP_SUPPORT, ASSISTANT_NAME
from helpers.filters import command, other_filters
from helpers.decorators import authorized_users_only
from helpers.gets import get_file_name, get_url
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, Voice
from cache.admins import admins as a
from PIL import Image, ImageFont, ImageDraw

aiohttpsession = aiohttp.ClientSession()
chat_id = None
DISABLED_GROUPS = []
useer ="NaN"

@Client.on_message(command("oynat") & other_filters)
@errors
async def oynat(_, message: Message):

    lel = await message.reply("🔄 **ꜱᴇꜱʟᴇʀ ɪꜱʟᴇɴɪʏᴏʀ..**🔥")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🌀 ᴀꜱɪꜱᴛᴀɴ",
                        url=f"https://t.me/musicbotasistann"),
                    InlineKeyboardButton(
                        text="💬 ɢʀᴏᴜᴘ​",
                        url=f"https://t.me/SemtBizimEvKiraa")
                 ],
                 [
                    InlineKeyboardButton(
                        text="🇹🇷 ᴄʀᴇᴀᴛᴏʀ 🇹🇷",
                        url=f"https://t.me/jackdanielssx"),
                    InlineKeyboardButton(
                        text="🇹🇷 ᴄʀᴇᴀᴛᴏʀ 🇹🇷",
                        url=f"https://t.me/mahoaga")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("🤷‍♀️ ʙᴀɴᴀ ᴏʏɴᴀᴛɪʟᴀᴄᴀᴋ ᴍᴘ3 ꜰᴏʀᴍᴀᴛɪ ᴠᴇʀᴍᴇᴅɪɴ.!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="https://i.ibb.co/Qkz78hx/images-1.jpg",
        caption="**👤 ᴛᴀʟᴇᴘ ᴇᴅᴇɴ:** {}\n\n**#⃣ ꜱɪʀᴀᴅᴀᴋɪ ᴘᴀʀᴄᴀ ᴇᴋʟᴇɴᴅɪ:** {}".format( 
        message.from_user.mention(), position
        ),
        reply_markup=keyboard)
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://i.ibb.co/nwHdB2D/images.jpg",
        reply_markup=keyboard,
        caption="▶️ **ᴏʏɴᴀᴛɪʟɪʏᴏʀ** ʙᴜʀᴀᴅᴀ ɪꜱᴛᴇɴᴇɴ ꜱᴀʀᴋɪ ᴛᴀʀᴀꜰɪɴᴅᴀɴɪᴢᴅᴀɴ {}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
