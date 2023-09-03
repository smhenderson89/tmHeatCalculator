# Tracker to use while playing single player Terraforming Mars Game
# Goal:
# Keep track of user income, resources, generations
# Determine when one track will fullfill by itself without needing additional help
# Based on current resource, will complete game by Generation 14?


# Intialize Tracker

import re

#Max Values
max_temp = 8
max_oxygen = 14
max_ocean = 9
max_generation = 14

#Stating Values
start_temp = -30
start_oxygen = 0
start_ocean = 0

#Starting Currencies
mc_resource = 0
mc_production = 0
steel_resource = 0
steel_producton = 0
titanium_resource = 0
titanium_producton = 0
plant_resource = 0
plant_production = 0
energy_resource = 0
energy_producton = 0
heat_resource = 0
heat_production = 0
t_rating = 0

start_generation = 1
game_over = False

grid_spacing = 6 # Spacing for grid

currency_list = ['MC','Steel','Titan','Plant','Energy','Heat']

resource_list = [mc_resource, steel_resource, titanium_resource,
                 plant_resource, energy_resource, heat_resource]

production_list = [mc_production, steel_producton, titanium_producton,
                   plant_production, energy_producton, heat_production]

#Intialize grid resources into two sets of lists that can be access from random memory

PrepDone = False # Initialize the game with the current cuurency

# Ask User for Intial Board State
#Intialize Values:

# Show types of resources, amount of resource and production
def production_grid():
    global mc_resource
    global mc_production
    global steel_resource
    global steel_producton
    global titanium_resource
    global titanium_producton
    global plant_resource
    global plant_production
    global energy_resource
    global energy_producton
    global heat_resource
    global heat_production
    global t_rating

    # Print out table using individaul varaiable names, making a list will cause too many issues down the road
    print('Type:'.center((grid_spacing-1),'*'),end=' ')
    for i in range(0,6):
        print(str(currency_list[i]).center(grid_spacing,'-'),end='|')
    print('\nProd:'.center(grid_spacing,'*'), end=' ')
    print(str(mc_production).center(grid_spacing, '-'), end='|')
    print(str(steel_producton).center(grid_spacing, '-'), end='|')
    print(str(titanium_producton).center(grid_spacing, '-'), end='|')
    print(str(plant_production).center(grid_spacing, '-'), end='|')
    print(str(energy_producton).center(grid_spacing, '-'), end='|')
    print(str(heat_production).center(grid_spacing, '-'), end='|')
    print('\n# of:'.center(grid_spacing,'*'), end=' ')
    print(str(mc_resource).center(grid_spacing,'-'),end='|')
    print(str(steel_resource).center(grid_spacing, '-'), end='|')
    print(str(titanium_resource).center(grid_spacing, '-'), end='|')
    print(str(plant_resource).center(grid_spacing, '-'), end='|')
    print(str(energy_resource).center(grid_spacing, '-'), end='|')
    print(str(heat_resource).center(grid_spacing, '-'), end='|')

production_grid()
# TODO: Create index to interpret inputs from user to upgrade resources sheet
    # TODO: Identity which commands that I want to implement to change in the resources sheet
        # TODO: MR #, MP # (Mega-credits resource and production)
        # TODO: SR #, SP # (Steel creits/production)
        # TODO: TR #, TP #
        # TODO: PR #, PP #
        # TODO: ER #, EP #
        # TODO: HR #, HP #
while PrepDone == False:
    print('\nIs this grid correct? Y or N')
    response = input()
    if response == 'Y':
        PrepDone = True
    if response == 'N':
        print('What values need to be changed?')
        response = input()
        # Update grid with correct values

        # TODO: Use Regex to determine which command is being used from first two letters
        # TODO: Example input = 'mr 1' -> Mega Credits Resources + 1
        # TODO: Use a switcher-method to determine specific case within
        # TODO: https://jaxenter.com/implement-switch-case-statement-python-138315.html (Use dictionary mapping for
        # TODO: function
        if response == 'mr1':
            # Look at way to update the variables in the table by their name
            # Update the variable name and the list of variables to be correct
            mc_resource = mc_resource + 1# increase Mega Credits resource by 1
            production_grid()
