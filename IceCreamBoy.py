'''
    "IceCreamBoy" is simple AI bot for the Discord platform, written in the Python programming language. If you have any questions or suggestions, please contact me by email "moderkascriptsltd@gmail.com". Have a nice day!
    Copyright (C) 2023 ttwiz_z

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


from Configuration import *
from VercelAI import Client
from disnake.ext import commands
from disnake import Intents
from disnake import Activity
from disnake import ActivityType

if USE_RECURSION:
    from sys import setrecursionlimit
    setrecursionlimit(RECURSION_LIMIT)

if PROXY != "":
    ice = Client(proxy = PROXY)
else:
    ice = Client()

def answer(message : str):
    try:
        result = ""
        for chunk in ice.generate(MODEL, message):
            result += chunk
        return result
    except:
        if USE_RECURSION:
            return answer(message)
        else:
            return "Oh, I think I'm out of ice cream! 🍨 I'm really sorry, please try again later! 😔"

bot = commands.InteractionBot(intents = Intents.all())

@bot.event
async def on_command_error(_, exception):
    try:
        if isinstance(exception, commands.errors.CommandNotFound):
            return None
    except:
        pass

@bot.event
async def on_ready():
    try:
        await bot.change_presence(activity = Activity(type = ActivityType.watching, name = "/ai"))
        if DEBUG:
            print(f"{bot.user} is online!")
    except:
        pass

@bot.slash_command(description = "Generates a response to your message! 🍨")
async def ai(inter, message : str):
    await inter.response.defer()
    try:
        await inter.edit_original_response(answer(message))
    except:
        await inter.edit_original_response("Oh, I think I'm out of ice cream! 🍨 I'm really sorry, please try again later! 😔")

bot.run(TOKEN)