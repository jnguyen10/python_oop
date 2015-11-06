### Python OOP - Assignment #1 - Bike
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "Price of Bike:", self.price
		print "Max Speed of Bike:", self.max_speed
		if self.miles > 0:
			print "Total Miles Ridden:", self.miles
		else:
			print "Total Miles Ridden: 0"

	def ride(self):
		print "Riding"
		self.miles += 10

	def reverse(self):
		print "Reversing"
		self.miles -= 5


cannondale = Bike("$200", "25mph")

cannondale.displayInfo()

cannondale.ride()
cannondale.ride()
cannondale.ride()
cannondale.reverse()

cannondale.displayInfo()

specialized = Bike("$150", "20mph")

specialized.displayInfo()

specialized.ride()
specialized.ride()
specialized.reverse()
specialized.reverse()

specialized.displayInfo()

bianchi = Bike("$100", "15mph")

bianchi.displayInfo()

bianchi.reverse()
bianchi.reverse()
bianchi.reverse()

bianchi.displayInfo()



