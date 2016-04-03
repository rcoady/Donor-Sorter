import csv
import math
import random
import sys


donorArray = [["Ryan Coady", "Ryan Coady", 450, "Database coordinator"], ["Amber Dalgaard", "Stuff", 751, "Donating to an ILS fundraiser"]]
donationLevel = 250
fullDonorArray = []
leaderArray = ['Ryan Coady', 'Amber Dalgaard', 'Hopper', 'Kristin', 'Jon', 'Jon', 'Leah', 'Jenna', 'Annalisa']


for donor in donorArray:
    # Checks for the contributor and contact being the same person
    if donor[0] == donor[1]:
        donor[1] = ''

    # How many thank you's a person should receive
    amount = int(math.ceil(float(donor[2])/donationLevel))
    print int(math.ceil(float(donor[2])/donationLevel))
    print "The total amount that " + donor[0] + " donated is $", donor[2], "and should receive", amount, "thank you's"

    while amount > 0:
        temp_list = []
        temp_list.extend([donor[0]])
        temp_list.extend([donor[1]])
        temp_list.extend([donor[3]])
        amount -= 1
        fullDonorArray.append(temp_list)

print fullDonorArray
random.shuffle(leaderArray)
print leaderArray

# To Do
# Read in csv for donors
# Read in csv for leaders
# Assign leaders to donors
