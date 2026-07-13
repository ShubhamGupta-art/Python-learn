# A dictionary of programming concepts and their meanings
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'list': 'A collection of items stored in a specific order.',
    'dictionary': 'A collection of key-value pairs used to store data.',
    'tuple': 'An immutable sequence of values.',
    'set': 'A collection of unique items.',
    'class': 'A blueprint for creating objects.',
    'object': 'An instance of a class.',
    'module': 'A file containing Python code that can be imported and used in other programs.'
}

for word, meaning in glossary.items():
    print(f"{word.title()} : {meaning}")