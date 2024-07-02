from pyrogram import Client, filters
from PBXMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command(["owner"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.group
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1232e6dca7142e8ed175a.jpg",
        caption=f"""☠ ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ 🌸""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" ʙᴀᴅ 🌸", url=f"https://t.me/ll_BAD_MUNDA_ll"
                    ),
                    InlineKeyboardButton(
                        text=" ᴍᴀɴɪ 🌸", url=f"https://t.me/ll_mxni_ll"
                    ),
                ],
            ]
        ),
    )


@app.on_message(
    filters.command(["owner"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.group
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1232e6dca7142e8ed175a.jpg",
        caption=f"""☠ ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ 🌸""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" ʙᴀᴅ 🌸", url=f"https://t.me/ll_BAD_MUNDA_ll"
                    ),
                    InlineKeyboardButton(
                        text=" ᴍᴀɴɪ 🌸", url=f"https://t.me/ll_mxni_ll"
                    ),
                ],
            ]
        ),
    )


@app.on_message(
    filters.command(["owner"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.group
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1232e6dca7142e8ed175a.jpg",
        caption=f"""☠ ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ 🌸""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=" ʙᴀᴅ 🌸", url=f"https://t.me/ll_BAD_MUNDA_ll"
                    ),
                    InlineKeyboardButton(
                        text=" ᴍᴀɴɪ 🌸", url=f"https://t.me/ll_mxni_ll"
                    ),
                ],
            ]
        ),
    )
