def employee_card(name, sex, age):
    card = []
    card.append(name)
    card.append(sex)
    card.append(age)
    return card

manager = employee_card('Pavlo', 'M', 39)
# именованный аргумент manager = employee_card(sex='M', name='Pavlo', age=27)
project_manager = employee_card('Vova', 'M', 7)
developer = employee_card('Mark', 'M', 0.25)
boss = employee_card('Natali', 'W', 38)

print('Name', manager[0])
print('Sex', manager[1])
print('Age', manager[2])

print('Name', project_manager[0])
print('Sex', project_manager[1])
print('Age', project_manager[2])

print('Name', developer[0])
print('Sex', developer[1])
print('Age', developer[2])

print('Name', boss[0])
print('Sex', boss[1])
print('Age', boss[2])
