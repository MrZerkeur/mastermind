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
        userColor = input("Choisir couleur "+str(i+1)+" : ")
        userTry.append(userColor)

    if code == userTry:
        print("Congratulations, you win")
    else:
        colorPos(userTry)

def colorPos(userTry):
    ColorIn = 0
    ColorInGoodPos = 0
    for i in range(len(userTry)):
        if userTry[i] == code[i]:
            ColorInGoodPos += 1
        if userTry[i] in code:
            ColorIn += 1
    print("Vous avez "+str(ColorIn)+" couleurs présentes")
    print("Vous avez "+str(ColorInGoodPos)+" couleurs bien placées")
    
userTurn()