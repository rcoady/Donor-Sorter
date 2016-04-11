import csv
import math
import random
import sys


# Opens Donor file and reads it into an array
with open('2016 Donation Thank Yous.csv', 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donationLevel = 250
fullDonorArray = []
multipleDonor = []

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

    # Array for Multiple thank yous
    if amount > 1:
        multipleDonor.append([donor[0], donor[1]])

    while amount > 0:
        amount -= 1
        fullDonorArray.append([donor[0], donor[1], donor[3], amount + 1])

print fullDonorArray
# print leaderArray
print len(fullDonorArray)

# Writes everything in the fullDonorArray to a csv file
with open("Full Donor.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Reason for Thanking", "Count"])
    writer.writerows(fullDonorArray)


# TODO Read in full CSV for donors
# TODO Make spreadsheet for Mailing labels
# TODO Remove staff from spreadsheet for mailing labels
# TODO Read in csv for leaders
# TODO Assign leaders to donors
