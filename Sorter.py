import csv
import math
import random
import sys

# donorArray = [["Ryan Coady", "Ryan Coady", "0", "Database coordinator"],
#              ["Amber Dalgaard", "Stuff", "751", "Donating to an ILS fundraiser"]]


# Opens Donor file and reads it into an array
with open('2016 Donation Thank Yous.csv', 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)


donationLevel = 250
fullDonorArray = []
leaderArray = [['Ryan Coady', '1'], ['Amber Dalgaard', '2'], ['Hopper', '2'], ['Kristin', '3'], ['Jon', '4'],
               ['Jon', '4'], ['Leah', '5'], ['Jenna', '5'], ['Annalisa', '7']]

for donor in donorArray:
    # Checks for the contributor and contact being the same person
    if donor[0] == donor[1]:
        donor[1] = ''
    if donor[2] == '':
        donor[2] = 0

    # How many thank you's a person should receive
    donation = float(donor[2])
    amount = int(math.ceil(donation / donationLevel))

    # Catches edge case if the donation is zero or blank
    if amount == 0:
        amount = 1
        print donor[0] + " made an in-kind donation and should receive", amount, "thank you"
    else:
        print "The total amount that", donor[0], "donated is $" + donor[2], "and should receive", amount, "thank you's"

    while amount > 0:
        amount -= 1
        fullDonorArray.append([donor[0], donor[1], donor[3], amount + 1])

print fullDonorArray
random.shuffle(leaderArray)
print leaderArray
print len(fullDonorArray)

# Writes everything in the fullDonorArray to a csv file
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Reason for Thanking", "Count"])
    writer.writerows(fullDonorArray)

# To Do
# Read in csv for donors
# Read in csv for leaders
# Assign leaders to donors
