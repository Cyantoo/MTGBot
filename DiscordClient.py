import discord
import ask_api


email = "myemail"  # Replace myemail by the email for your bot account
password = "mypassword"  # Replace mypassword by the password for your bot account

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print("New message")
    content = message.content
    end = len(content)
    start = content.find("[") + 1
    while start > 0:
        # ss1 = content[start: end]
        end = content.find("]", start)
        request = content[start: end]
        print("Request : " + request)
        if len(request) > 2:
            msg_list = ask_api.ask_card(request)
            for msg in msg_list:
                await client.send_message(message.channel, msg)
        start = content.find("[", end) + 1


client.run(email, password)
