### Python OOP - Assignment #4 - Animal

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Name of Animal:", self.name
		print "Health of Animal:", self.health
		return self

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "THIS IS A DRAGON!"
		super(Dragon, self).displayHealth();
		
		

		

animal = Animal("Cat")

animal.walk().walk().walk().run().run().displayHealth()

dog = Dog("Fido the Dog")

dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Boss Dragon")

dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

animal.pet()	## Not suppose to work
animal.fly()	## Not suppose to work
		