import os
import csv

total_months = 0
net_total = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
dates = [] 
profit_losses = []
greatest_increase_month = 0 
greatest_decrease_month = 0

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_reader = next(csvreader, None)
    header = next(csvreader, None)

    total_months += 1
    net_total += int(header[1]) 
    month_before = int(header[1]) 
    for header in csvreader:

        total_months += 1
        net_total += int(header[1])
        profitlosses_change = int(header[1]) - month_before
        dates.append(profitlosses_change)
        month_before = int(header[1])
        profit_losses.append(header[0])
        
        if int(header[1]) > greatest_increase_profits:
            greatest_increase_profits = int(header[1]) 
            greatest_increase_month = header[0] 
        if int(header[1]) < greatest_decrease_profits:
            greatest_decrease_profits = int(header[1])
            greatest_decrease_month = header[0] 
    
    greatest_profit_amount= max(dates) 
    greatest_losses_amount = min(dates)
    
    average_change = sum(dates) / len(dates) 


print(f"----------------FINANCIAL ANALYSIS----------------")
print(f"--------------------------------------------------")
print(f"--------------------------------------------------")
print(f"TOTAL MONTHS: {total_months}")
print(f"TOTAL: ${net_total}")
print(f"AVERAGE CHANGE: ${average_change:.2f}")
print(f"GREATEST INCREASE IN PROFITS: {greatest_increase_month}, (${greatest_profit_amount})")
print(f"GREATEST DECRESE IN PROFITS: {greatest_decrease_month}, (${greatest_losses_amount})")

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
