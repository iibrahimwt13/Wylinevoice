from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

import callsmusic

import converter
import youtube
import queues

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError
from helpers.filters import command, other_filters
from helpers.wrappers import errors


@Client.on_message(
    filters.command("volume")
)
@wrap
def volume(client, message):
    if len(message.text.split()) == 2 and message.from_user.id in SUDO_USERS:
        try:
            volume = int(message.text.split()[1])
            if volume in range(1, 101):
                volume = f"{volume}%"
                subprocess.Popen(
                    [
                        "pactl",
                        "set-sink-volume",
                        "MySink",
                        volume
                    ]
                ).wait()
                message.reply_text(
                    _("volume_2").format(volume)
                )
                return
        except:
            pass

    current_volume = "".join(re.search(r"Volume\:(.+)\n", subprocess.check_output(
        ["pactl", "list", "sinks"]).decode()).group(0).split()).split("/")[1]

    if message.from_user.id in SUDO_USERS:
        message.reply_text(
            _("volume_1").format(current_volume),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➖",
                            callback_data="decrease_volume"
                        ),
                        InlineKeyboardButton(
                            "➕",
                            callback_data="increase_volume"
                        )
                    ]
                ]
            ),
            quote=True
        )
    else:
        message.reply_text(
            _("volume_1").format(current_volume),
        )


