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
			i+=1
			n.append(card.name)
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
			if cardname == card.name:
				l = [msg]
				break
			else:
				l.append(msg)
	return l
	
	# Renvoie un json
