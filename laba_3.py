def method_gradien_descent(eps):
	print("")
	pass

def method_fast_descent(eps):
	print("")
	pass
	
def method_nuthons(eps):
	print("")
	pass

def calculation_function(x1, x2):
	y=0
	y = 129*x1*x1 - 256*x1*x2 + 129*x2*x2 - 51*x1 - 149*x2 - 27
	return y

def grad(x1, x2):
	# (258*x1 - 256*x2 - 51) + (-256*x1 + 258*x2 - 149)
	y = 2*x1 + 2*x2 - 200 
	return y

	
eps = 0.0001
alfa
print ("comands:")
print ("1 - method gradient descent")
print ("2 - method fast descent")
print ("3 - method nuthon")
print ("4 - exit.")
while True:
	comands = input()
	if int(comands)==1:
		method_gradien_descent(eps)
	elif int(comands)==2:
		method_fast_descent(eps)
	elif int(comands)==3:
		method_nuthons(eps)
	elif int(comands)==4:
		break