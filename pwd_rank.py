import string
import random

# menu function
# Displays the Menu List of the Program
def menu():
    print("1. Check the Strength of Password from the file.")
    print("2. Generate New Password.")
    print("3. End Program")

# function that generate random password
def generatePassword():
    '''Takes Zero Arguments and returns the randomly generated password as per password requirements rule defined.'''
    specialChar = ['!','+','-','=','?','#','%','*','@','&','^','$','_']
    passwordRequirementRules = string.ascii_letters + string.digits + ''.join(specialChar)
    randomPassword = ''.join(random.choice(passwordRequirementRules) for _ in range(12))
    return randomPassword

# prints the user entered username and password
# Ask the saving choice to the user and return it to main program
def printingCustomUserInformation(username,password):
    '''Takes two arguments username and password and returns the saving choice of the user.'''
    print("--------------------------------------")
    print("Your User Name = ", username)
    print("Your Password = ", password)
    print("---------------------------------------")
    savingChoice = input("Would You like to save this Password (Y/N): ").upper()
    return savingChoice
    
# takes one argument 
# returns the strength of password i.e strong, moderate or the poor
def passwordStrengthCheck(password):
    '''Takes one argument password and return its strength'''
    specialChar = ['!','+','-','=','?','#','%','*','@','&','^','$','_']
    strength = "Strong"
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char in specialChar for char in password) and len(password) > 11:
        strength = "Strong"
    
    elif not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in specialChar for char in password) and len(password) in range(8,12):
        strength = "Modrate"
    else:
        strength = "Poor"
    return strength



# Main program

# runs until terminated by the user
while True:
    print("Bulk Password Checker")
    print("-----------------------")
    menu()
    choice = int(input("Choose any options: "))
    # user validation for limiting the choice from 1 to 3.
    while choice not in range(1,4):
        print("Invalid Choice. Try Again")
        menu()
        choice = int(input("Choose any options: "))

    if choice == 1:
        try:
            fp = open("Users-Pwds.txt",'r')
            dataCount = 0
            outputFile = open("Users-Pwds-chked.txt",'w')
            for data in fp:
                dataCount += 1
                username = data.split(',')[0]
                password = data.split(',')[1]
                strength = passwordStrengthCheck(password)
                finalDataToWrite = username.strip() + "," + password.strip() + ","+strength + "\n"
                outputFile.write(finalDataToWrite)
            outputFile.close()
            print("------------------------------------------------------------------------")
            print("Password Checked Successfully.")
            print("The Number of Password Checked: ",dataCount)
            print("The feedback for the password can be found on Users-Pwds-cheked.txt")
            print("------------------------------------------------------------------------")
        except IOError:
            print("Error in Reading the file.")
        except:
            print("Error.Something went wrong.")
        finally:
            fp.close()
    elif choice == 2:
        username = input("Please Enter the UserName: ")
        while len(username) > 20:
            print("Length Of UserName Cannot Exceed 20 Character. Try Again...")
            username = input("Please Enter the UserName: ")
        returnedPassword = generatePassword()
        savingChoice = printingCustomUserInformation(username,returnedPassword)
        while savingChoice == "N":
            differentPassword = input("Would you like to have different password for the user (Y/N):").upper()
            if differentPassword == "Y":
                returnedPassword = generatePassword()
                printingCustomUserInformation(username,returnedPassword)
            else:
                break
        if savingChoice == "Y":
            try:
                fp = open("Users-Pwds.txt",'a')
                userInfo = "\n"+username +","+returnedPassword
                fp.write(userInfo)
                fp.close()
            except IOError:
                print("Error in Reading the file.")
            except:
                print("Error.Something went wrong.")
        
    else:
        print("This Program is Courtesy of Anoop.")
        exit()

