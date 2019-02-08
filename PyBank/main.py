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
# Print all rows , mainpulate rows       
    for row in csvreader:
        # print (row)
# Define values to []extract       
        date = str(row[0])
        pr_lo = int(row[1])
# populate lists       
        dates.append(date)
        prft_loss.append(pr_lo)
        tmon= str(len(dates))
        prlo= sum(prft_loss)
print ("Total Months: " + (tmon))
print ("Total: $" + str(prlo)) 
# check lists
# print (dates)
# print (prft_loss)

# Calculate average change  
# def substraction (x, y):
#     total = x - y
#     return total

for i in range (len(prft_loss)-1):
    difference = prft_loss[i] - prft_loss[i+1]
    pch.append(difference)
print (pch[2])
print (sum(pch))
print (round(((sum(pch)) / (len(pch))),2))

# Greatest increase max()
# Greatest decrease min()








