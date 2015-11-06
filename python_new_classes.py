### New Inherited Classes
from python_oop_test import Human
class Wizard(Human):
	def __init__(self):
		super(Wizard, self).__init__()
		self.intellegence = 10
	def heal(self):
		self.health += 10

class Ninja(Human):
	def __init__(self):
		super(Ninja, self).__init__()
		self.stealth = 10
	def steal(self):
		self.stealth += 5

class Samurai(Human):
	def __init__(self):
		super(Samurai, self).__init__()
		self.strength = 10
	def sacrifice(self):
		self.health -= 5

harry = Wizard()
rain = Ninja()
tom = Samurai()

print harry.health
print rain.health
print tom.health

harry.heal()
print "Harry's Health:", harry.health

rain.steal()
print "Rain's Stealth:", rain.stealth

tom.sacrifice()
print "Tom's Health:", tom.health
print "Tom's Stealth:", tom.stealth
