import random

def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
        except:
            print("Число введено неправильно.")

def ListCreate(number):
    array = []
    for i in range(number):
        array.append(random.randint(1, 9))
    return array

def ListShuffle(arrayIn):
    chosenIndexArray = []
    arrayOut = []
    for i in range(len(arrayIn)):
        while True:
            tempIndex = random.randrange(len(arrayIn))
            if tempIndex not in chosenIndexArray:
                arrayOut.append(arrayIn[tempIndex])
                chosenIndexArray.append(tempIndex)
                break
    return arrayOut

array1 = ListCreate(CheckNumbers("Введите число элементов в массиве:"))
print(array1)
array2 = ListShuffle(array1)
print(array2)