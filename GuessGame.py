from random import randint
import math

rightNum=0;          totalTries=0;      score=0;    level=1;    

def randnomNumGenerator(sc):
    global rightNum;   rightNum=randint(0,(level)*10)

def intro():
    print("Welcome to MOSGuess game \t .... Mohamed Osama Saleh .... \t")
    print("You are allowed to ask three questions about the unknown number from the following then guess the number")
    print("NOTE: The same question is allowed & the unknown number is donated by X\n")
    questionsVariety()

def questionsVariety():
    print("\t1]Is it divisible by specific number \n\t2]Is it prime number")
    print("\t3]Is it greater or smaller than specific number")
    print("\t4]Is it even or odd number \n\t5]Does it's square root is integer\n\n")

def isDivisbleBy(x):
    if rightNum%x==0:
        return "X is divisible by {y}".format(y=x)
    else:
        return "X isn't divisible by {y}".format(y=x)
        
def isPrime():
    if rightNum==0 or rightNum==1:
        return "X isn't prime number"
    for i in range(2,rightNum):
        if rightNum%i==0:
            return "X isn't prime number"
    return "X is prime number"

def isEvenVsOdd():
    if rightNum%2==0:
        return "X is even number"
    else:
        return "X is odd number"

def isGreaterVsSmaller(x):
    if rightNum>x:
        return "X is greater than {y}".format(y=x)
    else:
        return "X isn't greater than {y}".format(y=x)
    
def haveIntSquareRoot():
    if rightNum%math.sqrt(rightNum)==0:
        return "Yes it's square root is an integer"
    else:
        return "No it's square root isn't an integer"

def questionDecider(x):
    if x==1:
        y=input("Enter the number you want to check whether X is divisible by or not:  "); print(isDivisbleBy(int(y)))
    elif x==2:
        print(isPrime())
    elif x==3:
        y=input("Enter the number you want to whether X is greater or smaller than:  "); print(isGreaterVsSmaller(int(y)))
    elif x==4:
        print(isEvenVsOdd())
    elif x==5:
        print(haveIntSquareRoot())
    else:
        y=input("Enter only a number from 1 to 5:\n");   questionDecider(int(y))
   
def answerIsCorrect(x):
    global totalTries;    global score;   global level;   peak=3
    if x==rightNum:
        print("You guess is correct");     score+=1;  level+=1;
    else:
        print("You guess isn't correct; The correct number was {rN}".format(rN=rightNum))
    totalTries+=1;
   
def continueCheck():
    x=input("\nDo you want to continue [Y/N]\t")
    if x=='Y' or x=='y':
        print("\n\n");  questionsVariety();    gamePlay()
    else:
        print("\n\nYour total score is {sc}/{tT}".format(sc=score,tT=totalTries))
  
def gamePlay():
    global peak;   peak=3
    randnomNumGenerator(score);     print("\nYou are in LEVEL {l} ; X is between 0 & {p}".format(l=level,p=level*10))
    if score%3==0 and score!=0:
        peak+=1;       print("\n*** You current questions are {sc}, GOOD LUCK ***\n".format(sc=peak))
    for i in range(peak):
        z=input("\n\n\nChoose which question you want to ask:\n");   questionDecider(int(z))
        
    y=input("\n\nWhat is your guess: ");       answerIsCorrect(int(y));
    continueCheck();        print("\n\n")
    
intro()
gamePlay()