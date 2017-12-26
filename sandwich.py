# -*- coding: utf-8 -*-

def bread(func):
	"""This is my decorator"""
	def wrapper():
		print "</''''''''''\>"
		func()
		print "<\__________/>"
	return wrapper

def cheese(func):
	"""This is my decorator"""
	def wrapper():
		print " [[[cheese]]]"
		func()
		print " [[[cheese]]]"
	return wrapper

def cotlet(func):
	"""This is my decorator"""
	def wrapper():
		print "  ==cotlet=="
		func()
		print "  ==cotlet=="
	return wrapper

def tomato(func):
	"""This is my decorator"""
	def wrapper():
		print "   _tomato_"
		func()
	return wrapper

def salad(func):
	"""This is my decorator"""
	def wrapper():
		func()
		print "  ~~~salad~~~"
	return wrapper

@bread
@cheese
@cotlet
@tomato
@salad
def sandwich():
	print "    --ham--"

	
sandwich()
