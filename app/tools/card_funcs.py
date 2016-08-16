import random
import game_classes as gc

def start_game(deck1, deck2):
	'''
	Initialize decks, draw until no mulligans, and place prizes
	'''
	p1_deck = gc.Deck(deck1)
	p2_deck = gc.Deck(deck2)

	p1_hand = gc.Hand()
	p2_hand = gc.Hand()

	p1_hand.draw_hand(p1_deck)
	p2_hand.draw_hand(p2_deck)

	return p1_deck, p2_deck, p1_hand, p2_hand


def dmg_calc():
	pass

def flip(H='', T='', n=1, until_tails=False):
	if until_tails:
		if n != 1:
			for i in range(n):
				result = random.uniform(0,1)
				if result > 0.5:
					exec(H)
				else:
					exec(T)
					return
		else:
			result = random.uniform(0,1)
			while result > 0.5:
				exec(H)
				result = random.uniform(0,1)
			exec(T)

	else:
		for i in range(n):
			result = random.uniform(0,1)
			if result > 0.5:
				exec(H)
			else:
				exec(T)