import colorama
from colorama import Fore, Back, Style
from sys import exit
from random import randint

class church(object):

	def __init__(self, name):
		self.name = name

	def inThenarthex(self):
		print "You are in the church narthex ... \n"
