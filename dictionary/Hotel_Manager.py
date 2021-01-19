def Intvalidate (question , error_message):
    while True:
        try:
            return int(input(question))
            
        except :
             print(error_message)
def stringValidate (question, error_message):
    user_input = input(question)
    while user_input.isdigit():
        print (error_message)
        user_input = input(question)
    return user_input  
hotel = {}


def CheckIn ():
    floor = Intvalidate("what Floor is your room on? ", "please enter a valid room")
    
    room =Intvalidate("What Room number do you have? ", "please enetr a valid number.")
    # hotel[floor] = room
    guest_num = Intvalidate("how many occupants is there? ", "please enter a number")
    counter = 0
    guest = []
    while counter < guest_num:
        guest.append(stringValidate(f"Who is guest {counter+1}? ", "please enter a name. "))
        counter+=1
    # hotel[floor][room] = guest
    hotel= {floor : {room : [guest]}}
    print([floor])

       
        





def Menu():
    while True:
        print("[1] Check in ")
        print("[2] Check out")
        user_input = input ("please pick an option. ")
        if user_input == "1":
            CheckIn()
            break
        elif user_input =="2":
            print("check out")
            break
        else:
            print("Please enter a valid option. ")

Menu()


        




