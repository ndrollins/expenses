import matplotlib.pyplot as plt
import numpy as np

expenses = [
    
        ]
gsList = [0, 58, 0]
#gsList = ['0', '58', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
eatList = [0, 25, 21]
#eatList = ['0', '25', '21', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
ratsList = [0, 0, 114]
#ratsList = ['0', '0', '114', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
clothesList = [0, 0, 0]
#clothesList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
taobaoList = [0, 0, 65]
#taobaoListList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
transportationList = [4, 18, 5]
#transportationList = ['4', '18', '5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
hotelList = [0, 0, 0]
#hotelsList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
skateboardingList = [0, 0, 0]
#skateboardingList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
otherList = [0, 0, 0]
#otherList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
paybackList = [0, 1100, 345]
#paybackList = ['0', '1100', '345', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
utilitiesList = [100, 0, 0]
#utilitiesList = ['100', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


days = []
for day in range(1,32):
    days.append(day)

groceriesSupplies = dict(zip(days,gsList))
eatingOut = dict(zip(days,gsList))
rats = dict(zip(days,gsList))
clothes = dict(zip(days,gsList))
taobao = dict(zip(days,gsList))
transportation = dict(zip(days,transportationList))
hotels = dict(zip(days,gsList))
skateboarding = dict(zip(days,gsList))
other = dict(zip(days,gsList))



x = days = np.linspace(1, 31, 3)
#y = transportationList[:]
fig, ax = plt.subplots()
ax.grid()

plt.figure(figsize=None,facecolor='magenta')

plt.plot(x, transportationList, 'bd-')
plt.plot(x, utilitiesList, "r-*")
plt.plot(x, taobaoList, "g-*")
plt.plot(x, ratsList, "y-*")
plt.plot(x, eatList, "c-*")
plt.plot(x, gsList, "m-*")
plt.xlabel('Days', fontsize=16)
plt.title('March', fontsize=26)
plt.ylabel('Expenses', fontsize=16)
plt.show()

#print(transportation)
    
#allDays = [days for day in range(1,32)]
#print(allDays)

