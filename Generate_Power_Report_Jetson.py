#!/user/bin/env python

import csv
import os
from os.path import basename

csvFiles = []

path = raw_input("Enter the path where power csv files are stored:\n")
os.chdir(path)
if os.path.exists("Power_Summery.csv"):
	os.remove("Power_Summery.csv")
fp = open("Power_Summery.csv", 'a')

fp.write("UseCase Name"+","+"CPU_Power"+","+"GPU_Power"+","+"SOC_Power"+","+"DRAM"+","+"AP_RAM\n")

for file in os.listdir(path):
	if file.endswith(".csv"):
		csvFiles.append(file)
		
for file in csvFiles:
	tmpFile=open(file, 'r')
	reader = csv.reader(tmpFile)
	for line in reader:
		if any("Source" in s for s in line):
			continue
		if not line:
			continue
		if any("Scan started" in s for s in line):
			break
		else :
			if line[0]=="VDD_CPU_Power":
				fp.write(os.path.splitext(file)[0]+","+'%.1f' % float(line[4]))
			if line[0]=="VDD_GPU_Power":
				fp.write(","+'%.1f' % float(line[4]))
			if line[0]=="VDD_SOC_Power":
				fp.write(","+'%.1f' % float(line[4]))
			if line[0]=="DRAM":
				fp.write(","+'%.1f' % float(line[4]))
			if line[0]=="AP_RAM":
				fp.write(","+'%.1f' % float(line[4])+"\n")
			else:
				continue

fp.close()
print("Power_Summery.csv file generated")

