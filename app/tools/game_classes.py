import random
import json
import os

ROOT_DIR = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])

with open(os.path.join(ROOT_DIR, 'static', 'card_data.json')) as card_data:
	card_database = json.load(card_data)

with open(os.path.join(ROOT_DIR, 'static', 'decks.json')) as deck_data:
	deck_database = json.load(deck_data)

class Card(object):
	'''
	Base class for card objects
	Should only contain base properties 
	shared between all card types
	'''

	def __init__(self, card_params):
		self.name = card_params['name']
		self.card_type = card_params['card_type']
		self.card_subtype = card_params['card_subtype']
		self.turns_in_play = 0

	def __str__(self):
		return "{0}".format(self.name)
		

class Trainer(Card):
	'''
	The card_params should be a dictionary of 
	card specifications
	'''
	def __init__(self, card_params):
		self.effect = card_params['effect']
		super(self.__class__, self).__init__(card_params)


class Energy(Card):
	'''
	The card_params should be a dictionary of 
	card specifications
	'''
	def __init__(self, card_params):
		super(self.__class__, self).__init__(card_params)


class Pokemon(Card):
	'''
	The card_params should be a dictionary of 
	card specifications
	'''
	def __init__(self, card_params):
		self.hp = card_params['hp']
		if 'atk_1' in card_params:
			self.atk_1 = card_params['atk_1']
		if 'atk_2' in card_params:
			self.atk_2 = card_params['atk_2']
		if 'atk_3' in card_params:
			self.atk_3 = card_params['atk_3']
		self.poke_status = None
		self.type = card_params['type']
		self.weakness = card_params['weakness']
		self.resistance = card_params['resistance']
		self.retreat_cost = card_params['retreat_cost']
		super(self.__class__, self).__init__(card_params)


class Deck(object):
	'''
	Reads in a list of 60 cards and instantiates a deck
	'''
	def __init__(self, deck_list):
		if len(deck_list) != 60:
			raise ValueError('Your deck must be exactly 60 cards!')
		self.cards = []
		for card_name in deck_list:
			if card_database[card_name]['card_type'] == 'Pokemon':
				card = Pokemon(card_database[card_name])
			elif card_database[card_name]['card_type'] == 'Trainer':
				card = Trainer(card_database[card_name])
			elif card_database[card_name]['card_type'] == 'Energy':
				card = Energy(card_database[card_name])
			else:
				raise ValueError('{0} is not a valid card type'.format(card_database[card_name]['card_type']))
			self.cards.append(card)
			self.shuffle()

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def shuffle(self):
		random.shuffle(self.cards)

	def add_card(self, card):
		self.cards.append(card)

	def pop_card(self, i=-1):
		"""Removes and returns a card from the deck.

		i: index of the card to pop; by default, pops the last card.
		"""
		return self.cards.pop(i)

	def move_cards(self, dest, num):
		"""Moves the given number of cards from the deck into the Hand.

		hand: destination Hand object
		num: integer number of cards to move
		"""
		for i in range(num):
			dest.add_card(self.pop_card())


class Hand(Deck):
	
	def __init__(self):
		self.cards = []

	def mulligan(self, dest):
		self.subtypes = [card.card_subtype for card in self.cards]
		while not('Basic' in self.subtypes):
			self.move_cards(dest, len(self.cards))
			dest.shuffle()
			dest.move_cards(self, 7)
			self.subtypes = [card.card_subtype for card in self.cards]

	def draw_hand(self, dest):
		dest.move_cards(self,7)
		self.mulligan(dest)