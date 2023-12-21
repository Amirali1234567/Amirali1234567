while True:
    a = int(input("enter a number : "))
    b = 0
    if a == 0:
        b = 1
        print(str(a) + " has " + str(b) + " digit")
    else:
        while a!=0:
            a = int(a/10) 
            b = b + 1
        print("Digits of your number is " + str(b))
