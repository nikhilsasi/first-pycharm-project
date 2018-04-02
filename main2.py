from default1 import spy #importing function from other file
from steganography.steganography import Steganography #importing steganography file
from datetime import datetime


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


def select_friend():
  item_number = 0
  for friend in friends:
    print '%d. %s' % (item_number + 1), friend['name']
    item_number = item_number + 1
    friend_choice= raw_input(input("choose from your friend"))
    friend_choice_position = friend_choice - 1
    return friend_choice_position

def read_message():#function for reading message
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = {
          "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print("Your secret message has been saved!")
Friends_name = []
Friends_age = []
Friends_rating = []
Friends_is_online = []



def add_friend():  # adding friend
        dictionary_name = ['rahul', 'lalit', 'krishan']
        Friend_name = raw_input("enter you friend_name:\n")
        if Friend_name in dictionary_name:
              print "name already exist"
        else:
          print "its a new name continue"
          Friend_salutation = raw_input("mr/mrs")
          new_name = Friend_salutation + " " + Friend_name
          Friend_age = int(input("enter your friend age\n"))
          Friend_rating = float(input("what is rating of your friend:\n"))
          print("%s %s is your new friend his/her age is %d and gave rating %0.2f" % (Friend_salutation, Friend_name, Friend_age,Friend_rating))
          if len(Friend_name) > 0 and Friend_age > 17 and Friend_rating > 0:
            Friends_name.append(new_name)
            Friends_age.append(Friend_age)
            Friends_rating.append(Friends_rating)
            Friends_is_online.append(True)
          else:
              print("Please enter right details")
friends=[]

def select_friend():
  for friend in friends:
    print '%s aged %d with rating %.2f is online' %(friend['name'], friend['age'], friend['rating'])

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
            status_message =['rahul','nik']

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
print("welcome to spy_chat project") #welcome message
selection = raw_input("continue as %s %s (y/n)" %(spy['default_salutation'], spy['default_name']))
if selection.upper() == "Y":
    menu(spy['default_salutation'], spy['default_name'])
elif selection.upper() == "N":
    spy_name = raw_input("enter new name")
    if len(spy_name) > 0:
             print(spy_name)
             salutation = raw_input("what we call you(Mr. or mrs)?\n")

             print("Alright " + salutation + " " + spy_name + "I'd like to know a little bit more about you...")

             age = int(raw_input("what's your age\n"))  # asking for age

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

    else:
        print("enter correct name\n")

else:
    print("enter your choice between y/n")
