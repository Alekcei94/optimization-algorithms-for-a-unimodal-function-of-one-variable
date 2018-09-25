import math

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

def grad_p3(x1, x2):
	#y = math.sqrt((258*x1 - 256*x2 - 51)**2 + (-256*x1 + 258*x2 - 149)**2)
	y = 2*x1 + 2*x2 - 200 
	return y

def grad_p2(x1, x2):
	return y
	
def partial_derivative_p3_x1(x1):
	y = 258*x1 - 256*x2 - 51
	return y
	
def partial_derivative_p3_x2(x2):
	y = -256*x1 + 258*x2 - 149
	return y
	
def partial_derivative_p2_x1(x1):
	return y
	
def partial_derivative_p2_x1(x2):
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