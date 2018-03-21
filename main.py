# objective1 Create a file  main.py
# objective2 Greet the user with a welcome message and ask for their name and salutation.
# objective3 The app should ask the user if they want to continue with the default user or create their own.

print("welcome to my first project")
spy_name = input("type your name")
print(spy_name)
salutation = input("what we call you(Mr. or mrs)?")
print("Alright " + salutation +" " + spy_name + "I'd like to know a little bit more about you...")  # objective2
selection = input("does you want to continue (default or new) account")  # objective3
if selection == "new":  # for new account
      spy_name1 = input("enter new name")
      print(spy_name1)
      selection1 = input("what we call you(Mr. or mrs)?")
      print("Alright " + selection1 + " " + spy_name1 + "I'd like to know a little bit more about you...")

else:
      exit(0) 