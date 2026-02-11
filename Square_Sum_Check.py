# Square_Sum_Check.py
# Finds a solution for square-sum problem for given range of integers M to N (M < N)
# Last Modified: 2/10/2026
# Author: Timothy Anglea

import math
import time

## Functions ##
''' Displays current date and time to the screen
'''
def DisplayDateTime():
	# Month day, Year, Hour:Minute:Seconds
	date_time = time.strftime("%B %d, %Y, %H:%M:%S", time.localtime())
	print("Current Time:", date_time)

''' Search for all Hamiltonian paths in graph starting a specific vertex
	Parameters:
		x = int; Starting vertex
		graph_dict = dictionary; dictionary representing the graph to search
	Returns:
		path = list; sequence of found path, or empty list if no path found
'''
def search(x, graph_dict):
	debug = False # Set to True to enable debugging output
	path = [] # Empty path to start
	max_num = len(graph_dict.keys()) # Maximum length of path
	if debug:
		print("Finding paths starting with vertex {0}.".format(x)) # Include for debugging
	initial_path = []
	initial_path.append(x) # Start at the beginning
	path_list = []
	path_list.append(initial_path) # Add the inital path to the pathlist
	if debug:
		loop = 0 # initialize loop counter
		start_time = time.time()
	while path_list: # While something is in the pathlist
		current_path = path_list.pop(-1) # Take last path from the list
		#print("Current Path: {0}".format(current_path)) # Include for debugging
		if len(current_path) == max_num: # If the current_path has a length of num...
			path = current_path # Save the path we found
			if debug:
				print("Final Answer:", path)
			break # Stop finding solutions
		
		point = current_path[-1] # Take the last vertex of the current path
		# Find all vertices that can follow point
		for neighbor in graph_dict[point]:
			if neighbor not in current_path: # If the neighbor number hasn't been used yet...
				new_path = list(current_path) # Make a new path based on the current path
				new_path.append(neighbor) # Add the neighbor point to the new path
				path_list.append(new_path) # Add the new path to the list
			# Else, that point is already in the list
		# End for neighbor...
		if debug:
			loop += 1 # Add one to while loop counter; Include for debugging
		# Go back and check the next path
	# End while path_list
	
	if debug:
		end_time = time.time()
		print("Time of search: {0:.3f} seconds".format(end_time-start_time))
		DisplayDateTime()
		print("Number of loops: {0}".format(loop))
	
	return path

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

def hypertetra(size):
	# Return sequence of hypertetrahedral numbers to required size
	seq = [1]
	i = 2
	while seq[-1] < 2*size:
		x = int(i*(i+1)*(i+2)*(i+3)/24)
		seq.append(x)
		i += 1
	return seq

def primes(size):
	seq = [] # List of prime numbers
	pflag = True
	for n in range(2,2*size):
		for p in seq:
			x = n/p
			if x == int(x):
				pflag = False
				break
			#End if
		#End for p
		if pflag:
			seq.append(n)
		pflag = True
	#End for n
	return seq

seq_dict = {0: [squares, "SquareSum.npy"],
			1: [cubes, "CubeSum.npy"],
			2: [triangular, "TriangleSum.npy"],
			3: [pentagonal, "PentagonSum.npy"],
			4: [tetrahedral, "TetraSum.npy"],
			5: [fibonacci, "FibSum.npy"],
			6: [lucas, "LucasSum.npy"],
			7: [hypertetra, "HypertetraSum.npy"],
			8: [primes, "PrimeSum.npy"]
			}

## Main Code ##
# Data Input and Validation
# while True:
# 	try:
# 		seq_opt = int(input("Sequence Option: ")) # Choose set sequence
# 		if seq_opt not in seq_dict.keys():
# 			print("Not a valid option. Please try again.")
# 			continue
# 		break
# 	except:
# 		print("That is not an integer. Please try again.")
seq_opt = 0 # Default to square sequence

