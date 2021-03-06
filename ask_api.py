from mtgsdk import Card


def ask_card(cardname):
    cards = Card.where(name=cardname).all()
    l = []
    n = []
    i = 0
    for card in cards:
        if i == 20:
            break
        if card.name not in n:
            msg = "**" + card.name + "**" + " "
            if card.mana_cost is not None:
                msg += card.mana_cost
                #  if card.set_name=='Unhinged' or card.set_name=='Unglued' :
                msg += " - *"
                last_set = card.printings[-1]
                for set in card.printings:
                    msg += set
                    if set == last_set:
                        msg += "*"
                    else:
                        msg += ", "
            msg += "\n"
            if card.type is not None:
                msg += card.type
            if "Creature" in card.types:
                msg += " " + card.power + "/" + card.toughness
            elif "Planeswalker" in card.types:
                msg += ". Starting Loyalty " + str(card.loyalty)
            if card.text is not None:
                msg += "\n" + card.text
            msg += "\n"
            if cardname.lower() == card.name.lower():
                l = [msg]
                break
            else:
                l.append(msg)
                i += 1
                n.append(card.name)
    return l
