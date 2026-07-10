pizzas = ["margrita","corn","onion"]
friend_pizzas = pizzas[:]

pizzas.append("chicken")
friend_pizzas.append("pepperoni")

print("my favourite pizzas are:")
for pizza in pizzas:
    print(f"I linke {pizza} pizza.")

print("my friends favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"Friend linke {pizza} pizza.")