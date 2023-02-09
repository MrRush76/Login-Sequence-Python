import time #imports the time package A package contains third-party that can be imported and used throught the code 
import sys #imports the "sys" package
from random import * # imports "*" from the "random" package "from" imports selected function's from the package
import os # imports the os package 
from time import sleep  # imports the sleep module from the time package
def recoveryoptions(): # defines a function called "recoveryoptions " A function is a reusable bit of code that can be called multiple times throughout the program and can have variables passed into it. A print function displays a string to the terminal
    print("You are going to be asked 5 questions.... These will be your recovery options if you forget your password") # this is a print function it prints to the terminal what is inside it the "" speechmarks declare anything inside as a string
    global recoveryoptions1  # {
    global recoveryoptions2  #  
    global recoveryoptions3  #
    global recoveryoptions4  #
    global recoveryoptions5  # mkes these variables global. Global means to make the variable able to be used outside the function it is created in   
    recoveryoptions1 = str(input("What is your Favourite Colour?\n")) # defines "recoveryoptions1" as a user input. A varibale is a type of storage where a valubale can be stored to a name in this example the name is "recoveryoptions1" and it's value is an input which means the user types something in following the prompt which is defined inside the input function. The "str" means that anything inside is defined as a string(a sequence of characters)
    recoveryoptions2 = str(input("What is your Favourite Food?\n")) # defines "recoveryoptions2" as a user input
    recoveryoptions3 = str(input("Name a school teacher you once had?\n")) # defines "recoveryoptions3" as a user input
    recoveryoptions4 = str(input("What is your favourite subject?\n")) # defines "recoveryoptions4" as a user input
    recoveryoptions5 = str(input("What is your facourite number?\n")) # defines "recoveryoptions5" as a user input
    print("Thank you for answering these questions....")#print function 
    file = open("passwordrecovery.txt" , "w") # "open" is a function which opens a text file to be used in the program. the open function takes two attributes the text file it is opening "untitled.txt" and how it is opening it. In this case we are using "W" because we are opening to write to it . The data from this textfile is then stored in the variable "file"
    file.write(recoveryoptions1) #{ 
    file.write("\n")
    file.write(recoveryoptions2)
    file.write("\n")
    file.write(recoveryoptions3)
    file.write("\n")  # "\n" is a symbol inside a string that goes to a new line 
    file.write(recoveryoptions4)
    file.write("\n")
    file.write(recoveryoptions5) # ".write()" writes anything to the file that is inside the brackets 
    os.system("clear||cls") # "os" declares the package the function comes from ("clear||cls") clears the  
def changerecovery(): # defines a function called "changerecovery"
    print_slow("Would you like to change your Recovery Options? (Y/N)\n") # print function
    ans = input() # variable called "ans" takes input 
    if ans == "y" or ans == "Y": # An if statement is a logic gate which runs the code indented inside it if the parameters it says are met. The operators used or "==" that checks if the two variables hold the same data. and the or operator makes it so that the if statement will run if either of the two things run. 
        recoveryoptions() # runs the "recoveryoptions" function
