gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Do you like Dawn or Dusk, 1 for dawn, 2 for dusk')
answer = int(input('Enter a number 1-4: '))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input')


print("When I'm dead I want people to remember me as: ")
answer = int(input('1. The Good, 2. The Great, 3. The Wise, 4. The Bold: '))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong input')

print('Which kind of instrument most pleases your ear?')
answer = int(
    input('1. The violin, 2. The trumpet, 3. The piano, 4. The drum: '))

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print('Wrong input')

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print('You belong to: ')
if gryffindor == most_points:
    print('Gryffindor')
elif ravenclaw == most_points:
    print('Ravenclaw')
elif hufflepuff == most_points:
    print('Hufflepuff')
elif slytherin == most_points:
    print('Slytherin')
