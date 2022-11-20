from colorama import init, Fore, Back, Style
init()

print("Привет, добро пожаловать в программное обеспечение для расчета Биометрии тела!")
weight = float(input("Какой у тебя вес?: "))
height = float(input("А какой у тебя рост?: "))
print("")

bmi = float("{0:2f}".format(weight / ((height / 100) * (height / 100))))

print("Ваш текущий BMI: " + str(bmi))

if(bmi <= 16):
    print("(Высокий дефицит массы тела", end = '')

if(bmi >= 16 and bmi <= 18.5):
    print("(Недостаточная масса тела", end = '')

if(bmi >= 18.5 and bmi <= 25):
    print("(Ваш вес в порядке", end = '')

if(bmi >= 25 and bmi <= 30):
    print("(Избыточная масса тела", end = '')

if(bmi >= 30 and bmi <= 35 ):
    print("(Ожирение 1 степени", end = '')

if(bmi >= 35 and bmi <= 40):
    print("(Ожирение 2 степени", end = '')

if(bmi > 40):
    print("(ожирение 3 степени (патологическое)", end = '')

print(")", end = '')
input()
    
