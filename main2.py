from default1 import Spy, friends, ChatMessage, chats
from default1 import Spy
from datetime import datetime
import csv

##########################################################################################


def select_friend():
    item_number = 0
    for friend in friends:
        print ('%d. %s' % (item_number + 1, friend.name))

        item_number = item_number + 1

    friend_choice = int(raw_input("Choose from your friends(index number)"))

    friend_choice_position = friend_choice - 1

    return friend_choice_position

###########################################################################################################################################


def add_status(current_status_message):
    if current_status_message!= None:

        print (" Your current status is " + current_status_message + "\n")
    else:
        print (" You donot have any status message currently \n")

    default = raw_input("Do you want to select from the older status [Y/N] ?")

    if default.upper() == "N":
        new_status_message = raw_input(" What status message do you want to set ?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message

            print("Your updated status is " + updated_status_message)
            status_message.append(updated_status_message)

    elif default.upper() == "Y":
        item_position = 1
        for message in status_message:

            print(str(item_position) + " " + message)

            item_position = item_position + 1
        message_selection = int(input("\n Choose from the above messages"))

        if len(status_message) >= message_selection:
            updated_status_message = status_message[message_selection-1]

            print("Your updated status is " + updated_status_message)

            return updated_status_message

########################################################################################################################################


status_message =['rahul','nik']
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
###################################################################################################################################################


special_words = ['SAVE ME', 'SOS' , 'HELP']


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
    with open("chats.csv", 'a') as chat_record:
        writer = csv.writer(chat_record)
        writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
#############################################################################################################################################


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
#######################################################################################################################


def start_chat(spy_name, spy_age, spy_rating):


    current_status_message=None

    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=row[1], age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # load_chats() is a function which loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    load_friends()
    load_chats()

    show_menu = True

    while show_menu == True:

        menu_choices = (" What do you want to do ? \n 1. Add a status update \n2. Add a friend \n3. Show friends \n 4.Send a secret message \n5.Read a Secret message \n6.Read chats from a user \n7.Close Application \n")
        menu_choice = int(raw_input(menu_choices))
        if menu_choice == 1:
            print (" You choose to update the status")
            current_status_message = add_status(current_status_message)
            ####passing current_status_message as argument in the add_status function

        elif menu_choice == 2:
            number_of_friends = add_friend()
            print("you have %d friends. "%(number_of_friends))
            ##printing number of friends spy has

        elif menu_choice == 3:
            select_friend()

        elif menu_choice == 4:
            send_message()

        elif menu_choice == 5:
            read_message()

        elif menu_choice == 6:
            print("Reading chat from user")
            print "select a friend whose chat you want to see"
            choice = select_friend()
            readchat(choice)


        elif menu_choice == 7:
            show_menu = False


from default1 import spy   ##importing function from other file
print("welcome to spy_chat project") #welcome message
selection = raw_input("Do you want to continue as " +spy.salutation+spy.name+" or create a new one (y/n):\n")
if selection.upper() == "Y":
    start_chat(spy.name, spy.age, spy.rating)
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


#################################################################################################################


def read_chat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                # checking the chats of the current spy with selected friend
                if c.spy_name == spy_1.name and c.friend_name == name_friend:
                    print colored("You sent message to the Spy name: %s "%name_friend,"red")
                    print colored("On Time: [%s]"%c.time,"blue")
                    print("Message: %s"% c.message)
                    return 1
            except IndexError:
                pass
            continue

##############################################################################################################################


from datetime import datetime
time= datetime.now()
print(time)




