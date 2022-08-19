from random import randint
import math

gameMatrix=[]; userMatrix=[];  score=0;

def square(x):    return x*x

def buildGameMatrix(size):
    gameMatrix.clear()
    for i in range(size):
        gameMatrix.append(randint(0,9))

def buildUserMatrix(size):
    userMatrix.clear()
    print("\nEnter {sz} answers ".format(sz=size),"\n");
    for i in range(size):
        userMatrix.append(int(input()));    
        
def printMatrix(matrix,size):
    for i in range(size):
        if (i+1)%math.sqrt(size)==0 and i!=0:
            print(matrix[i]);
        else:
            print(matrix[i],end="  ");
    return ""    

def isSimilar(matrix1,matrix2,size):
    similar=False;    wrongAns=0;
    for i in range(size):
        if matrix1[i]!=matrix2[i]:
            wrongAns+=1
    if wrongAns==0:     
        similar=True;
    scoreCalculator(size-wrongAns,wrongAns)
    return similar

def scoreCalculator(right,wrong):
    global score;    score+=(right-wrong);
    
def printScore():
    print("Your current score is {sc}".format(sc=score))
    
def commongamePlay(size):
    print("\n\n\nYou are now in *** LEVEL {l} *** ".format(l=size-1))
    buildGameMatrix(square(size))
    print("\nPrint the matrix in your mind\n\n"); printMatrix(gameMatrix,square(size))
    clearFunc(size)
    buildUserMatrix(square(size))
    
def clearFunc(size):
    timeDelay=100000000*square(size)
    for i in range(timeDelay):
        pass
    print("\n"*square(size)*10000)
    
def gamePlayDie(i):
    commongamePlay(i)
    if isSimilar(gameMatrix,userMatrix,square(i)):
        i+=1;   print("\n You passed this level \t "+"Amazing "*(i-2),"\n");
        gamePlayDie(i)
    else:
        print("\n\nThis is your matrix");     printMatrix(userMatrix,square(i));
        print("\n\n\n\nThis is the right matrix");   printMatrix(gameMatrix,square(i));
        print("\n\n\n\n\n\nYour final level is {l}".format(l=(i-1)))
        print("\n\nSorry your memory didn't save you; Do you you want to try again [Y/N]\n\n\n\n")
        x=input()
        if (x=='Y'):  print("\n"*8); gamePlayDie(2)   
        else:         print("\nThanks for playing MOSMemory\t....\tMohamed Osama\t\n\n\n\n\n\n")

def gamePlayScore(i):
    commongamePlay(i)
    isSimilar(gameMatrix,userMatrix,square(i))
    print("\n\nThis is your matrix");     printMatrix(userMatrix,square(i));
    print("\n\n\n\nThis is the right matrix");   printMatrix(gameMatrix,square(i));
    printScore();
    print("\n\nDo you want to continue [Y/N]\n\n\n\n")
    x=input();   i+=1;
    if (x=='Y'):
        print("\n"*8); gamePlayScore(i);   
    else:
        print("\n\n\nYour total Score is {sc}".format(sc=score),"\nThanks for playing MOSMemory....\tMohamed Osama\t\n\n\n\n\n\n")

def gamePlay(i):
    print("The game has two mode:\t\n 1] LevelMode: You keep leveling up until you fail a level by guessing wrong number or more \t\n 2] ScoreMode: You keep playing where each right guess gains you a point\nand each wrong guess subtracts from you a point ")
    m=int(input("\n ENTER 1 or 2 to choose gameMode\n"))
    if (m==1):
        print("\nYou are on MOSMemory levelMode; **WELCOME**\n\n\n")
        gamePlayDie(i)
    elif (m==2):
        print("\nYou are on MOSMemory scoreMode; **WELCOME**\n\n\n")
        gamePlayScore(i)
    else:
        gamePlay(i)


gamePlay(2)