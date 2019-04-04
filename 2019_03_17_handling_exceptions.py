while True:
    try:
        age = int(input('Enter your age: '))

        if age > 21:
            print('A Big answer!')

        if age < 21:
            print('A small answer!')

        if age == 21:
            print('Correct answer!')

        if age < 0:
            raise ValueError ('Incorrect age!')

    except ValueError as error:
        print('Error')
        print(error)

#    else:
#        break
    finally:
        print('Thanks anyway!')

else:
    print('Not correct answer. ')
