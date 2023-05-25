# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 08:34:08 2020

@author: CFast
"""

import random
class Player():
    def __init__(self,hand=None):
        if hand==None:
            self.hand=[]
        else:    
            self.hand=hand

class Human(Player):
    def __init__(self,balance,hand):
        Player.__init__(self,hand)
        self.balance=balance
        
class Dealer(Player):
    def __init__(self,hand):
        Player.__init__(self,hand)

def hit(Player):   
    Player.hand.append(Deck.pop(0))

def stay(Player,Dealer,bet):
    dealerturn(Player,Dealer,bet)


def calculatesumofhand(Player):
    s=0
    for i in Player.hand:
        if i=="Jack" or i=="King" or i=="Queen":
            s=s+10
        elif i=="Ace":
            while True:
                print(Player.hand)
                new=int(input("What do u want the Ace to be 1 or 11  ?" ))
                if new==1 or new==11:
                    s=s+new
                    ss=Player.hand.index(i)
                    Player.hand[ss]=new
                   
                    break
                else:
                    continue
        else:
            s=s+i
    print(Player.hand)            
    #print(s)
    return s

def checkstateofplayer(Player):
    if calculatesumofhand(Player)>21:
        return "Bust"
    else:
        return "Still Going"
   
def choiceoftheplayer(Player,Dealer,bet):   
    while True:
        choice=input("Do u want to Hit or Stay ?  " )
        if choice.upper()=="HIT" or choice.upper()=="STAY":
            if choice.upper()=="HIT":
                hit(Player)
                print(Player.hand)
                stateofgame=checkstateofplayer(Player)
                if stateofgame=="Still Going":
                    choiceoftheplayer(Player,Dealer,bet)
                    break
                else:
                    print("You Have Lost the Game and Lost ur Money")  
                  #  Player.balance=Player.balance-bet
                    break
            else:
                stay(Player,Dealer,bet)
                break

                           
                    
def dealerturn(Human,Dealer,bet):         
    stateofdealer=checkstateofplayer(Dealer)
    #print(Dealer.hand)
    print(stateofdealer)
    sumofhuman=calculatesumofhand(Human)
    if stateofdealer=="Still Going":
       if calculatesumofhand(Dealer)>sumofhuman:
            print("You Have Lost the Game and Lost ur Money")
           # Human.balance=Human.balance-bet
       else:
           hit(Dealer)
           dealerturn(Human,Dealer,bet)
    else:
        Human.balance+=bet*2
        print("You have won the game the dealer busted")
        
           
Deck=["Ace",2,3,4,5,6,7,8,9,10,"Jack","King","Queen"]*4
random.shuffle(Deck)          


def Game():
    human1=Human(100,[])
    while human1.balance>0: 
        human1=Human(human1.balance, [])
        dealer1=Dealer([])
        human1.hand.append(Deck.pop(0))
        human1.hand.append(Deck.pop(0))
        dealer1.hand.append(Deck.pop(0))
        dealer1.hand.append(Deck.pop(0))
        while True:
            bet=int(input("Please Enter Ur Bet"))
            if bet>human1.balance:
                continue
            else:
                human1.balance=human1.balance-bet
                break
        print("Your Hand          |||     Dealer Hand and 1 Hidden")
        print(f"{human1.hand}            |||            {dealer1.hand[0:len(dealer1.hand)-1]}")
        choiceoftheplayer(human1,dealer1,bet)
        print(human1.balance)




Game()      

        
                
                
                
                
                
                
                
                
                
                
                
                