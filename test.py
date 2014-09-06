from spellbee.spellbee import spellbee

if __name__ == '__main__':
	string = 'Autimattic learning procejures can make use of stastical inference algorithmas to producse modals that are robost to unfamilear input'
	print string
	suggestions = spellbee._correct(string)
	for x in suggestions:
		print x