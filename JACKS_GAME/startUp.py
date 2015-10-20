import colorama
from colorama import Fore, Back, Style
from sys import exit
from random import randint

from fortress import fortress
from falls import falls
from church import church

class startingPoint(object):

	def __init__(self, name):
		self.name = name

	def selectStart(self):
		text = "Where would you like to start your quest?"
		print ""
		print (Fore.GREEN + text + Fore.RESET)
		print "\t [1] Jack's Impenetrable Fortress"
		print "\t [2] Spinacullum Falls"
		print "\t [3] The Church\n"

		jump_Off = raw_input("\t > ")

		if jump_Off == "1":
			print ""
			#fortress("firstMove")
			fortress("firstMove").atThedoor()

		elif jump_Off == "2":
			print ""
			#falls("firstMove")
			falls("firstMove").footOffalls()

		elif jump_Off == "3":
			print ""
			#church("firstMove")
			church("firstMove").inThenarthex()

		else:
			new_game.selectStart()

new_game = startingPoint("game_1")
new_game.selectStart()

