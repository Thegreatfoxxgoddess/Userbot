"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Please Set ALIVE_NAME In Heroku"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Gracias! Your Userbot Is Alive And Running!!`\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nFork by:` Akashi\n"
                     "`Bot created by:` [Akashi](tg://user?id=1089637689)\n"
                     "`Database Status: Normal!\n`"
                     f"`Userbot Owner`: **{DEFAULTUSER}**\n"
                     "[Deploy This Userbot Now](https://github.com/emperorakashi4/userbot)")
