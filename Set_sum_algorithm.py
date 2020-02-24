# Set_sum_algorithm.py
# Finds total number of all integer sequences of length n such that consecutive pairs
# of entries sum to an element of a given integer set.
# Last Modified: 2/23/2020
# Author(s): Timothy Anglea

import math
#import random
import time
import matplotlib.pyplot as plt
import numpy as np

## Functions ##
''' Search for all Hamiltonian paths in graph starting a specific vertex
	Parameters:
		x = int; Starting vertex
		graph_dict = dictionary; dictionary representing the graph to search
	Returns:
		pathcount = int; Total number of paths in graph_dict starting at x
'''
def search(x, graph_dict):
	pathcount = 0
	max_num = len(graph_dict.keys()) # Maximum length of path
	print("Finding paths starting with vertex {0}.".format(x))
	initial_path = []
	initial_path.append(x) # Start at the beginning
	path_list = []
	path_list.append(initial_path) # Add the inital path to the pathlist
	loop = 0 # initialize loop counter
	start_time = time.time()
	while path_list: # While something is in the pathlist
		current_path = path_list.pop(-1) # Take last path from the list
		if len(current_path) == max_num: # If the current_path has a length of num...
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

def squares(size):
	# Return sequence of square numbers to required size
	return [math.pow(a,2) for a in range(int(math.sqrt(2*size)+1))]

def cubes(size):
	# Return sequence of cube numbers to required size
	return [math.pow(a,3) for a in range(int(math.pow((2*size),(1/3))+1))]


seq_dict = {0: [squares, "SquareSum.npy"],
			1: [cubes, "CubeSum.npy"]
			}

## Main Code ##
# Data Input and Validation
while True:
	try:
		seq_opt = int(input("Sequence Option: ")) # Choose set sequence
		if seq_opt not in seq_dict.keys():
			print("Not a valid option. Please try again.")
			continue
		break
	except:
		print("That is not an integer. Please try again.")

while True:
	try:
		network_size = int(input("Whole number: ")) # Maximum network size
		if network_size < 0:
			print("Please enter a positive number.")
			continue
		break
	except KeyboardInterrupt:
		network_size = 1 # Default if exiting early; Plot total paths graph
		break
	except:
		print("That is not a whole number. Please try agian.")

# Check for previous file for the sequence option
file_name = seq_dict[seq_opt][1] # Get file name for sequence
try:
	finalcount_number = list(np.load(file_name))
except FileNotFoundError:
	print("File does not exist. Creating...")
	finalcount_number = []

# Main Loop: Find Hamiltonian paths in the network
for num in range(len(finalcount_number),network_size+1):
	# Create network dictionary
	sequence = seq_dict[seq_opt][0] # Retreive sequence set function
	set_seq = sequence(num) # Sequence set list
	set_sum_dict = {} # Empty	
	for i in range(1, num + 1):
		set_sum_dict[i] = [] # Initially empty list
		new = [int(a - i) for a in set_seq if i<a and a<(2*i)]
		for j in new:
			# Add link to dictionary for both entries
			set_sum_dict[i].append(j)
			set_sum_dict[j].append(i)
		# End for j in new
	# End for i in range(1, num + 1)
	# Display network dictionary
	print("Dictionary", set_sum_dict) # Include for debugging
	
	# Check for special vertices with two or fewer edges
	length1_list = []
	length2_list = []
	for n in set_sum_dict.keys():
		if len(set_sum_dict[n]) == 1:
			length1_list.append(n)
		elif len(set_sum_dict[n]) == 2:
			length2_list.append(n)
		# End if len(...) == 1
	# End for n in keys...
	print("Values with only one connection: {0}".format(length1_list)) # Include for debugging
	print("Values with only two connections: {0}".format(length2_list)) # Include for debugging
	
	# Modify network to simplify search, if possible
	mod_dict = set_sum_dict # Store copy of network dictionary to modify
	if len(length2_list) > 1: # If there are at least two vertices with only two neighbors...
		removed_v = [] # Empty
		for v in length2_list: # Check each vertex with only two edges
			if v in removed_v:
				continue # Already removed from mod_dict
			neighbor_v = mod_dict[v]
			for n in neighbor_v:
				if n in length2_list: # If the neighbor also has only two edges
					pass
					# Remove n from mod_dict
					# May want to move set_sum_dict entry for n to a new dictionary if I want to recreate the actual path
					# Make other neighbor of n (that is not v) to be a neighbor of v (and vice-versa)
					# Add n to removed_v list
				# Else, we continue on.
			# End for n
		# End for v ...
	# End if len(...) > 1
	
	# Begin checking for paths
	finalcount = 0
	if len(length1_list) == 0:
		# Need to check all vertices
		print("Check ALLLLL the numbers!")
		print("Searching graph size of {0}...".format(num))
		# pick a starting vertex, and create a path with that
		for x in range(1, num + 1): # x is the starting vertex
			count = search(x, set_sum_dict)
			finalcount += count
		# End for x in range(...)
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount//2))
		
		finalcount_number.append(finalcount//2)
		
	elif len(length1_list) > 2:
		# No paths are possible
		print("Don't waste your time!")
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
		
		finalcount_number.append(finalcount)
		
	else: # 1 or 2 vertices have only one connection
		# Need to check one vertex, and not halve the resulting number.
		print("Just check one of them.")
		print("Searching graph size of {0}...".format(num))
		# pick a starting vertex, and create a path with that
		x = length1_list[0] # Pick a vertex with only one neighbor.
		finalcount = search(x, set_sum_dict)
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
		
		finalcount_number.append(finalcount)
		
	# End if len(length1_list)...
# End for num in range...

# Save list of total paths for future use
np.save(file_name, finalcount_number)
# Plot total paths versus network size
seq_length = list(range(len(finalcount_number)))
plt.semilogy(seq_length, finalcount_number, "o")
plt.grid()
plt.show() # Include to display plot

