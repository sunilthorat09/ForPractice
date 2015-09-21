#!/user/bin/env python

import csv

fp = open("power.csv", "r+")
fp.write("Sunil,Thorat,20")
fp.write("Chetan,Jain,23")

fileContent = csv.reader(fp)
print(fileContent)


fp.close()