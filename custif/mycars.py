#!/usr/bin/python3

round = 0
answer = " "
seeall = "N"
coolcars = ["Maserati","Jeep","Alpha Romeo","Mopar","Citroen","Abarth","Dodge","Lancia"]
#print(coolcars)
while round < 3 and answer not in coolcars:
    round += 1     # increase the round counter by 1
    answer = input('Test your knowledge.  According to Hotcars.com, what is one of the top 8 cool cars by Stellantis?\n>> ').title()
    if answer in coolcars: # logic to check if user gave correct answer
        print("Correct! ", answer, "is one of the top 8 cool cars by Stellantis!")
        seeall = input('Would you like to see all of the top 8 cool cars by Stellantis? Y/N\n>> ').upper()
        if seeall == "Y":
            print("The top 8 cool cars by Stellantis are: ", coolcars)
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the top 8 cool cars by Stellantis are: ", coolcars)
    else:                 # if answer was wrong
        print("Sorry, ", answer, "is not a cool car. Try again.")

