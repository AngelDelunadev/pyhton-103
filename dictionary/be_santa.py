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

gift_num = Intvalidate("How many gifts do you want? ", "please enter a valid number ")
counter =0 
gifts = []
while counter < gift_num:
    gifts.append(stringValidate(f"What is gift #{counter+1}? ","Please enter a valid gift"))
    counter+=1

while True:

    good_or_bad = stringValidate("Have you been good or bad? ", "please enter a valid string")
    good_or_bad = good_or_bad.lower()
    if good_or_bad == "good":
        print(f"You will be receiveing a/an {gifts}")
        break
    elif good_or_bad == "bad":
        print("you will be receiveing a lump of coal.")
        break
    else:
        print("please enter good or bad")

            
        
