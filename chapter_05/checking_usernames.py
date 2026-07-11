current_users = ['admin', 'john_doe', 'JJJJJJJane_smith', 'charlie_brown', 'alex_jones']
lowered = list(value.lower() for value in current_users)
new_users = ['john_doe', 'jane_smith', 'pam_beesly', 'jane_smith', 'dwight_schrute']
new_lowered = list(value.lower() for value in new_users)

for  new_user in new_lowered :
    if new_user in lowered:
        print (f"{new_user} is already taken ,enter new username")
    else :
        print("username available")

print(lowered)