def changepassword(): # defines a function called "changepassword"
    os.system("clear||cls") # clears the terminal
    print_slow("To change Your Password Enter Your Previous Password:\n") # print function
    previouspassword = input() # defines variable "previouspassword" as an input
    print_slow("Confirm Password:\n ") # print function
    previouspassword1 = input() # defines variable "previouspassword1" as an input
    if previouspassword1 == previouspassword: #if statement checks if "previouspassword" and "previouspassword1" are the same thing
        print_slow("Now enter Your New Password: ") # print function
        newpassword1 = input() # defines a variable called "newpassword1" as an input 
        passwordlist = [] # the square brackets make the variable into a list, a list is a variable which stores many diferent values that can be found and used by there index each value has an index the first index starts out "0"
        f1 = open("untitled.txt" , "r") # opens the file "untitled.txt" in read mode as a variable - "f1" this variable is used for looking at the file 
        for i in range(10): # A for loop is a loop that runs however many times is declared inside the brackets in this case 10
            f1line = f1.readline() # this reads the line of code it is on 
            stripf1line = f1line.strip("\n") # strips it of its new line character 
            splitf1line = stripf1line.split(",") # splits it by the comma 
            passwordlist.append(splitf1line) # adds the line to the list "passwordlist"
        f1.close() # closes the file 
        passwordlistnosublist = []  # makes a new list called "passwordlistnosublist"
        for i in(passwordlist): # for loop iterates as many times as how long the list "passwordlist" is 
            passwordlistnosublist += i # adds to the list "passwordlistnosublist" the current item in the list "passwordlist"
        passwordpos = passwordlistnosublist.index(previouspassword) # defines the variable "passwordpos" as the index of the string stored in the variable "previouspassword"
        passwordlistnosublist[passwordpos] = newpassword1 #changes the item in the list "passwordlistnosublist" t the index that is stored in the variavle "passwordpos" to the string stored in the variable "newpassword1" 
        f1 = open("untitled.txt" , "w") # opens the file "untitled.txt" in write mode in the variable "f1"
        while("" in passwordlistnosublist): # While loop - A while loop is a loop that runs until the parameters inside it are not met. In this case it runs when there are still empty spaces in the list 
            passwordlistnosublist.remove("") # removes whitespace from the list "passwordlistnosublist"
        for i in range(0, len(passwordlistnosublist), 2): # for loop iterates from 0 to to the length of the list "passwordlistnosublist" and increases in increments of 2. This for loop takes 3 parameters: The first two are the starting number it runs through and the second one is the one it runs up to. The last one is what the for loop increments in 
            f1.write(",".join(passwordlistnosublist[i:i+2]) + "\n") # writes to the file the item in "passwordlistnosublist" followed by a comma then the next item and then goes to a new line
        print("Password Changed Successfully... ") # print function
    else: # else block
        print_slow("Passwords did not match returning to login screen.....") # print function
        sleep(2) # does nothing for 2 seconds
        os.system("clear||cls") # clears the terminal 
        loginsequence() # runs the function "loginsequence"
def passwordrecovery():
    os.system("clear||cls") # clears the terminal
    questionslist = [] # defines a new empty list called "questionslist"
    f = open("passwordrecovery.txt" , "r") # opens the file "passwordrecovery.txt" in read mode 
    for i in range(5): # for loop iterates 5 times 
        line = f.readline() # reads the line of code 
        stripline = line.strip("\n") # removes its new line function
        questionslist.append(stripline) # appends to the list "questionslist" with the line "stripline"
    questionsright = 0 # defines the variable "questionsright" and assigns "0" to it 
    x =randint(1,5) # defines a variable called "x" that picks a random number between 1 and 5 sing the package random . 
    if x  ==  1: # if statement checks if x is equal to 1 
        recoveryoptions1question = str(input("What is your Favourite Colour?\n")) # defines variable "recoveryoptions1question as a string input"
        if recoveryoptions1question == questionslist[0]: # if statement checks if "recoveryoptions1question" is equal to the item in index "0" in the list "questionslist"
            questionsright+=1 # adds 1 to the "questionsright" variable Note: the rest of these if statement do the same thing but for different questions so no need to comment
    if x  == 2:
        recoveryoptions2question = str(input("What is your Favourite Food?\n"))
        if recoveryoptions2question == questionslist[1]:
            questionsright+=1 
    if x  == 3:
        recoveryoptions3question = str(input("Name a school teacher you once had?\n"))
        if recoveryoptions3question == questionslist[2]:
            questionsright+=1 
    if x  == 4:
        recoveryoptions4question = str(input("What is your favourite subject?\n"))
        if recoveryoptions4question == questionslist[3]:
            questionsright+=1
    if x  == 5:
        recoveryoptions5question = str(input("What is your facourite number?\n"))
        if recoveryoptions5question == questionslist[4]:
            questionsright+=1
    x2 = randint(1,5) # same with this here all code until next comment is very similar so already commented 
    while x2 == x:
        x2 = randint(1,5)
    if x2  == 1:
        recoveryoptions1question = str(input("What is your Favourite Colour?\n"))
        if recoveryoptions1question == questionslist[0]:
            questionsright+=1
    if x2  == 2:
        recoveryoptions2question = str(input("What is your Favourite Food?\n"))
        if recoveryoptions2question == questionslist[1]:
            questionsright+=1
    if x2  == 3:
        recoveryoptions3question = str(input("Name a school teacher you once had?\n"))
        if recoveryoptions3question == questionslist[2]:
            questionsright+=1
    if x2  == 4:
        recoveryoptions4question = str(input("What is your favourite subject?\n"))
        if recoveryoptions4question == questionslist[3]:
            questionsright+=1
    if x2  == 5:
        recoveryoptions5question = str(input("What is your facourite number?\n"))
        if recoveryoptions5question == questionslist[4]:
            questionsright+=1
    if questionsright == 2: # if statement checks if the variable "questionsright" is equal to 2 
        data = open("untitled.txt" , "r") #opens he text file "untitled.txt" in read mode 
        lists1 = [] #creates a new list with nothing in it called "lists"
        for i in range(10): #creates a for loop that will iterate 10 times
            line1 = data.readline() #reads the line of the file 
            line11 = line1.strip("\n") #removes the new line symbol
            linesplit1 = line11.split(",") # splits the line into a username and password by the comma 
            lists1.append(linesplit1) # adds the usernname and password into the list "lists" as a sub list
        usernameinput = input("You Have Answered the Questions Right... Provide Your Username and We Will Tell You Your Password\n") # defines variable: "usernameinput" as a user input 
        incorrectusername = 0 #defines variable "incorrectusername" and sets it to 0 
    else: #else block 
        print("one or more questions answered incorrectly") # print function 
        exit() #ends the code 
    for i in range(10): # for loop iterates 10 times 
        if usernameinput == lists1[i][0]: # if statement check is the variable "usernameinput" is equal to the item in list "lists1" at index [i(the iteration of the loop)][0]
            print("Here is your Password:" , lists1[i][1]) # prints the users password
            print("You will now be returned to the menu....") # print function 
            sleep(3) # does nothing for 3 seconds 
            loginsequence() # runs the loginsequence function 
        else: # else block 
            incorrectusername+=1 # adds one to the variable "incorrectusername"
        if incorrectusername == 10: # if statement checks if the "incorrect username" variable is equal to 10 
            print_slow("Incorrect Username. Unable to Retrieve Password....") # print function 
            exit() # ends the code
