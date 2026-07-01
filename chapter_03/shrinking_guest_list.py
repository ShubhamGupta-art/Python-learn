guest = ['ramu','shamu','pappu']



guest_not_comming = guest.pop()
print(f" {guest_not_comming }, cant make it to the dinner")

guest.append('kaku')
print("Great news! I found a bigger dinner table.\n")

guest.insert(0,'jhappu')
guest.insert(2,'tappu')
guest.append('cuppu')
print(f"you are invited {guest[0]}")
print(f"you are invited {guest[1]}")
print(f"you are invited {guest[2]}")
print(f"you are invited {guest[3]}")
print(f"you are invited {guest[4]}")
print(f"you are invited {guest[5]}")

print(f"Current full list: {guest}")

print('you can invite only two people for dinner.')

person_1 = guest.pop()
print(f"sorry I can’t invite you to dinner {person_1}")
person_2 = guest.pop()
print(f"sorry I can’t invite you to dinner {person_2}")
person_3 = guest.pop()
print(f"sorry I can’t invite you to dinner {person_3}")
person_4 = guest.pop()
print(f"sorry I can’t invite you to dinner {person_4}")
print(guest)


print(f"you are still invited {guest[0]}")
print(f"you are still invited {guest[1]}")

print(guest)

del guest[0]
del guest[0]

print(guest)