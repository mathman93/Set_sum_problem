# Set_sum_algorithm.py
# Finds total number of all integer sequences of length n such that consecutive pairs
# of entries sum to an element of a given integer set.
# Last Modified: 2/22/2020
# Author(s): Timothy Anglea

import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np

number = int(input('Whole number: '))

data_label = "Data_Stuff5.txt"
seq_length = []
finalcount_number = []
with open(data_label, "r") as f:
    finalcount_number = eval(f.readline())
seq_length = list(range(1,len(finalcount_number)+1))


for num in range(len(finalcount_number)+1,number+1):
    '''
    sum_square_dict = {} # Empty
    links = 0 # initialize
    network_size = [] # Empty
    link_ratio = [] # Empty
    
    # Create network dictionary (squares)
    square_seq = [] # Empty
    square_seq[:] = [pow(a,2) for a in range(int(math.sqrt(2*num)+1))]
    # End while True
    for x in range(1, num + 1):
        sum_square_dict[x] = [] # Initially empty list
        new = []
        new[:] = [a - x for a in square_seq if x<a and a<(2*x)]
        for y in new:
            # Add link to dictionary
            link_list = sum_square_dict[x]
            link_list.append(y)
            sum_square_dict[x] = link_list
            # Add links in both entries
            link_list = sum_square_dict[y]
            link_list.append(x)
            sum_square_dict[y] = link_list
            # Update number of network links
            links += 1
        # End for y in new
        # Save values for network size and number of links
        network_size.append(x)
        link_ratio.append(links/x)
        # Print ratio of edges to vertices
        #print("{0}: {1:.5f}".format(x, links/x))
    # End for x in range(1, num + 1)
    # Create plot of network size vs. link ratio
    #plt.semilogx(network_size, link_ratio)
    #plt.show() # Include to display plot
    # Display network dictionary
    #print("Dictionary", sum_square_dict)
    '''
    
    '''
    sum_cube_dict = {} # Empty
    links = 0 # initialize
    network_size_cube = [] # Empty
    link_ratio_cube = [] # Empty
    
    # Create network dictionary (cubes)
    cube_seq = [] # Empty
    cube_seq[:] = [pow(a,3) for a in range(int(math.pow(2*num,1/3)+1))]
    # End while True
    for x in range(1, num + 1):
        sum_cube_dict[x] = [] # Initially empty list
        new = []
        new[:] = [a - x for a in cube_seq if x<a and a<(2*x)]
        for y in new:
            # Add link to dictionary
            link_list = sum_cube_dict[x]
            link_list.append(y)
            sum_cube_dict[x] = link_list
            # Add links in both entries
            link_list = sum_cube_dict[y]
            link_list.append(x)
            sum_cube_dict[y] = link_list
            # Update number of network links
            links += 1
        # End for y in new
        # Save values for network size and number of links
        network_size_cube.append(x)
        link_ratio_cube.append(links/x)
        # Print ratio of edges to vertices
        #print("{0}: {1:.5f}".format(x, links/x))
    # End for x in range(1, num + 1)
    # Create plot of network size vs. link ratio
    #plt.plot(network_size_cube, link_ratio_cube)
    #plt.show() # Include to display plot
    # Display network dictionary
    #print("Dictionary", sum_cube_dict)
    '''
    '''
    sum_fib_dict = {} # Empty
    network_size_fib = [] # Empty
    link_ratio_fib = [] # Empty
    links = 0 # Reset
    
    # Create network dictionary (Fibonacci)
    fib_seq = [1,2] # Initial sequence
    while True:
        fib_seq.append(fib_seq[len(fib_seq)-1]+fib_seq[len(fib_seq)-2])
        if fib_seq[len(fib_seq)-1] > (2*num):
            break
        # End if fib_seq[len(fib_seq)-1] > (2*num)
    # End while True
    for x in range(1,num+1):
        sum_fib_dict[x] = [] # Initially empty list
        new = []
        new[:] = [a - x for a in fib_seq if x<a and a<(2*x)]
        for y in new:
            # Add link to dictionary
            link_list = sum_fib_dict[x]
            link_list.append(y)
            sum_fib_dict[x] = link_list
            # Add links in both entries
            link_list = sum_fib_dict[y]
            link_list.append(x)
            sum_fib_dict[y] = link_list
            # Update number of network links
            links += 1
        # End for y in new
        # Save values for network size and number of links
        network_size_fib.append(x)
        link_ratio_fib.append(links/x)
        # Print ratio of edges to vertices
        #print("{0}: {1:.5f}".format(x, links/x))
    # End for x in range(1, num + 1)
    # Create plot of network size vs. link ratio
    #plt.semilogx(network_size_fib, link_ratio_fib)
    #plt.grid(True)
    #plt.show() # Include to display plot
    # Display network dictionary
    print("Dictionary", sum_fib_dict)
    '''
    '''
    sum_pent_dict = {} # Empty
    links = 0 # initialize
    network_size_pent = [] # Empty
    link_ratio_pent = [] # Empty
    
    # Create network dictionary (pentagonal)
    pent_seq = [] # Empty
    pent_seq[:] = [int((a*(3*a-1))/2) for a in range(2,int((1/3)*(math.pow(6*(2*num)+0.25,0.5)+0.5)+1))]
    
    for x in range(1, num + 1):
        sum_pent_dict[x] = [] # Initially empty list
        new = []
        new[:] = [a - x for a in pent_seq if x<a and a<(2*x)]
        for y in new:
            # Add link to dictionary
            link_list = sum_pent_dict[x]
            link_list.append(y)
            sum_pent_dict[x] = link_list
            # Add links in both entries
            link_list = sum_pent_dict[y]
            link_list.append(x)
            sum_pent_dict[y] = link_list
            # Update number of network links
            links += 1
        # End for y in new
        # Save values for network size and number of links
        network_size_pent.append(x)
        link_ratio_pent.append(links/x)
        # Print ratio of edges to vertices
        #print("{0}: {1:.5f}".format(x, links/x))
    # End for x in range(1, num + 1)
    # Create plot of network size vs. link ratio
    #plt.plot(network_size_pent, link_ratio_pent)
    #plt.show() # Include to display plot
    # Display network dictionary
    #print("Dictionary", sum_pent_dict)
    '''

    sum_tetra_dict = {} # Empty
    network_size_tetra = [] # Empty
    link_ratio_tetra = [] # Empty
    links = 0 # Reset
    
    # Create network dictionary (Tetragonal)
    tetra_seq = [] # Empty
    index = 1
    while True:
        tetra_seq.append(int((index*(index+1)*(index+2))/6))
        if tetra_seq[-1] > 2*num:
            break
        index = index+1 # Increment counter        
    # End while True
    #tetra_seq[:] = [int((a*(a+1)*(a+2))/6) for a in range(1,int((1/3)*(math.pow(6*(2*num)+0.25,0.5)+0.5)+1))]
    
    for x in range(1,num+1):
        sum_tetra_dict[x] = [] # Initially empty list
        new = []
        new[:] = [a - x for a in tetra_seq if x<a and a<(2*x)]
        for y in new:
            # Add link to dictionary
            link_list = sum_tetra_dict[x]
            link_list.append(y)
            sum_tetra_dict[x] = link_list
            # Add links in both entries
            link_list = sum_tetra_dict[y]
            link_list.append(x)
            sum_tetra_dict[y] = link_list
            # Update number of network links
            links += 1
        # End for y in new
        # Save values for network size and number of links
        network_size_tetra.append(x)
        link_ratio_tetra.append(links/x)
        # Print ratio of edges to vertices
        #print("{0}: {1:.5f}".format(x, links/x))
    # End for x in range(1, num + 1)
    # Create plot of network size vs. link ratio
    #plt.semilogx(network_size_tetra, link_ratio_tetra)
    #plt.grid(True)
    #plt.show() # Include to display plot
    # Display network dictionary
    print("Dictionary", sum_tetra_dict)
    
    
    length1_list = []
    for n in sum_tetra_dict.keys():
        if len(sum_tetra_dict[n]) == 1:
            length1_list.append(n)
        # End if len(...) == 1
    # End for n in keys...
    print("Values with only one connection: {0}".format(length1_list))

    finalcount = 0
    if len(length1_list) == 0:
        # Need to check all vertices
        print("Check ALLLLL the numbers!")
        print("Searching graph size of {0}...".format(num))
        # pick a starting vertex, and create a path with that
        for x in range(1, num + 1): # x is the starting vertex
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
                    #print("FinalAnswer", current_path)
                    finalcount += 1 # We have found a solution
                
                point = current_path[-1] # Take the last vertex of the current path
                # Find all numbers that can follow the value point
                for neighbor in sum_tetra_dict[point]:
                    if neighbor not in current_path: # If the neighbor number hasn't been used yet...
                        new_path = list(current_path) # Make a new path based on the current path
                        new_path.append(neighbor) # Add the neighbor point to the new path
                        path_list.append(new_path) # Add the new path to the list
                    # Else, that point is already in the list
                # End for neighbor...
                loop += 1 # Add one to loop counter
                # Go back and check the next path
            # End while path_list
            end_time = time.time()
            print("Time of search: {0:.3f} seconds".format(end_time-start_time))
            print("Number of loops: {0}".format(loop))
            #print(" Total paths found after searching vertex {0}: {1}".format(x, finalcount))
        # End for x in range(...)
        print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount//2))
        
        finalcount_number.append(finalcount//2)
        seq_length = list(range(1,len(finalcount_number)+1))
        
    elif len(length1_list) > 2:
        # No paths are possible
        print("Don't waste your time!")
        print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))
        
        finalcount_number.append(finalcount)
        seq_length = list(range(1,len(finalcount_number)+1))
        
    else:
        # 1 or 2 vertices have only one connection
        # Need to check one vertex, and not halve the resulting number.
        print("Just check one of them.")
        print("Searching graph size of {0}...".format(num))
        # pick a starting vertex, and create a path with that
        x = length1_list[0] # Pick a vertex with only one neighbor.
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
                print("Final Answer: {0}".format(current_path))
                finalcount += 1 # We have found a solution
            #if len(current_path) > 0.90*num:
            #    print("Searching long path...")
            
            point = current_path[-1] # Take the last vertex of the current path
            # Find all numbers that can follow the value point
            for neighbor in sum_tetra_dict[point]:
                if neighbor not in current_path: # If the neighbor number hasn't been used yet...
                    new_path = list(current_path) # Make a new path based on the current path
                    new_path.append(neighbor) # Add the neighbor point to the new path
                    path_list.append(new_path) # Add the new path to the list
                # Else, that point is already in the list
            # End for neighbor...
            loop += 1 # Add one to loop counter
            # Go back and check the next path
        # End while path_list
        end_time = time.time()
        print("Time of search: {0:.3f} seconds".format(end_time-start_time))
        print("Number of loops: {0}".format(loop))
        #print(" Total paths found after searching vertex {0}: {1}".format(x, finalcount))
        
        print("Sum-Square Sequences of Length {0}: {1}".format(num, finalcount))

        finalcount_number.append(finalcount)
        seq_length = list(range(1,len(finalcount_number)+1))
        
    # End if len(length1_list)...

    with open(data_label, "w+") as f:
        f.write(str(finalcount_number))
        
# End for num in range...

plt.plot(seq_length, finalcount_number, "bo")
plt.grid(True)
plt.show() # Include to display plot


