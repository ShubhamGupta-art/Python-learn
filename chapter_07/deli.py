sandwich_orders = ["tuna", "chicken", "veggie", "ham", "turkey"]
finished_sandwich = []


while len(sandwich_orders)>0 :
        item = sandwich_orders.pop()
        print(f"I made your {item} sandwich")
        finished_sandwich.append(item)
        

print(sandwich_orders)
print(finished_sandwich)
