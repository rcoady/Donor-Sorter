import csv
import math
import os
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
    # Shuffles the leaders names
    random.shuffle(leaderArray)

    total = 0
    # 300 will be changed after reading in the length of the donor array
    amount = int(math.ceil(length / float(len(leaderArray))))
    while total < amount:
        for leader in leaderArray:
            fullLeaderArray.append([leader[0], leader[1], leader[2]])
        total += 1


def write_leader_file(leader_array):
    with open(os.path.join('Output', 'Leaders.csv'), "wb") as f:
        writer = csv.writer(f)
        writer.writerow(["First Name", "Last Name", "Group"])
        writer.writerows(leader_array)


# Opens Leader file and reads it into an array
with open(os.path.join('Input', 'testLeaders2013.csv'), 'rb') as f:
    reader = csv.reader(f)
    leaderArray = list(reader)
