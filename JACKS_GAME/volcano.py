import textwrap
import colorama
from colorama import Fore, Back, Style
from sys import exit
from random import randint

class volcano(object):

	def __init__(self, name):
		self.name = name

	def atEdge(self):
		volc = "volcano"
		volc_f = (Fore.RED + volc + Fore.RESET)	

		print "You are now looking out over a tremendous fiery " + volc_f
		print ""
		#print "\t [1] Investigte the mess on the floor"
		#print "\t [2] Open the storage chest"
		#print "\t [3] Exit"
		#print ""
	#
	#	#jump_Off = raw_input("\t > ")
	#
	#	#if jump_Off == "1":
	#	#	print ""
	#	#	self.theMess()
	#
	#	#if jump_Off == "2":
	#	#	print ""
		#	self.storageUnit()