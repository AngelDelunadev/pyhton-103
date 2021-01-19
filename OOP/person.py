class Person:
    def __init__(self, name, email, phone, friends = [], greeting_count =0):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count = self.greeting_count + 1

    
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number is {self.phone}")
    
    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return(len(self.friends))

    def __str__(self):
        return f"{self.name} email: {self.email} phone: {self.phone} {self.name} has {self.num_friends()} friends and has greeted others {self.greeting_count} times"


    

        


sonny = Person("Sonny","sonny@hotmail.com", "483-586-3456")
jordan = Person("Jordan", "jordan@a0l.com", "495_586-3446")

sonny.greet(jordan)
jordan.greet(sonny)
sonny.print_contact_info()

jordan.add_friend(sonny)

jordan.num_friends()

jordan.greeting_count

print(jordan)
