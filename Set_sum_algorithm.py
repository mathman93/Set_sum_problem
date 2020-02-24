# Set_sum_algorithm.py
# Finds total number of all integer sequences of length n such that consecutive pairs
# of entries sum to an element of a given integer set.
# Last Modified: 2/24/2020
# Author(s): Timothy Anglea
# Need to check that modified dictionary can be search through properly if vertices are removed

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

''' Reduce size of graph for easier searching
	Looks for long chains and shortens them
	Parameters:
		graph_dict = dictionary; The network to reduce
		keep_node = int; starting node of path; keep this in the network when reducing
	Returns:
		new_dict = dictionary; reduced dictionary
'''
def reduce(graph_dict, keep_node=None):
	# Modify network to simplify search, if possible
	new_dict = {} # Empty
	for i in graph_dict.keys():
		new_dict[i] = list(graph_dict[i]) # Store copy of network dictionary to modify
	if keep_node == None:
		removed_v = [] # Empty
	else:
		removed_v = [keep_node] # Do not remove this vertex
	
	length2_list = []
	for n in new_dict.keys():
		if len(new_dict[n]) == 2:
			length2_list.append(n)
		# End if len(...) == 1
	# End for n in keys...
	print("Values with only two connections: {0}".format(length2_list)) # Include for debugging

	if len(length2_list) > 1: # If there are at least two vertices with only two neighbors...
		for v in length2_list: # Check each vertex with only two edges
			if v in removed_v:
				continue # Already removed from new_dict
			neighbor_v = new_dict[v]
			for n in neighbor_v:
				if n in length2_list: # If the neighbor also has only two edges
					neighbor_v2 = new_dict[v] # Get neighbors of v (identical to neighbor_v)
					# Remove v from new_dict
					for x in neighbor_v2:
						new_dict[x].remove(v) # Remove connection to node n from neighbors of n
					del new_dict[v] # Delete entry of node n from dictionary
					#memory_dict[v] = neighbor_v # Move entry for n to a new dictionary if I want to recreate the actual path
					# Make other neighbor of v (that is not n) to be a neighbor of n (and vice-versa)
					neighbor_v2.remove(n)
					o = neighbor_v2[0] # Other neighbor of v that is not n
					new_dict[n].append(o)
					new_dict[o].append(n)
					# Add v to removed_v list
					removed_v.append(v)
				# Else, we continue on.
			# End for n
		# End for v ...
	# End if len(...) > 1
	return new_dict

def squares(size):
	# Return sequence of square numbers to required size
	return [int(math.pow(a,2)) for a in range(int(math.sqrt(2*size)+1))]

def cubes(size):
	# Return sequence of cube numbers to required size
	return [int(math.pow(a,3)) for a in range(int(math.pow((2*size),(1/3))+1))]

def triangular(size):
	# Return sequence of triangular numbers to required size
	seq = [1]
	i = 2
	while seq[-1] < 2*size:
		x = int(i*(i+1)/2)
		seq.append(x)
		i += 1
	return seq

def pentagonal(size):
	# Return sequence of pentagonal numbers to required size
	seq = [1]
	i = 2
	while seq[-1] < 2*size:
		x = int(i*((3*i)-1)/2)
		seq.append(x)
		i += 1
	return seq

def tetrahedral(size):
	# Return sequence of tetrahedral numbers to required size
	seq = [1]
	i = 2
	while seq[-1] < 2*size:
		x = int(i*(i+1)*(i+2)/6)
		seq.append(x)
		i += 1
	return seq

def fibonacci(size):
	# Return sequence of Fibonacci numbers to required size
	seq = [2,3] # Don't need numbers <= 1
	while seq[-1] < 2*size:
		x = seq[-1] + seq[-2]
		seq.append(x)
	return seq

def lucas(size):
	# Return sequence of Lucas numbers to required size
	seq = [3,4] # Don't need numbers <= 1
	while seq[-1] < 2*size:
		x = seq[-1] + seq[-2]
		seq.append(x)
	return seq

seq_dict = {0: [squares, "SquareSum.npy"],
			1: [cubes, "CubeSum.npy"],
			2: [triangular, "TriangleSum.npy"],
			3: [pentagonal, "PentagonSum.npy"],
			4: [tetrahedral, "TetraSum.npy"],
			5: [fibonacci, "FibSum.npy"],
			6: [lucas, "LucasSum.npy"]
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
	for n in set_sum_dict.keys():
		if len(set_sum_dict[n]) == 1:
			length1_list.append(n)
		# End if len(...) == 1
	# End for n in keys...
	print("Values with only one connection: {0}".format(length1_list)) # Include for debugging
	
	# Begin checking for paths
	finalcount = 0
	if len(length1_list) == 0:
		# Need to check all vertices
		print("Check ALLLLL the numbers!")
		print("Searching graph size of {0}...".format(num))
		# pick a starting vertex, and create a path with that
		for x in range(1, num + 1): # x is the starting vertex
			mod_dict = reduce(set_sum_dict, x)
			#print("Modified Dictionary", mod_dict) # Include for debugging
			#print("Original Dictionary", set_sum_dict) # Include for debugging
			print("Network Reduction:", len(set_sum_dict.keys())-len(mod_dict.keys()))
			count = search(x, mod_dict)
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
		mod_dict = reduce(set_sum_dict)
		#print("Modified Dictionary", mod_dict) # Include for debugging
		#print("Original Dictionary", set_sum_dict) # Include for debugging
		print("Network Reduction:", len(set_sum_dict.keys())-len(mod_dict.keys()))
		finalcount = search(x, mod_dict)
		print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
		
		finalcount_number.append(finalcount)
		
	# End if len(length1_list)...
	# Save list of total paths for future use
	np.save(file_name, finalcount_number)
# End for num in range...

# Plot total paths versus network size
seq_length = list(range(len(finalcount_number)))
plt.plot(seq_length, finalcount_number, "o")
plt.yscale("log")
plt.grid()
plt.show() # Include to display plot

