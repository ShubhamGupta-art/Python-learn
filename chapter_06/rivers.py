# Dictionary of rivers and the countries they flow through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'United States',
    'Danube': 'Germany',
    'Ganges': 'India',
    'Volga': 'Russia',
    'Mekong': 'Vietnam',
    'Thames': 'United Kingdom',
    'Rhine': 'Netherlands'
}

# Print the dictionary
for river,country in rivers.items():
    print(f"\n The {river} runs through {country}")
    
for river in rivers.keys():
    print(f"\n{river}")

for country in rivers.values():
    print(f"\n{country}")