# ElectionAndBudgetAnalysis


Budget Data Analysis(PyBank)

  The code in main.py starts with creating an appropriate path to the budget_data.csv file that will be used for the analysis. Once this is done, the csv file is opened and first value (the date) in each row is placed into a list. 

  The sum of the profits/losses (second value) is also calculated. Each individual profit/loss is placed into a second list. The difference between each row and its predecessor is calculated and appended into a third list. This loop starts at the second value in the list because the first value has no predecessor. The sum of all the values in this third list is calculated to get the sum of total differences. This total difference sum is then divided by the number of differences to attain the average change in differences. For more accuracy, this mean is rounded to 2 decimal places. Next, the highest difference value and its corresponding date is calculated. In order to do this, a new list is created that removes the first value in the date list. The reason for this is the same as why the earlier started at the second value in the list: the first value doesn't have a predecessor so you are unable to calculate the difference for this value. 

  This new date is then zipped with the list of differences. Each of the values in this zipped tupple are looked at one after another, and if the second value of the tupple is greater than the value of its predecessor, this larger value will be stored as the greater value. The first value in the respective tuple will be stored as the date of the greater value. Similarly, if the tuple's second value is lower than any of the values previous to it, it will be stored as the lowest value and its corresponding date will be stored as well. This process will continue all the way to the end of the tuple and the program will have stored the highest value, its respective date, the lowest value, and its respective date. 
  
  A series of print statements will show the complete analysis in the terminal. Lastly, a new text file will be created under the Analysis folder which also contains the same analysis that the terminal shows.  
