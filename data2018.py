year = 2018
data = {'Sebastian Vettel': [25, 50, 54, 66, 78, 96, 121, 131, 146, 171, 171, 189, 214, 226, 241, 256, 264, 276, 294, 302, 320], 
        'Lewis Hamilton': [18, 33, 45, 70, 95, 110, 120, 145, 145, 163, 188, 213, 231, 256, 281, 306, 331, 346, 358, 383, 408], 
        'Kimi Räikkönen': [15, 15, 30, 48, 48, 60, 68, 83, 101, 116, 131, 146, 146, 164, 174, 186, 196, 221, 236, 251, 251], 
        'Daniel Ricciardo': [12, 12, 37, 37, 47, 72, 84, 96, 96, 106, 106, 118, 118, 118, 126, 134, 146, 146, 146, 158, 170], 
        'Fernando Alonso': [10, 16, 22, 28, 32, 32, 32, 32, 36, 40, 40, 44, 44, 44, 50, 50, 50, 50, 50, 50, 50], 
        'Max Verstappen': [8, 8, 18, 18, 33, 35, 50, 68, 93, 93, 105, 105, 120, 130, 148, 158, 173, 191, 216, 234, 249], 
        'Nico Hulkenberg': [6, 14, 22, 22, 22, 26, 32, 34, 34, 42, 52, 52, 52, 52, 53, 53, 53, 61, 69, 69, 69], 
        'Valtteri Bottas': [4, 22, 40, 40, 58, 68, 86, 92, 92, 104, 122, 132, 144, 159, 171, 189, 207, 217, 227, 237, 247], 
        'Stoffel Vandoorne': [2, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12], 
        'Carlos Sainz': [1, 1, 3, 13, 19, 20, 24, 28, 28, 28, 28, 30, 30, 34, 38, 38, 39, 45, 45, 45, 53], 
        'Sergio Perez': [0, 0, 0, 15, 17, 17, 17, 17, 23, 24, 30, 30, 40, 46, 46, 47, 53, 57, 57, 58, 62], 
        'Esteban Ocon': [0, 1, 1, 1, 1, 9, 11, 11, 19, 25, 29, 29, 37, 45, 45, 47, 49, 49, 49, 49, 49], 
        'Charles Leclerc': [0, 0, 0, 8, 9, 9, 10, 11, 13, 13, 13, 13, 13, 13, 15, 21, 21, 21, 27, 33, 39], 
        'Lance Stroll': [0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6], 
        'Brendon Hartley': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4], 
        'Romain Grosjean': [0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 20, 21, 27, 27, 27, 27, 31, 31, 31, 35, 37], 
        'Kevin Magnussen': [0, 10, 11, 11, 19, 19, 19, 27, 37, 39, 39, 45, 49, 49, 49, 53, 53, 53, 53, 55, 56], 
        'Pierre Gasly': [0, 12, 12, 12, 12, 18, 18, 18, 18, 18, 18, 26, 28, 28, 28, 28, 28, 28, 29, 29, 29], 
        'Marcus Ericsson': [0, 2, 2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 6, 6, 6, 6, 6, 7, 9, 9, 9], 
        'Sergey Sirotkin': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Sebastian Vettel': 'Ferrari', 'Lewis Hamilton': 'Mercedes', 'Kimi Räikkönen': 'Ferrari', 
                      'Daniel Ricciardo': 'Red Bull Racing TAG Heuer', 'Fernando Alonso': 'McLaren Renault', 
                      'Max Verstappen': 'Red Bull Racing TAG Heuer', 'Nico Hulkenberg': 'Renault', 'Valtteri Bottas': 'Mercedes', 
                      'Stoffel Vandoorne': 'McLaren Renault', 'Carlos Sainz': 'Renault', 'Sergio Perez': 'Force India Mercedes', 
                      'Esteban Ocon': 'Force India Mercedes', 'Charles Leclerc': 'Sauber Ferrari', 'Lance Stroll': 'Williams Mercedes', 
                      'Brendon Hartley': 'Scuderia Toro Rosso Honda', 'Romain Grosjean': 'Haas Ferrari', 'Kevin Magnussen': 'Haas Ferrari', 
                      'Pierre Gasly': 'Scuderia Toro Rosso Honda', 'Marcus Ericsson': 'Sauber Ferrari', 'Sergey Sirotkin': 'Williams Mercedes'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing TAG Heuer': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Renault': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Haas Ferrari': 'Haas', 
              'Scuderia Toro Rosso Honda': 'Toro Rosso', 
              'Williams Mercedes': 'Williams', 
              'Renault': 'Renault'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Force India': '#F363B9', 
                     'Sauber': '#A50F2D', 
                     'Haas': '#F7F5EC', 
                     'Toro Rosso': '#A39064',
                     'Williams': '#00A0DE', 
                     'Renault': '#FFF500'}
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


raceLocations = ["Australia", "Bahrain", "China", "Azerbaijan", "Spain", 
                 "Monaco", "Canada", "France", "Austria", "Great Britain", 
                 "Germany", "Hungary", "Belgium", "Italy", "Singapore", 
                 "Russia", "Japan", "United States", "Mexico", "Brazil", 
                 "Abu Dhabi"]

