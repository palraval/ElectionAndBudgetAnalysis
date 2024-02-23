#importing os and csv
import os
import csv





#creating the path to the budget_data.csv data file
budget_path = os.path.join("/Users/palashraval/Desktop/UCB_Bootcamp/Bootcamp_Duplicate/Homework/ElectionAndBudgetAnalysis/PyBank/Resources/budget_data.csv")


#creates 2 lists and sets sum calculator to 0
date = []
net_value = 0
difference = []

#opens the csv file and skips the header row(1st row)
with open(budget_path) as budget:
    csv_reader = csv.reader(budget, delimiter=",")
    next(csv_reader)
#adds all the dates in the file into a list
#sums the net total of the profits/losses
#adds each profit/loss into the second list
    for row in csv_reader:
        date.append(row[0])
        net_value = net_value + int(row[1])
        difference.append(row[1])


#creates a third list
list_of_difference = []

#calculates the differences between each row and places into the third list
for i in range(1, len(difference)):
    difference2 = int(difference[i]) - int(difference[i - 1])
    list_of_difference.append(difference2)


#sets the total number of values counter to 0
count = 0

#counts the sum of total differences in the third list 
for num in list_of_difference:
    count = count + num

#finds the average change in differences to 2 decimal places
average_change = count/len(list_of_difference)
average_change = round(average_change,2)



#new list containing all the dates except the first one
new_date = date[1:]

#creates a tuple containing the dates and their respective difference compared to the date previous to it
greatest_values = zip(new_date, list_of_difference)


#sets highest and values to 0 
highest_value = 0
lowest_value = 0

for pair in greatest_values: 
#finds the highest difference value and the date associated with it
    if pair[1] > highest_value:
        highest_value = pair[1]
        highest_date = pair[0]
#finds the lowest difference value and the date associated with it
    elif pair[1] < lowest_value:
        lowest_value = pair[1]
        lowest_date = pair[0] 



#prints all the results into the terminal 
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${net_value}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {highest_date} (${highest_value})")
print(f"Greatest Decrease in Profits: {lowest_date} (${lowest_value})")

#creates and writes a .txt file containing the data's summary
with open("/Users/palashraval/Desktop/UCB_Bootcamp/Bootcamp_Duplicate/Homework/ElectionAndBudgetAnalysis/PyBank/Analysis/budget_results.txt", "w") as budgetfile:
    budgetfile.writelines(("----------------------------"))
    budgetfile.writelines("\n")
    budgetfile.writelines(f"Total Months: {len(date)}")
    budgetfile.writelines("\n")
    budgetfile.writelines(f"Total: ${net_value}")
    budgetfile.writelines("\n")
    budgetfile.writelines(f"Average Change: ${average_change}")
    budgetfile.writelines("\n")
    budgetfile.writelines(f"Greatest Increase in Profits: {highest_date} (${highest_value})")
    budgetfile.writelines("\n")
    budgetfile.writelines(f"Greatest Decrease in Profits: {lowest_date} (${lowest_value})")
