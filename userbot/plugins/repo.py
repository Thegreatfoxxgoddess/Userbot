from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("repo ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("You")
        await asyncio.sleep(0.2)
        await event.edit("Like")
        await asyncio.sleep(0.2)
        await event.edit("My")
        await asyncio.sleep(0.2)
        await event.edit("Userbot?")
        await asyncio.sleep(0.2)
        await event.edit("Here's")
        await asyncio.sleep(0.2)
        await event.edit("The")
        await asyncio.sleep(0.2)
        await event.edit("Link")
        await asyncio.sleep(0.2)
        await event.edit("Click [Here](https://github.com/emperorakashi4/Userbot) To Deploy This Userbot.")
