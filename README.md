# ElectionAndBudgetAnalysis


## _Budget Data Analysis(PyBank)_

    The code in main.py starts with creating an appropriate path to the budget_data.csv file that will be used for the analysis. Once this is done, the csv file is opened and first value (the date) in each row is placed into a list. 

    The sum of the profits/losses (second value) is also calculated. Each individual profit/loss is placed into a second list. The difference between each row and its predecessor is calculated and appended into a third list. This loop starts at the second value in the list because the first value has no predecessor. The sum of all the values in this third list is calculated to get the sum of total differences. This total difference sum is then divided by the number of differences to attain the average change in differences. For more accuracy, this mean is rounded to 2 decimal places. Next, the highest difference value and its corresponding date is calculated. In order to do this, a new list is created that removes the first value in the date list. The reason for this is the same as why the earlier started at the second value in the list: the first value doesn't have a predecessor so you are unable to calculate the difference for this value. 

    This new date is then zipped with the list of differences. Each of the values in this zipped tupple are looked at one after another, and if the second value of the tupple is greater than the value of its predecessor, this larger value will be stored as the greater value. The first value in the respective tuple will be stored as the date of the greater value. Similarly, if the tuple's second value is lower than any of the values previous to it, it will be stored as the lowest value and its corresponding date will be stored as well. This process will continue all the way to the end of the tuple and the program will have stored the highest value, its respective date, the lowest value, and its respective date. 
  
    A series of print statements will show the complete analysis in the terminal. Lastly, a new text file will be created under the Analysis folder which also contains the same analysis that the terminal shows.  

## _Election Data Analysis(PyPoll)_

    The main.py file under the PyPoll folder firstly establishes a path to the election_data.csv which contains the data that will be analyzed here. This csv file is opened and the number of rows is counted to total the amount of voters that are included in this data file. For each row, the third value in this file (candidate's name) is also looked at. If the candidate's name is not present inside a newly made dictionary, the candidate's name will be become the key and the value will be set to 1. If the candidate's name is present in the dictionary, the value of that candidate's key increases by one. After the final row has passed, the final result will be a dictionary containing all the candidate's names and the number of times that their name appeared. From this, the sum of total votes is found by adding up all the values in the dictionary.

    A second dictionary is created which will contain the vote percentage each candidate received. This is done by making a loop of each candidate's name and making it the key for the second dictionary. The value of each key is then found by accessing the value of the first dictionary for each candidate (vote count), dividing by the sum of total votes, multiplying by 100, and rounding to three decimal points. This will result in a dictionary that contains the candidate's names as the key and this calculated percentage for each candidate as the corresponding value. A series of print statements are then used to display the total votes, the candidate's names, the count of votes each of them received, and the percentage of the votes for each candidate. 

    Next, the keys inside the first dictionary are found (candidate's names) and then looped to separate each candidate's name and individually put into an empty list. Likewise, the values in the first dictionary are found (candidate's votes), looped to separate each vote, and placed into another empty list. Each element of this second list is compared to the element before it. If the element is greater than its predecessor, the vote is stored. The corresponding index of this stored vote value is then used to access the first list and that candidate's name is stored as well. The purpose of all of this is to determine which candidate has the highest vote and should be declared the winner of the election. A few print statements are placed at the end to show the winner in the terminal. 

    Finally, a new text file will be created under the Analysis folder that will display the results of the analysis like the terminal does. 


