#  W1l1z-Userbot - telegram userbot
#  Copyright (C) 2024-present W1l1z Userbot Organization

import random

from pyrogram import Client, types
from .. import loader, utils


@loader.module("TagAll", "sh1tn3t")
class TagAllMod(loader.Module):
    """Тегает всех в чате"""

    async def tagall_cmd(self, app: Client, message: types.Message, args: str):
        """Начинает всех тегать. Использование: tagall [текст]"""
        chat = message.chat
        if chat.type == "private":
            return await utils.answer(
                message, "Это не чат")

        args = args or "говно залупное\n                пашет." 

        users = [
            f"<a href=\"tg://user?id={member.user.id}\">\u2060</a>"
            async for member in chat.iter_members()
            if not (member.user.is_bot or member.user.is_deleted)
        ]

        random.shuffle(users)
        await message.delete()

        for output in [
            users[i: i + 5]
            for i in range(0, len(users), 5)
        ]:
            await message.reply(args + "\u2060".join(output))

        return