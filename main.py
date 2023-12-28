#declarations and initializations of variables
userInput = numPos = numNeg = userSum = 0
userList = []
value = False

#while loop which runs until the value is True
while value == False:
    #getting user input as an integer
    userInput = int(input("Enter a Number (0 to stop): "))

    #conditional statement which runs if user input is zero
    if userInput == 0:
        value = True

    #conditional statement checking if user input is any number other than zero   
    else:
        #appending user's input to the list userList
        userList.append(userInput)

        #conditional statement which runs if user input is positive
        if userInput > 0:
            numPos += 1
        #conditional statement which runs if the user input is negative
        else:
            numNeg += 1

#while loop which runs through each iteration of the list
for iteration in userList:
    userSum += iteration

#printing some statistics of the user's input values
print("\nNumber of positives = " + str(numPos))
print("Number of negatives = " + str(numNeg))
print("Sum = " + str(userSum))
print("Average = " + ("{:.2f}".format(userSum / (numPos + numNeg))))               