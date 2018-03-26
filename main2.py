print("welcome to my first spychat")
spy_name = input("type your name\n")
if len(spy_name) > 0:

        print(spy_name)
else:
        print("enter correct name\n")
salutation = input("what should we call you(Mr. or mrs)?\n")
print("Alright " + salutation +" " + spy_name + "I'd like to know a little bit more about you...")  # objective2
def defv():
    print("your default name is  " + default1.default_salutation + " " + default1.default_name + " your default age is " + default1.default_age)
selection = input("does you want to continue (default or new) account")  # objective3
if selection == "new":  # for new account
 spy_name1 = input("enter new name\n")

 if len(spy_name1) > 0:

  print(spy_name1)
 else:
            print("enter correct name\n")
            selection1 = input("what we call you(Mr. or mrs)?\n")
            print("Alright " + selection1 + " " + spy_name1 + "I'd like to know a little bit more about you...")
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
 print("hello " + salutation + " " + spy_name + "your age is " +age+ "your rating " +rating_of_spy)  #objective6

elif selection == "default":
    import default1  # importing data from another file
    defv()  # calling function

else:
    print("enter choice between new and default")