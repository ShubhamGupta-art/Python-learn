guest = ['ramu','shamu','pappu']

message = f"you are invited {guest[0]}"
print(message)
message = f"you are invited {guest[1]}"
print(message)

guest_not_comming = guest.pop()
message = f" {guest_not_comming }, cant make it to the dinner"
print(message)

guest.append('kaku')
message = f"you are invited {guest[2]}"
print(message)