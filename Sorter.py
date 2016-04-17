import csv
import math
import random
import sys


# Opens Donor file and reads it into an array
with open('testDonors2013.csv', 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donationLevel = 250
addressArray = []
fullDonorArray = []
multipleDonor = []

for donor in donorArray:
    # Checks for the contributor and contact being the same person
    if donor[0] == donor[1]:
        donor[1] = ''
    if donor[2] == '':
        donor[2] = 0

    # Writes donor name, contact, and address to an array
    if donor[4] != "Staff":
        addressArray.append([donor[0], donor[1], donor[5], donor[6], donor[7], donor[8]])

    # How many thank you's a person should receive
    donation = float(donor[2])
    amount = int(math.ceil(donation / donationLevel))

    # Catches edge case if the donation is zero or blank
    if amount == 0:
        amount = 1

    # Array for Multiple thank yous
    if amount > 1:
        multipleDonor.append([donor[0], donor[1]])

    while amount > 0:
        amount -= 1
        fullDonorArray.append([donor[0], donor[1], donor[3], amount + 1])



# Writes everything in the fullDonorArray to a csv file
with open("Full Donor.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Reason for Thanking", "Count"])
    writer.writerows(fullDonorArray)

with open("Address Labels.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Address", "City", "State", "Zip"])
    writer.writerows(addressArray)

# TODO Read in csv for leaders
# TODO Assign leaders to donors
