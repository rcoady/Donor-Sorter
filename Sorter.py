import csv
import Leaders
import donors

# Opens Donor file and reads it into an array
with open('testDonors2013.csv', 'rb') as f:
    reader = csv.reader(f)
    donorArray = list(reader)

donors.filtername(donorArray)
donors.donoraddress(donors.cleanedArray)
donors.calculatethankyouamount(donors.cleanedArray)


def writefile(filename, header, array):
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(array)


writefile("Full Donor.csv", ["Company", "Contact", "Reason for Thanking", "Count"], donors.fullDonorArray)

print "The full donor list has been made"

with open('testLeaders2013.csv', 'rb') as f:
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

writefile("Full List.csv",
          ["Company", "Contact", "Reason for Thanking", "Count", "Leader First", "Leader Last", "Group"],
          new_array)

# TODO Assign leaders to donors
# TODO Clean donor file of extra spaces
