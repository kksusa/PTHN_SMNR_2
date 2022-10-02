def CheckN():
    while True:
        try:
            number = int(input("Введите число N: "))
            if number > 0:
                return number
        except:
            print("Число введено неправильно.")

def CheckCoordinate(param):
    while True:
        try:
            number = float(input(f"{param} "))
            return number
        except:
            print("Координата введена неправильно.")

def DistanceCalculation(N):
    arrayA = []
    arrayB = []
    for i in range(N):
        arrayA.append(CheckCoordinate(f"Введите {i + 1}-ую координату точки A:"))
    for i in range(N):    
        arrayB.append(CheckCoordinate(f"Введите {i + 1}-ую координату точки B:"))
    result = 0
    for i in range(N):
        result += ((arrayB[i] - arrayA[i]) ** 2)
    return round((result ** 0.5), 2)

N = CheckN()
print(f"Расстояние между точками A и B в {N}-мерном пространстве равно {DistanceCalculation(N)}.")