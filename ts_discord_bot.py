import discord
from googlesearch import search
from random import randint
import datetime
from dateutil.relativedelta import relativedelta
from discord.ext import commands
import time
import sched

site = "site:https://wotlk-twinhead.twinstar.cz/"

file = discord.File('duc.wav')

dodgin_insults = {0: "I need an innervate. Now another. and another"}

raid_times = "Thursday: \t8:30PM PST - 12:00AM PST\nSunday: \t8:00PM PST - 12:00AM PST\nTuesday: \t8:45PM PST - 12:00AM PST (OPTIONAL SIGNUP 10M)"

loot_rules = """Our loot system is a hybrid Loot Council and EPGP style point system.

Players receive loot points for hard mode items, players with higher loot points have lower priority on hard-mode loot than players who have not yet received hard-mode loot. This is tracked in a publicly viewable spreadsheet."""

commands_list = ["!db/!item:\t Search twinstar for a specific item or mob\n"
                 "!raidtimes:\t Display our raid times\n"
                 "!loot:\t Display our loot rules\n"
                 "!raid:\t Display time until next raid\n"
                 "!flush:\t Display time until next arena point flush\n"
                 "!nerf:\t Display time until Ulduar nerfs\n"
                 "!docs:\t Display loot spreadsheet\n"
                 "!logs:\t Display a link to our World of Logs\n"
                 "\nMeme Commands:\n----------------------\n"
                 "!dodgin:\t Meme Dodgin\n"
                 "!insult (user):\t Insult a user\n"
                 "!REEE:\t REEEEE\n"
                 "!drakes:\t How many drakes though?\n"
                 "!oom:\t oom\n"
                 "!fresh:\t fresh?\n"
                 "!duc: \tThe Troll Mage"]

commands_dict = {
    "!db/!item:":       "Search twinstar for a specific item or mob",
    "!raidtimes:":      "Display our raid times",
    "!loot:":           "Display our loot rules",
    "!raid:":           "Display time until next raid",
    "!flush:":          "Display time until next arena point flush",
    "!nerf:":           "Display time until Ulduar nerfs",
    "!docs:":           "Display loot spreadsheet",
    "!logs:":           "Display a link to our World of Logs",
    "\n------    Meme Commands":    "    ------",
    "!dodgin:":         "Meme Dodgin",
    "!insult (user):":  "Insult a user",
    "!REEE:":           "REEEEE",
    "!drakes:":         "How many drakes though?",
    "!oom:":            "oom",
    "!fresh:":          "Fresh?",
    "!duc:":            "The Troll Mage```",
}

ree = "FUCKING NORMIES\nREEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

emoji_list = [631560107871961128, 643813055540625408, 633520718780432414]

drakes = ["But how many drakes are we doing?", "Are we doing 2 or 3 drakes?"]

fresh_list = ["Did someone say F R E S H?", "Fresh?", "Did I hear FRESH?", "Fresh server?", "FRESHBOIS"]

