#!/user/bin/env python

import csv

fp = open("power.csv", "r+")
#fp.write("Sunil,Thorat,20\n")
#fp.write("Chetan,Jain,23")

fileContent = csv.reader(fp)

for row in fileContent:
	print(row)

fp.close()