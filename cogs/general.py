import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Ping
    @commands.command(name='ping',aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f"{round(self.client.latency*1000)}ms")

    #DM
    @commands.command(name='dm')
    async def dm(self, ctx, user: discord.Member = None, *, message=None):
        if user is None:
            await ctx.send('Provide a valid username.')
        else:
            if message is None:
                await ctx.send('What is the messge you are sending?')
            else:
                myembed = discord.Embed()
                myembed.add_field(name=f'{ctx.author} sent you: ', value=message)
                myembed.set_footer(text='If this text is inappropriate, please contact server admin.')
                await user.send(embed=myembed)
                await ctx.send('Message sent successfully!')

    #Avatar
    @commands.command(name='avatar',aliases=['av','pfp'])
    async def avatar(self, ctx, user: discord.User = None):
        if user is None:
            user=ctx.message.author
        img=user.avatar_url
        await ctx.send(img)

    #LetMeGoogleItForYou
    @commands.command(name='lmgify',aliases=['googlesearch','gs'])
    async def googlesearch(self, ctx, *, x: str = None):
        s=''
        for i in x:
            if i == ' ':
                s+='+'
            else:
                s+=i
        link=f'https://www.google.com/search?q={s}'
        await ctx.send(link)

def setup(client):
    client.add_cog(General(client))
