year = 2016
data = {'Nico Rosberg': [25, 50, 75, 100, 100, 106, 116, 141, 153, 168, 186, 198, 223, 248, 273, 288, 313, 331, 349, 367, 385], 
        'Lewis Hamilton': [18, 33, 39, 57, 57, 82, 107, 117, 142, 167, 192, 217, 232, 250, 265, 265, 280, 305, 330, 355, 380], 
        'Sebastian Vettel': [15, 15, 33, 33, 48, 60, 78, 96, 96, 98, 110, 120, 128, 143, 153, 153, 165, 177, 187, 197, 212], 
        'Daniel Ricciardo': [12, 24, 36, 36, 48, 66, 72, 78, 88, 100, 115, 133, 151, 161, 179, 204, 212, 227, 242, 246, 256], 
        'Felipe Massa': [10, 14, 22, 32, 36, 37, 37, 38, 38, 38, 38, 38, 39, 41, 41, 41, 43, 49, 51, 51, 53], 
        'Romain Grosjean': [8, 18, 18, 22, 22, 22, 22, 22, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29], 
        'Nico Hulkenberg': [6, 6, 6, 6, 6, 14, 18, 20, 20, 26, 27, 33, 45, 46, 46, 50, 54, 54, 60, 66, 72], 
        'Valtteri Bottas': [4, 6, 7, 19, 29, 29, 44, 52, 54, 54, 56, 58, 62, 70, 70, 80, 81, 81, 85, 85, 85], 
        'Carlos Sainz': [2, 2, 4, 4, 12, 16, 18, 18, 22, 26, 30, 30, 30, 30, 30, 30, 30, 38, 38, 46, 46], 
        'Max Verstappen': [1, 9, 13, 13, 38, 38, 50, 54, 72, 90, 100, 115, 115, 121, 129, 147, 165, 165, 177, 192, 204], 
        'Jolyon Palmer': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
        'Kevin Magnussen': [0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7], 
        'Sergio Perez': [0, 0, 0, 2, 8, 23, 24, 39, 39, 47, 47, 48, 58, 62, 66, 74, 80, 84, 85, 97, 101], 
        'Jenson Button': [0, 0, 0, 1, 3, 5, 5, 5, 13, 13, 13, 17, 17, 17, 17, 19, 19, 21, 21, 21, 21], 
        'Felipe Nasr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2], 
        'Pascal Wehrlein': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Marcus Ericsson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Kimi Räikkönen': [0, 18, 28, 43, 61, 61, 69, 81, 96, 106, 114, 122, 124, 136, 148, 160, 170, 170, 178, 178, 186], 
        'Rio Haryanto': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Esteban Gutierrez': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Fernando Alonso': [0, 0, 0, 8, 8, 18, 18, 18, 18, 18, 24, 24, 30, 30, 36, 42, 42, 52, 52, 53, 54], 
        'Daniil Kvyat': [0, 6, 21, 21, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 25, 25, 25, 25, 25, 25, 25], 
        'Stoffel Vandoorne': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Esteban Ocon': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Nico Rosberg': 'Mercedes', 'Lewis Hamilton': 'Mercedes', 'Sebastian Vettel': 'Ferrari', 
                      'Daniel Ricciardo': 'Red Bull Racing TAG Heuer', 'Felipe Massa': 'Williams Mercedes', 
                      'Romain Grosjean': 'Haas Ferrari', 'Nico Hulkenberg': 'Force India Mercedes', 
                      'Valtteri Bottas': 'Williams Mercedes', 'Carlos Sainz': 'Toro Rosso Ferrari', 
                      'Max Verstappen': 'Red Bull Racing TAG Heuer', 'Jolyon Palmer': 'Renault', 
                      'Kevin Magnussen': 'Renault', 'Sergio Perez': 'Force India Mercedes', 'Jenson Button': 'McLaren Honda', 
                      'Felipe Nasr': 'Sauber Ferrari', 'Pascal Wehrlein': 'MRT Mercedes', 'Marcus Ericsson': 'Sauber Ferrari', 
                      'Kimi Räikkönen': 'Ferrari', 'Rio Haryanto': 'MRT Mercedes', 'Esteban Gutierrez': 'Haas Ferrari', 
                      'Fernando Alonso': 'McLaren Honda', 'Daniil Kvyat': 'Toro Rosso Ferrari', 'Stoffel Vandoorne': 'McLaren Honda', 
                      'Esteban Ocon': 'MRT Mercedes'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing TAG Heuer': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Honda': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Haas Ferrari': 'Haas', 
              'Toro Rosso Ferrari': 'Toro Rosso', 
              'Williams Mercedes': 'Williams', 
              'Renault': 'Renault',
              'MRT Mercedes': 'MRT'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Force India': '#F363B9', 
                     'Sauber': '#1d45aa', 
                     'Haas': '#F7F5EC', 
                     'Toro Rosso': '#A39064',
                     'Williams': '#00A0DE', 
                     'Renault': '#FFF500',
                     'MRT': '#FF0000'}
driverTeamData = {driver: teamChange[team] for driver, team in tempDriverTeamData.items()}
teamsWithDrivers = {}
for driver, team in driverTeamData.items():
    if team not in teamsWithDrivers:
        teamsWithDrivers[team] = []
    teamsWithDrivers[team].append(driver)

teamsWithPoints = {}
for team in teamsWithDrivers:
    tempList = []
    for driver in teamsWithDrivers[team]:
        if tempList == []:
            tempList = data[driver]
        else:
            tempList = [temp + pts for temp, pts in zip(tempList, data[driver])]
    teamsWithPoints[team] = tempList
teamsWithPoints = dict(sorted(teamsWithPoints.items(), key=lambda item: item[1][-1], reverse=True))
for team in teamsWithPoints:
    teamsWithPoints[team] = [teamsWithPoints[team]]

for team in teamsWithPoints:
    points = teamsWithPoints[team][0]
    delta = [points[0]]
    for i in range(len(points) - 1):
        delta.append(points[i+1] - points[i])
    teamsWithPoints[team].append(delta)

delta = {key:value[1] for key, value in teamsWithPoints.items()}

driverDelta = {key:None for key in data}
for driver in data:
    points = data[driver]
    tempDelta = [points[0]]
    for i in range(len(points) - 1):
        tempDelta.append(points[i+1] - points[i])
    driverDelta[driver] = tempDelta

driverData = data
driverDelta = driverDelta

driverData = {key:[value1, value2] for key, value1, value2 in zip(driverData, driverData.values(), driverDelta.values())}


raceLocations = ["Australia", "Bahrain", "China", "Russia", "Spain",
                 "Monaco", "Canada", "Azerbaijan", "Austria", "Great Britain",
                 "Hungary", "Germany", "Belgium", "Italy", "Singapore",
                 "Malaysia", "Japan", "United States", "Mexico", "Brazil",
                 "Abu Dhabi"]

