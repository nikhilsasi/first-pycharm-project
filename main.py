# objective1 Create a file  main.py
# objective2 Greet the user with a welcome message and ask for their name and salutation.
# objective3 The app should ask the user if they want to continue with the default user or create their own.
# objective4 For a new user app should ask for the name and other details of the user such as rating, saluation.
# objective5 Based on spy rating display an appropriate message using at least one if, elif and else sequence
# objective6 Print an appropriate final welcome message with the name, salutation, age and rating of the spy.

print("welcome to my first spychat")
spy_name = input("type your name\n")
if len(spy_name) > 0:
      print(spy_name)
else:
      print("enter correct name\n")
salutation = input("what should we call you(Mr. or mrs)?\n")
print("Alright " + salutation +" " + spy_name + "I'd like to know a little bit more about you...")  # objective2
selection = input("does you want to continue (default or new) account")  # objective3
if selection == "new":  # for new account
      spy_name1 = input("enter new name\n")
      if len(spy_name1) > 0:
            print(spy_name1)
      else:
            print("enter correct name\n")
      selection1 = input("what we call you(Mr. or mrs)?\n")
      print("Alright " + selection1 + " " + spy_name1 + "I'd like to know a little bit more about you...")
      age = input("what's your age\n")
      rating_of_spy = input("type the rating of program\n")  #objective4
      type(float(rating_of_spy))

      if  float(rating_of_spy) >= 5:  # objective5
            print("you gave A++ grade")
      elif float(rating_of_spy) > 4:
            print("you gave A+ grade")
      elif float(rating_of_spy) > 3:
            print("you gave A grade")
      elif  float(rating_of_spy) > 2:
            print("you gave B+ grade")
      else :
            print("you gave B grade")

      print("hello" +salutation+ " " +spy_name+ "your age is " +age+ "your rating " +rating_of_spy)  #objective6
else:
      exit(0)
