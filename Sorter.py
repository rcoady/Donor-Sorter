import csv
import Leaders
import donors
import os
import sys

donors_file = raw_input("What file would you like to use for the donors? : ")
leaders_file = raw_input("What file would you like to use for the leaders? : ")

if donors_file == '':
    donors_file = 'testDonors2013.csv'
    print("You are using " + donors_file)

elif not os.path.isfile('Input/' + donors_file):
    sys.exit("Sorry, that file doesn't exist, please check that the file was put into the correct folder")

if leaders_file == '':
    leaders_file = 'testLeaders2013.csv'
    print("You are using " + leaders_file)
elif not os.path.isfile('Input/' + leaders_file):
    sys.exit("Sorry, that file doesn't exist, please check that the file was put into the correct folder")


print donors_file
print leaders_file

print os.path.isfile('Input/'+donors_file)

# Opens Donor file and reads it into an array
with open(os.path.join('Input', donors_file), 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donors.filtername(donorArray)
donors.lookup(donors.cleanedArray)
donors.donoraddress(donors.test_array)
donors.calculatethankyouamount(donors.test_array)


def writefile(folder, filename, header, array):
    with open(os.path.join(folder, filename), "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(array)


writefile("Output", "Full Donor.csv", ["Company", "Contact", "Reason for Thanking", "Count"], donors.fullDonorArray)

print "The full donor list has been made"

with open(os.path.join('Input', leaders_file), 'rb') as f:
    reader = csv.reader(f)
    leaderArray = list(reader)

Leaders.namecleaner()
Leaders.needaname(len(donors.fullDonorArray))
Leaders.write_leader_file(Leaders.fullLeaderArray)

new_array = []
# Stops after last assigned thank you
print len(donors.fullDonorArray)
count = 0
for donor in donors.fullDonorArray:
    new_array.append(donors.fullDonorArray[count] + Leaders.fullLeaderArray[count])
    count += 1
final_array = []
for donor in new_array:
    if donor[4] == '':
        if int(donor[7]) < 4:
            donor[4] = '1'
        elif int(donor[7]) < 7:
            donor[4] = '2'
        elif int(donor[7]) < 10:
            donor[4] = '3'
        elif int(donor[7]) < 13:
            donor[4] = '4'
        elif int(donor[7]) < 16:
            donor[4] = '5'
    final_array.append([donor[0], donor[1], donor[2], donor[3], donor[4], donor[5], donor[6], donor[7]])

writefile("Output", "Full List.csv",
          ["Company", "Contact", "Reason for Thanking", "Count", "Lookup", "Leader First", "Leader Last", "Group"],
          final_array)

# TODO Assign leaders to donors
# TODO Clean donor file of extra spaces
