import default1   # importing data from another file
import friend
print("welcome to my spychat")  #welcoming new user

Friends_name = []
Friends_age = []
Friends_rating = []
Friends_is_online = []

def add_status(current_status)  :

    updated_status = None
    if len(current_status)>0:
        print("You current status is:\n"+current_status)
    else:
        print("you didn't enter any status")
    choice=input("do you want to select status from you old status or add a new one ?(previous/new):\n")
    if choice.lower() == 'previous':
        count = 0
        status_messages = ['lalit', 'rohit']
        for message in status_messages:
            print(str(count+1) + " ." + message)
            count = count+1
        status_choice = int(input("Select status you want to set\n"))
        new_status = status_messages[status_choice-1]
        return new_status
    else:
        new_status = input("enter status:\n")
        if len(new_status) > 0:
            status_messages = ['lalit', 'rohit']
            status_messages. append(new_status)
            print("successfully entered")
        else:
            print("please enter a valid status")
    return new_status

def add_friend():  #adding friend
    friend_name = input("enter you friend_name:\n")
    friend_salutation = input("\n")
    new_name = friend_salutation+" "+friend_name
    friend_age = int(input("enter your friend age\n"))
    friend_rating = float(input("what is rating of your friend:\n"))
    if len(friend_name) > 0 and friend_age > 17 and friend_rating > 0:
        Friends_name.append(new_name)
        Friends_age.append(friend_age)
        Friends_rating.append(Friends_rating)
        Friends_is_online.append(True)
    else:
        print("Please enter right details")
    return len(new_name)

def menu(default_salutation, default_name):  #defining function
    choice = True
    # printing full message
    print("your default name is " +
         default1.default_salutation + " " + default1.default_name + " your default age is " + default1.default_age)

    while choice:
        print("1) Add a status update 2) Add a friend 3) Send a secret message")
        print(" 4) Read a secret message 5) Read chats from a user 6) Close application")
        choice = int(input("enter your choice"))  # entering option
        if choice == 1:
            status = input("enter status:\n")
            print("%s %s status saved" % (default_salutation, default_name))
        elif choice == 2:
            friend.add_friend()
        elif choice == 3:
            status = input("enter new message")
        elif choice ==4:
            print("1.your previous status\n 2. enter new status 3. exit")
            status_choice = input("enter your choice")
            if status_choice == 1:
                status = None
                print("no status present")
            elif status_choice == 2:
                status_new = input("enter new status")
            else:
                exit(0)
        elif choice == 5:
            status = input("reading chat from user")
        else:
            choice = False
            print("quitting")


def add_status(current_status_message):
    if current_status_message != None:
      print("Your current status message is " + current_status_message + "\n")
    else:
      print ('You don\'t have any status message currently \n')

# asking for default user or new one
selection = input("Do you want to continue as " +default1.default_salutation + " "
                  + default1.default_name + " (Y/N)? ")

# asking user for continuing as nikhil or creating new
if selection.upper() == "N":# for new account
    spy_name = input("enter new name")
    if len(spy_name) > 0:# checking wheather name is entered or not
             print(spy_name)
    else:
        print("enter correct name\n")
    selection1 = input("what we call you(Mr. or mrs)?\n")
    print("Alright " + selection1 + " " + spy_name + "I'd like to know a little bit more about you...")

    salutation = input("what should we call you(Mr. or mrs)?\n")  #asking for salutation

    age = input("what's your age\n")#asking for age

    rating_of_spy = input("type the rating of program\n")  #asking for rating
    if float(rating_of_spy) >= 5:  #checking the user inputed rating
        print("you gave A++ grade")
    elif float(rating_of_spy) > 4:
         print("you gave A+ grade")
    elif float(rating_of_spy) > 3:
         print("you gave A grade")
    elif float(rating_of_spy) > 2:
         print("you gave B+ grade")
    else:
          print("you gave B grade")
    print("hello " + salutation + " " + spy_name + "your age is " + str(age) + "your rating "
          + rating_of_spy)
elif selection.upper() == "Y": #if user want the default one
        menu(default1.default_salutation, default1.default_name)  # calling function
else:
    print("enter choice between new and default")
