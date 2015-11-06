### Python OOP - Assignment #3 - Bike (Chaining)
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "-------------------------"
		print "Price of Bike:", self.price
		print "Max Speed of Bike:", self.max_speed
		if self.miles > 0:
			print "Total Miles Ridden:", self.miles
		else:
			print "Total Miles Ridden: 0"

		print "-------------------------"

		return self

	def ride(self):
		print "Riding"
		self.miles += 10

		return self

	def reverse(self):
		print "Reversing"
		self.miles -= 5

		return self


cannondale = Bike("$200", "25mph")

cannondale.displayInfo().ride().ride().ride().reverse()

cannondale.displayInfo()

specialized = Bike("$150", "20mph")

specialized.displayInfo().ride().ride().reverse().reverse()

specialized.displayInfo()

bianchi = Bike("$100", "15mph")

bianchi.displayInfo().reverse().reverse().reverse()

bianchi.displayInfo()



