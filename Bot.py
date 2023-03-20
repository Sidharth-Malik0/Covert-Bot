import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command()
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

bot.run('MTA2NTIyNzE2NjE5Mjc3OTI5NA.GXr4F0.wLdpRB2MIbNqVZ0zHqk43lgAHV5-pU12mqjM4c')
