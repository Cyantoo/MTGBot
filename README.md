MTGBot
===

Discord Bot to fetch and display Magic : the Gathering cards.
---

If you're interested in this bot, you should probably first check out the Scryfall bot. It does mostly the same thing, better : https://scryfall.com/bots .

### Installation instructions :

1. Download Python 3 on https://www.python.org/downloads/ (On Windows, don't forget to check "Add Python to PATH")

2. The following instructions have to be executed in command line (On Windows, you can use an emulator such as Cmder (http://cmder.net/))

  * Download discord.py (https://github.com/Rapptz/discord.py) with :
```pip install -U discord.py```

  * Download mtgsdk for python (https://github.com/MagicTheGathering/mtg-sdk-python) with :
```pip install mtgsdk```

3. Create a Discord account for your Bot and add him to your server and the right channels on the server

4. Open DiscordClient.py with your favorite IDE/text editor and fill the fields email and password lines 4 and 5 (replace "myemail" and "mypassword" by the IDs of your bot, keep the quotes)
5. Run DiscordClient.py and let it run in the background

### In Discord
Use [cardname] to get the card whose name is “cardname” (or the first 20 cards in alphabetical order whose names contain “cardname” if it does not exist)
