print("Welcome to Quiz game!!!")
player = input("Are you interested to play?\n yes or no\n")
if player=="yes":
    print("Let's begin!!!")
else:
    print("Thank you")
    quit()
print("If your answer has spelling mistake it will display incorrect answer\n")

score = 0

question1=input("1.Who is the founder of Python?\n Guido van rossum or Bjarne Stroustrup\n")
if question1=="Guido van rossum":
    print("Correct\n")
    score+=1
else:
    print("Incorrect\n")
   
question2=input("2.How do you insert COMMENTS in Python code?\n #Comment or %Comment\n")
if question2=="#Comment":
    print("Correct\n")
    score+=1
else:
    print("Incorrect\n")

question3=input("3.How do you find the minimum value of list?\n min or Min\n")
if question3=="min":
    print("Correct\n")
    score+=1
else:
    print("Incorrect\n")

question4=input("4.How do you find the length of the list?\n len() or Len()\n")
if question4=="len()":
    print("Correct\n")
    score+=1
else:
    print("Incorrect\n")

question5=input("5.How do you sort the list?\n list.sort() or list.(sort)\n")
if question5=="mylist.sort()":
    print("Correct\n")
    score+=1
else:
    print("Incorrect\n")
   

print("Your score:"+ str(score))
print("\n CONGRATS")
