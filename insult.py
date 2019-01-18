# insult.py
# generates a waaaacky insult!
# by gull! on 1/18/19

import random

def insult(insultee):
	you = {
		1: str(f'{insultee}, you are a'),
		2: str(f'{insultee}! Thou art a'),
		3: str(f'{insultee}! Knave, thyst mother is a'),
		4: str(f'{insultee}, you'),
		5: str(f'{insultee}, thou'),
		6: str(f'Damn you, {insultee}, you'),
		7: str(f'{insultee}, you truly are the shining example of a'),
		8: str(f'Here\'s a good description of you, {insultee},... a'),
		9: str(f'There\'s no need for formalities, {insultee}. We all know you\'re a'),
		10: str(f'{insultee}, your mom\'s a')
	}
	adjective = {
		1: "good-for-nothing",
		2: "scurrilous",
		3: "dimwitted",
		4: "filthy",
		5: "two-faced",
		6: "malformed",
		7: "dull-headed",
		8: "pea-brained",
		9: "thick-skulled",
		10: "foolish"
	}
	object = {
		1: "cur",
		2: "fool",
		3: "abomination",
		4: "halfwit",
		5: "dork",
		6: "ass",
		7: "bonehead",
		8: "weasel",
		9: "dunderhead",
		10: "pathetic excuse for a human being"
	}
	exclamation = {
		1: ".",
		2: "!"
	}
	print(you[random.randrange(1,10)], adjective[random.randrange(1,10)], object[random.randrange(1,10)] + exclamation[random.randrange(1,2)])
	
def main():
	try:
		name = input("Who do you wish to insult? ")
	except:
		name = " "
	insult(name)
	
main()
