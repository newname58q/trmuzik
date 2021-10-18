from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ᴏɴᴄᴇ ʙᴇɴɪ ʏᴏʀ ɢʀᴜʙᴜɴᴜɴ ʏᴏɴᴇᴛɪᴄɪꜱɪ ᴏʟᴀʀᴀᴋ ᴇᴋʟᴇ</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "SerenityHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"ᴍᴇʀʜᴀʙᴀ ꜱᴇꜱᴛᴇ ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀᴋ ɪᴄɪɴ ɢᴇʟᴅɪᴍ")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>ʏᴀʀᴅɪᴍᴄɪ ʙᴏᴛ ᴢᴀᴛᴇɴ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇ</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 ᴀꜱɪꜱᴛᴀɴ ʙᴏᴛ ɢʀᴜʙᴀ ᴋᴀᴛɪʟᴀᴍᴀᴅɪ 🛑 \n ᴋᴜʟʟᴀɴɪᴄɪ {user.first_name} ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ɢʀᴜᴘᴛᴀ ʏᴀꜱᴀᴋʟᴀɴᴍᴀᴅɪɢɪɴᴅᴀɴ ᴇᴍɪɴ ᴏʟᴜɴ."
            "\n\nᴠᴇʏᴀ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇʟ ɪʟᴇ ᴇᴋʟᴇʏɪɴ ᴠᴇ ʏᴇɴɪᴅᴇɴ ᴅᴇɴᴇʏɪɴ</b>",
        )
        return
    await message.reply_text(
            "<b>ʏᴀʀᴅɪᴍᴄɪ ᴜꜱᴇʀʙᴏᴛ ꜱᴏʜʙᴇᴛɪɴɪᴢᴇ ᴋᴀᴛɪʟᴅɪ</b>",
        )
    
@USER.on_message(filters.group & filters.command(["asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>ᴋᴜʟʟᴀɴɪᴄɪ ɢʀᴜʙᴜɴᴜᴢᴅᴀɴ ᴀʏʀɪʟᴀᴍᴀᴅɪ! ꜰʟᴏᴏᴅᴡᴀɪᴛꜱ ᴏʟᴀʙɪʟɪʀ."
            "\n\nʏᴀ ᴅᴀ ʙᴇɴɪ ᴍᴀɴᴜᴇʟ ᴏʟᴀʀᴀᴋ ɢʀᴜʙᴜɴᴜᴢᴀ ᴀᴛᴀʙɪʟɪʀꜱɪɴɪᴢ.</b>",
        )
        return
