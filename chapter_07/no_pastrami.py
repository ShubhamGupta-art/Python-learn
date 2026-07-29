sandwich_orders = ["tuna", "chicken", "veggie", "ham", "turkey", "pastrami", "pastrami", "pastrami", "pastrami"]
finished_sandwich = []

print("we have ran out of pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while len(sandwich_orders)>0 :
        item = sandwich_orders.pop()
        print(f"I made your {item} sandwich")
        finished_sandwich.append(item)
        

print(sandwich_orders)
print(finished_sandwich)
