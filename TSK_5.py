import random
import datetime
def Comparizon(number):
    timeStart = int(datetime.datetime.now().strftime('%f'))

    array1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    array2 = []
    trueFalse = [True, False]
    expression1 = ""
    expression2 = ""
    expression1logical = ""
    expression2logical = ""

    for i in range(number):
        array2.append(random.choice(trueFalse))

    for j in range(number):
        expression1 = expression1 + str(array1[j]) + " or "
        expression1logical = expression1logical + str(array2[j]) + " or "
        expression2 = expression2 + "not " + str(array1[j]) + " and "
        expression2logical = expression2logical + "not " + str(array2[j]) + " and "

    expression1 = expression1[:-4]
    expression1 = "not(" + expression1 + ")"
    expression1logical = expression1logical[:-4]
    expression1logical = "not(" + expression1logical + ")"
    expression2 = expression2[:-5]
    expression2logical = expression2logical[:-5]
    expressionPrint1 = expression1logical.replace("not", "¬")
    expressionPrint1 = expressionPrint1.replace("or", "⋁")
    expressionPrint2 = expression2logical.replace("not", "¬")
    expressionPrint2 = expressionPrint2.replace("and", "⋀")

    print(f"Сгенерировано выражение 1: {expression1}.")
    print(f"Подставлены случайные предикаты: {expression1logical}.")
    print(f"Сгенерировано выражение 2: {expression2}.")
    print(f"Подставлены случайные предикаты: {expression2logical}.")

    if bool(expression1logical) == bool(expression2logical):
        print(f"Утверждение {expressionPrint1} = {expressionPrint2} верно.")
    else:
        print(f"Утверждение {expressionPrint1} = {expressionPrint2} не верно.")

    timeEnd = int(datetime.datetime.now().strftime('%f'))
    print(f"Время выполнения цикла: {(timeEnd - timeStart) / 1000} мс.")
    input('Нажмите "Enter" для продолжения.')
    print()

for i in range(10):
    print(f"Сравнение {i + 1}: ")
    Comparizon(random.randint(5, 11))