from mtgsdk import Card
import json

def ask_card (cardname) :
	cards = Card.where(name = cardname).all()
	l = []
	n = []
	i=0
	for card in cards :
		if i==20:
			break
		if card.name not in n:
			types = card.types
			msg = "**"+card.name+"**"+" "
			if card.mana_cost is not None :
				msg += card.mana_cost
			msg += "\n"
			if card.type is not None :
				msg += card.type
			if "Creature" in card.types :
				msg += " "+card.power + "/" + card.toughness
			if "Planeswalker" in card.types :
				msg+= ". Starting Loyalty "+str(card.loyalty)
			if card.text is not None :
				msg +="\n" + card.text
			msg +="\n"
			if cardname.lower() == card.name.lower():
				l = [msg]
				break
			else:
				l.append(msg)
				i++
				n.append(card.name)
	return l
	
	# Renvoie un json
