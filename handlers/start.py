from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Merhaba {message.from_user.first_name}!</b>

Gruplarınızda müzik çalmanıza izin veren açık kaynaklı bir bot olan WylineBot'tum. 

Hakkımda daha fazla bilgi edinmek için aşağıdaki düğmeleri kullanın.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂️Kullanma Kodları", url="https://t.me/WylineVoiceHelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/OlympusCh4t"
                    ),
                    InlineKeyboardButton(
                        "Support Grup 🔈", url="https://t.me/wylinesupport"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Bir YouTube videosu aramak ister misin?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Hayır ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
