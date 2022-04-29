from discord.ext import commands
from discord import utils
import discord
import asyncio


class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_message(self, message):
    if message.author.bot:
        return

    if isinstance(message.channel, discord.DMChannel):
        guild = self.bot.get_guild(968367426150473798)
        categ = utils.get(guild.catergories, name = "Modmail tickets")
        if not categ:
            overwrites = {
                guild.default_role : discord.PermissionOverwrite(read_messages = False),
                guild.me : discord.PermissionOverwrite(read_message = True)
            }
            categ = await guild.create_catergory(name = "Modmail Tickets", overwrites = overwrites)
        
        channel = utils.get(categ.channels, topic str[messsage.author.id]) 
        if not channel:
            channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topic = str(message))
            await channel.send(f"New Ticket created by {message.author.mention}")

        embed = discord.Embed(description = message.content, colour = 0x696969)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await channel.send( embed = embed)

    elif isinstance(message.channel, discord.TextChannel):
        if message.content.startswith(self.bot.commands_prefix):
            pass
        else:
            topic = message.channel.topic
            if topic:
                member = message.guild.get_member(int(topic))
                if member:
                    embed = discord.Embed(description = message.content, colour = 0x696969)
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await member.send(embed = embed)
    @commands.command()
    async def close(self, ctx):
        if ctx.channel.catergory.name == "Modmail Tickets":
            await ctx.send("Deleting channel in 10 secs!")
            await asyncio.sleep(10)
            await channel.delete()

def setup(bot):
    bot.add_cog(onMessage(bot)) 