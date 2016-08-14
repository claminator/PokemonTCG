import random

def dmg_calc():
	pass

def flip(H='', T='', n=1, until_tails=False):
	if until_tails:
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