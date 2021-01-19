def Getword ():
    user_input = input("please enter a word ")
    while user_input.isdigit():
        print ("please enter a valid word")
        user_input = input("Please enter a word ")
    return user_input  
        
    
                
word = Getword()
histogram = {}
word = sorted(word)
for letter in word:
    if letter in histogram.keys():
        histogram[letter] += 1
    else:
        histogram[letter] = 1

print(histogram)

    