def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

# Create a function that has two variables. 
# One called greeting and another called myName. 
# Print out greeting and myName two different ways without using the following examples    
def problem1():
    greeting = "Hello world"
    myName = "Chey"
    print("%s my name is %s." %(greeting,myName))
    # print(f"{greeting} my name is {myName}.")


# Create a function that asks the user for a secret password. 
# Create a loop that quits with the user's quit word. 
# If the user doesn't enter that word, ask them to guess again.   
def problem2():
    secretPassword = input("Enter secret password ")
    while (True):
        password = input("Enter password ")
        if password == secretPassword:
            break
        else:
            print("Try Again!!")


# Create a function that prints 0 to 100 three times in a row (vertically).
def problem3():
    for firstLoop in range(3):
        for secondLoop in range(101):
             print(secondLoop)
    

def problem4():
    randomNum = random.randint(0,5)
    userInput = "" 
    while(userInput != str(randomNum)):
        userInput = input("Guess the number")
        
        
if __name__ == '__main__':
    main()