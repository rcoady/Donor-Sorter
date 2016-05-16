import csv
import Leaders
import donors
import os

# Opens Donor file and reads it into an array
with open(os.path.join('Input', 'testDonors2013.csv'), 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donors.filtername(donorArray)
donors.lookup(donors.cleanedArray)
donors.donoraddress(donors.test_array)
donors.calculatethankyouamount(donors.test_array)


def writefile(filename, header, array):
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(array)


writefile("Full Donor.csv", ["Company", "Contact", "Reason for Thanking", "Count"], donors.fullDonorArray)

print "The full donor list has been made"

with open(os.path.join('Input', 'testLeaders2013.csv'), 'rb') as f:
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




writefile("Full List.csv",
          ["Company", "Contact", "Reason for Thanking", "Count", "Lookup", "Leader First", "Leader Last", "Group"],
          final_array)

# TODO Assign leaders to donors
# TODO Clean donor file of extra spaces
