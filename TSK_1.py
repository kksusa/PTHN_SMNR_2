def CheckNumbers(param):
    while True:
        try:
            number = float(input(f"{param} "))
            return number 
        except:
            print("Число введено неправильно.")

def digitsSum (number):
    intPart = int(number // 1)
    fracPart = float('%g'%(number % 1))
    sum = 0
    while (intPart > 0):
        sum += intPart % 10
        intPart //= 10
    while fracPart % 1 != 0:
        sum += fracPart * 10 // 1
        fracPart = float('%g'%(fracPart * 10 % 1))
        sum = int(sum)
    return sum

number = CheckNumbers("Введите любое вещественное или целое число:")
print(f"Сумма цифр в числе равна {digitsSum(number)}.")