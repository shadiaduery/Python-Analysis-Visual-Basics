"PyBank Homework Solution"

#Import required packages
import csv
import os

#Files to load and output
file_to_load = os.path.join('Resources','budget_data.csv')
file_to_output = os.path.join('analysis','output_budget_data.txt')

# Create placeholders for the variables
months=0
pl_total=0
pl_change=0
total_pl_change=0
first_time= True
greatest_pl_increase= 0
greatest_pl_decrease= 9999999
greatest_month_increase=""
greaters_month_decrease=""

with open(file_to_load) as budget_data:

    reader = csv.reader(budget_data, delimiter=",")

    print(reader)

    header= next(reader)

    # Loop through each row, re-grab each field and store in the new list
    for row in reader:
    
        # Grab month and store it into a variable and calculate the total number of months
        months = months + 1

        # Grab profit/loss and store it into a variable and calculate the profit/loss total
        pl_total = pl_total + int(row[1])

        # Calculate profit/loss change
        if not first_time:
            pl_change = int(row[1])-previous
            total_pl_change = round(total_pl_change + pl_change)

            # If the current change is greater than previous change 
            if pl_change > greatest_pl_increase:
                greatest_pl_increase = pl_change
                greatest_month_increase = (row[0]) 

            # If the current change is greater than previous change 
            if pl_change < greatest_pl_decrease:
                greatest_pl_decrease = pl_change
                greatest_month_decrease = (row[0])

        previous = int(row[1])
        first_time = False

    print("Final Analysis")
    print("_________________________")
    print("Total Months: ",(months))
    print("Total: $",(pl_total))
    print("Average Change: ", round(total_pl_change/months - 1))
    print("Greatest Increase in Profits: ",greatest_month_increase, greatest_pl_increase)
    print("Greatest Decrease in Profits: ",greatest_month_decrease, greatest_pl_decrease)

# Specify the file to write to
file_to_output = os.path.join('analysis','output_budget_data.txt')

# Open the file using the "write" mode. Specify the variable to hold the contents
output = open(file_to_output, 'w')
output.write("Financial Analysis\n")
output.write("____________________________\n")
output.write(f"Total Months: {months}\n")
output.write(f"Total: $ {pl_total}\n")
output.write(f"Average Change:{total_pl_change/months - 1}\n")
output.write(f"Greatest Increase in Profits: {greatest_month_increase, greatest_pl_increase}\n")
output.write(f"Greatest Decrease in Profits: {greatest_month_decrease, greatest_pl_decrease}\n")