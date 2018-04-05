def menu(salu,name):  #defining function
    choice = True
    while choice:
        print("1) Add a status update 2) Add a friend 3) Send a secret message")
        print(" 4) Read a secret message 5) Read chats from a user 6) Close application")
        choice = int(input("enter your choice"))  # entering option
        if choice == 1:
            status_choice_up =int(raw_input("1.add status or 2.choose from old status"))
            if status_choice_up =="1":
                status = raw_input("enter status:\n")
                if len(status)>0:
                    updated_status =status
                    status.append(updated_status)
                print(status)
                print("%s %s status saved" % (salu, name))
            elif status_choice_up =="2":
                for message in status_message:
                    read_message()
        elif choice == 2:
            add_friend()
        elif choice == 3:
            send_message()
        elif choice == 4:
            read_message()

        elif choice == 5:
            status = input("reading chat from user")
        else:
            choice = False
            print("quitting")

from default1 import spy #importing function from other file
print("welcome to spy_chat project") #welcome message
selection = raw_input("continue as %s %s (y/n)" %(spy['default_salutation'], spy['default_name']))
if selection.upper() == "Y":
    menu(spy['default_salutation'], spy['default_name'])
elif selection.upper() == "N":
    spy_name = raw_input("enter new name")
    if len(spy_name) > 0:  #checking name
             print(spy_name)
             salutation = raw_input("what we call you(Mr. or mrs)?\n")
             print("Alright " + salutation + " " + spy_name + "I'd like to know a little bit more about you...")

             age = int(raw_input("what's your age\n"))  # asking for age
             if age < 12 or age > 50:  #checking age
                 print("sorry! your age is invalid to be a spy")
             else:
                 spy_experience = raw_input("For how many years you are working as a spy ?")
             rating_of_spy = float(raw_input("type the rating of program\n"))  # asking for rating
             if float(rating_of_spy) >= 5:  # checking the user inputed rating
                 print("you gave A++ grade")
             elif float(rating_of_spy) > 4:
                 print("you gave A+ grade")
             elif float(rating_of_spy) > 3:
                 print("you gave A grade")
             elif float(rating_of_spy) > 2:
                 print("you gave B+ grade")
             else:
                 print("you gave B grade")
             print("hello %s %s your age %d is your rating %.2f" % (salutation, spy_name, age, rating_of_spy))
             menu(salutation,spy_name)
    else:
        print("enter correct name\n")

else:
    print("enter your choice between y/n")

##############################################
from steganography.steganography import Steganography #importing steganography file

def send_message():  #function for sendingmessage
    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice]['chats'].append(new_chat)
    print("Your secret message is ready!")

from datetime import datetime  #import date and time
time= datetime.now()
print(time)
def read_message():#for reading message

  sender = select_friend()
  output_path = raw_input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
  print(secret_text)

  new_chat = {
      "message": secret_text,
      "time": datetime.now(),
      "sent_by_me": False
  }

  friends[sender]['chats'].append(new_chat)
  print "Your secret message has been saved!"

friends = []
status_message =['rahul','nik']
def select_friend():
  item_number = 0
  for friend in friends:
    print('%d. %s' % (item_number + 1), friend['name'])
    item_number = item_number + 1
    friend_choice= raw_input(input("choose from your friend"))
    friend_choice_position = friend_choice - 1
    return friend_choice_position


friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
def add_friend():  # adding friend
        dictionary_name = ['rahul', 'lalit', 'krishan']
        friend_name = raw_input("enter you friend_name:\n")
        if friend_name in dictionary_name:
              print "name already exist"
        else:
          print "its a new name continue"
          friend_salutation = raw_input("mr/mrs")
          new_name = friend_salutation + " " + friend_name
          friend_age = int(input("enter your friend age\n"))
          friend_rating = float(input("what is rating of your friend:\n"))
          print("%s %s is your new friend his/her age is %d and gave rating %0.2f" % (friend_salutation, friend_name, friend_age,friend_rating))
          if len(friend_name) > 0 and friend_age > 17 and friend_rating > 0:
            friends_name.append(new_name)
            friends_age.append(friend_age)
            friends_rating.append(friends_rating)
            friends_is_online.append(True)
          else:
              print("Please enter right details")
def add_status(current_status_message):
    ####function to add status
    if current_status_message != None:
        ###initiallly current status will be none
        print (" Your current status is " + current_status_message + "\n")
    else:
        print (" You dont have any status message currently \n")

    default = raw_input ("Do you want to select from the older status [Y/N] ?")

    if default.upper() == "N":
        new_status_message =raw_input(" What status message do you want to set ?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message

            print("Your updated status is " + updated_status_message)
            status_message.append(updated_status_message)

    elif default.upper() == "Y":
        item_position = 1
        for message in status_message:
            ###use of for loop in the list
            print(str(item_position) + " " + message)
            ##printing status list
            item_position = item_position +1
        message_selection = int(input("\n Choose from the above messages"))
        ##asking user which status u want to add
        if len(status_message) >= message_selection:
            updated_status_message = status_message[message_selection-1]

            print("Your updated status is " + updated_status_message)

            return updated_status_message






