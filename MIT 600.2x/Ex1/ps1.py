###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    copy_cow = cows.copy()
    all_cow_list = []
    while len(copy_cow) != 0:
        full_house = False
        this_trip_list = []
        current_limit = limit
        continute_flag = False
        while not full_house:
            if not continute_flag:
                i = 0
            cow_weight = sorted(copy_cow.values(), reverse = True)
            #print(i)
            #print(cow_weight)
            try:
                taken_weight = cow_weight[i]
            except IndexError:
                break
            #print(taken_weight)
            for key in copy_cow.keys():
                if copy_cow[key] == taken_weight:
                    current_limit -= taken_weight
                    if current_limit > 0:
                        this_trip_list.append(key)
                        copy_cow.pop(key)
                    elif current_limit == 0:
                        this_trip_list.append(key)
                        copy_cow.pop(key)
                        full_house = True
                    else:
                        current_limit += taken_weight
                        continute_flag = True
                        i += 1
                    break
            if len(copy_cow) == 0:
                break
        all_cow_list.append(this_trip_list)
    return all_cow_list


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    copy_cow = cows.copy()
    cow_names = copy_cow.keys()
    min_number_of_trip = len(cow_names)
    for trips in get_partitions(cow_names):
        is_possible = True
        number_of_trip = len(trips) + 1
        for trip in trips:
            weight = 0
            for name in trip:
                weight += copy_cow[name]
            if weight > limit:
                is_possible = False
                break
        if number_of_trip < min_number_of_trip and is_possible == True:
            min_number_of_trip = number_of_trip
            result = trips
    return result

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start_greedy = time.time()
    greedy_cow_transport(cows, limit)
    end_greedy = time.time()
    print(end_greedy - start_greedy)
    
    start_brute = time.time()
    brute_force_cow_transport(cows, limit)
    end_brute = time.time()
    print(end_brute - start_brute)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=80
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


