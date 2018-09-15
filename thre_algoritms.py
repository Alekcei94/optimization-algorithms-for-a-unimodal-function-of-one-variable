def method_midpoint(a, b, eps):
	iterator = 0
	while True:
		iterator = iterator + 1
		xi = (a+b)/2
		yi=calculation_function_derivative(xi)
		if abs(yi)<=eps:
			x_min = xi
			y_min = calculation_function(xi)
			print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
			break
		else:
			if yi>0:
				b = xi
			else:
				a = xi
	pass

def method_hord(a, b, eps):
	iterator = 0
	ya=calculation_function_derivative(a)
	yb=calculation_function_derivative(b)
	while True:
		iterator = iterator +1
		xi= a-((ya/(ya-yb))*(a-b))
		yi = calculation_function_derivative(xi)
		if abs(yi)<=eps:
			x_min = xi
			y_min = calculation_function(xi)
			print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
			break
		else:
			if yi>0:
				b=xi
				yb=yi
			else:
				a=xi
				ya=yi
	pass

def method_step(a, b, eps):
	y_min=calculation_function(a)
	iterator = 0
	xi = a
	#direction = 1
	delta = (abs(a)+abs(b))/4
	while True:
		iterator = iterator + 1
		xi = xi+delta
		if xi>b:
			print ("exit b > xi ? big delta")
			break
		yi = calculation_function(xi)
		#print (" x = " + str(xi) + " y = " + str(yi) + " y_min = " + str(y_min) + " delta = " + str(delta))
		if yi>y_min:
			if abs(delta)<=eps:
				x_min = xi
				y_min = calculation_function(x_min)
				print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
				break
			y_min = yi
			#a = xi
			#b = a
			delta = delta/4 *(-1)
			#direction = (-1)*direction
		else:
			y_min = yi
	pass

def dixotomii(a,b,eps):
	iterator = 0
	tetta=eps*1.5
	while True:
		iterator = iterator + 1
		x1 = (b+a-tetta)/2
		x2 = (b+a+tetta)/2
		y1 = calculation_function(x1)
		y2 = calculation_function(x2)
		if y1 <= y2:
			b=x2
		else:
			a=x1
		U=(b-a)/2
		if U<=eps:
			x_min = (a+b)/2
			y_min = calculation_function(x_min)
			print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
			break
	pass

def gold_section(a, b, eps):
	iterator = 0
	t = (5**0.5 - 1)/2
	x2 = a+t*(b-a)
	x1 = a+b-x2
	y2 = calculation_function(x2)
	y1 = calculation_function(x1)
	while True:
		iterator = iterator + 1
		if y1<=y2:
			b=x2
			x2=x1
			y2=y1
			x1=a+b-x1
			y1= calculation_function(x1)
		else:
			a=x1
			x1=x2
			y1=y2
			x2=a+b-x2
			y2 = calculation_function(x2)
		U=(b-a)/2
		if U<eps:
			x_min = (a+b)/2
			y_min = calculation_function(x_min)
			print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
			break
	pass
	
def method_all_point(a, b, eps):
	iterator = 0
	x_min = a
	xi = a
	y_min = calculation_function(a)
	while True:
		iterator = iterator +1
		xi = xi + eps
		if xi>b:
			print ("colition iteration = " + str(iterator) + " x_min = " + str(x_min) + " y_min = " + str(y_min)) 
			break
		yi = calculation_function(xi)
		if yi<y_min:
			y_min = yi
			x_min = xi
	pass
	
def calculation_function(x):
	y=x**4+x**2+x+1
	return y

	
def calculation_function_derivative(x):
	y=4*(x**3) + 2*x + 1 
	return y

a = -1
b = 0
eps = 0.0001
 
#while testt==0:
print ("comands:")
print ("1 - method calculation all points;")
print ("2 - method_step;")
print ("3 - dixotomii;")
print ("4 - gold_section;")
print ("5 - method_hord;")
print ("6 - method_midpoint;")
print ("7 - ;")
print ("8 - exit.")
while True:
	comands = input()
	if int(comands)==1:
		method_all_point(a, b, eps)
	elif int(comands)==2:
		method_step(a, b, eps)
	elif int(comands)==3:
		dixotomii(a, b, eps)
	elif int(comands)==4:
		gold_section(a, b, eps)
	elif int(comands)==5:
		method_hord(a, b, eps)
	elif int(comands)==6:
		method_midpoint(a, b, eps)
	elif int(comands)==7:
		break
	elif int(comands)==8:
		break