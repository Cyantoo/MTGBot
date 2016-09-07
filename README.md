MTGBot
===

Discord Bot to fetch and display Magic : the Gathering cards.
---

### Installation instructions :

* Download Python 3 on https://www.python.org/downloads/ (On Windows, don't forget to check "Add Python to PATH")

The following instructions have to be executed in command line (On Windows, you can use an emulator such as Cmder (http://cmder.net/))

+ Download discord.py (https://github.com/Rapptz/discord.py) with :
pip install -U discord.py

+ Download mtgsdk for python (https://github.com/MagicTheGathering/mtg-sdk-python) with :
pip install mtgsdk

* Create a Discord account for your Bot and add him to your server and the right channels on the server

* Open DiscordClient.py with your favorite IDE/text editor and fill the fields email and password lines 4 and 5 (replace "myemail" and "mypassword" by the IDs of your bot, keep the quotes)
* Run DiscordClient.py and let it run in the background

### In Discord
Use [cardname] to get the card whose name is “cardname” (or the first 20 cards in alphabetical order whose names contain “cardname” if it does not exist)
