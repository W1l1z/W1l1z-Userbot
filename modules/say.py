#  W1l1z-Userbot - telegram userbot
#  Copyright (C) 2024-present W1l1z Userbot Organization

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(filters.command(["say", "s"], prefix) & filters.me)
async def say(_, message: Message):
    if len(message.command) == 1:
        return
    command = " ".join(message.command[1:])
    await message.edit(f"<code>{command}</code>")


modules_help["say"] = {
    "say [command]*": "Send message that won't be interpreted by userbot",
}
