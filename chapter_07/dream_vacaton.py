locations = {}

polling_active = True

while polling_active:
    name = input("enter your name")
    response = input ("what is you dream location")

    locations[name] = response
    
    repeat = input("would you like to let another person respond(yes/no)")
    if repeat == "no":
        polling_active = False

print("Polling result")
for name ,response in locations.items():
    print(f"{name} would like to go to {response}")