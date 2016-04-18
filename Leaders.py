import csv
import math
import random
import sys
import sqlite3
# import Sorter

fullLeaderArray = []


def namecleaner():
    for leader in leaderArray:
        leader[0] = leader[0].strip()
        leader[1] = leader[1].strip()


def needaname():
    total = 0
    # 300 will be changed after reading in the length of the donor array
    amount = int(math.ceil(300 / float(len(leaderArray))))
    while total < amount:
        for leader in leaderArray:
            fullLeaderArray.append([leader[0], leader[1], leader[2]])
        total += 1

    # Shuffles the leaders names
    random.shuffle(fullLeaderArray)


# Opens Leader file and reads it into an array
with open('testLeaders2013.csv', 'rb') as f:
    reader = csv.reader(f)
    leaderArray = list(reader)

# Strips extra spaces from the leader first and last name
namecleaner()

# Writes the leaders to fullLeaderArray while the amount has not been fulfilled
needaname()

# Writes everything in the fullDonorArray to a csv file
with open("Leaders.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Last Name", "Group"])
    writer.writerows(fullLeaderArray)
