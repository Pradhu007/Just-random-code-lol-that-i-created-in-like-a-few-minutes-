import random



characters = ['A','B',"C"]
numbers = [1,2,3,4,5,6,7]

test = ''
while True:
    characterrand = random.choice(characters)
    numbersrand = random.choice(numbers)

    if len(test) != 4:
        test = test + characterrand + str(numbersrand)
    else:
        break
print(test)

# Creates a 4 digit number plate number which is random hahahah
