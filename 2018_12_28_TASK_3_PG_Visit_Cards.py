# 2018.12.28. TASK_3_PG_Visit Cards Индусский код, сорям нормально не разобрался в функциях (((

print("data_for_Visit_Cards")
print("1. country")
print("2. company")
print("3. position")
print("4. first_name")
print("5. last_name")
print("6. address")
print("7. phone")
print("8. mobile_phone")

person_data_001 = {'country': 'Ukraine', 'company': 'Government', 'position': 'President', 'first_name': 'Petro', 'last_name': 'Poroshenko', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557333', 'mobile_phone': '+380503108911'}
person_data_002 = {'country': 'Ukraine', 'company': 'Government', 'position': 'Prime_minister', 'first_name': 'Volodymyr', 'last_name': 'Groysman', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557334', 'mobile_phone': '+380503108912'}
person_data_003 = {'country': 'Ukraine', 'company': 'Government', 'position': 'Head_of_city', 'first_name': 'Vitaly', 'last_name': 'Klichko', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557335', 'mobile_phone': '+380503108913'}
person_data_004 = {'country': 'Ukraine', 'company': 'Private', 'position': 'Head_of_the_Planet_earth', 'first_name': 'Leonid', 'last_name': 'Pupkin', 'address': ['Goloseevska_Street', '13', 'Kyiv', '03039'], 'phone': '+380441111111', 'mobile_phone': '+380674314438'}

personal_data = input("Print_please_last_name: ")

if personal_data == person_data_001['last_name']:
    print(person_data_001['country'])
    print(person_data_001['company'])
    print(person_data_001['position'])
    print(person_data_001['first_name'])
    print(person_data_001['last_name'])
    print(person_data_001['address'])
    print(person_data_001['phone'])
    print(person_data_001['mobile_phone'])

if personal_data == person_data_002['last_name']:
    print(person_data_002['country'])
    print(person_data_002['company'])
    print(person_data_002['position'])
    print(person_data_002['first_name'])
    print(person_data_002['last_name'])
    print(person_data_002['address'])
    print(person_data_002['phone'])
    print(person_data_002['mobile_phone'])

if personal_data == person_data_003['last_name']:
    print(person_data_003['country'])
    print(person_data_003['company'])
    print(person_data_003['position'])
    print(person_data_003['first_name'])
    print(person_data_003['last_name'])
    print(person_data_003['address'])
    print(person_data_003['phone'])
    print(person_data_003['mobile_phone'])

if personal_data == person_data_004['last_name']:
    print(person_data_004['country'])
    print(person_data_004['company'])
    print(person_data_004['position'])
    print(person_data_004['first_name'])
    print(person_data_004['last_name'])
    print(person_data_004['address'])
    print(person_data_004['phone'])
    print(person_data_004['mobile_phone'])

if personal_data != person_data_001['last_name']:
    print('Unfortunately we did not find your last name on our list. You_need_to_print_mobile_phone')
    personal_data = input("Print_please_mobile_phone: ")


    if personal_data == person_data_001['mobile_phone']:
        print(person_data_001['country'])
        print(person_data_001['company'])
        print(person_data_001['position'])
        print(person_data_001['first_name'])
        print(person_data_001['last_name'])
        print(person_data_001['address'])
        print(person_data_001['phone'])
        print(person_data_001['mobile_phone'])


    if personal_data == person_data_002['mobile_phone']:
        print(person_data_002['country'])
        print(person_data_002['company'])
        print(person_data_002['position'])
        print(person_data_002['first_name'])
        print(person_data_002['last_name'])
        print(person_data_002['address'])
        print(person_data_002['phone'])
        print(person_data_002['mobile_phone'])

    if personal_data == person_data_003['mobile_phone']:
        print(person_data_003['country'])
        print(person_data_003['company'])
        print(person_data_003['position'])
        print(person_data_003['first_name'])
        print(person_data_003['last_name'])
        print(person_data_003['address'])
        print(person_data_003['phone'])
        print(person_data_003['mobile_phone'])

    if personal_data == person_data_004['mobile_phone']:
        print(person_data_004['country'])
        print(person_data_004['company'])
        print(person_data_004['position'])
        print(person_data_004['first_name'])
        print(person_data_004['last_name'])
        print(person_data_004['address'])
        print(person_data_004['phone'])
        print(person_data_004['mobile_phone'])
