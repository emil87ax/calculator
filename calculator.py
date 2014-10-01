print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")

CHOICE = raw_input("Enter the Numbers:")

if CHOICE == "1":
    a = input("Enter the value of a:")
    b = input("Enter the value of b:")
    c = a + b
    print c

elif CHOICE == "2":
    a = input("Enter the value of a:")
    b = input("Enter the value of b:")
    c = a - b
    print c

elif CHOICE == "3":
    a = input("Enter the value of a:")
    b = input("Enter the value of b:")
    c = a * b
    print c

elif CHOICE == "4":
    a = input("Enter the value of a:")
    b = input("Enter the value of b:")
    c = a / b
    print c

else: 
 print "Invalid Number"
 print "\n"
