squares = []

for num in range(0,11):
    # squ = num**2
    # squares.append(squ)
    squares.append(num**2)


print(squares)


comprehension_list_of_squares = [value**2 for value in range(0,11)]
print(comprehension_list_of_squares)