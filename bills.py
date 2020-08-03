import csv
from datetime import datetime
import pandas as pd

f=open(r'D:\Users\KasaiYuki\Downloads\BillPayments.csv')
csv_f = csv.reader(f)

data = []
for row in csv_f:
    data.append(row)


def whatsDue():
    today = datetime.today()
    dueDates = []
    for row in data:
        dueDates.append(row[4])
        
    dueDates.pop(0)
    pastDue = []
    
    for i in range(len(dueDates)):
        dateDue = datetime.strptime(dueDates[i], '%m/%d/%y')
        if(today > dateDue):
            pastDue.append(data[i+1][1])
            
    return pastDue