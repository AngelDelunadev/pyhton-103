def GetSentence ():
    user_input = input("please enter a sentence ")
    while user_input.isdigit():
        print ("please enter a valid sentence")
        user_input = input("Please enter a sentence ")
    return user_input.lower()  

sentence = GetSentence()
word_list = sentence.split(' ')
histogram = {}
for word in word_list:
    if word in histogram.keys():
        histogram[word] += 1
    else :
        histogram[word] = 1

print(histogram)

sorted_histogram = sorted(histogram.items(),key=lambda x: x[1], reverse=True)
counter = 0
print("the top 3 word are")
print(sorted_histogram)
for i in  sorted_histogram:
    print(i[0], i[1])
    counter += 1
    if counter == 3:
        break
    


