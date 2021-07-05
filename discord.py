import discord

client = BOT()

class BOT(discord.Client):
    async def on_ready(self):
        print("login")
        
    async def on_message(self, message):
        if "" in message.content:
            with open("log.txt", "a") as w:
                w.write("[NAME]:" + message.author.name + " [MESSAGE]:" + message.content + "\n")
            print("[NAME]:" + message.author.name + " [MESSAGE]:" + message.content)
            
client.run('ODYxNTQ5ODA1NzkyOTE5NTUy.YOLayA.R86xVf1OqyjArUmfsTR7jxbLMq0')
