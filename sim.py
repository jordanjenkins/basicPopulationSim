import random

# Initial Variables
startingPopulation = 50
## Infant Mortality Percentage
infantMortalitiy = 25
## Unit food produced per person
agriculture = 5 
disasterChance = 10
food = 0
fertilityx = 18
fertilityy = 35

peopleDictionary = []

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age

# Harvest Function

def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople += 1

    food += ablePeople * agriculture

    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary) - food)]
        food = 0
    else:
        food =- len(peopleDictionary)

# reproduce function

def reproduce(fertilityx, fertilityy):
    for person in peopleDictionary:
        if person.gender == 1 and person.age > fertilityx and person.age < fertilityy:
            if random.randint(0,5) == 1:
                peopleDictionary.append(Person(0))

# Initiate simulation
def beginSim():
    for x in range(startingPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))

def runYear(food, agriculture, fertilityx, fertilityy):
    harvest(food, agriculture)
    reproduce(fertilityx, fertilityy)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age += 1
    print len(peopleDictionary)

beginSim()

while len(peopleDictionary) < 100000 and len(peopleDictionary) > 1:
    runYear(food, agriculture, fertilityx, fertilityy)
