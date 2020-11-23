import discord # pip install discord.py
import config

client = discord.Client()
num = "idk"

@client.event
async def on_ready():
    global num
    print('logged in as {0.user}'.format(client))
    num = open("data.txt", mode="r")
    num = int(num.read())

@client.event
async def on_message(message):
    global num
    if message.author == client.user:
        return
    else:
        channel = message.channel.name
        if channel == "counting":
            if message.author.guild_permissions.manage_messages and message.content.startswith("!purge"):
                update = open("data.txt", mode="w")
                update.write(str(1))
                update.close()
                num = open("data.txt", mode="r")
                num = int(num.read())
                await message.channel.send("purged the internal number list. please remove all channel messages!")
            elif " " + str(num) + " " in message.content.lower() or message.content.startswith(str(num)) or message.content.endswith(str(num)):
                num = num + 1
                update = open("data.txt", mode="w")
                update.write(str(num))
                update.close()
            else:
                try:
                    await message.delete()
                except(discord.errors.Forbidden):
                    await message.channel.send("Can not remove messages - check permissions")

client.run(config.token)