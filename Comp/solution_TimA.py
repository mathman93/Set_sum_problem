
''' Search for all Hamiltonian paths in graph starting a specific vertex
	Parameters:
		x = int; Starting vertex
		graph_dict = dictionary; dictionary representing the graph to search
	Returns:
		path = list; sequence of found path, or empty list if no path found
'''
def search(x, graph_dict):
	path = [] # Empty path to start
	max_num = len(graph_dict.keys()) # Maximum length of path
	initial_path = []
	initial_path.append(x) # Start at the beginning
	path_list = []
	path_list.append(initial_path) # Add the inital path to the pathlist
	while path_list: # While something is in the pathlist
		current_path = path_list.pop(-1) # Take last path from the list
		#print("Current Path: {0}".format(current_path)) # Include for debugging
		if len(current_path) == max_num: # If the current_path has a length of num...
			path = current_path # Save the path we found
			break # Stop finding solutions
		
		point = current_path[-1] # Take the last vertex of the current path
		# Find all vertices that can follow point
		for neighbor in reversed(graph_dict[point]):
			if neighbor not in current_path: # If the neighbor number hasn't been used yet...
				new_path = list(current_path) # Make a new path based on the current path
				new_path.append(neighbor) # Add the neighbor point to the new path
				path_list.append(new_path) # Add the new path to the list
			# Else, that point is already in the list
		# End for neighbor...
		# Go back and check the next path
	# End while path_list
	return path

## Main Code ##
k = int(input()) # Length of sequence
#k = 40 # Hard Code
vals = [int(i) for i in input().split()] # Values in sequence
#vals = list(range(1, k+1)) # Hard Code

# Length 30 sequences #
# Easy
#vals = [10, 19, 26, 37, 44, 55, 64, 73, 82, 89, 100, 107, 118, 125, 134, 143, 152, 161, 172, 181, 190, 199, 206, 215, 226, 235, 242, 251, 260, 269]
#vals = [8, 17, 28, 35, 46, 53, 62, 71, 80, 91, 98, 109, 116, 127, 136, 145, 154, 163, 170, 179, 188, 197, 208, 217, 224, 233, 244, 253, 262, 271]
#vals = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270]
# Length 40 sequences #
# Hard
#vals = [8, 17, 28, 35, 46, 53, 64, 73, 80, 91, 98, 109, 116, 127, 134, 145, 152, 161, 172, 179, 190, 197, 208, 215, 226, 233, 244, 251, 262, 269, 280, 289, 296, 307, 314, 325, 332, 343, 350, 361] # Values in sequence
# Easy
#vals = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270, 279, 288, 297, 306, 315, 324, 333, 342, 351, 360]

set_seq = [a**2 for a in range(1, int((2*max(vals))**0.5)+1)] # Squares

set_sum_dict = {} # Empty	
for i in vals: # Fill set_sum_dict
    set_sum_dict[i] = [] # Initially empty list
    new = [int(a - i) for a in set_seq if i<a and a<(2*i)] # Assumes vals are in ascending order.
    for j in new:
        if j in vals: # Only add if j is in the sequence
            # Add link to dictionary for both entries
            set_sum_dict[i].append(j)
            set_sum_dict[j].append(i)
        # End if j in vals
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
#if len(length1_list) > 0:
#    print("Values with only one connection: {0}".format(length1_list)) # Include for debugging
#if len(length0_list) > 0:
#    print("Values with no connections: {0}".format(length0_list)) # Include for debugging

foundpath = False # Flag for if we have found a path yet
if len(length0_list) > 0:
    pass # No paths are possible
	
elif len(length1_list) == 0: # Need to check all vertices
    # pick a starting vertex, and create a path with that
    for x in vals: # x is the starting vertex
        found = search(x, set_sum_dict)
        if len(found) > 0:
            foundpath = True
            break
        # End if len(found) > 0
    # End for x in range(...)
    
elif len(length1_list) > 2:
    pass # No paths are possible
    
else: # 1 or 2 vertices have only one connection
    # Need to check one vertex, and not halve the resulting number.
    # pick a starting vertex, and create a path with that
    x = length1_list[0] # Pick a vertex with only one neighbor.
    found = search(x, set_sum_dict)
    if len(found) > 0:
        foundpath = True
	# End if len(found) > 0
# End if len(length1_list)...

if foundpath:
	print("YES")
	#print("Path Found: {0}".format(found)) # Include for debugging
else:
	print("NO")
# End if