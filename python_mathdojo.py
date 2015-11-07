#Python - MathDojo

class MathDojo(object):
	def __init__(self):
		self.total = 0

	def add(self, *vals):
		for i in vals:
			if type(i) is list or type(i) is tuple:
				for j in i:
					self.total += j
			else:
				self.total += i
		return self

	def subtract(self, *vals):
		total = 0
		for i in vals:
			if type(i) is list or type(i) is tuple:
				for j in i:
					self.total -= j
			else:
				self.total -= i
		return self

	def result(self):
		print self.total


md = MathDojo()

# md.add(2).add(2, 5).subtract(3, 2).result()
md.add([1],3,(2,1,1)).add([3,5,7,8], [2, 4.3, 1.25]).subtract(2,[2,3],[1.1,2.3]).result()

# def add(val, *more_val):
# 	print len(more_val)
# 	# newList = list(more_val)
# 	print "Got ", val, " and ", more_val

# 	newNum = val
# 	for i in range(0,len(more_val)):
# 		newNum += more_val[i]

# 	print newNum

# md = add(2,3,4,5,6)
