my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("These are my favourite foods:")
for item in my_foods:
    print(item)

friend_foods.append('ice cream')

print("These are my friend's favourite foods:")
for item in friend_foods:
    print(item)