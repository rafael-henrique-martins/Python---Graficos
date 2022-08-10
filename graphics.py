import matplotlib.pyplot as plt
import numpy as np

sale_of_the_month = np.array([1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762])
month = np.array(['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'])

# Step 1 - pass a list and use .show to show
plt.plot(sale_of_the_month)
plt.show()

# Step 2 - adding label
plt.plot(sale_of_the_month)
plt.ylabel("Sale")
plt.xlabel('Month')
plt.show()

# Step 2.1 - Inserting the names for the labels on the x and y axes
plt.plot(month, sale_of_the_month)
plt.ylabel("Sale")
plt.xlabel('Month')
plt.show()

# Step 3 - Inserting a scale for the graph
plt.plot(month, sale_of_the_month)
plt.ylabel("Sale")
plt.xlabel('month')
plt.axis([0, 12, 0, 3000])
plt.show()

# Step 3.1 - Same as the previous step, difference that I don't need to manually put the beginning and end of the graph
plt.plot(month, sale_of_the_month)
plt.ylabel("Sale")
plt.xlabel('month')
plt.axis([0, 12, 0, max(sale_of_the_month)])
plt.show()

# Step 3.2 - Same as the previous step, but adding value to improve the graph
plt.plot(month, sale_of_the_month)
plt.ylabel("Sale")
plt.xlabel('month')
plt.axis([0, 12, 0, max(sale_of_the_month) + 500])
plt.show()

# plt.fill_between(sale_of_the_month, month, alpha=0.2, where=(sale_of_the_month < 0), color='red')
