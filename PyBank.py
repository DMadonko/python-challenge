import os
import csv

csvpath = os.path.join(".","Resources", "budget_data.csv")
with open("budget_data.csv", "r") as budget_file:
    budget_csv_reader = csv.reader(budget_file, delimiter = ",")
    header = next(budget_csv_reader)

months = []
profits_losses = []
change = []
greatestincdate = ""
greatstdecdate = ""

# The total number of months included in the dataset
for row in budget_csv_reader:
    months.append(row[0])

# The net total amount of "Profit/Losses" over the entire period
for row in budget_csv_reader:
    profits_losses.append(int(row[1]))

# The average of the changes in "Profit/Losses" over the entire period
for i in range(len(change)-1):
    profits_losses.append(change[i+1]- change[i])

# The greatest increase in profits (date and amount) over the entire period
greatestinc = max(change)
greatestincdate = str(months[change.index(max(change))])

# The greatest decrease in losses (date and amount) over the entire period
greatestdec = min(change)
greatestdecdate = str(months[change.index(min(change))])

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", len(months))
print("Net Total: $", sum(profits_losses))
print("Average Change: $", round(change))  
print("Greatest Increase: ", greatestincdate, "($", greatestinc,")")
print("Greatest Decrease: ", greatestdecdate, "($", greatestdec,")")