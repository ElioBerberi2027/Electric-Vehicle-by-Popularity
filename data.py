file = open("Electric_Vehicle_Population_Data.csv", "r")
reader = file.readlines()

seenCars = {} # this is going to be a dictionary that will hold the car models and the number of times they appear
seenCounty = {}
seenPostal = {}
totalCars = 0
totalInCounty = 0
print("THESE ARE EV's BY POPULARITY")
print()
# were going to use this to get the data from the csv file
for model in reader[1:]: # this is going to read the data from the csv file
    carModel = model.split(",") # this is going to split the data by the comma
    carModel = carModel[6] # this is the column that has the car model
    if carModel not in seenCars: # this is going to check if the car model is in the dictionary
        seenCars[carModel] = 1  # if it is not in the dictionary then it will add it to the dictionary
        totalCars += 1
    else:
        seenCars[carModel] += 1 # if it is in the dictionary then it will add 1 to the count
        totalCars += 1

averageTeslas = seenCars['TESLA'] / totalCars
percentTeslas = averageTeslas * 100
percentTeslas = round(percentTeslas)

for model in sorted(seenCars, key=seenCars.get, reverse=True): # this is going to sort the dictionary by the number of times the car model appears
    print(model, seenCars[model]) # this is going to print the car model and the number of times it appears

print('-------------------------------------------------------------')
print(f"Tesla makes up {percentTeslas}% of EV's in Washington State")
print('-------------------------------------------------------------')

print()
print("THES ARE COUNTIES WITH MOST TO LEAST EVs")
print()
for county in reader[1:]:
    countyName = county.split(",")
    countyName = countyName[1] # this is the column that has the conty data
    if countyName not in seenCounty: # if the county is not in the dictionary
        seenCounty[countyName] = 1 # we add it
        totalInCounty += 1
    else:  # if it is  
        seenCounty[countyName] += 1 # we add count
        totalInCounty += 1

for county in sorted(seenCounty, key=seenCounty.get, reverse=True)[:20]:
    print(county, seenCounty[county])

averageInConty = seenCounty['King'] / totalInCounty
percentInCounty = averageInConty * 100
percentInCounty = round(percentInCounty)

print('-------------------------------------------------------------')
print(f"King County makes up {percentInCounty}% of EV's in Washington State")
print('-------------------------------------------------------------')

print('-------------------------------------------------------------')
print("Postals with most to least EV's")
print('-------------------------------------------------------------')

for postal in reader[1:]:
    postalCode = postal.split(',')
    postalCode = postalCode[4]
    if postalCode not in seenPostal:
        seenPostal[postalCode] = 1
    else:
        seenPostal[postalCode] += 1

for postal in sorted(seenPostal, key=seenPostal.get, reverse=True)[:20]:
    print(postal, seenPostal[postal])