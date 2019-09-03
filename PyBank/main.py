#PyBank - Homework 3

## Data is composed of two columns, Data and Profit/Losses
## You will give a set of financial data called [budget_data.csv]
##Your task is to create a Python script that analyzes the records 
## to calculate each of the following:

## The total number of months included in the dataset
## The net total amount of "Profit/Losses" over the entire period
## The average of the changes in "Profit/Losses" over the entire period
## The greatest increase in profits (date and amount) over the entire period
## The greatest decrease in losses (date and amount) over the entire period

# From what I can already see, there are 86 Months, first row is taken up 
# by Date,Profit/Losses -- Go through notes starting from August 20th, skipping header!
# += -- StackOverflow - add whatever is to the right of the += to the variable on the left of the +=
# https://www.quora.com/What-does-total-+-a-in-Python-mean

# 1st - Import the necessary dependencies for os.path.join() -- (August 20th Notes)
import os
import csv

# 2nd - Create necessary variables to solve the problem, reference what's needed
# [] -- shows us that we are working with a list, 0-- working with a variable, setting up a counter
# Variables - Total Months, Net Total, Average of Changes (Equation), Greatest Increase in Profit, 
# Greatest Decrease in Profits | CSV Variables - Date, Profit/Losses -- Variable to show changes?
total_months = 0
net_total = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
dates = [] 
profit_losses = []
greatest_increase_month = 0 #10 Going to use this as a variable, idea from looking at Elie's code
greatest_decrease_month = 0 #11 Greatest increase in dates and profit, add to top variable _profits

# 3rd - Read in a .csv file  -- opening the file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# 4th - Opening the file (August 24th Notes) -- No space in between ""
with open (csvpath, newline="") as csvfile:
    
    # 5th - Reading our dataset 
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # 6th - To skip the header simply call for next(reader, None)
    csv_reader = next(csvreader, None)
    header = next(csvreader, None)

    # 7th - The total number of months included in the dataset -- using += - variable total_months will be adding the value
    # of 1 until it hits the end of the CSV file (csvreader)
    # Equations needed in loop (Important for setting the variables with header, without this my answers were off by a month,
    # so this gives me the first row to start with, next it'll add the second row to the first and so on): 
    total_months += 1
    net_total += int(header[1]) #int(row[location])
    month_before = int(header[1]) #knowing that the previous one worked as a starting point in net_total - added from #9
    for header in csvreader:

        total_months += 1

    #print(f"Total Months: {total_months}")

    # 8th - The net total amount of "Profit/Losses" over the entire period -- Add all the values of everything 
    # next to Dates column -- list/array order starts from 0, so the values (Profit/Losses) needed are in 1 of the CSV
    # StackOverflow for finding a sum,  total += float(row[1]), don't need float for this because there are no decimals
        net_total += int(header[1])
    
    #print(f"Total: ${net_total}")

    # 9th - The average of the changes in "Profit/Losses" over the entire period
    # Need to find a way to find the average, things needed, difference in profit/losses between a month and a 
    # previous month, divide that with the total number of months. Do I need more variables? This is because I 
    # need something to represent what's needed from above, might be useful for the Greatest Increase and Decrease as well
    # If needed add variables to #2, something is needed as a new equation as well in #7
        profitlosses_change = int(header[1]) - month_before #using print(profitloss_change), it prints out a list of negative numbers - need to combine
        #print(profitloss_change)
        # Anthony - use .append() - StackOverflow - Append: Adds its argument as a single element to the end of a list. 
        # The length of the list increases by one. (my_list.append(object)); max and min?
        dates.append(profitlosses_change)
        month_before = int(header[1])
        profit_losses.append(header[0])
    
    # Average summary for #9, sum of list of dates in header[1] / length of list of dates header[1] 
    #average_change = sum(dates) / len(dates) #FIX INDENT? It's going through lines of loops? >> Move to the end!!!
    #print(f"Average Change: {average_change}") #decimal is too long need a round here, 2 decimal places 
    # StackOverflow recommends >>> print("{:.2f}" - similar to round, this is an fstring/decimal object
    #print(f"Average Change: ${average_change:.2f}") #might have to move this to the end

    # 10th - The greatest increase in profits date over the entire period; variable added
        if int(header[1]) > greatest_increase_profits: # if profit/losses column is greater than 0
            greatest_increase_profits = int(header[1]) # Then that zero trurns into said date
            greatest_increase_month = header[0] #New variable equals to said date
    #print(f"Greatest Increase In Profits: {greatest_increase_month}")
    
    # 11th - The greatest decrease in losses date over the entire period; variable added
        if int(header[1]) < greatest_decrease_profits:
            greatest_decrease_profits = int(header[1])
            greatest_decrease_month = header[0] 
    #print(f"Greatest Decrease In Profits: {greatest_decrease_month}")

    # 12th - Finding the greatest increase and decrease dates ; max and min
    greatest_profit_amount= max(dates) 
    greatest_losses_amount = min(dates)
    #print(f"Greatest Profit Amount: ${greatest_profit_amount}")
    #print(f"Greatest Losses Amount: ${greatest_losses_amount}")

    average_change = sum(dates) / len(dates) # 9th Part Avg Formula

# 13th - Combining and printing everything, need to comment out the prints from above and move the average formula down
# or anything else with the indents that have to be moved backed
print(f"")
print(f"FINANCIAL ANALYSIS")
print(f"")
print(f"---------------------------------------------------")
print(f"")
print(f"TOTAL MONTHS: {total_months}")
print(f"TOTAL: ${net_total}")
print(f"AVERAGE CHANGE: ${average_change:.2f}")
print(f"GREATEST INCREASE IN PROFITS: {greatest_increase_month}, (${greatest_profit_amount})")
print(f"GREATEST DECRESE IN PROFITS: {greatest_decrease_month}, (${greatest_losses_amount})")
print(f"")

# 14th - In addition, your final script should both print the analysis to the 
# terminal and export a text file with the results - Writing a csv file (August 20th - last slide of Python Cheat Sheet)
# w - write only; output shows a text on a single line, might need to use \n

data_output = os.path.join("..", "PyBank", "Resources", "final_budget_data.text")

with open(data_output, "w", newline="") as textfile:
    textfile.write(f"\n")
    textfile.write(f"FINANCIAL ANALYSIS\n")
    textfile.write(f"\n")
    textfile.write(f"---------------------------------------------------\n")
    textfile.write(f"\n")
    textfile.write(f"TOTAL MONTHS: {total_months}\n")
    textfile.write(f"TOTAL: ${net_total}\n")
    textfile.write(f"AVERAGE CHANGE: ${average_change:.2f}\n")
    textfile.write(f"GREATEST INCREASE IN PROFITS: {greatest_increase_month}, (${greatest_profit_amount})\n")
    textfile.write(f"GREATEST DECRESE IN PROFITS: {greatest_decrease_month}, (${greatest_losses_amount})\n")
    textfile.write(f"\n")
    
