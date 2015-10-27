import textwrap
import colorama
from colorama import Fore, Back, Style
from sys import exit
from random import randint
from volcano import volcano

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

	def storageUnit(self):
		storage = "storage"
		storage_f = (Fore.GREEN + storage + Fore.RESET)
		locks = "locks"
		locks_f = (Fore.RED + locks + Fore.RESET)
		unlock = "unlock"
		unlock_f = (Fore.BLUE + unlock + Fore.RESET)
		chest = "chest"
		chest_f = (Fore.GREEN + chest + Fore.RESET)
		points = "40"
		points_f = (Fore.GREEN + "+" + points + " points!" + Fore.RESET)
		shelfTxt = '''
		The ''' + storage_f + ''' chest has 4 ''' + locks_f + '''.  Solve each math problem to ''' + unlock_f + ''' and open the ''' + chest_f + '''.\n'''
		dedented_shelf_text = textwrap.dedent(shelfTxt).strip()
		ansTxt = points_f
		dedented_ans_text = textwrap.dedent(ansTxt).strip()

		print dedented_shelf_text + "\n"

		#while statements for each lock
		
		ans_1="0"

		while (ans_1 != "34"):
			print "\t [*] lock 1"
			print "\t 15 + 10 + 9 = "

			lock_1 = raw_input("\t > ")
			print ""

			if lock_1 == "34":
				print "\t correct!"
				unlock = "unlocked"
				unlock_f = (Fore.BLUE + unlock + Fore.RESET)
				print "\t lock 1 " + unlock_f + " !\n"

				ans_1 = "34"
			else:
				ans_1="0"

		ans_2="0"

		while (ans_2 != "52"):
			print "\t [*][*] lock 2"
			print "\t 20 + 20 + 12 = "

			lock_2 = raw_input("\t > ")
			print ""

			if lock_2 == "52":
				print "\t correct!"
				unlock = "unlocked"
				unlock_f = (Fore.BLUE + unlock + Fore.RESET)
				print "\t lock 2 " + unlock_f + " !\n"

				ans_2 = "52"
			else:
				ans_2="0"	

		ans_3="0"

		while (ans_3 != "27"):
			print "\t [*][*][*] lock 3"
			print "\t 3 + 10 + 14 = "

			lock_3 = raw_input("\t > ")
			print ""

			if lock_3 == "27":
				print "\t correct!"
				unlock = "unlocked"
				unlock_f = (Fore.BLUE + unlock + Fore.RESET)
				print "\t lock 3 " + unlock_f + " !\n"

				ans_3 = "27"
			else:
				ans_3="0"	

		ans_4="0"

		while (ans_4 != "68"):
			print "\t [*][*][*][*] lock 4"
			print "\t 20 + 25 + 23 = "

			lock_4 = raw_input("\t > ")
			print ""

			if lock_4 == "68":
				print "\t correct!"
				unlock = "unlocked"
				unlock_f = (Fore.BLUE + unlock + Fore.RESET)
				print "\t lock 4 " + unlock_f + " !\n"

				ans_4 = "68"
			else:
				ans_4="0"	

		print "\t" + dedented_ans_text + "\n"
		tele = "teleported!"
		tele_f = (Fore.MAGENTA + tele + Fore.RESET)
		print "The chest opens to reveal a portal ... you are immediately " + tele_f + "\n"
		volcano("teleport").atEdge()


	def atThedoor(self):
		libp = "library"
		libq = (Fore.BLUE + libp + Fore.RESET)	

		print "You are in the fortress " + libq + " ... the next step is to:"
		print (Fore.RESET)
		print ""
		print "\t [1] Investigte the mess on the floor"
		print "\t [2] Open the storage chest"
		print "\t [3] Exit"
		print ""

		jump_Off = raw_input("\t > ")

		if jump_Off == "1":
			print ""
			self.theMess()

		if jump_Off == "2":
			print ""
			self.storageUnit()

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


