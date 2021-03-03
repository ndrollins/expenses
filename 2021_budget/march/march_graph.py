
expenses = [
    
        ]

gsList = ['0', '58']
eatList = ['0', '25']
ratsList = ['0', '0']
clothesList = ['0', '0']
taobaoListList = ['0', '0']
transportationList = ['4', '18']
hotelsList = ['0', '0']
skateboardingList = ['0', '0']
otherList = ['0', '0']


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




print(transportation)
    
#allDays = [days for day in range(1,32)]
#print(allDays)

