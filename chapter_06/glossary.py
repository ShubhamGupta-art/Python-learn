# A dictionary of programming concepts and their meanings
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'list': 'A collection of items stored in a specific order.',
    'dictionary': 'A collection of key-value pairs used to store data.'
}

# Print the glossary
for data in glossary:
    print(f"\n{data.title()} : \n{glossary[data]}")