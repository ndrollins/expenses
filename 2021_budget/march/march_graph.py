import matplotlib.pyplot as plt
import numpy as np

expenses = [
    
        ]
gsList = [0, 58, 0, 0, 60 + 180 + 35, 4, 0, 26, 0, 0, 0, 54 + 13]
#gsList = ['0', '58', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
eatList = [0, 25, 21, 0, 0, 70, 457, 90, 50, 244, 0, 0]
#eatList = ['0', '25', '21', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
ratsList = [0, 0, 114, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#ratsList = ['0', '0', '114', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
clothesList = [0, 0, 0, 0, 0, 43 + 43 + 59, 0, 47 + 33, 0, 0, 0, 0]
#clothesList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
taobaoList = [0, 0, 65, 0, 25, 0, 0, 0, 0, 0, 0, 31]
#taobaoListList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
transportationList = [4, 18, 5, 1, 24, 22, 0, 15, 34, 50, 58, 6]
#transportationList = ['4', '18', '5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
hotelList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#hotelsList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
skateboardingList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#skateboardingList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
otherList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#otherList = ['0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
paybackList = [0, 1100, 345, 0, 0, 0, 0, 200, 0, 0, 0, 100]
#paybackList = ['0', '1100', '345', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
utilitiesList = [100, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0]
#utilitiesList = ['100', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


days = []
for day in range(1,32):
    days.append(day)

#groceriesSupplies = dict(zip(days,gsList))
#eatingOut = dict(zip(days,gsList))
#rats = dict(zip(days,gsList))
#clothes = dict(zip(days,gsList))
#taobao = dict(zip(days,gsList))
#transportation = dict(zip(days,transportationList))
#hotels = dict(zip(days,gsList))
#skateboarding = dict(zip(days,gsList))
#other = dict(zip(days,gsList))

gsTotal = sum(gsList)
eatTotal = sum(eatList)
taobaoTotal = sum(taobaoList)
ratsTotal = sum(ratsList)
utilitiesTotal = sum(utilitiesList)
transportationTotal = sum(transportationList)
clothesTotal = sum(clothesList)
grandTotal = gsTotal + eatTotal + taobaoTotal + ratsTotal + utilitiesTotal + transportationTotal + clothesTotal

def listLength():
    print("gs list = " + str(len(gsList)))
    print("eat list = " + str(len(eatList)))
    print("taobao list = " + str(len(taobaoList)))
    print("rats list = " + str(len(ratsList)))
    print("utilities list = " + str(len(utilitiesList)))
    print("transportation list = " + str(len(transportationList)))
    print('clothes list = ' + str(len(clothesList)))
    

listLength()

x = days = np.linspace(1, 12, 12)
y = otherList
fig, ax = plt.subplots()
ax.grid()

plt.figure(figsize=None,facecolor='white')

plt.plot(x, transportationList, 'bd-')
plt.plot(x, utilitiesList, "r-*")
plt.plot(x, taobaoList, "g-*")
plt.plot(x, ratsList, "y-*")
plt.plot(x, eatList, "c-*")
plt.plot(x, gsList, "m-*")
plt.plot(x, clothesList, "k-*")
plt.xlabel('Days', fontsize=16)
plt.title('March', fontsize=26)
plt.ylabel('Expenses', fontsize=16)


plt.errorbar(x, transportationList, label=f'transportation total: {transportationTotal}')
plt.errorbar(x, utilitiesList, label=f'utilites total: {utilitiesTotal}')
plt.errorbar(x, taobaoList, label=f'taobao total: {taobaoTotal}')
plt.errorbar(x, ratsList, label=f'rats total: {ratsTotal}')
plt.errorbar(x, clothesList, label=f'clothes total: {clothesTotal}')
plt.errorbar(x, eatList, label=f'fine dining total: {eatTotal}')
plt.errorbar(x, gsList, label=f'groceries and supplies total: {gsTotal}')
plt.errorbar(x, y, label=f'Grand total: {grandTotal}')
plt.legend()
plt.show()
#print(transportation)
    
#allDays = [days for day in range(1,32)]
#print(allDays)

