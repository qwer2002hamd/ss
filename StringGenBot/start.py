from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},
Tʜɪs ɪs {me2},
ᴇʟʟᴏ ʙᴀʙʏ 😻,
             🙈  ᴍᴇᴏᴡ ᴍᴇᴏᴡ ❤️

𖢵 Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ!

┏━━━━━━━━━━━━━━━━━
┠ ๏ Uᴘᴅᴀᴛᴇꜱ :- @sukunupdates
┠ ๏ Sᴜᴘᴘᴏʀᴛ :- @sukunsupports
┗━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ ᴛᴇᴀᴍ sᴜᴋᴜɴ ❣️", url="https://t.me/TeamSukun"),
                    InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", user_id=OWNER_ID)
                ],
                [
                    InlineKeyboardButton("ᴀᴅᴅ ѕυкυη χ мυѕι¢", url="https://t.me/sukunmusicrobot?startgroup=new")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
