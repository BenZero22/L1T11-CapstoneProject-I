# This tool can be used to calculate interest earned on an investment, or calculate the repayment amount on a bond.
import math

# Determine the need of the user
need = input("""\nWelcome to your finance tool!\nChoose either 'investment' or 'bond' from the menu below to proceed:
                
Investment\t- to calculate the amount of interest you will earn on interest
Bond\t\t- to calculate the amount you'll have to pay on a home loan

> """)

# Create a 'while' loop to prevent app from closing if the user does not enter invest or bond
while need.lower()[0] != "i" or "b":
    # Determine which equations will need to take place in order to meet the users need.
    # Users entry will be indexed to the first letter AND cast in lower case to avoid errors
    if need.lower()[0] == "i":
        # Obtain perimeters for interest formulae from user
        capital = float(input("How much would you like to deposit as your  capital amount?\n> R"))
        i_rate_input = float(input("What is the current interest rate %?\n> "))
        # Divide interest by 100 and cast to get a float for formula
        i_rate = float(i_rate_input/100)
        term_years = float(input("For how many YEARS would you like to invest this money?\n> "))
        interest = input('Would your interest "simple" or "compound"?\n> ')
        # Determine which way to calculate interest based on users selection
        if interest.lower()[0] == "s":
            interest_earned = capital*(1+i_rate*term_years)
            print("Simple Interest : The total amount of investment including interest is: R{}".format(round(float(interest_earned), 2)))
        elif interest.lower()[0] == "c":
            interest_earned = capital * math.pow((1+i_rate),term_years)
            print("Compound Interest : The total amount of investment including interest is: is: R{}".format(round(float(interest_earned), 2)))
        # Prevent the same series of questions looping
        break

    elif need.lower()[0] == "b":
        prop_value  = float(input("What is the current value of the house?\n> R"))
        i_rate_input = float(input("What is the current interest rate %?\n>" ))
        # Divide interest by 100 and cast to get a float for formula
        i_rate_annually = float(i_rate_input/100)
        i_rate_monthly = float(i_rate_annually/12)
        # Obtain perimeters for repayment formula from user
        term = int(input("Up to how many months would you like to take to repay?\n> "))
        # Calculate the monthly repayment amount
        repay = (i_rate_monthly * prop_value) / (1-(1+i_rate_monthly)**(-term))
        print("Your monthly repayment amount is R{}.".format(round(repay)),2)
        break
    # if the user did not enter a selection relating to 'Invest' or 'Bond', to ask user to re-enter
    else:
        need = input("Please enter either 'Invest' or 'Bond', your entry is not case sensative\n> ")

else:
    print("Thank you for using the finance tool")