import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Help
    @commands.command(name='help')
    async def help(self, ctx, category=None):
        if category is None:
            help_embed = discord.Embed(title='MyBot Help')
            help_embed.set_thumbnail(url=self.client.user.avatar_url)
            val='''
    **1.** `GENERAL`
    **2.** `MODERATION`
    **3.** `MINIGAMES`
    **4.** `FUN`
    **5.** `DETAILS`
            '''
            help_embed.add_field(name='Categories', value=val)
            help_embed.set_footer(text='Type ?help <category / category_number> to know more!')
            await ctx.send(embed=help_embed)

        else:
            if category.lower()=='general' or category=='1':
                help_embed = discord.Embed(title='MyBot Help - General')
                help_embed.set_thumbnail(url=self.client.user.avatar_url)

                desc='''
**Command:** `?ping`
**Aliases:** `?ping` `?latency`
**Description:** Allows you to see the latency of the bot.

**Command:** `?dm <member> <message>`
**Aliases:** None
**Description:** Allows you to dm a member of the server.

**Command:** `?avatar <member>`
**Aliases:** `?av` `?pfp`
**Description:** Allows you to see the profile pic of a server member/bot.

**Command:** `?lmgify <search_text>`
**Aliases:** `?googlesearch` `?gs`
**Description:** Allows you to search something in Google.
                '''
                help_embed.description=desc
                help_embed.set_footer(text='Can be used by all members.')
                await ctx.send(embed=help_embed)

            elif category.lower()=='moderation' or category=='2':
                help_embed = discord.Embed(title='MyBot Help - Moderation')
                help_embed.set_thumbnail(url=self.client.user.avatar_url)

                desc='''
**__Channel Moderation__**
**Command:** `?create-category <category>`
**Aliases:** `?cc`
**Description:** Allows you to create a new category.

**Command:** `?delete-category <category>`
**Aliases:** `?dc`
**Description:** Allows you to delete a category.

**Command:** `?create-text-channel <channel> <category>`
**Aliases:** `?ctc`
**Description:** Allows you to create a new text channel within the given category.

**Command:** `?delete-text-channel <channel>`
**Aliases:** `?dtc`
**Description:** Allows you to delete a text channel.

**Command:** `?clear <amount> <channel>`
**Aliases:** `?clrchat`
**Description:** Allows you to purge upto a maximum of 100 messages from the given channel.


**__Member Moderation__**
**Command:** `?ban <member>`
**Aliases:** None
**Description:** Allows you to ban a member.

**Command:** `?unban <member>`
**Aliases:** None
**Description:** Allows you to unban a member.

**Command:** `?kick <member>`
**Aliases:** None
**Description:** Allows you to kick a member.

**Command:** `?nickname <member> <nickname>`
**Aliases:** `?setnick` `?nick`
**Description:** Allows you to set a nickname to a member.


**__Role Moderation__**
**Command:** `?new-role <role>`
**Aliases:** None
**Description:** Allows you to create a new role.

**Command:** `?add-role <member> <role>`
**Aliases:** None
**Description:** Allows you to add a role to a member.

**Command:** `?delete-role <role>`
**Aliases:** `?delrole`
**Description:** Allows you to delete a role.

**Command:** `?remove-role <member> <role>`
**Aliases:** `?remrole`
**Description:** Allows you to remove a role from a member.
                '''
                help_embed.description=desc
                help_embed.set_footer(text='Requires ADMINISTRATOR permission.')
                await ctx.send(embed=help_embed)

            elif category.lower()=='minigames' or category=='3':
                help_embed = discord.Embed(title='MyBot Help - Minigames')
                help_embed.set_thumbnail(url=self.client.user.avatar_url)

                desc='''
**Command:** `?meme`
**Aliases:** None
**Description:** Shows a meme.

**Command:** `?8ball`
**Aliases:** `?chance` `?8b`
**Description:** Check the possibility of something.

**Command:** `?truthordare <truth | t | dare | d>`
**Aliases:** `?tord`
**Description:** Play Truth or Dare.

**Command:** `?guessthenum`
**Aliases:** `?guess` `?gtn`
**Description:** Guess the number (between 1-10).

**Command:** `?highlow`
**Aliases:** `?hl`
**Description:** Guess if the number is higher/lower than the key.
                '''
                help_embed.description=desc
                help_embed.set_footer(text='Can be used by all members.')
                await ctx.send(embed=help_embed)

            elif category.lower()=='details' or category=='5':
                help_embed = discord.Embed(title='MyBot Help - Minigames')
                help_embed.set_thumbnail(url=self.client.user.avatar_url)

                desc='''
**Command:** `?invite`
**Aliases:** `?inv`
**Description:** Sends you the bot's invite link.

**Command:** `?version`
**Aliases:** `?ver`
**Description:** Displays the bot version.

**Command:** `?updates`
**Aliases:** None
**Description:** Tells you the recent updates of the bot.
                '''
                help_embed.description=desc
                help_embed.set_footer(text='Can be used by all members.')
                await ctx.send(embed=help_embed)

def setup(client):
    client.add_cog(Help(client))
