#!usr/bin/python

class Operation(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def sum(self):
		return self.x + self.y

	def subtraction(self):
		return self.x - self.y

	def multiplication(self):
		return self.x * self.y

	def division(self):
		return self.x / self.y

def main():
	while True:
		try:
			F_num = input("enter 1st number: ")
			S_num = input("enter 2nd number: ")
			break
		except:
			print "please enter only floats or integers"

	operation = Operation(F_num, S_num)

	while True:
		try:
			decision = raw_input("""
-------------------------
type desired operation
s : sum
d : divide
m : multiply
r : subtract
-------------------------
""")
			break
		except ValueError:
			print "please try again"

	print "--------------------------"
	if decision == "s":
		print "summation: " + str(operation.sum())
        elif decision == "d":
		print "division: " + str(operation.division())
      	elif decision == "m":
       		print "multiplication: " + str(operation.multiplication())
       	elif decision == "r":
       		print "subtraction: " + str(operation.subtraction())
	else:
		print "invalid input"


if __name__ == "__main__":
	main()
