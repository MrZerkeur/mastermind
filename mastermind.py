import random

couleurs = ["rouge","jaune","vert", "bleu", "blanc", "orange", "violet", "rose"]
turnLeft = 12

code = []
for i in range(4): 
    num = random.randint(0,7)
    code.append(couleurs[num])

print(code)



def userTurn():
    userTry = []
    for i in range(4): 
        userColor = input("Choisir couleur : ")
        userTry.append(userColor)

    if code == userTry:
        print("yes")
    else:
        print("no")

userTurn()