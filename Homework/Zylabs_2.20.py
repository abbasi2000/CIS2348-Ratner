# EMAD ABBASI # 2095022
lemon_cups = int(input('Enter amount of lemon juice (in cups):'))
print()
water_cups = int(input('Enter amount of water (in cups):'))
print()
agave_cups = float(input('Enter amount of agave nectar (in cups):'))
print()
servings_first = int(input('How many servings does this make?'))
print('\n')

# converter float conversion
print('Lemonade ingredients - yields {:.2f} servings'.format(servings_first))
print('{:.2f} cup(s) lemon juice'.format(lemon_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(agave_cups))
print()

# converter calculation
required_servings = int(input('How many servings would you like to make?'))
print('\n')
print('Lemonade ingredients - yields {:.2f} servings'.format(required_servings))
serv_formula = required_servings / servings_first
lemon_cups = serv_formula * lemon_cups
water_cups = serv_formula * water_cups
agave_cups = serv_formula * agave_cups
print('{:.2f} cup(s) lemon juice'.format(lemon_cups))
print('{:.2f} cup(s) water'.format(water_cups))
print('{:.2f} cup(s) agave nectar'.format(agave_cups))
print()

# gallon conversion
gallons_required_lemon = lemon_cups / 16
gallons_required_water = water_cups / 16
gallons_required_agave = agave_cups / 16

# final output
print('Lemonade ingredients - yields {:.2f} servings'.format(required_servings))
print('{:.2f} gallon(s) lemon juice'.format(gallons_required_lemon))
print('{:.2f} gallon(s) water'.format(gallons_required_water))
print('{:.2f} gallon(s) agave nectar'.format(gallons_required_agave))