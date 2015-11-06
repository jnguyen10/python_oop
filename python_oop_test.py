### Python OOP Test Page
import urllib
import arithmetic
import random


### CLASSES AND OBJECTS
class Human(object):
	def __init__(self, clan=None):
		print "New Human!"

		self.clan = clan
		#fixed attributes
		self.health = 100
		self.strength = 3
		self.intelligence = 3
		self.stealth = 3

	def taunt(self):
		print "You want a piece of me?"

	def attack(self, numAtk):
		self.taunt()

		while numAtk > 0:
			luck = round(random.random() * 100)
			if(luck > 50):
				if(luck * self.stealth > 150):
					print 'attacking!'
					# return True
				else:
					print 'attack failed'
					# return False
			else:
				self.health -= self.strength
				print "attack failed"
				# return False
				
			print self.health

			numAtk -= 1

class Cat(object):
	def __init__(self, color, type, age):
		self.color = color
		self.type = type
		self.age = age


# michael = Human('Ninja')
# jimmy = Human('Turtle')

# jimmy.attack(10)



# print michael.clan
# print michael.health
# print jimmy.clan
# print jimmy.health


# garfield = Cat('orange', 'fat', 5)
# print "Garfield's Color:", garfield.color
# print "Garfield's Type:", garfield.type
# print "Garfield's Age:", garfield.age