#{
def print_slow(str): 
  for char in str: 
    time.sleep(0.08)
    sys.stdout.write(char)
    sys.stdout.flush()             #   all of this code is optional}  it imports the sys package and defines a nw function that iterates and prints each character of a string one by one instead of all at once
  return ""
def login():#defines a function called "login"
    os.system("clear||cls")
    print_slow("Logging In..... \n") #prints "Logging in......" and then goes onto a new line
    data = open("untitled.txt" , "r") #opens he text file "untitled.txt" in read mode
    lists = [] #creates a new list with nothing in it called "lists"
    for i in range(10): #creates a for loop that will iterate 10 times
        line = data.readline() #reads the line of the file 
        line1 = line.strip("\n") #removes the new line symbol
        linesplit = line1.split(",") # splits the line into a username and password by the comma 
        lists.append(linesplit) # adds the usernname and password into the list "lists" as a sub list
    def loginagain():  #defines a new function called "loginagain"
        loginsuccess = False  # defines a boolean variable called "loginsuccess" and sets it to False
        username = str(input(print_slow(("Enter a Username: \n")))) #defines a variable called "username" defines as a string variable and then asks the user for an input and then assigns that input to the variable
        password = str(input(print_slow(("Enter a Password: (if you have forgotten your passcode enter it as \"unknown\" \n")))) #defines a variable called "password" defines as a string variable and then asks the user for an input and then assigns that input to the variable
        if password == "unknown":
            passwordrecovery()
        for i in range(10): #creates a for loop that will iterate 10 times
            if username == lists[i][0] and password == lists[i][1]: # if statement that checks if both the "username" and "password" variables are the same as the strings on the line of the text file "untitled.txt" that the for loop is iterating through
                print_slow("Succesfully Signed In! \n ")# prints "succesfully signed in!" and then goes to a new line
                loginsuccess = True # sets the "loginsuccess" boolean variabl to "True"
        if loginsuccess == False: # if statement that checks if the boolean variable "loginsuccess" is False 
            print_slow("Incorrect Username or Password Please Try Again : \n ") # Prints "Incorrect Username or Password Please Try Again" and then goes to a new line 
            loginagain() #runs the function "loginagain"
        else: # if the previous does happen then:
            exit() #ends the program 
    loginagain() # runs the function "loginagain"
    data.close() # closes the textfile assigned to the variable "data"
