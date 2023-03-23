# Module 3 python challenge
# Kristen Pollok
# 3/16/2023
# pyBank/ main.py

#In this Challenge, you are tasked with creating a Python script to analyze the financial records
 #of your company. You will be given a financial dataset called budget_data.csv. The dataset is
 #composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#import dependencies
import os
import csv

budget_data_CSV = os.path.join("Resources", "budget_data.csv") #saves path of csv
months = []                                                     #create list and set variables
total_list = []
Avg_change =0

with open(budget_data_CSV, encoding ='utf') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
#count the total months
    for row in csvreader:  #adds info to the list months and total list
        months.append(row[0])
        total_list.append(row[1])
     
    total_months =int(len(months)) #length of months list is total months
    total =0
    change_num_list=[]      #set variables and create a list
    increase_profits =0
    decrease_profits =0

    for i in range(len(total_list)): #loops through the whole list
        num= int(total_list[i])
        total += num          #counts the profits and losses
        
        if i< (len(total_list)-1):
             num2=int(total_list[i+1])   #the value of the next month
             change_value= num2 - num  #calculates change value
             change_num_list.append(change_value)   #add the difference between months to a change value list
    change_num=0
    sum_change_num =0
    for j in range(len(change_num_list)):
        change_num = int(change_num_list[j])
        sum_change_num += change_num    #calculate the total of change values to calculate average change

        if ((int(change_num_list[j])) > increase_profits):   #find the greatest increase and decrease profits
            increase_profits =int(change_num_list[j])
            increase_profits_name = months[j+1]
        elif ((int(change_num_list[j])) < decrease_profits):
            decrease_profits =int(change_num_list[j])
            decrease_profits_name = months[j+1]

    Avg_change = sum_change_num / (total_months -1)
#print to terminal
print("Financial Analysis\n")
print("----------------------------")    
print("Total Months:", total_months)
print("Total: %", total )
print(f"Average Change: $ {round(Avg_change,2)}")
print(f"Greatest Increase in Profits:  {increase_profits_name} (${increase_profits})")
print(f"Greatest Decrease in Profits:  {decrease_profits_name} (${decrease_profits})")

#write print statements to the txt file

out_file = open('Analysis/output.txt', "w")
    
line1 = (f"""Financial Analysis
----------------------------
Total Months: {str(total_months)}
Total: %{str(total)}
Average Change: ${round(Avg_change,2)}
Greatest Increase in Profits: {str(increase_profits_name)} (${str(increase_profits)})
Greatest Decrease in Profits: {str(decrease_profits_name)} (${str(decrease_profits)})""")
    
out_file.write(line1)
