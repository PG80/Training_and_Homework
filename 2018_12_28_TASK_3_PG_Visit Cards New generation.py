# 2018.12.28. TASK_3_PG_Visit Cards New generation

#We_have_initial_data_from_famous_people )))
#Poroshenko
#Groysman
#Klichko
#Pupkin

person_data_001 = {'country': 'Ukraine', 'company': 'Government', 'position': 'President', 'first_name': 'Petro', 'last_name': 'Poroshenko', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557333', 'mobile_phone': '+380503108911'}
person_data_002 = {'country': 'Ukraine', 'company': 'Government', 'position': 'Prime_minister', 'first_name': 'Volodymyr', 'last_name': 'Groysman', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557334', 'mobile_phone': '+380503108912'}
person_data_003 = {'country': 'Ukraine', 'company': 'Government', 'position': 'Head_of_city', 'first_name': 'Vitaly', 'last_name': 'Klichko', 'address': ['Bankova_Street', '11', 'Kyiv', '02000'], 'phone': '+380442557335', 'mobile_phone': '+380503108913'}
person_data_004 = {'country': 'Ukraine', 'company': 'Private', 'position': 'Head_of_the_Planet_earth', 'first_name': 'Leonid', 'last_name': 'Pupkin', 'address': ['Goloseevska_Street', '13', 'Kyiv', '03039'], 'phone': '+380441111111', 'mobile_phone': '+380674314438'}

userInput = input("Would you like to start a new visit card? Print_please_yes_or_no: ")

if userInput == 'no':
    print ('We_work_only_with_visit_cards_and_thanks_for_your_time))) Good luck!')

if userInput == 'yes':
    print ('Excellent!')
    userInput = input("Would you like to start create a new visit card? (Print_please: new) or use existing information (Print_please: existing): ")

    if userInput == 'existing':
        print('Ok_we_need_to find_information')
        userInput = input("Print_please_yours_last_name: ")

        if userInput == (person_data_001 ['last_name']):
            print('We_have_your_data, check please')
            print(person_data_001['country'])
            print(person_data_001['company'])
            print(person_data_001['position'])
            print(person_data_001['first_name'])
            print(person_data_001['last_name'])
            print(person_data_001['address'])
            print(person_data_001['phone'])
            print(person_data_001['mobile_phone'])
            print('We_load_your data_to_our_system')

        if userInput == (person_data_002['last_name']):
            print('We_have_your_data, check please')
            print(person_data_002['country'])
            print(person_data_002['company'])
            print(person_data_002['position'])
            print(person_data_002['first_name'])
            print(person_data_002['last_name'])
            print(person_data_002['address'])
            print(person_data_002['phone'])
            print(person_data_002['mobile_phone'])
            print('We_load_your data_to_our_system')

        if userInput == (person_data_003['last_name']):
            print('We_have_your_data, check please')
            print(person_data_003['country'])
            print(person_data_003['company'])
            print(person_data_003['position'])
            print(person_data_003['first_name'])
            print(person_data_003['last_name'])
            print(person_data_003['address'])
            print(person_data_003['phone'])
            print(person_data_003['mobile_phone'])
            print('We_load_your data_to_our_system')

        if userInput == (person_data_004['last_name']):
            print('We_have_your_data, check please')
            print(person_data_004['country'])
            print(person_data_004['company'])
            print(person_data_004['position'])
            print(person_data_004['first_name'])
            print(person_data_004['last_name'])
            print(person_data_004['address'])
            print(person_data_004['phone'])
            print(person_data_004['mobile_phone'])
            print('We_load_your data_from_our_system')

            print('Please_order_and_within_15_minutes_your_business_cards_will_be_ready')


    if userInput == 'new':
        print ('Ok_we_can_create_new. Please, print your data')

        country = userInput = input("country: ")
        company = userInput = input("company: ")
        position = userInput = input("position: ")
        first_name = userInput = input("first_name: ")
        address = userInput = input("address: ")
        phone = userInput = input("phone: ")
        mobile_phone = userInput = input("mobile_phone: ")

        print('We_load_your_data')
        print('country: ' + country)
        print('company: ' + company)
        print('position: ' + position)
        print('first_name: ' + first_name)
        print('address: ' + address)
        print('phone: ' + phone)
        print('mobile_phone: ' + mobile_phone)
        print('Please_order_and_within_15_minutes_your_business_cards_will_be_ready')