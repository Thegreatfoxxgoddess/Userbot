#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils
import random


def register(cb):
    cb(YesNoMod())


@loader.tds
class YesNoMod(loader.Module):
    """Helps you make important life choices"""
    strings = {"name": "YesNo"}

    def __init__(self):
        self.name = self.strings["name"]

    async def yesnocmd(self, message):
        """Make a life choice"""
        # TODO translate
        yes = ["Yes", "Yup", "Absolutely", "Non't"]
        no = ["No", "Nope", "Nah", "Yesn't"]
        if random.getrandbits(1):
            response = random.choice(yes)
        else:
            response = random.choice(no)
        await utils.answer(message, response)
