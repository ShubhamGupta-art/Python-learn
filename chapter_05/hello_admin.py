# usernames = ['admin', 'john_doe', 'jane_smith', 'alice', 'bob']
usernames = []

if usernames:
    for user in usernames :
        if user == 'admin':
            print("hello admin, would you like to see a status report?")
        else :
            print(f"Hello {user} ,thank you for logging in again")
else :
    print("We need to find some users")