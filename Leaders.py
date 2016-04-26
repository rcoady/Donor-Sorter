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


def needaname(length):
    total = 0
    # 300 will be changed after reading in the length of the donor array
    amount = int(math.ceil(length / float(len(leaderArray))))
    while total < amount:
        for leader in leaderArray:
            fullLeaderArray.append([leader[0], leader[1], leader[2]])
        total += 1

    # Shuffles the leaders names
    random.shuffle(fullLeaderArray)


def write_leader_file(leader_array):
    with open("Leaders.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerow(["FirstName", "Last Name", "Group"])
        writer.writerows(leader_array)

# Opens Leader file and reads it into an array
with open('testLeaders2013.csv', 'rb') as f:
    reader = csv.reader(f)
    leaderArray = list(reader)


