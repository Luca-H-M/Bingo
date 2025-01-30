#bingo funfa
import random
#------------------------------presets-------------------------------------

wincondition = 0
x = 0
y = 0
z = 0
dificuldade = -1
player1 = "waiting"
player2 = "waiting"
numbers = 10
player1tab = [1]
player2tab = [3]

p1adder = 0
p2adder = 0

numberslist = [0]
#------------------------------dificuldade---------------------------------

print("selecione a velocidade do jogo, 1 para rapido e 2 para normal")

dificuldade = input()

if dificuldade == "1":
    print("rapido")
    x = 3
elif dificuldade == "1":
    print("normal")
    x = 5
else:
    print("so you have chosen death")
    x = 9

player1 = x
player2 = x
numbers *= x

x = x*x
p1adder = x
p2adder = x
player1 = x
player2 = x

player1tab [0] = random.randint(0, numbers)
player1tab [0] = random.randint(0, numbers)
    
player2tab [0] = random.randint(0, numbers)
player2tab [0] = random.randint(0, numbers)

while x!= 0:
    y = random.randint(0, numbers)
    y = random.randint(0, numbers)
    z = random.randint(0, numbers)
    z = random.randint(0, numbers)
    if y not in player1tab and p1adder != 0:
        player1tab.append(y)
        x -= 0.5
        p1adder -= 1
    if z not in player2tab and p2adder != 0:
        player2tab.append(z)
        x -= 0.5
        p2adder -= 1

x = int(x)
while x != numbers:
    x += 1
    numberslist.append(x)
#----------------parte que deixa o jogo rodando---------------------------
while wincondition == 0:
    print (player1tab)
    print(player2tab)
    x = input("aperte enter para continuar")
    x = random.randint(0, numbers)
    if x in numberslist:
        print(x)
        numberslist.remove(x)
        if x in player1tab:
            y = player1tab.index(x)
            player1tab[y] = f'({x})'
            player1 -= 1
        if x in player2tab:
            z = player2tab.index(x)
            player2tab[z] = f'({x})'
            player2 -= 1
    if player1 == 0:
        wincondition += 1
    if player1 == 0:
        wincondition += 2

print(player1tab)
print(player2tab)