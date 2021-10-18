from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import cache.admins

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'ᴅᴜʀᴅᴜʀᴜʟᴅᴜ'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 ᴍᴜᴢɪᴋ ᴀᴄɪᴋ ᴅᴇɢɪʟ!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**ɴᴏꜱᴛᴀʟᴊɪ ᴍᴜᴢɪᴋ :-** 🤐 ᴅᴜʀᴅᴜʀᴜʟᴅᴜ!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 ʜɪᴄʙɪʀꜱᴇʏ ᴅᴜʀᴅᴜʀᴜʟᴍᴀᴅɪ!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**ɴᴏꜱᴛᴀʟᴊɪ ᴍᴜᴢɪᴋ :-** 🥳 ᴅᴇᴠᴀᴍ ᴇᴅɪʏᴏʀ!")


@Client.on_message(command("son") & other_filters)
@errors
@authorized_users_only
async def bitir(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**ɴᴏꜱᴛᴀʟᴊɪ ᴍᴜᴢɪᴋ :-** 🙄 ʜɪᴄʙɪʀꜱᴇʏ ᴏʏɴᴀᴛɪʟᴍɪʏᴏʀ!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ **ᴍᴜᴢɪᴋ ᴋᴀᴘᴀᴛɪʟᴅɪ!**\n\n• **ᴜꜱᴇʀʙᴏᴛ'ᴜɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛ ʙᴀɢʟᴀɴᴛɪꜱɪ ᴋᴇꜱɪʟᴅɪ**")



@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("🙆‍♂️ ᴀᴛʟᴀᴛɪʟᴀᴄᴀᴋ ᴍᴜᴢɪᴋ ʏᴏᴋ!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("➡️ **ʙɪʀ ꜱᴏɴʀᴀᴋɪ ᴘᴀʀᴄᴀʏᴀ ɢᴇᴄɪʟᴅɪ!**\n\n• **ᴏʏɴᴀᴛɪʟɪʏᴏʀ.. 🥳**" )

@Client.on_message(command("admincache"))
@errors
@authorized_users_only 
async def admincache(_, message: Message):
    cache.admins.set(
        message.chat.id,
        [member.user for member in await message.chat.get_members(filter="administrators")]
    )
    await message.reply_text("👮‍♀️ ʏᴏɴᴇᴛɪᴄɪ ᴏɴʙᴇʟʟᴇɢɪ ʏᴇɴɪʟᴇɴᴅɪ!") 
