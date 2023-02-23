from line_graph import *   # personal .py file



# Repeatedly transforms a given number (through the Collatz process) until it becomes 1.
def transformNaturalNumber(num, graph):

	transformable_num = num #An editable copy of the given number
	number_of_steps_taken = 0
	
	while transformable_num != 1:
		# If the number is NOT even,
		if transformable_num % 2 != 0:
			# the new number is obtained through (3n + 1)
			transformable_num = 3*transformable_num + 1
		else:
			# the number would be even, and the new number is obtained through (n/2)
			transformable_num = transformable_num // 2
	
		print("=>", transformable_num) 
		
		graph.x_values.append(len(graph.x_values))
		graph.y_values.append(transformable_num)
		number_of_steps_taken += 1 # increments the number of steps taken
	
	print("\n>>> Number of steps taken to reach 1: ", number_of_steps_taken) #Ultimately prints the number of times the number has been transformed to reach 1


# (Forever until program is ended)
while True:
	initial_number = int(input("\nEnter a natural number: ")) #Allows user to input a natural number
	
	# If the number is not natural (below 1),
	if initial_number < 1:
		raise Exception("Number must be natural (1, 2, 3, 4, ... Inf)") #An exception is raised

	
	# Graph to represent how a given number ends up at 1 through the Collatz process
	number_transformation_graph = LineGraph([0], [initial_number], "Collatz Conjecture Visualization (n = {})".format(initial_number), "index", "values of n")
	
	
	transformNaturalNumber(initial_number, number_transformation_graph) #Repeatedly transforms the initial number (through the Collatz process) until it becomes 1
	print(">>> Initial number: ", initial_number) #Prints the inital number (to refer to)
			
	number_transformation_graph.show() # Graph is shown
