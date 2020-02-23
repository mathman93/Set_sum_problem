# Set_sum_algorithm.py
# Finds total number of all integer sequences of length n such that consecutive pairs
# of entries sum to an element of a given integer set.
# Last Modified: 2/22/2020
# Author(s): Timothy Anglea

import math
#import random
import time
import matplotlib.pyplot as plt
import numpy as np

''' Search for all Hamiltonian paths in graph starting a specific vertex
	Parameters:
		x = int; Starting vertex
		graph_dict = dictionary; dictionary representing the graph to search
	Returns:
		pathcount = int; Total number of paths in graph_dict starting at x
'''
def search(x, graph_dict):
	pathcount = 0
	print("Finding paths starting with vertex {0}.".format(x))
	initial_path = []
	initial_path.append(x) # Start at the beginning
	path_list = []
	path_list.append(initial_path) # Add the inital path to the pathlist
	loop = 0 # initialize loop counter
	start_time = time.time()
	while path_list: # While something is in the pathlist
		current_path = path_list.pop(-1) # Take last path from the list
		if len(current_path) == num: # If the current_path has a length of num...
			#print("Final Answer:", current_path) # Include for debugging
			pathcount += 1 # We have found a solution
			continue # Go to next path
		
		point = current_path[-1] # Take the last vertex of the current path
		# Find all vertices that can follow point
		for neighbor in graph_dict[point]:
			if neighbor not in current_path: # If the neighbor number hasn't been used yet...
				new_path = list(current_path) # Make a new path based on the current path
				new_path.append(neighbor) # Add the neighbor point to the new path
				path_list.append(new_path) # Add the new path to the list
			# Else, that point is already in the list
		# End for neighbor...
		loop += 1 # Add one to while loop counter
		# Go back and check the next path
	# End while path_list
	end_time = time.time()
	print("Time of search: {0:.3f} seconds".format(end_time-start_time))
	print("Number of loops: {0}".format(loop))
	#print(" Total paths found after searching vertex {0}: {1}".format(x, finalcount))
	
	return pathcount

while True:
	try:
		number = int(input('Whole number: '))
		break
	except KeyboardInterrupt:
		number = 1
		break
	except:
		print("That is not an integer. Please try agian.")

file_name = "SquareSum.npy"
try:
	finalcount_number = list(np.load(file_name))
except FileNotFoundError:
	print("File does not exist. Creating...")
	finalcount_number = []

for num in range(len(finalcount_number),number+1):
	sum_square_dict = {} # Empty	
	# Create network dictionary (squares)
	square_seq = [] # Empty
	square_seq[:] = [pow(a,2) for a in range(int(math.sqrt(2*num)+1))]
	for i in range(1, num + 1):
		sum_square_dict[i] = [] # Initially empty list
		new = []
		new[:] = [a - i for a in square_seq if i<a and a<(2*i)]
		for j in new:
			# Add link to dictionary for both entries
			link_list = sum_square_dict[i]
			link_list.append(j)
			sum_square_dict[i] = link_list
			# sum_square_dict[i].append(j)
			link_list = sum_square_dict[j]
			link_list.append(i)
			sum_square_dict[j] = link_list
			# sum_square_dict[j].append(i)
		# End for j in new
	# End for i in range(1, num + 1)
	# Display network dictionary
	#print("Dictionary", sum_square_dict) # Include for debugging
	
	length1_list = []
	length2_list = []
	for n in sum_square_dict.keys():
		if len(sum_square_dict[n]) == 1:
			length1_list.append(n)
		elif len(sum_square_dict[n]) == 2:
			length2_list.append(n)
		# End if len(...) == 1
	# End for n in keys...
	#print("Values with only one connection: {0}".format(length1_list)) # Include for debugging
	#print("Values with only two connections: {0}".format(length2_list)) # Include for debugging
	
	finalcount = 0
	if len(length1_list) == 0:
		# Need to check all vertices
		print("Check ALLLLL the numbers!")
		print("Searching graph size of {0}...".format(num))
		# pick a starting vertex, and create a path with that
		for x in range(1, num + 1): # x is the starting vertex
			count = search(x, sum_square_dict)
			finalcount += count
		# End for x in range(...)
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount//2))
		
		finalcount_number.append(finalcount//2)
		
	elif len(length1_list) > 2:
		# No paths are possible
		print("Don't waste your time!")
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
		
		finalcount_number.append(finalcount)
		
	else:
		# 1 or 2 vertices have only one connection
		# Need to check one vertex, and not halve the resulting number.
		print("Just check one of them.")
		# pick a starting vertex, and create a path with that
		x = length1_list[0] # Pick a vertex with only one neighbor.
		finalcount = search(x, sum_square_dict)
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
		
		finalcount_number.append(finalcount)
		
	# End if len(length1_list)...

	np.save(file_name, finalcount_number)
		
# End for num in range...

seq_length = list(range(len(finalcount_number)))
plt.semilogy(seq_length, finalcount_number, "o")
plt.grid()
plt.show() # Include to display plot

