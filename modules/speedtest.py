#  W1l1z-Userbot - telegram userbot
#  Copyright (C) 2024-present W1l1z Userbot Organization

import speedtest

from pyrogram import Client, types
from .. import loader, utils


def speed_test():
    tester = speedtest.Speedtest()
    tester.get_best_server()
    tester.download()
    tester.upload()
    return tester.results.dict()


@loader.module(name="SpeedTest", author="sh1tn3t")
class SpeedTestMod(loader.Module):
    """Тест интернет-соединения"""

    async def speedtest_cmd(self, app: Client, message: types.Message):
        """Запускает тест скорости. Использование: speedtest"""
        await utils.answer(
            message, "<b>Запускаем тест...</b>")
 
        result = speed_test()
        text = (
            f"<b>Результаты теста:</b>\n\n"
            f"<b>Скачивание:</b> <code>{round(result['download'] / 2 ** 20 / 8, 2)}</code> <b>мб/с</b>\n"
            f"<b>Загрузка:</b> <code>{round(result['upload'] / 2 ** 20 / 8, 2)}</code> <b>мб/c</b>\n"
            f"<b>Задержка:</b> <code>{round(result['ping'], 2)}</code> <b>мc</b>"
        )
        return await utils.answer(
            message, text)