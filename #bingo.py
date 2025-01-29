#bingo
import random
#------------------------------presets-------------------------------------

wincondition = 0
x = 0
y = (0, 0)
z = (0, 0)
dificuldade = -1
player1 = "waiting"
player2 = "waiting"
numbers = 10
player1tab = (0, 1)(2, 3)
player2tab = (1, 2)(3, 4)

p1adder = 0
p2adder = 0
#------------------------------dificuldade---------------------------------

print("selecione a velocidade do jogo, 1 para rapido e 2 para normal")

dificuldade = input()

if dificuldade == 1:
    print("rapido")
    x = 3
elif dificuldade == 2:
    print("normal")
    x = 5
else:
    print("so you have chosen death")
    x = 9

player1 = x
player2 = x
numbers *= x
p1adder = x
p2adder = x

player1tab [0][0] = random.radint(0, numbers)
player1tab [0][1] = random.radint(0, numbers)
    
player2tab [0][0] = random.radint(0, numbers)
player2tab [0][1] = random.radint(0, numbers)

while x!= 0:
    y[0][0] = random.randint(0, numbers)
    y[0][1] = random.randint(0, numbers)
    z[0][0] = random.randint(0, numbers)
    z[0][1] = random.randint(0, numbers)
    if y not in player1tab and p1adder != 0:
        player1tab.add(y)
        x -= 0.5
        p1adder -= 1
    if z not in player2tab and p2adder != 0:
        player2tab.add(z)
        x -= 0.5
        p2adder -= 1




#----------------parte que deixa o jogo rodando---------------------------
while wincondition == 0:
    if player1 == 0:
        wincondition += 1
    if player2 == 0:
        wincondition += 2
    print (x)