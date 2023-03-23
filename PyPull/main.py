# Module 3 python challenge
# Kristen Pollok
# 3/18/2023
# pyPull/ main.py

# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three
# columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes 
# the votes and calculates each of the following values:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#import dependencies
import os
import csv
#set path for csv file
election_data_CSV = os.path.join("Resources", "election_data.csv")
Votes_cast = []
county_list = []
candidates = []
total_votes=0     #set vote count to 0

with open(election_data_CSV, encoding ='utf') as csvfile:  #open the csv file 
    csvreader =csv.reader(csvfile, delimiter=",")         
    header = next(csvreader)                               #skip the header row
    for row in csvreader:                                  #add the info of the csv file to different list
        Votes_cast.append(row[0])
        county_list.append(row[1])
        candidates.append(row[2])

    total_Votes =int(len(Votes_cast))                     #length of the total votes list 

    data_dictionary = {"name":[],     #create a dictionary with 3 empty lists where the indexes will match up for each candidate
                       "vote count": [],
                       "vote percentage":[]}
    i=0
    vote_count =0    
    percentage =0
    data_dictionary["name"].append(candidates[0]) #add the first candidate to list name to compare
    for i in range((len(candidates))):            #loops through the whole csv 
            if candidates[i] not in data_dictionary["name"]:  #if the candidate name is not in the list name in the dictionary add it
                 data_dictionary["name"].append(candidates[i])
          
    for i in range (len(data_dictionary["name"])): #loops through the list of names in the dictionary
        for j in range(len(candidates)):           #loops through the whole csv
            if candidates[j] == data_dictionary["name"][i]:
                 vote_count +=1    #counts everytime a candidate gets a vote
        data_dictionary["vote count"].append(vote_count) #stores the vote count for a candidate with the same index
        percentage =(vote_count/total_Votes)*100   # calculates percentage
        data_dictionary["vote percentage"].append(percentage) #stores the percentage for a candidate with the same index

 #reset count and percent
        vote_count =0
        percentage =0
        
 # The winner of the election based on popular vote.
    winner =0
    
    for x in range(len(data_dictionary["name"])):

        if ((data_dictionary["vote count"][x]) > winner):
            winner_name = data_dictionary["name"][x]
            winner = data_dictionary["vote count"][x]

# print values to the terminal
    print("Election Results\n")
    print("----------------------------")    
    print("Total Votes: ", total_Votes)
    print("----------------------------")   
    for k in range (len(data_dictionary["name"])): 
        print(f' {data_dictionary["name"][k]}: {round(data_dictionary["vote percentage"][k],3)}% ({data_dictionary["vote count"][k]})')
    print("----------------------------")
    print(f"Winner:", winner_name)
    print("----------------------------")

#write print statements to the txt file

out_file = open('Analysis\output.txt', "w")
line1= "Election Results\n"
out_file.write(line1)
line2 = "----------------------------\n"
out_file.write(line2)    
line3 = f"Total Votes: {total_Votes}\n"
out_file.write(str(line3))
line4 = "----------------------------\n"
out_file.write(line4)   
for k in range (len(data_dictionary["name"])): 
    line5 =f' {data_dictionary["name"][k]}: {round(data_dictionary["vote percentage"][k],3)}% ({data_dictionary["vote count"][k]})\n'
    out_file.write(line5)
line6="----------------------------\n"
out_file.write(line6)
line7=f"Winner:  {winner_name}\n"
out_file.write(str(line7))
line8= "----------------------------\n"
out_file.write(line8)
out_file.close()