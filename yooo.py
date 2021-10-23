#ask if you want to add to a list or recive fromt he list
#if add, call a function that adds your input to a list
#if recive, print a random item from the list using listx[rnd.randrange(int(len(listx))-1, int(len(listx)))]
import random as rng
x = True
lista = [] #cum, yes, no

def cum(nigger):
    lista.append(nigger)

def cum2():
    print(lista[rng.randrange(int(len(lista))-1, int(len(lista)))])

    

while x == True:
    print("Do you want to add or receive the item?")
    response = input()
    if (response == "add"):
        print("You little bitch what do u want to add papa?")
        pig = input()
        cum(pig)
    elif (response == "receive"):
        cum2()
        x = False




