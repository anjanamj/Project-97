# pocketMoney = int(input("Enter the pocket money you get every month:"))
# if (pocketMoney>500):
#  print("You are a rich kid")
# elif (pocketMoney>100):
#  print("You have a good life")
# else:
#     print("I know what you feel!")

# charCount = 0
# wordCount = 1
# intro = input("Give an intro about you:")
# for i in intro:
#     print(charCount)
#     charCount = charCount + 1
    
#     if(i==' '):
#         wordCount = wordCount + 1
# print("WordCount"+ str(wordCount))

import random

chances = 5
num = random.randint(1,9)
while(chances>0):
    chances = chances -1
    guessed = int(input("Guess a number between 1 & 9:"))
    if(guessed == num):
        print("Congrats")
        break
    else:
        print("Wrong guess. "+str(chances)+ " more attempts left")
if(guessed != num):
    print("Oops!!You are out of chances")
