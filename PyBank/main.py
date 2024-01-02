import csv

# open the file in read mode
filename = open('Resources/budget_data.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
month = []
totalprofit = []

# allowing for total variable to change
total = 0

# values to empty list through column iterations
for col in file:
    month.append(col['Date'])
    totalprofit.append(int(col['Profit/Losses']))

# Calculate total of profit column
for element in totalprofit:
        total += int(element)
    

average_change = round(total/len(month),2)
min_row_month = month[totalprofit.index(min(totalprofit))]
max_row_month = month[totalprofit.index(max(totalprofit))]
min_row_value = totalprofit[totalprofit.index(min(totalprofit))]
max_row_value = totalprofit[totalprofit.index(max(totalprofit))]

# printing lists
print("Financial Analysis") #Title
print("---------------------") #Spacer
print("Total months: ", len(month)) #Number of months in sheet
print("Overall profit/loss: ", total) #Overall change in value from start
print("Average monthly change", average_change) #Average change of value per month
print(f'Month with minimum profit/loss: {min_row_month} ( {min_row_value} )') #minimum value and corresponding month
print(f'Month with maximum profit/loss: {max_row_month} ( {max_row_value} )') #maximum value and corresponding month

