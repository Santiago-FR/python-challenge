# Import Modules  for operating system and to read CSV
import os
import csv
# Locate the file,
csvpath = os.path.join("Resources","election_data.csv")
# Use improved reading method
with open(csvpath,'r',newline="") as csvfile:
# Specifiy delimeter and the variable to hold it
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)  
# Print the header and pull it out of rows.
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

# Create lists
    votes = []
    candidates = []

# Print/check all rows , mainpulate rows     
    for row in csvreader:
        # print (row) too much data do not!
# Define values to []extract       
        vote = int(row[0])
        candidate = str(row[2])
# populate lists       
        votes.append(vote)
        candidates.append(candidate)
# Get total votes
        tvotes = len(votes)
# print (str(tvotes))
# Identify candidates
ucan = set(candidates) 
# print (ucan)
# print (len(ucan))
#determine how many time eac appears in candidates
c_1 = candidates.count('Li')
c_2 = candidates.count('Khan')
c_3 = candidates.count('Correy')
c_4 = candidates.count("O'Tooley")

p_one = round((c_1 * 100) / tvotes,3)
p_two = round((c_2 * 100) / tvotes,3)
p_three = round((c_3 * 100) / tvotes,3)
p_four = round((c_4 * 100) / tvotes,3)

print ("Election Results")
print ("-------------------------")
print ("Total Votes: "+ (str(tvotes)))
print ("-------------------------")
print ("Khan: " + str(p_two) + "%   " + "("+ str(c_2) + ")")
print ("Correy: " + str(p_three) + "%   " + "("+ str(c_3) + ")")
print ("li: " + str(p_one) + "%   " + "("+ str(c_1) + ")")
print ("O'Tooley: " + str(p_four) + "%   " + "("+ str(c_4) + ")")
print ("-------------------------")
print ("Winner: Kahn")
# check lists
# # print (dates)
# # print (prft_loss)

#Print to text file
f = open("Election Results.txt", "w")
# Print multiple lines, add \n to the begining of each line to make sure it separates.
lines= [
    "Election Results",
    "\n-------------------------",
    "\nTotal Votes: "+ (str(tvotes)),
    "\n-------------------------",
    "\nKhan: " + str(p_two) + "%   " + "("+ str(c_2) + ")",
    "\nCorrey: " + str(p_three) + "%   " + "("+ str(c_3) + ")",
    "\nli: " + str(p_one) + "%   " + "("+ str(c_1) + ")",
    "\nO'Tooley: " + str(p_four) + "%   " + "("+ str(c_4) + ")",
    "\n-------------------------",
    "\nWinner: Kahn"]
f.writelines(lines) 
#Remember to close or the file wont be written.
f.close()













