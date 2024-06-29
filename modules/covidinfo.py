
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import modules_help, prefix
from utils.scripts import import_library

Covid = import_library("covid").Covid


@Client.on_message(filters.command("covid", prefix) & filters.me)
async def covid_local(_, message: Message):
    region = " ".join(message.command[1:])
    await message.edit("<b>Data retrieval...</b>")
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit(
            "<b>=======🦠 COVID-19 STATUS 🦠=======</b>\n"
            + f"<b>Region</b>: <code>{local_status['country']}</code>\n"
            + "<b>====================================</b>\n"
            + f"<b>🤧 New cases</b>: <code>{local_status['new_cases']}</code>\n"
            + f"<b>😷 New deaths</b>: <code>{local_status['new_deaths']}</code>\n"
            + "<b>====================================</b>\n"
            + f"<b>😷 Сonfirmed</b>: <code>{local_status['confirmed']}</code>\n"
            + f"<b>❗️ Active:</b> <code>{local_status['active']}</code>\n"
            + f"<b>⚠️ Critical</b>: <code>{local_status['critical']}</code>\n"
            + f"<b>💀 Deaths</b>: <code>{local_status['deaths']}</code>\n"
            + f"<b>🚑 Recovered</b>: <code>{local_status['recovered']}</code>\n"
        )
    except ValueError:
        await message.edit(f"<b>There is no region called {region}</b>")


@Client.on_message(filters.command("regions", prefix) & filters.me)
async def regions_cmd(_, message: Message):
    countries = ""
    await message.edit("<b>Data retrieval...</b>")
    covid = Covid(source="worldometers")
    for region in covid.list_countries():
        countries += f"<code>{region}</code>\n"
    await message.edit(countries)


modules_help["covidinfo"] = {
    "covid [region]*": "COVID-19 status by region",
    "regions": "Available regions</i>\n\n"
    "<b>Worldometer.info statistics are used</b><i>",
}
