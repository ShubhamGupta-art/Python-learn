my_foods = ['pizza', 'falafel', 'carrot cake', 'tacos', 'sushi', 'burger', 'pasta']

print("The first three items in the list are:")

for item in my_foods[:3]:
    print(item)


print("Three items from the middle of the list are:")

for item in my_foods[2:5]:
    print(item)


print("The last three items in the list are:")
for item in my_foods[-3:]:
    print(item)