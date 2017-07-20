import random
num = random.randint(1,9) 
guess = raw_input("please choose a number or exit to quit: ")
count = 0
print ("the random number is: {}".format(num))
#print ("you selection is: {}".format(guess))

while (guess != "exit"):
    if guess == exit:
      break
    guess = int(guess)
    count += 1
    if (guess < num):
      print ("your guess is lower than the number")
    elif (guess > num ):
      print ("your guess is too high")
    else :
      print ("You got it")
      print "And it only took you",count,"tries"
      break
    guess = raw_input("please choose a number or exit to quit: ")
