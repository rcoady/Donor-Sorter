import csv
import math
import random
import sys
import Leaders


# Opens Donor file and reads it into an array
with open('testDonors2013.csv', 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donationLevel = 250
addressArray = []
fullDonorArray = []
cleanedArray = []


def filtername(donorfile):
    for donor in donorfile:
        if donor[0] == donor[1]:
            donor[1] = ''
        if donor[2] == '':
            donor[2] = 0
        cleanedArray.append([donor[0], donor[1], donor[2], donor[3], donor[4], donor[5], donor[6], donor[7], donor[8]])
    return cleanedArray


def donoraddress(donorfile):
    for donor in donorfile:
        if donor[4] != "Staff":
            addressArray.append([donor[0], donor[1], donor[5], donor[6], donor[7], donor[8]])

    with open("Address Labels.csv", "wb") as f:
        address_writer = csv.writer(f)
        address_writer.writerow(["Company", "Contact", "Address", "City", "State", "Zip"])
        address_writer.writerows(addressArray)


def calculatethankyouamount(donorfile):
    for donor in donorfile:
        donation = float(donor[2])
        amount = int(math.ceil(donation / donationLevel))

        if amount == 0:
            amount = 1
        while amount > 0:
            amount -= 1
            fullDonorArray.append([donor[0], donor[1], donor[3], amount + 1])
    return fullDonorArray


filtername(donorArray)
donoraddress(cleanedArray)
calculatethankyouamount(cleanedArray)



# Writes everything in the fullDonorArray to a csv file
with open("Full Donor.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Reason for Thanking", "Count"])
    writer.writerows(fullDonorArray)
print "The full donor list has been made"


with open('testLeaders2013.csv', 'rb') as f:
    reader = csv.reader(f)
    leaderArray = list(reader)
Leaders.namecleaner()
Leaders.needaname(len(fullDonorArray))
Leaders.write_leader_file(Leaders.fullLeaderArray)

new_array = []
# Stops after last assigned thank you
print len(fullDonorArray)
count = 0
for donor in fullDonorArray:
    new_array.append(fullDonorArray[count] + Leaders.fullLeaderArray[count])
    count += 1

with open("Full List.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Contact", "Reason for Thanking", "Count", "Leader First", "Leader Last", "Group"])
    writer.writerows(new_array)
# TODO Assign leaders to donors
# TODO Clean donor file of extra spaces
