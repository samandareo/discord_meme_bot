import discord
import credentials as cred
import connection as conn

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "$info":
            await message.reply("Hello! I am a bot that can send you random memes. You can use the following commands:\n$random_meme - sends a random meme\n$programming_meme - sends a programming meme", mention_author=True)
            await message
        if message.content == '$random_meme':
            meme = await conn.get_meme()
            await message.reply(meme, mention_author=True)

        if message.content == '$programming_meme':
            meme = await conn.get_new_meme()
            await message.reply(meme, mention_author=True)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(cred.SECRET_TOKEN)