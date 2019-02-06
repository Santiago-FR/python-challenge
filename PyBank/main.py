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
# Print the header and pull it out of rows.
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
#Print all rows    
    dates = []
    prft_loss = []
    
    for row in csvreader:
        date = row[0]
        pr_lo = int(row[1])
        dates.append(date)
        prft_loss.append(pr_lo)
        tmon= str(len(dates))
        tprlo= sum(prft_loss)
    print(row)
    print(dates)
    print(prft_loss)
    print ("Total Months:" + (tmon))
    print ("Total: $" + str(tprlo))
    
