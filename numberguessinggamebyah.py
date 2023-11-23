#no. guessing game by <A/H>
import random
print("welcome  to number guessing game -by<A/H>")
print("let's start")
print("hint:the no. is in range (0,100)")
def game():
    num=random.randint(0,100)
    while True:
        a=int(input("guess the no:"))

        if a<num:
            print("opps!,your no. is too low")
        if a>num:
            print("try again!,your no. is too high ")
        if a==num:
            print('Bravo! , you got it ')
            break

game()