duc_list = [
    "You're trolling",
    "Stop memeing",
    "Alright you just went full pepega that pull. It's alright",
    "Mjolnir is BIS on FDK",
    "Turn on your monitor",
]

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await client.change_presence(activity=discord.Game(name="Hello Kitty Island Adventure"))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!"):
            if message.content.casefold().startswith('!hello'):
                await message.channel.send('Hello {0.author.mention}'.format(message))

            elif message.content.casefold().startswith("!db"):
                query = message.content.replace('!db', '')
                print(query)
                for i in search(site + " " + query, tld="co.in", num=1, stop=1, pause=2):
                    await message.channel.send(i)

            elif message.content.casefold().startswith("!item"):
                query = message.content.replace('!item', '')
                print(query)
                for i in search(site + " " + query, tld="co.in", num=1, stop=1, pause=2):
                    await message.channel.send(i)

            elif message.content.casefold().startswith("!dodgin"):
                random = randint(0, (len(dodgin_insults) - 1))
                insult = dodgin_insults[random]
                await message.channel.send(insult)

            elif message.content.casefold().startswith("!raidtimes"):
                await message.channel.send(raid_times)

            elif message.content.casefold().startswith("!loot"):
                await message.channel.send(loot_rules)

            elif message.content.casefold().startswith("!commands"):
                # for i in commands_list:
                #     await message.channel.send(i)
                msg = "```"
                for i in commands_dict:
                    margin = 18 - len(i)
                    msg = msg + (i + (" " * margin) + commands_dict.get(i) + "\n")
                await message.channel.send(msg)

            elif message.content.casefold().startswith("!insult"):
                user = ""
                members = client.get_all_members()
                query = message.content.replace('!insult ', '')
                for i in members:
                    if str(query).casefold() in str(i).casefold():
                        user = i
                        break
                try:
                    await message.channel.send("Fuck you " + user.mention)
                except AttributeError:
                    pass

            elif message.content.casefold().startswith("!reee"):
                emoji = client.get_emoji(645497006420131841)
                await message.channel.send(ree)
                await message.channel.send(emoji)

            elif message.content.casefold().startswith("!oom"):
                await message.channel.send("Dodgin needs an innervate!")

            elif message.content.casefold().startswith("!drakes"):
                if randint(0, 1) == 0:
                    await message.channel.send(drakes[randint(0, len(drakes) - 1)])
                else:
                    await message.channel.send("{} drakes?".format(randint(0,100)))

            elif message.content.casefold().startswith("!fresh"):
                await message.channel.send(fresh_list[randint(0, len(fresh_list)-1)])

            elif message.content.casefold().startswith("!log"):
                await message.channel.send("http://www.worldoflogs.com/guilds/351589/")

            elif message.content.casefold().startswith("!docs"):
                await message.channel.send("https://docs.google.com/spreadsheets/d/1ZqjFpP6gS1sTgu0rjR_eKvAKLu-gQhwMbLIetoFaxNA/edit#gid=421726345")

            elif message.content.casefold().startswith("!duc"):
                await message.channel.send(duc_list[randint(0, len(duc_list) - 1)])

            elif message.content.casefold().startswith("!nerf"):
                now = datetime.datetime.today()
                nerfs = datetime.datetime(year=now.year, month=5, day=30)
                nerftime = relativedelta(nerfs, now)
                await message.channel.send("Time until Ulduar nerfs: {} month, {} days, {} hours, {} minutes".format(nerftime.months, nerftime.days, nerftime.hours, nerftime.minutes))

            elif message.content.casefold().startswith("!audiotest"):
                await message.channel.send(file=file)

            elif message.content.casefold().startswith("!asynctest"):
                MyClient.timer(self)


            elif message.content.casefold().startswith("!raid"):
                min_diff = None
                day_diff = None
                now = datetime.datetime.today()
                today_weekday = now.weekday()
                print(today_weekday)
                try:
                    if today_weekday == 0:      # monday
                        day_diff = now.day + 3
                        min_diff = 30
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, minute=min_diff, second=0, microsecond=0)
                    elif today_weekday == 1:    # tuesday
                        day_diff = now.day + 2
                        min_diff = 30
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, minute=min_diff, second=0, microsecond=0)
                    elif today_weekday == 2:    # wednesday
                        day_diff = now.day + 1
                        min_diff = 30
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, minute=min_diff, second=0, microsecond=0)
                    elif today_weekday == 3:    # thursday
                        day_diff = now.day
                        min_diff = 30
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, minute=min_diff, second=0, microsecond=0)
                    elif today_weekday == 4:    # friday
                        day_diff = now.day + 2
                        min_diff = 0
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, second=0, microsecond=0)
                    elif today_weekday == 5:    # saturday
                        day_diff = now.day + 1
                        min_diff = 0
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, second=0, microsecond=0)
                    elif today_weekday == 6:    # sunday
                        day_diff = now.day
                        min_diff = 0
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=23, second=0, microsecond=0)
                except ValueError:
                    # january, march, may, july, august, october, december
                    if now.month == 12 or now.month == 2 or now.month == 4 or now.month == 6 or now.month == 7 or now.month == 9 or now.month == 11:
                        new_day = day_diff - 30
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=23, minute=min_diff, second=0, microsecond=0)

                    # april, june, september, november
                    elif now.month == 3 or now.month == 6 or now.month == now.month == 8 or now.month == 10:
                        new_day = day_diff - 29
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=23, minute=min_diff, second=0, microsecond=0)

                    # february
                    elif now.month == 1:
                        new_day = day_diff - 27
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=23, minute=min_diff, second=0, microsecond=0)

                try:
                    next_raid_time = relativedelta(next_raid, now)
                    if next_raid_time.seconds > 30:
                        await message.channel.send("```Time until next raid: {} days, {} hours, {} minutes```".format(next_raid_time.days, next_raid_time.hours, next_raid_time.minutes+1))
                    else:
                        await message.channel.send("```Time until next raid: {} days, {} hours, {} minutes```".format(next_raid_time.days, next_raid_time.hours, next_raid_time.minutes))
                except:
                    await message.channel.send("```Error```")

            elif message.content.casefold().startswith("!flush"):
                now = datetime.datetime.today()
                today_weekday = now.weekday()
                print(today_weekday)
                try:
                    if today_weekday == 0:      # monday
                        day_diff = now.day + 6
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, minute=0, second=0, microsecond=0)
                    elif today_weekday == 1:    # tuesday
                        day_diff = now.day + 5
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, minute=0, second=0, microsecond=0)
                    elif today_weekday == 2:    # wednesday
                        day_diff = now.day + 4
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, minute=0, second=0, microsecond=0)
                    elif today_weekday == 3:    # thursday
                        day_diff = now.day + 3
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, minute=0, second=0, microsecond=0)
                    elif today_weekday == 4:    # friday
                        day_diff = now.day + 2
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, second=0, microsecond=0)
                    elif today_weekday == 5:    # saturday
                        day_diff = now.day + 1
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, second=0, microsecond=0)
                    elif today_weekday == 6:    # sunday
                        day_diff = now.day
                        next_raid = datetime.datetime(year=now.year, month=now.month, day=day_diff, hour=17, second=0, microsecond=0)
                except ValueError:
                    # january, march, may, july, august, october, december
                    if now.month == 12 or now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month == 11:
                        new_day = day_diff - 30
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=17, minute=0, second=0, microsecond=0)

                    # april, june, september, november
                    elif now.month == 3 or now.month == 5 or now.month == now.month == 8 or now.month == 10:
                        new_day = day_diff - 29
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=17, minute=0, second=0, microsecond=0)

                    # february
                    elif now.month == 1:
                        new_day = day_diff - 27
                        next_raid = datetime.datetime(year=now.year, month=now.month+1, day=new_day, hour=17, minute=0, second=0, microsecond=0)

                try:
                    next_raid_time = relativedelta(next_raid, now)
                    if next_raid_time.seconds > 30:
                        await message.channel.send("Time until arena points flush: {} days, {} hours, {} minutes".format(next_raid_time.days, next_raid_time.hours, next_raid_time.minutes+1))
                    else:
                        await message.channel.send("Time until arena points flush: {} days, {} hours, {} minutes".format(next_raid_time.days, next_raid_time.hours, next_raid_time.minutes))

                except:
                    await message.channel.send("Error")

                #####################
                # MUSIC BOT
                #####################

        if "dragonaut" in message.content.casefold():
            emoji = client.get_emoji(emoji_list[randint(0, len(emoji_list) - 1)])
            await message.add_reaction(emoji)

client = MyClient()
client.run('')