while True:
	try:
		seq_min = int(input("M = ")) # Maximum network size
		if seq_min < 0:
			print("Please enter a positive number.")
			continue
		break
	except KeyboardInterrupt:
		seq_min = 1 # Default if exiting early
		break
	except:
		print("That is not a whole number. Please try again.")
		
while True:
	try:
		seq_size = int(input("N = ")) # Maximum network size
		if seq_size < 0:
			print("Please enter a positive number.")
			continue
		break
	except KeyboardInterrupt:
		seq_size = 1 # Default if exiting early
		break
	except:
		print("That is not a whole number. Please try again.")
#seq_min = 10001 # Minimum integer of sequence
#seq_size = 200 # Number of integers in sequence
seq_max = seq_min + seq_size - 1 # Maximum integer of sequence

DisplayDateTime()

# Main Loop: Find Hamiltonian paths in the network

# Create network dictionary
sequence = seq_dict[seq_opt][0] # Retreive sequence set function
set_seq = sequence(seq_max) # Generate sequence set list
set_sum_dict = {} # Empty	
for i in range(seq_min, seq_max + 1): # Fill set_sum_dict
    set_sum_dict[i] = [] # Initially empty list
    new = [int(a - i) for a in set_seq if (i+seq_min-1)<a and a<(2*i)]
    for j in new:
        # Add link to dictionary for both entries
        set_sum_dict[i].append(j)
        set_sum_dict[j].append(i)
    # End for j in new
# End for i in range
# Display network dictionary
#print("Dictionary", set_sum_dict) # Include for debugging

# Check for special vertices with two or fewer edges
length1_list = [] # List of vertices with only one connection; If more than 2, no paths are possible
length0_list = [] # List of vertices with no connections; If any, no paths are possible
for n in set_sum_dict.keys():
    if len(set_sum_dict[n]) == 1:
        length1_list.append(n)
    elif len(set_sum_dict[n]) == 0:
        length0_list.append(n)
    # End if len(...) == 1
# End for n in keys...
if len(length1_list) > 0:
    print("Values with only one connection: {0}".format(length1_list)) # Include for debugging
if len(length0_list) > 0:
    print("Values with no connections: {0}".format(length0_list)) # Include for debugging

# Begin checking for paths
foundpath = False # Flag for if we have found a path yet
if len(length0_list) > 0:
    # No paths are possible
    print("Don't waste your time!")
	
elif len(length1_list) == 0:
    # Need to check all vertices
    print("Check ALLLLL the numbers!")
    print("Searching graph size of {0}...".format(seq_size))
    # pick a starting vertex, and create a path with that
    for x in range(seq_min, seq_max + 1): # x is the starting vertex
        mod_dict = set_sum_dict # Include for no reductions
        #mod_dict = reduce(set_sum_dict, x)
        #print("Modified Dictionary", mod_dict) # Include for debugging
        #print("Original Dictionary", set_sum_dict) # Include for debugging
        #print("Network Reduction:", len(set_sum_dict.keys())-len(mod_dict.keys()))
        found = search(x, mod_dict)
        if len(found) > 0:
            foundpath = True
            break
        
    # End for x in range(...)
    
elif len(length1_list) > 2:
    # No paths are possible
    print("Too many dead ends!")
    
else: # 1 or 2 vertices have only one connection
    # Need to check one vertex, and not halve the resulting number.
    print("Just check one of them.")
    print("Searching graph size of {0}...".format(seq_size))
    # pick a starting vertex, and create a path with that
    x = length1_list[0] # Pick a vertex with only one neighbor.
    mod_dict = set_sum_dict # Include for no reduction
    #mod_dict = reduce(set_sum_dict)
    #print("Modified Dictionary", mod_dict) # Include for debugging
    #print("Original Dictionary", set_sum_dict) # Include for debugging
    #print("Network Reduction:", len(set_sum_dict.keys())-len(mod_dict.keys()))
    found = search(x, mod_dict)
    if len(found) > 0:
        foundpath = True
	# End if len(found) > 0
# End if len(length1_list)...

if foundpath:
	print("Found path:", found)
else:
	print("No path found.")
# End if
