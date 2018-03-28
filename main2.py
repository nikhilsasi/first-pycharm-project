print("welcome to my spychat")  #welcoming new user
def menu(default_salutation, default_name):
    choice = True
    while choice:
     print("1) Add a status update 2) Add a friend 3) Send a secret message")
     print(" 4) Read a secret message 5) Read chats from a user 6) Close application")
     choice = int(input("enter your choice"))
     if choice == 1:
        status = input("enter status:\n")
        print("%s %s status saved" % (default_salutation, default_name))
     elif choice ==2:
         print("1.your previous status\n 2. enter new status 3. exit")
         status_choice = input("enter your choice")
         if(status_choice == 1):
             status = None
     elif choice == 6:
         choice= False
    print("your default name is  " + default1.default_salutation + " " + default1.default_name + " your default age is " + default1.default_age)

def add_status(current_status_message):

    if current_status_message != None:
      print("Your current status message is " + current_status_message + "\n")
    else:
      print ('You don\'t have any status message currently \n')

selection = input("does you want to continue as nikhil Y/N")  # asking user for continuing as nikhil or creating new
if selection.upper() == "Y":  # for new account
 spy_name = input("enter new name\n")
 if len(spy_name) > 0:
    print(spy_name)
 else:
            print("enter correct name\n")
            selection1 = input("what we call you(Mr. or mrs)?\n")
            print("Alright " + selection1 + " " + spy_name + "I'd like to know a little bit more about you...")

 salutation = input("what should we call you(Mr. or mrs)?\n")
 age = input("what's your age\n")
 rating_of_spy = input("type the rating of program\n")
 if float(rating_of_spy) >= 5:  # objective5
            print("you gave A++ grade")
 elif float(rating_of_spy) > 4:
            print("you gave A+ grade")
 elif float(rating_of_spy) > 3:
            print("you gave A grade")
 elif float(rating_of_spy) > 2:
            print("you gave B+ grade")
 else:
            print("you gave B grade")
 print("hello " + salutation + " " + spy_name + "your age is " + str(age) + "your rating " +rating_of_spy)  #objective6
elif selection == "N":
        import default1  # importing data from another file
        menu(default1.default_salutation, default1.default_name)  # calling function
else:
    print("enter choice between new and default")
