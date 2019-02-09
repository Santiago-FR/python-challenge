# Import Modules  for operating system and to read CSV
import os
import csv
# Locate the file,
csvpath = os.path.join("Resources","budget_data.csv")
# Use improved reading method
with open(csvpath,'r',newline="") as csvfile:
# Specifiy delimeter and the variable to hold it
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)  
# # Print the header and pull it out of rows.
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
# Create lists
    dates = []
    prft_loss = []
    pch = []
# Print/check all rows , mainpulate rows     
    for row in csvreader:
        # print (row)
# Define values to []extract       
        date = str(row[0])
        pr_lo = int(row[1])
# populate lists       
        dates.append(date)
        prft_loss.append(pr_lo)
# Get totals for number of months and total profit loss
        tmon= (len(dates))
        prlo= sum(prft_loss)

# check lists
# print (dates)
# print (prft_loss)

for i in range (len(prft_loss)-1):
    difference = prft_loss[i+1] - prft_loss[i]
    pch.append(difference)

#Final print terminal

print ("Financial Analysis")
print ("----------------------------------")
print ("Total Months: " + str(tmon))
print ("Total Profit: $" + str(prlo)) 
print ("Average Change: $" + str((round(((sum(pch)) / (len(pch))),2))))
print ("Greatest Increase in Profits: " + (dates[pch.index(max(pch))]) + "  ($" + str(max(pch)) + ")")
print ("Greatest Decrease in Profits: " + (dates[pch.index(min(pch))]) + "  ($" + str(min(pch)) + ")")

#Print to text file
f = open("Financial Analysis.txt", "w")
# Print multiple lines, add \n to the begining of each line to make sure it separates.
lines= [
    "Financial Analysis",
    "\n----------------------------------", 
    "\nTotal Months: " + str(tmon), 
    "\nTotal Profit: $" + str(prlo), 
    "\nAverage Change: $" + str((round(((sum(pch)) / (len(pch))),2))),
    "\nGreatest Increase in Profits: " + (dates[pch.index(max(pch))]) + "  ($" + str(max(pch)) + ")", 
    "\nGreatest Decrease in Profits: " + (dates[pch.index(min(pch))]) + "  ($" + str(min(pch)) + ")"
    ] 
f.writelines(lines) 
#Remember to close or the file wont be written.
f.close()
