
flag = True

while flag :
    age = input("enter your age : ")
    
    if age == "quit":
        break
    age = int (age)
    if age < 3:
        print("ticket is free")
    elif age >=3 and age < 12 :
        print("ticket is 10 rupee")
    else:
        print("ticket is 15 rupee")