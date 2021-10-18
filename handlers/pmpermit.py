from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"ᴍᴇʀʜᴀʙᴀ, ᴍᴜᴢɪᴋ ᴀꜱɪꜱᴛᴀɴɪ ʜɪᴢᴍᴇᴛɪᴅɪʀ.\n\n ❗️ ᴋᴜʀᴀʟʟᴀʀ:\n   - ꜱᴏʜʙᴇᴛᴇ ɪᴢɪɴ ʏᴏᴋ\n   - ɪꜱᴛᴇɴᴍᴇʏᴇɴ ᴘᴏꜱᴛᴀʏᴀ ɪᴢɪɴ ᴠᴇʀɪʟᴍᴇᴢ\n\n 👉 **ᴜꜱᴇʀʙᴏᴛ ɢʀᴜʙᴜɴᴜᴢᴀ ᴋᴀᴛɪʟᴀᴍᴀᴢꜱᴀ ɢʀᴜᴘ ᴅᴀᴠᴇᴛ ʙᴀɢʟᴀɴᴛɪꜱɪ ᴠᴇʏᴀ ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ ɢᴏɴᴅᴇʀ.**\n\n ⚠️ ꜱᴏʀᴜᴍʟᴜʟᴜᴋ: ʙᴜʀᴀᴅᴀ ʙɪʀ ᴍᴇꜱᴀᴊ ɢᴏɴᴅᴇʀɪʏᴏʀꜱᴀɴɪᴢ, ʏᴏɴᴇᴛɪᴄɪ ᴍᴇꜱᴀᴊɪɴɪᴢɪ ɢᴏʀᴇᴄᴇᴋ ᴠᴇ ꜱᴏʜʙᴇᴛᴇ ᴋᴀᴛɪʟᴀᴄᴀᴋᴛɪʀ\n    - ʙᴜ ᴋᴜʟʟᴀɴɪᴄɪʏɪ ɢɪᴢʟɪ ɢʀᴜᴘʟᴀʀᴀ ᴇᴋʟᴇᴍᴇʏɪɴɪᴢ.\n   - ᴏᴢᴇʟ ʙɪʟɢɪʟᴇʀɪ ʙᴜʀᴀᴅᴀ ᴘᴀʏʟᴀꜱᴍᴀʏɪɴ\n\n")
  return                        
