from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""ᴍᴇʀʜᴀʙᴀ 👋! **ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘʟᴀʀɪɴɪɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪɴᴅᴇ ᴍᴜᴢɪᴋ ᴄᴀʟᴀʙɪʟɪʏᴏʀᴜᴍ. ꜱɪᴢɪ ꜱᴀꜱɪʀᴛᴀᴄᴀᴋ ᴘᴇᴋ ᴄᴏᴋ ʜᴀʀɪᴋᴀ ᴏᴢᴇʟʟɪɢɪᴍ ᴠᴀʀ!** 🥳 \n\n🔴 **ᴛᴇʟᴇɢʀᴀᴍᴅᴀ ʙᴇɴɪ ɴᴀꜱɪʟ ᴋᴜʟʟᴀɴᴀʙɪʟᴇᴄᴇɢɪɴɪᴢɪ ᴏɢʀᴇɴᴍᴇᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ >> /help ʙᴜᴛᴏɴᴜɴᴀ ʙᴀꜱɪɴɪᴢ.** \n\n🔴 **ɢʀᴜʙᴜɴᴜᴢᴜɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛɪɴᴅᴇ, ᴍᴜᴢɪᴋ ᴄᴀʟᴀʙɪʟᴍᴇᴍ ɪᴄɪɴ ᴀꜱɪꜱᴛᴀɴɪɴ ɢʀᴜʙᴜɴᴜᴢᴅᴀ ᴏʟᴍᴀꜱɪ ɢᴇʀᴇᴋɪʀ.** \n\n🔵 ʙᴜ ᴄᴀʟɪꜱᴍᴀ [Jack Medya](https://t.me/SemtBizimEvKira) ᴛᴀʀᴀꜰɪɴᴅᴀɴ ᴋᴇʏꜰᴇ ᴅᴇɢᴇʀ ᴅᴜᴢᴇɴʟᴇɴᴍɪꜱᴛɪʀ.!
      """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📣 ʀᴇꜱᴍɪ ᴋᴀɴᴀʟ", url="https://t.me/jackmedya")
                  ],[
                    InlineKeyboardButton(
                        "💬 ꜱᴏʜʙᴇᴛ ɢʀᴜʙᴜ", url="https://t.me/SemtBizimEvkira"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎵 ᴍᴘ3 ᴀʀᴀᴍᴀ ʙᴏᴛᴜ", url="https://t.me/DeezerMusicBot"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "🎯 ᴜꜱᴇʀᴛᴀɢɢᴇʀ ʙᴏᴛ", url="https://t.me/jacktaggerbot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏꜱᴜ ᴀʀᴀᴍᴀᴋ ɪꜱᴛɪʏᴏʀ ᴍᴜꜱᴜɴᴜᴢ? ?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 ɢʀᴏᴜᴘ", url="https://t.me/SemtBizimEvKira"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.first_name}! 
\n/oynat - ᴍᴘ3 ꜰᴏʀᴍᴀᴛɪɴᴀ ᴜʏɢᴜɴ ᴅᴏꜱʏᴀʟᴀʀɪ ᴄᴀʟɪꜱᴛɪʀᴍᴀᴋ ɪᴄɪɴ ᴅᴇᴇꜱᴇʀ ᴍᴜꜱɪᴄ ᴅᴇꜱᴛᴇᴋʟᴇʀ
/bul - ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ꜱᴀʀᴋɪʟᴀʀɪ ʜɪᴢʟɪ ʙɪʀ ꜱᴇᴋɪʟᴅᴇ ɪɴᴅɪʀɪɴ
/ytplay - ʏᴏᴜᴛᴜʙᴇ'ᴅᴀɴ ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ᴍᴜᴢɪɢɪ ᴄᴀʟᴀʀ
/id - ꜱᴏʜʙᴇᴛ ɪᴅ ᴠᴇ ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ɪᴅ'ꜱɪ ʜᴀᴋᴋɪɴᴅᴀ ʙɪʟɢɪ ᴠᴇʀɪʀ
\n*🙋‍♂️ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ɪᴄɪɴ*
/durdur - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴀᴋʟᴀᴛᴍᴀ
/devam - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏᴀ ᴅᴇᴠᴀᴍ ᴇᴛ
/atla - ꜱᴏɴʀᴀᴋɪ ꜱᴀʀᴋɪʏɪ ᴄᴀʟ
/son- ᴍᴜᴢɪᴋ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴅᴜʀᴍᴀ
/asistan - ᴀꜱɪꜱᴛᴀɴɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ
/asistanby - ᴀꜱɪꜱᴛᴀɴɪɴɪᴢɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇɴ ᴄɪᴋᴀʀɪʀ
/admincache - ʏᴏɴᴇᴛɪᴍ ᴏɴ ʙᴇʟʟᴇᴋ ʏᴇɴɪʟᴇʀ
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 ᴍᴜᴢɪᴋ ᴋᴀɴᴀʟɪ", url="https://t.me/jackmedya"
                    )
                ]
            ]
        )
    )    
