guest = ['ramu','shamu','pappu']



guest_not_comming = guest.pop()
message = f" {guest_not_comming }, cant make it to the dinner"
print(message)

guest.append('kaku')


guest.insert(0,'jhappu')
guest.insert(2,'tappu')
guest.append('cuppu')
print(f"you are invited {guest[0]}")
print(f"you are invited {guest[1]}")
print(f"you are invited {guest[2]}")
print(f"you are invited {guest[3]}")
print(f"you are invited {guest[4]}")
print(f"you are invited {guest[5]}")

print(guest)