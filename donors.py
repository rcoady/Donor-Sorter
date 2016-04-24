import csv
import math

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
