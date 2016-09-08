import discord
import ask_api

email = "myemail" # Replace myemail by the email for your bot account
password = "mypassword" # Replace mypassword by the passowrd for your bot account

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

	print("Nouveau message")
	content = message.content
	fin = len(content)
	debut = content.find("[") +1
	while debut > 0 :
		#ss1 = content[ouvert: fin]
		fin = content.find("]", debut)
		requete = content[debut: fin]
		print("Requete : "+requete)
		if len(requete) > 2 :
			msg_list = ask_api.ask_card(requete)
			for msg in msg_list :
				await client.send_message(message.channel, msg)
		debut = content.find("[", fin) +1
		
client.run(email, password)
