from datetime import datetime
default_name = "nikhil"
default_salutation = "mr"
default_age = 22
spy = {
    'default_name': 'nikhil',
    'default_salutation':'mr',
    'default_age': 22,
}

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('Nikhil', 'Mr.', 21, 4.6)

class ChatMessage:
    def __init__(self, spy_name, friend_name, time, message):
        self.spy_name = spy_name
        self.friend_name = friend_name
        self.message = message
        self.time = datetime.now()


friends = []

chats = []
