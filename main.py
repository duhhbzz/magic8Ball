# import functionality for random number generator
import random

# variable callouts
name = input("Enter Name:")
question = input("Enter Question:")
answer = ""

# random number range 1 - 9 
random_number = random.randint(1,12)

# if else statement to hold different outputs based from
# the random number selected
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
 elif random_number == 10:
  answer = "Cannot predict now"
elif random_number == 11:
  answer = "My reply is no"
elif random_number == 12:
  answer = "Outlook very good"
else:
  answer = "Error"

#loop is for error handling - if user does not input a name, or question  
if len(question) != "":  
  if len(name) == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question)
  print("Magic 8 Ball says: " + answer)
else:
  print("Magic 8 Ball does not understand what you are asking, please try again")
