import discord
from discord.ext import commands

class Details(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command('invite',aliases=['inv'])
    async def invite_bot(self, ctx):
        invite_embed=discord.Embed()
        invite_embed.description = '''
        [Click here](https://discord.com/oauth2/authorize?client_id=861798750459527198&permissions=8&scope=bot) to invite me to your server.
        '''
        await ctx.send(embed=invite_embed)

    @commands.command(name='version', aliases=['ver'])
    async def version(self, ctx):
        await ctx.send('`VERSION:` `v3`')

    @commands.command(name='updates')
    async def updates(self, ctx):
        update_embed = discord.Embed(title="MyBot Updates")
        update_embed.set_thumbnail(url=self.client.user.avatar_url)
        version_updates = '''
**v1**
`Bot initial release.`

**v2**
`Custom help command. Respond to users when mentioned.`

**v3**
`Category FUN (and its commands) added.`
        '''
        update_embed.description=version_updates

        await ctx.send(embed=update_embed)

def setup(client):
    client.add_cog(Details(client))
