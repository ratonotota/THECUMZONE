import random as rnd
x = True    
response = ""
response2 = ""

def rolldice(guess):
    numb = rnd.randrange(1,6)
    print("the dice rolled " +  str(numb) + " while you guessed " + str(guess))



while x == True:
    print("Want to roll again?")
    response = input()
    if (response == "yes"):
        print("guess the number : ")    
        guessN = input()
        rolldice(int(guessN))
    else:
        print("bye then")
        x == False


        

         


        