def signup():# defines a new function called "signup"
    os.system("clear||cls")
    data = open("untitled.txt" , "a") #open the file containing the usernames and passwords in append mode 
    newuser = input(print_slow("\nEnter a New Username: ")) # asks the user for an input and assigns it to a variable
    newpassword = input(print_slow("\nEnter a New Password: ")) # asks the user for an input and assigns it to a variable
    def validate_password(password): #defines a new function called "validate_password" that takes one attribute "password"
        global valid # defines the variable "valid" as a global variable (ca be used outside this funciton)
        valid = True # sets the boolean variable "valid" to "True"
        if not any(characters.isdigit() for characters in password): #if statement checks if there are no numerical characters in the string variable "password"
            print("Password must have at least one numeric character.\n") # prints "Password must have at least one numeric character." and goes to a new line 
            valid = False #sets the boolean variable "valid" to "False"
        if not any(characters.isupper() for characters in password): # if statement checks if there are no upper case characters in the string variable "password"
            print_slow('Password must have at least one uppercase character\n') #prints "Password must have at least one uppercase character" and goes to a new line 
            valid = False #sets the boolean variable "valid" to "False". A boolean variable can only be set to True or False
        if not any(characters.islower() for characters in password): # if statement chcks if there are no lower case characters in the string variable "password"
            print_slow('Password must have at least one lowercase character\n') # prints "Password must have at least one lowercase character" and goes to a new line 
            valid = False #sets the boolean variable "valid" to "False" 
    validate_password(newpassword) #passes the users inputted password through the validation function
    if valid == True: # if statement checks if the boolean variable "valid" is set to "True"
        print_slow("Sign Up Complete\n")  #prints "Sign Up Complete"
    else: # if the previous does not happen (if valid is not set to True)
        signup() # run the function "signup"
    data.write("\n") # writes to the textfile assigned to data to go to a new line 
    data.write(newuser) # writes to the textfile assigned to data the string assigned to the variable "newuser"
    data.write(",") # writes to the textfile assigned to data the string ","
    data.write(newpassword) # writes to the textfile assigned to data the string assigned to the variable "newpassword"
    data.close() #closes the file assigned to the variavle "data"
    os.system("clear||cls")
    recoveryoptions()
    print_slow("Returning to menu....")
    sleep(3)
    os.system("clear||cls")
    loginsequence()
def loginsequence(): # defines a new function called "loginsequence"
    os.system("clear||cls")
    print("""  
    ************************************************************      
    ******************---Login Sequence---**********************
    ************************************************************                
    ********************---1: Login---**************************
    *******************---2: Sign Up---*************************
    ****************---3: Forgot Password?**********************
    ****************---4. Change Password---********************
    ****************---5. Recovery Options---*******************
    *********************---6. Exit---**************************
    ************************************************************
    """) #prints out a splash screen that displays starts and text
    decision = input(print_slow("Please select an option.... \n")) # prompts the user with an input with the text "Please select an option...." and then assigns it to the variable "decision"
    if decision == "1":  # if statemnt checks if "decision" = "1"
        login() # runs the login function
    elif decision == "2": # elif statemnt checks if "decision" = "2". ELif is like a if function but it goes after the first if statement. You cant have two if statements in a row only an if and an elif.
        signup() # urns the signup function
    elif decision == "3": # elif statemnt checks if "decision" = "3"
        if os.path.getsize("passwordrecovery.txt") == 0:
            recoveryoptions()
        else:
            passwordrecovery()
    elif decision == "4":
        changepassword()
    elif decision == "5":
        changerecovery()
    elif decision == "6":
        exit()
    else: # if none of the previous happen. Else is a statement that if none of the if or elif statements happen then this runs 
        print_slow("ERROR") # prints "ERROR"
        loginsequence() # runs the function "loginsequence"
loginsequence() # runs the function "loginsequence"
