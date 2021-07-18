import discord
from discord.ext import commands

class ChannelModeration(commands.Cog):
    def __init__(self, client):
        self.client = client

    #CreateNewCategory
    @commands.command(name='create-category',aliases=['cc'])
    @commands.has_permissions(administrator=True)
    async def create_category(self, ctx, *, category_name):
        guild = ctx.message.guild
        await guild.create_category(category_name)
        await ctx.send('Category created successfully!')

    #DeleteExistingCategory
    @commands.command(name='delete-category',aliases=['dc'])
    @commands.has_permissions(administrator=True)
    async def delete_category(self, ctx, *, category_name):
        guild=ctx.message.guild
        cat=discord.utils.get(guild.categories, name=category_name)
        await cat.delete()
        await ctx.send('Category deleted successfully!')

    #CreateNewTextChannel
    @commands.command(name='create-text-channel',aliases=['ctc'])
    @commands.has_permissions(administrator=True)
    async def create_text_channel(self, ctx, channel_name = None, *, category_name = None):
        guild = ctx.message.guild
        if channel_name is None:
            await ctx.send('What is the name of the channel?')
        else:
            if category_name is None:
                await guild.create_text_channel(channel_name)
                await ctx.send('Channel created successfully!')
            else:
                cat = discord.utils.get(ctx.guild.categories, name=str(category_name))
                await guild.create_text_channel(channel_name, category=cat)
                await ctx.send('Channel created successfully!')

    #DeleteExistingTextChannel
    @commands.command(name='delete-text-channel',aliases=['dtc'])
    @commands.has_permissions(administrator=True)
    async def delete_text_channel(self, ctx, channel_name = None):
        if channel_name is None:
            await ctx.send('What is the name of the channel?')
        else:
            guild = ctx.guild
            existing_channel = discord.utils.get(guild.channels, name= channel_name)
            try:
                await existing_channel.delete()
                await ctx.send('Channel deleted successfully!')
            except:
                await ctx.send('Channel not found!')

    #DeleteMessagesInChat
    @commands.command(name='clear',aliases=['clrchat'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100, channel_name=None):
        if channel_name is None:
            if amount>=100 or amount<0:
                await ctx.channel.purge(limit=100)
            else:
                await ctx.channel.purge(limit=amount)
        else:
            existing_channel = discord.utils.get(ctx.guild.channels, name= channel_name)
            try:
                if amount>=100 or amount<0:
                    await existing_channel.purge(limit=100)
                else:
                    await existing_channel.purge(limit=amount)
            except:
                await ctx.send('Channel not found!')

class MemberModeration(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Ban
    @commands.command(name='ban')
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.User=None, reason =None):
        if member is None or member == ctx.message.author:
            await ctx.channel.send('You cannot ban yourself!')
            return
        if reason is None:
            reason = 'For being a jerk!'
        await member.ban(reason=reason)

    #Unban
    @commands.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member = None):
        if member is None:
            await ctx.send("Who do you want to unban?")
        else:
            banned_users = await ctx.guild.bans()
            member_name,member_discriminator = member.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await member.send(f'You have been unbanned from {ctx.guild.name}!')

    #Kick
    @commands.command(name='kick')
    @commands.has_permissions(administrator=True)
    async def kickuser(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send('Mention the user to kick.')
        else:
            await ctx.guild.kick(user)

    #Nickname
    @commands.command(name='nick',aliases=['setnick','nickname'])
    @commands.has_permissions(administrator=True)
    async def nickname(self, ctx, member: discord.Member = None, nickname = 'Nickname'):
        if member is None:
            member = ctx.message.author
        await member.edit(nick=nickname)

class RoleModeration(commands.Cog):
    def __init__(self, client):
        self.client = client

    #CreateNewRole
    @commands.command(name='new-role')
    @commands.has_permissions(administrator=True)
    async def new_role(self, ctx, rolename = None):
        guild=ctx.guild
        if rolename is None:
            await ctx.send('Provide a valid name.')
        else:
            await guild.create_role(name=rolename, colour=discord.Colour(0x000000))
            await ctx.send('Role created successfully!')

    #AddRoleToAMember
    @commands.command(name='add-role')
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, user: discord.Member = None, role: discord.Role = None):
        if user is None:
            await ctx.send('Provide a valid username.')
        else:
            if role is None:
                await ctx.send('What is the role you want to add?')
            else:
                await user.add_roles(role)
                await ctx.send(f'{role.name} has been added to {user.name}')

    #DeleteExistingRole
    @commands.command(name='delete-role',aliases=['delrole'])
    @commands.has_permissions(administrator=True)
    async def del_role(self, ctx, rolename):
        if rolename is None:
            await ctx.send('Provide a valid rolename.')
        else:
            role = discord.utils.get(ctx.message.guild.roles, name=rolename)
            await role.delete()
            await ctx.send('Role deleted successfully!')

    #RemoveRoleFromUser
    @commands.command(name='remove-role',aliases=['remrole'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: discord.Member, role: discord.Role):
        await user.remove_roles(role)
        await ctx.send(f'{role.name} has been removed from {user.name}')

def setup(client):
    client.add_cog(ChannelModeration(client))
    client.add_cog(MemberModeration(client))
    client.add_cog(RoleModeration(client))
