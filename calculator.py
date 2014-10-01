print("1: Addera")
print("2: Subtrahera")
print("3: Multiplicera")
print("4: Dividera")

CHOICE = raw_input("Skriv ett nummer:")

if CHOICE == "1":
    a = input("Skriv tal a:")
    b = input("skriv tal b:")
    c = a + b
    print c

elif CHOICE == "2":
    a = input("Skriv tal a:")
    b = input("Skriv tal b:")
    c = a - b
    print c

elif CHOICE == "3":
    a = input("Skriv tal a:")
    b = input("Skriv tal b:")
    c = a * b
    print c

elif CHOICE == "4":
    a = input("Skriv tal a:")
    b = input("Skriv tal b:")
    c = a / b
    print c

else: 
 print "felaktigt nummer"
 print "\n"
