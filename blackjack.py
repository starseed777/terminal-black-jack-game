import random

suits = ["Diamonds","Hearts","Spades","Clubs"]

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10 , "King": 10, "Ace": 11}


class Card:
    
    def __init__(self, suit, value,):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + " of " + self.suit 

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit,value))

    def shuffler(self):
        random.shuffle(self.deck)
        return self.deck
    
    def dealcard(self):
        return self.deck.pop()


class Hand:
    
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.ace = 0
        
    
    def addcard(self, card):
        self.card = card
        self.hand.append(self.card)
        return self.score()


    def score(self):
        self.handValue += values[self.card.value]
        if "Ace" in str(self.card):
            self.ace += 1

        if self.handValue > 21 and self.ace > 0:
            self.handValue -= 10
            self.ace -= 1

        return self.handValue


class Money:
    def __init__(self, amount = 50000):
        self.amount = amount
        
    
    def addmoney(self, bet):
        self.bet = bet
        self.amount += self.bet

    def losemoney(self, bet):
        self.bet = bet
        self.amount -= self.bet    


def intro():
    gameplay = input(" Welcome to BlackJack! Please type in yes if you are ready to play: ").lower()
    if gameplay == ("yes"):
        return True 
    else:
        return False

def gameplay():
    if intro() == True:
        print("Great lets get started!")
    else:
        return print("Rerun the program if you wish to play, otherwise goodbye")    

    playermoney = Money()
    

    print(f"Place your bet to begin, you currently have ${playermoney.amount}")
    
    playerbet = int(input(">>>Please type in how much you are willing to bet: "))
    while playermoney.amount > 0:
        if playerbet > playermoney.amount:
            print(f"Please bid within your amount of ${playermoney.amount}")
            playerbet = int(input(">>>Please type in how much you are willing to bet: "))
            continue
        break
      
        

    
    print(f"you're betting ${playerbet}")
    print("Lets get these cards shuffled!")
    

    deck = Deck()
    deck.shuffler()

    playerhand = Hand()
    dealerhand = Hand()
    
    playerhand.addcard(deck.dealcard())
    dealerhand.addcard(deck.dealcard())

    playerhand.addcard(deck.dealcard())
    dealerhand.addcard(deck.dealcard())

    print("Here are your cards:")
    print(playerhand.hand)
    

    print("This is the Dealer's hand: ")
    print(dealerhand.hand[0], ", other card remains hidden")

    while True:

         print(f"your current score is {playerhand.handValue} and your current hand is: {playerhand.hand}")


         print("Would you like to hit or stay?")

         hitstay = input(">>>Please type hit or stay: ").lower()

         if hitstay == "stay":
             if playerhand.handValue > dealerhand.handValue:
                 print(">>>YOU ARE A WINNER WINNER WINNER WINNER WINNER<<<")
                 print(f"DEALER current score is {dealerhand.handValue} and DEALER hand is: {dealerhand.hand}")
                 playermoney.addmoney(playerbet)
                 print(f"Congrats you now have ${playermoney.amount}!!!")
                 return
             else:
                 print("OOF SORRY YOU LOSE >_<")
                 print(f"DEALER current score is {dealerhand.handValue} and DEALER hand is: {dealerhand.hand}")
                 playermoney.losemoney(playerbet)
                 print(f"Ouch you now have ${playermoney.amount} :(")
                 return
                    

         if hitstay == "hit":
             playerhand.addcard(deck.dealcard())
             print(f"you were dealt: {playerhand.hand[-1]}")
             if playerhand.handValue > 21:
                 print(f"your current score is {playerhand.handValue}")
                 print("OOF SORRY YOU LOSE >_<")
                 playermoney.losemoney(playerbet)
                 print(f"DEALER current score is {dealerhand.handValue} and DEALER hand is: {dealerhand.hand}")
                 print(f"Ouch you now have ${playermoney.amount} :(")
                 return
             continue

         else:
             break
    
    while True:

        while dealerhand.handValue < playerhand.handValue:

         if dealerhand.handValue == 21:
                print("DEALER WINS")
                playermoney.losemoney(playerbet)
                print(f"You now have ${playermoney.amount}")
                return

         if playerhand.handValue == 21:
             print(">>> YOU WIN  <<<")
             playermoney.addmoney(playerbet)
             print(f"Congrats you now have ${playermoney.amount}!!!")
             return       

         if dealerhand.handValue < 16:
            dealerhand.addcard(deck.dealcard())
            print(f"DEALER was dealt: {dealerhand.hand[-1]}")
            
            if dealerhand.handValue > 21:
                print(f"DEALER current score is {dealerhand.handValue}")
                print(">>>YOU ARE A WINNER WINNER WINNER WINNER WINNER WINNER<<< *CONGRATS* (^__^)!!!!!!!!")
                playermoney.addmoney(playerbet)
                print(f"Congrats you now have ${playermoney.amount}!!!")
                break
            continue

        else:
            break 
        
gameplay()




    
            



