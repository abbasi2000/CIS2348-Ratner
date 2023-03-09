# EMAD ABBASI # 2095022
# dictionary
services_cost = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-' : "no service"}
# first menu
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()

# prompt
first_service = str(input('Select first service:'))
print()
second_service = str(input('Select second service:'))
print('\n')

service_one_cost = services_cost[first_service] if first_service != '-' else 0
service_two_cost = services_cost[second_service] if second_service != '-' else 0
# invoice
print("Davy's auto shop invoice\n")
if service_one_cost != 0:
    print('Service 1: {service}, ${cost}'.format(service = first_service, cost = services_cost[first_service]))
else:
    print('Service 1: No service')

if service_two_cost != 0:
    print('Service 2: {service}, ${cost}'.format(service = second_service, cost = services_cost[second_service]))
else:
    print('Service 2: No service')

# adding to the dictionary
total_cost = service_one_cost + service_two_cost

print()
print('Total:', "${}".format(total_cost))


