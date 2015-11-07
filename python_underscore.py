# Python - Underscore

class Underscore(object):
    def map(self, a_list, callback):
    	new_list = []
    	for i in a_list:
    		# append each new callback to a new array
    		new_list.append(callback(i))
        print "MAP:", new_list
    def reduce(self, a_list, callback):
        new_list = []
        total = 0
        for i in a_list:
        	# same as MAP
        	new_list.append(callback(i))
        for j in new_list:
        	# used to sum all the elements in the new list created
        	total += j
        print "REDUCE:", total

    def find(self, a_list, callback):
        for i in a_list:
        	# find the first true callback and print
        	# exit out of function when first true statement is found
        	if callback(i):
        		print "FIND:", i
        		return

    def filter(self, a_list, callback):
        new_list = []
        for i in a_list:
        	# append only callbacks that are true
        	if callback(i):
        		new_list.append(i)

        print "FILTER:", new_list

    def reject(self, a_list, callback):
        new_list = []
        for i in a_list:
        	# append only callbacks that are false
        	if callback(i) == False:
        		new_list.append(i)

        print "REJECT:", new_list





# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

plus_two = _.map([1, 2, 3, 4, 5, 6], lambda x: x + 2)
down_to_one = _.reduce([1, 2, 3, 4, 5, 6], lambda x: x ** 2)
truth_test = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above







