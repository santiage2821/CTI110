# A brief description of the project
# February 12, 2019
# CTI-110 P2T1 - Sales Prediction
# Ericka Santiago-Brodowski

#Get the projected total sales.
total_sales = float(input('Enter the project sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profits.
print('The profit is $', format(profit, ',.2f'))
