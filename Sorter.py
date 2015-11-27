import csv
import random
import sys


donorArray = [["Ryan Coady", "Ryan Coady", 251, "Database coordinator"], ["Amber Dalgaard", "Stuff", 750, "Donating to an ILS fundraiser"]]
donationLevel = 250
fullDonorArray = []
leaderArray = ['Ryan Coady', 'Amber Dalgaard', 'Hopper', 'Kristin', 'Jon', 'Jon', 'Leah', 'Jenna', 'Annalisa']


for donor in donorArray:
    # Checks for the contributor and contact being the same person
    if donor[0] == donor[1]:
        donor[1] = ''

    # How many thank you's a person should receive
    amount = donor[2] / donationLevel
    if donor[2] % donationLevel:
        amount += 1
    print "The total amount that " + donor[0] + " donated is $", donor[2], "and should receive", amount, "thank you's"

    thank_count = 0
    while donor[2] > 0:
        temp_list = []
        thank_count += 1
        amount = 0
        amount = donor[2]
        if amount < 250:
            thank_count += 1
            amount = 0
        temp_list.extend([donor[0]])
        temp_list.extend([donor[1]])
        temp_list.extend([amount])
        temp_list.extend([donor[3]])
        donor[2] -= donationLevel
        fullDonorArray.append(temp_list)
print fullDonorArray
random.shuffle(leaderArray)
print leaderArray

# To Do
# Read in csv for donors
# Read in csv for leaders
# Assign leaders to donors
