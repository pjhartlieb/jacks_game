import textwrap
import colorama
from colorama import Fore, Back, Style
from sys import exit
from random import randint

class fortress(object):

	def __init__(self, name):
		self.name = name

	def theMess(self):
		add = "3 + 5 + 2 = ?"
		add_f = (Fore.BLUE + add + Fore.RESET)
		goblin = "goblin"
		goblin_f = (Fore.RED + goblin + Fore.RESET)
		shout = "shouts"
		shout_f = (Fore.RED + shout + Fore.RESET)
		points = "10"
		points_f = (Fore.GREEN + "+" + points + " points!" + Fore.RESET)
		messTxt = '''
		You find yourself staring at 3 piles of well worn books on the floor ... one pile has 3 .. 
		the next has 5 ... and the last has 2 ... a small worker ''' + goblin_f + ''' to your left 
		is reshelving books ... he ''' + shout_f + ''' at you and asked how many books are there? \n'''
		dedented_mess_text = textwrap.dedent(messTxt).strip()
		ansTxt = ''' Correct! ''' + points_f + ''' ... the ''' + goblin_f + ''' mumbles something and wanders off in the dark \n'''
		dedented_ans_text = textwrap.dedent(ansTxt).strip()

		print dedented_mess_text + "\n"
		print "\t" + add_f + "\n"

		theMess_answer = raw_input("\t > ")
		print ""

		if theMess_answer == "10":
			print dedented_ans_text + "\n"

		else:
			self.theMess()

	def atThedoor(self):
		libp = "library"
		libq = (Fore.BLUE + libp)	

		libr = "... the next step is to:"
		libs = (Fore.WHITE + libr)	

		print "You are in the fortress " + libq + libs
		print (Fore.RESET)
		print ""
		print "\t [1] Investigte the mess on the floor"
		print "\t [2] Remove a book from the top shelf"
		print "\t [3] Exit"
		print ""

		jump_Off = raw_input("\t > ")

		if jump_Off == "1":
			print ""
			self.theMess()

		#elif jump_Off == "2":
		#	print ""
		#	#falls("firstMove")
		#	falls("firstMove").footOffalls()

		#elif jump_Off == "3":
		#	print ""
		#	#church("firstMove")
		#	church("firstMove").inThenarthex()

		#else:
		#	new_game.selectStart()


