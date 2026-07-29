prompt = "enter a series of pizza toppings"
prompt += "to stop enter quit : "

flag = True

while flag:
    topping = input(prompt)
    if topping.lower() == "quit":
        flag = False
    else:
        print(f"i will add {topping} to your pizza")