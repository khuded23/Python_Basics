import random
names = []
while True:
	name = input("Enter a name,type'done' when you are finished:")
	if name == 'done':
		break
	else:
		names.append(name)
print("randomizing the names provided")
for item in (random.sample(names,k=len(names))):
	print(item)

#commit to new branch