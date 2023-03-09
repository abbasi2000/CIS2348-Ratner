from math import ceil

# EMAD ABBASI # 2095022
wall_height = int(input('Enter wall height (feet):'))
print()
wall_width = int(input('Enter wall width (feet):'))
print()
# the wall area and amount of paint required
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')
paint_need = wall_area / 350
print("Paint needed: {:.2f} gallons".format(paint_need))

# number of cans needed
wall_per_gallon = 350
gallons_needed = 1
if wall_area < wall_per_gallon:
    gallons_needed = 1
elif wall_area > wall_per_gallon:
    gallons_needed = paint_need
print('Cans needed:', ceil(gallons_needed), 'can(s)')
print()
# choosing a paint and its associated cost
paint_color = str(input('Choose a color to paint the wall:'))
print()
p = {'red': 35, 'blue': 25, 'green': 23}
paint_value = ceil(gallons_needed) * p[paint_color]
print(f'Cost of purchasing', paint_color, 'paint:', "${}".format(paint_value))


