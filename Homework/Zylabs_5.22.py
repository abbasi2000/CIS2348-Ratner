# EMAD ABBASI # 2095022
# dictionary
services_cost = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
# first menu
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

# prompt
first_service = str(input('Select first service:'))
print(first_service)
second_service = str(input('Select second service:'))
print(second_service)

# invoice
print("Davy's auto shop invoice")
print('Service 1:', first_service, '$', services_cost[first_service])
print('Service 2:', second_service, '$', services_cost[second_service])

# adding to the dictionary
services_cost['no service'] = "-"

total_cost = services_cost[first_service] + services_cost[second_service]

print('Total:', "$", total_cost)


