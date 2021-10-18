import os
from os import path
import requests
import aiohttp
import youtube_dl
from pyrogram import Client
from pyrogram.types import Message, Voice
from youtube_search import YoutubeSearch
from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("ytplay") & other_filters)
@errors
async def ytplay(_, message: Message):

    lel = await message.reply("🔎 **ᴀʀɪʏᴏʀᴜᴍ** 😉 ʙᴇᴋʟᴇʏɪɴɪᴢ...")
    sender_id = message.from_user.id
    user_id = message.from_user.id
    sender_name = message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    await lel.edit("🎵 **ꜱᴇꜱʟᴇʀ ɪꜱʟᴇɴɪʏᴏʀ..** ʙɪʀᴀᴢ ᴢᴀᴍᴀɴ ᴀʟᴀʙɪʟɪʀ..")
    ydl_opts = {"format": "bestaudio[ext=m3a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        lel.edit(
            "❌ ꜱᴀʀᴋɪ ʙᴜʟᴜɴᴀᴍᴀᴅɪ.\n\nʙᴀꜱᴋᴀ ʙɪʀ ꜱᴀʀᴋɪ ᴅᴇɴᴇʏɪɴ ᴠᴇʏᴀ ᴅᴜᴢɢᴜɴ ʏᴀᴢɪɴ."
        )
        print(str(e))
        return
        
    keyboard4 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Watch On YouTube",
                        url=f"{url}")
                   
                ]
            ]
        )
        
    keyboard3 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Watch On YouTube",
                        url=f"{url}")
                   
                ]
            ]
        )

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💬 ɢʀᴏᴜᴘ",
                        url=f"https://t.me/SemtBizimEvKiraa"),
                    InlineKeyboardButton(
                        text="🌀 ᴀꜱɪꜱᴛᴀɴ",
                        url=f"https://t.me/musicbotasistann")
                   
                ]
            ]
        )

    keyboard2 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💬 ɢʀᴏᴜᴘ",
                        url=f"https://t.me/SemtBizimEvKiraa"),
                    InlineKeyboardButton(
                        text="🌀 ᴀꜱɪꜱᴛᴀɴ",
                        url=f"https://t.me/musicbotasistann")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None

    if audio:
        await lel.edit_text("Lel")

    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("🙆‍♂️ ʙᴀɴᴀ ᴏʏɴᴀʏᴀᴛᴀᴄᴀᴋ ʙɪʀ ꜱᴇʏ ᴠᴇʀᴍᴇᴅɪɴ.!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=thumb_name, 
        caption=f"#⃣ ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ꜱᴀʀᴋɪ **ꜱɪʀᴀʏᴀ** ᴀʟɪɴᴅɪ. 😉 {position}!",
        reply_markup=keyboard2)
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo=thumb_name,
        reply_markup=keyboard,
        caption="▶️ **ᴏʏɴᴀᴛɪʟɪʏᴏʀ** ʙᴜʀᴀᴅᴀ ɪꜱᴛᴇɴᴇɴ ꜱᴀʀᴋɪ {} ʏᴏᴜᴛᴜʙᴇ ᴀʀᴀᴄɪʟɪɢɪʏʟᴀ 🥳".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
