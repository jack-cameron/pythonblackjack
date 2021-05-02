import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def cardprint(self):
        print(str(self.value[0]) + " of " + self.suit)

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def welcome(self):
        print("welcome, " + self.name + "!")
    def checkscore(self):
        if(self.score>21):
            return True
        return False

def generatecard():
    suits = ["hearts","spades","clubs","diamonds"]
    value = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king":10, "ace": (1,11)}
    
    num1 = random.randint(0,3)
    x = random.choice(list(value.items()))
    if(x[0]=="ace"):
        inp = input("ace: 11 or 1?: ")
        if(11 == int(inp)):
            x = ("ace", 11)
        else:
            x = ("ace", 1)
    c = Card(suits[num1], x)

    return c


def control():
    flag = True
    print("enter your name: ")
    x = raw_input()
    p1 = Player(str(x), 0)
    p1.welcome()
    p2 = Player("dealer", 0)
    while(flag):
        print("dealer's cards")
        c1= generatecard()
        c1.cardprint()
        p2.score += c1.value[1]
        c2 = generatecard()
        p2.score += c2.value[1]
        print("??????")

        print("your cards")
        c3=generatecard()
        c3.cardprint()
        p1.score += c3.value[1]
        c4=generatecard()
        c4.cardprint()
        p1.score += c4.value[1]
        while(1):
            x = raw_input("hit or stay?")
            if(x=="hit"):
                c = generatecard()
                c.cardprint()
                p1.score += c.value[1]
                if(p1.checkscore()):
                    print("bust! dealer wins")
                    print("dealer's score: " + str(p2.score))
                    print("player's score: " + str(p1.score))
                    return
            if(x=="stay"):
                break
        while(p2.score<17):
            c = generatecard()
            c.cardprint()
            p2.score += c.value[1]
        if((p1.score < p2.score) and p2.score<22):
            print(p2.name+ " wins!")
            print("dealer's score: " + str(p2.score))
            print("player's score: " + str(p1.score))
        else:
            print("player wins!")
            print("dealer's score: " + str(p2.score))
            print("player's score: " + str(p1.score))
        y = raw_input("play again? ")
        if(y == "yes"):
            p1.score = 0
            p2.score =0
        else:
            print("thanks for playing!")
            return

control()











