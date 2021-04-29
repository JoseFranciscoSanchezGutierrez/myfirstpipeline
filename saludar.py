import random


def saludo1():
    return "Hola Jose Francisco desde el Master de DevSecOps"


def saludo2():
    return "Buenos días mi gente del Master"


def saludo3():
    return "Hola, ¿Qué tal llevas el Master?"


saludo = random.randint(0, 2)

if saludo == 0:
    print(saludo1())
elif saludo == 1:
    print(saludo2())
elif saludo == 2:
    print(saludo3())
else:
    print("Jaque Mate")
