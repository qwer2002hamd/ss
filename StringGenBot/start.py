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
        text=f"""✷ مـرحبا بـك عزيزي {msg.from_user.mention},
✷ انا بـوت {me2},
✷ لاستخراج جلسات البايروجرام و تيرمكس,

✷ يمكنك استخراج الجلسه من الاوامر والازرار ادناه 👇🏻✔️
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="‹ بدء ›", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("‹ قـناة البوت ›", url="https://t.me/ah07v"),
                    InlineKeyboardButton("‹ مـطور الـبوت ›", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
