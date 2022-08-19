import time
import random 
import string

def intro():
    print("Welcome to MOS Typing speed tester   \t ... Mohamed Osama Saleh ... \t\n");
    print("You will be tested with two sentences one is meaningful & the other isn't");  initialize()

def initialize():
    global randomSentence;
    x=input("\nHow many random characters you want to test yourself with in case of non meaningful ?: ")
    randomSentence=temp.get(random.randint(1,7))
    global randomString;
    randomString=''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=int(x)))

temp={1:"Leo Messi is regarded as the football GOAT due to winning seven ballon d'ors",
2:"Cristiano Ronaldo is the football top goalscorer with more than eight hundred goals",
3:"Ricardo Kaka,Ronaldinho,Rivaldo are the brazilian players who won ballon d'or, champions league and world cup",
4:"Shirt number three in AC Milan is retired as it's their all time captain shirt who's Paolo Maldini",
5:"Real Madrid is the only team who won five consecutive champions league tournaments",
6:"Barcelona is the only team who won one sextuple and two fivetuple",
7:"Mohamed Osama is considered the greatest Programmer & thinker of all time",
8:"Al-Andalus nowadays is the region including Portugal, Spain and Gibraltar"}

def charCountNoSpaces(s):
    return len(s)-s.count(" ")
def wordCount(s):
    return len(s.split())
    
def timeCount():
    return t1-t0
def perMinute(count,line):
    return (count(line)/timeCount())*60
    
def similar(string1,string2):
    return string1==string2
    
def test(x,count,line):
    global t1;  global t0;
    t0=time.time(); enteredSentence=input("\nEnter this sentence :\n{s}\n\n".format(s=line)); t1=time.time()
    if similar(line,enteredSentence):
        printResults(x,count,line)
    else:
        print("You didn't typically copy the sentence");   test(x,count,line)

def printResults(x,count,line):
    print("\n\nTime taken: "+str(timeCount())+" seconds")
    if x==1:
        print("Number of words: "+str(count(line))); print("Word/minute: "+str(perMinute(wordCount,line))+" WPM")
    if x==0:
        print("Number of characters: "+str(count(line)))
    print("Char/minute: "+str(perMinute(charCountNoSpaces,line))+" CPM\n\n")

def checkContinuety():
    x=input("\n\n\nDo you want to try again ? [Y/N]\n\n\n")
    if x=='Y' or x=='y':
        initialize(); test(1,wordCount,randomSentence); test(0,charCountNoSpaces,randomString); checkContinuety()
    else:
        z=input("Thanks for trying the test")

def main():    
    intro()
    test(1,wordCount,randomSentence)
    test(0,charCountNoSpaces,randomString)
    checkContinuety()
    
main()