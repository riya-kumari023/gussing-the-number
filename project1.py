#PROJECT GUESSING THE NUMBER
print(".....................PROJECT GUESSING THE NUMBER....................................\n")
import random
number = random.randint(1,100)
atmpt=1
guess= int(input("Guess the number :"))
while(True):
    if (guess>number):
        guess= int(input("this number io  big.......\nGuess the number :"))
        atmpt+=1
    elif(guess<number):
        guess= int(input("\nthis number io small.......\nGuess the number :"))
        atmpt+=1
    else:
        print("\nCongratulations u guess the correct number....||| ")
        break
print(f"u guess this number in {atmpt} attempts")
print("attempts")
if(atmpt>1 and atmpt<=3):
      print("suberb")
elif(atmpt>3 and atmpt<=5):
       print("excellent")
elif(atmpt>5 and atmpt<=10):
      print("very good")
elif(atmpt>10 and atmpt<=15):
       print("good")
else:
       print("improve ur self|||||")
with open("highestscore.txt","r") as f:
     highestscore = int(f.read())
if atmpt<highestscore :
     print("you have jst broken the highest score..........")
     with open("highestscore.txt","w") as f:
          f.write(str(atmpt))
          