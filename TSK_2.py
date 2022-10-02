def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
        except:
            print("Число введено неправильно.")

def Multiplication(number):            
    dict = {}
    key = 1
    result = ""
    for i in range(1, number + 1):
        key *= i
        result += str(i) + "*"
        dict[key] = result
    key = 1
    for i in range(1, number + 1):
        key *= i
        dict[key] = dict[key][:-1]
    print(dict)

Multiplication(CheckNumbers("Введите число N:"))