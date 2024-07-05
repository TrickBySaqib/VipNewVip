from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from PBXMUSIC import app


X = "PUNJABI_CHATTING_HUB"


@app.on_message(filters.incoming & filters.private, group=-1)
async def _channel(app: Client, msg: Message):
    if not X:
        return
    try:
        try:
            await app.get_chat_member(X, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/PUNJABI_CHATTING_HUB" + X
            else:
                chat_info = await app.get_chat(X)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="url",
                    caption=f"hello",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="ᴄʟɪᴄᴋ",
                                    url="https://t.me/THE_PUNJABI_BANDE",
                                ),
                            ],
                        ]
                    ),
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print("promote admin me ")
