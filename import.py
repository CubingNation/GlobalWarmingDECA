import csv
import pandas as pd
billsSheet = pd.read_csv('C:\\Users\\suchu\\Downloads\\Bills.csv')
print ("-------------------------------------")
x = open("Bills.csv")
csv_x = csv.reader(x)
next(csv_x,None) #Eliminates first row
for row in csv_x: #for each row in the spreadsheet
    paidDate = [row[5].split('/')] 
    dueDate = [row[4].split('/')] 
    achChecker = row[7] #capture the value of the Ref. No# column
    if dueDate <= paidDate and achChecker != ("ACH"): #Comparison
        print(row[0] + "----" +row[1] +"---OVERDUE")
    #else:
        #print(row[1] + "---Overdue")
print ("-------------------------------------")

   
    