# This code takes a previously created *.csv file and extracts data from a 
# specified column. Then that data is plotted onto a line graph.


import matplotlib.pyplot as plt
import csv

filename = "test.csv"
x = []
y = []

with open(filename, 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    counter = 0
    for row in plots:
        # x.append(int(row[0+1]))
        # y.append(counter)
        # counter += 1
        # print(plots)
        if counter != 0:
            print(row[0])
            print(counter)
            x.append(row[0])
            y.append(counter)
        counter += 1

plt.plot(y, x, label='ETHUSD Prices')
plt.title('ETHUSD Prices')
plt.xlabel('Time (1 s)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
