year = 2015
data = {'Lewis Hamilton': [25, 43, 68, 93, 111, 126, 151, 169, 194, 202, 227, 252, 252, 277, 302, 327, 345, 363, 381], 
        'Nico Rosberg': [18, 33, 51, 66, 91, 116, 134, 159, 177, 181, 199, 199, 211, 229, 229, 247, 272, 297, 322], 
        'Sebastian Vettel': [15, 40, 55, 65, 80, 98, 108, 120, 135, 160, 160, 178, 203, 218, 236, 251, 251, 266, 278], 
        'Felipe Massa': [12, 20, 30, 31, 39, 39, 47, 62, 74, 74, 82, 97, 97, 97, 109, 109, 117, 117, 121], 
        'Felipe Nasr': [10, 10, 14, 14, 14, 16, 16, 16, 16, 16, 16, 16, 17, 17, 25, 27, 27, 27, 27], 
        'Daniel Ricciardo': [8, 9, 11, 19, 25, 35, 35, 36, 36, 51, 51, 55, 73, 73, 73, 74, 84, 84, 92], 
        'Nico Hulkenberg': [6, 6, 6, 6, 6, 6, 10, 18, 24, 24, 24, 30, 30, 38, 38, 38, 44, 52, 58], 
        'Marcus Ericsson': [4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 9, 9, 9, 9, 9, 9, 9, 9], 
        'Carlos Sainz': [2, 6, 6, 6, 8, 9, 9, 9, 9, 9, 9, 9, 11, 12, 12, 18, 18, 18, 18], 
        'Sergio Perez': [1, 1, 1, 5, 5, 11, 11, 13, 15, 15, 25, 33, 39, 39, 54, 64, 68, 68, 78], 
        'Jenson Button': [0, 0, 0, 0, 0, 4, 4, 4, 4, 6, 6, 6, 6, 6, 8, 16, 16, 16, 16], 
        'Kimi Räikkönen': [0, 12, 24, 42, 52, 60, 72, 72, 76, 76, 82, 92, 107, 119, 123, 123, 123, 135, 150], 
        'Max Verstappen': [0, 6, 6, 6, 6, 6, 6, 10, 10, 22, 26, 26, 30, 32, 33, 45, 47, 49, 49], 
        'Romain Grosjean': [0, 0, 6, 12, 16, 16, 17, 17, 17, 23, 38, 38, 38, 44, 44, 44, 45, 49, 51], 
        'Pastor Maldonado': [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 12, 12, 12, 16, 22, 26, 26, 27, 27], 
        'Daniil Kvyat': [0, 2, 2, 4, 5, 17, 19, 19, 27, 45, 57, 58, 66, 66, 76, 76, 88, 94, 95], 
        'Kevin Magnussen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Valtteri Bottas': [0, 10, 18, 30, 42, 42, 57, 67, 77, 77, 79, 91, 101, 111, 111, 111, 126, 136, 136], 
        'Roberto Merhi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Fernando Alonso': [0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11], 
        'Will Stevens': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Alexander Rossi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Lewis Hamilton': 'Mercedes', 'Nico Rosberg': 'Mercedes', 'Sebastian Vettel': 'Ferrari', 
                      'Felipe Massa': 'Williams Mercedes', 'Felipe Nasr': 'Sauber Ferrari', 'Daniel Ricciardo': 'Red Bull Racing Renault', 
                      'Nico Hulkenberg': 'Force India Mercedes', 'Marcus Ericsson': 'Sauber Ferrari', 'Carlos Sainz': 'STR Renault', 
                      'Sergio Perez': 'Force India Mercedes', 'Jenson Button': 'McLaren Honda', 'Kimi Räikkönen': 'Ferrari', 
                      'Max Verstappen': 'STR Renault', 'Romain Grosjean': 'Lotus Mercedes', 'Pastor Maldonado': 'Lotus Mercedes', 
                      'Daniil Kvyat': 'Red Bull Racing Renault', 'Kevin Magnussen': 'McLaren Honda', 'Valtteri Bottas': 'Williams Mercedes', 
                      'Roberto Merhi': 'Marussia Ferrari', 'Fernando Alonso': 'McLaren Honda', 'Will Stevens': 'Marussia Ferrari', 
                      'Alexander Rossi': 'Marussia Ferrari'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Renault': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Honda': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Lotus Mercedes': 'Lotus', 
              'STR Renault': 'Toro Rosso', 
              'Williams Mercedes': 'Williams', 
              'Marussia Ferrari': 'Marussia'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Force India': '#F363B9', 
                     'Sauber': '#1d45aa', 
                     'Toro Rosso': '#A39064',
                     'Williams': '#00A0DE', 
                     'Marussia': '#d82f20',
                     "Lotus": "#86995B"}
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


raceLocations = ["Australia", "Malaysia", "China", "Bahrain", "Spain",
                 "Monaco", "Canada", "Austria", "Great Britain", "Hungary",
                 "Belgium", "Italy", "Singapore", "Japan", "Russia",
                 "United States", "Mexico", "Brazil", "Abu Dhabi"]

