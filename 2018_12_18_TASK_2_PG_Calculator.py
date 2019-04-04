# 2018.12.18. TASK_2_PG_Calculator (A_little_better)

PGCalculator = True


while PGCalculator:
   print("1. Plus")
   print("2. Minus")
   print("3. Multiplication")
   print("4. Division")
   print("5. Exponentiation")
   print("6. Clear the data")

   cmd = int(input ("Enter Your Choice From 1 to 6"))

   if cmd == 1:
       print("Plus")
       First = int(input("Enter First Number"))
       Second = int(input("Enter Second Number"))
       Result = First + Second
       print (First , '+' , Second , '=' , Result)

   elif cmd == 2:
       print("Minus")
       First = int(input("Enter first number"))
       Second = int(input("Enter Second Number"))
       Result = First - Second
       print(First, '-', Second, '=', Result)

   elif cmd == 3:
       print("Multiplication")
       First = int(input("Enter first number"))
       Second = int(input("Enter Second Number"))
       Result = First * Second
       print(First, '*', Second, '=', Result)

   elif cmd == 4:
       print("Division")
       First = int(input("Enter first number"))
       Second = int(input("Enter Second Number"))
       Result = First / Second
       print(First, '/', Second, '=', Result)

   elif cmd == 5:
       print("Exponentiation")
       First = int(input("Enter first number"))
       Second = int(input("Enter Second Number"))
       Result = First ** Second
       print(First, '**', Second, '=', Result)

   elif cmd == 6:
       print("Clear the data")