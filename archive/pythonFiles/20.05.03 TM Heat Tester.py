# TODO: Determine all numbers that each number is divisible by as a test for Terraforming Mars

# For a given range,
    # Test numbers in sequence from 1 to the number itself that the number will have interger division equally
    # Example: 8 -> 1, 2, 4 Not 3, 5, 6, 7

start_num = int(input('Type a number a beginning of range'))
end_num = int(input('Type a number at end of range'))
num_range = (start_num, end_num, 1)
print('Range is ' + str(start_num) + ' to ' + str(end_num))
dict = {}
divisible = []

#TODO: Determine lenght of a list without having to actually create the list
# Example:

# list = []
# for i in range(4,12,3):
#   list.append(i):
#   len(list)


# Iterable for all numbers from 1-input

for i in range(0, len(num_range)): # For each number in a list
    divisible = [] # Reset dvisible list to be empty at start of the loop
    for j in range(1, len(num_range)): # For number, checking intergers 1 thru - number in range
        if (num_range[i] % j) == 0: # Check what numbers divide evenly into the number
            divisible.append(j) # add divisible numbers to a list
    if len(divisible) > 1: # If the number is divisible by more than just 1
        # Add number and it's divisible to a dictionary
        dict.setdefault(num_range[i], divisible)

# Display numbers sequentially
print(dict)

