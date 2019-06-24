import os
import csv

#File to load
csvFile = os.path.join("C:\\Users\\vuntu\Desktop\\HomeWork-Python\\Python-Challange\\PyBank\\budget_data.csv")

#Output file
txtFile = os.path.join("PyBank", "analyzed_budget.txt")

#Financial data to be analyzed:
monthCount = 0
totalNet = 0
monthChange = []
netPLChange = []
greatestIncreaseP = [" ", 0]
greatestDecreaseL = [" ", 0]

#Read CSV file and convert into list of dictionaries
with open(csvFile) as performData:
	csvReader = csv.reader(performData)

	#Read header row
	header = next(csvReader)

	#Extract first row and avoid append Profit and Loss change
	firstRow = next(csvReader)
	monthCount = monthCount + 1
	totalNet = totalNet + int(firstRow[1])
	prevNet = int(firstRow[1])
		
	for row in csvReader:

		#Track total
		monthCount = monthCount + 1
		totalNet = totalNet + int(row[1])


		#Track monthChange
		netChange = int(row[1]) - prevNet
		prevNet = int(row[1])
		netPLChange = netPLChange + [netChange]
		monthChange = monthChange + [row[0]]

		#Greatest Increase
		if netChange > greatestIncreaseP[1]:
			greatestIncreaseP[0] = row[0]
			greatestIncreaseP[1] = netChange

		#Greatest Decrease
		if netChange < greatestDecreaseL[1]:
			greatestDecreaseL[0] = row[0]
			greatestDecreaseL[1] = netChange

#Average netChange
netMonthlyAve = sum(netPLChange) / len(netPLChange)

#Create summary txtFile
analysis = (
f"\nPerformance Analysis\n"
f"---------------------\n"
f"Total Months: {monthCount}\n"
f"Total: ${totalNet}\n"
f"Average Change: ${netMonthlyAve: .2f}\n"
f"Greatest Increase in Profits: {greatestIncreaseP[0]} (${greatestIncreaseP[1]})\n"
f"Greatest Decrease in Profits: {greatestDecreaseL[0]} (${greatestDecreaseL[1]})\n")

print(analysis)

with open("C:\\Users\\vuntu\Desktop\\HomeWork-Python\Python-Challange\\PyBank\\analyzed_budget.txt", "w") as txt_file:
	 txt_file.write(analysis)
		
