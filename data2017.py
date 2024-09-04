year = 2017
data = {'Sebastian Vettel': [25, 43, 68, 86, 104, 129, 141, 153, 171, 177, 202, 220, 235, 235, 247, 247, 265, 277, 302, 317], 
        'Lewis Hamilton': [18, 43, 61, 73, 98, 104, 129, 139, 151, 176, 188, 213, 238, 263, 281, 306, 331, 333, 345, 363], 
        'Valtteri Bottas': [15, 23, 38, 63, 63, 75, 93, 111, 136, 154, 169, 179, 197, 212, 222, 234, 244, 262, 280, 305], 
        'Kimi Räikkönen': [12, 22, 34, 49, 49, 67, 73, 73, 83, 98, 116, 128, 138, 138, 138, 148, 163, 178, 193, 205], 
        'Max Verstappen': [10, 25, 25, 35, 35, 45, 45, 45, 45, 57, 67, 67, 68, 68, 93, 111, 123, 148, 158, 168], 
        'Felipe Massa': [8, 8, 16, 18, 18, 20, 20, 20, 22, 23, 23, 27, 31, 31, 33, 34, 36, 36, 42, 43], 
        'Sergio Perez': [6, 8, 14, 22, 34, 34, 44, 44, 50, 52, 56, 56, 58, 68, 76, 82, 86, 92, 94, 100], 
        'Carlos Sainz': [4, 10, 10, 11, 17, 25, 25, 29, 29, 29, 35, 36, 36, 48, 48, 48, 54, 54, 54, 54], 
        'Daniil Kvyat': [2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5], 
        'Esteban Ocon': [1, 2, 3, 9, 19, 19, 27, 35, 39, 43, 45, 47, 55, 56, 57, 65, 73, 83, 83, 87], 
        'Nico Hulkenberg': [0, 0, 2, 6, 14, 14, 18, 18, 18, 26, 26, 34, 34, 34, 34, 34, 34, 34, 35, 43], 
        'Antonio Giovinazzi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Stoffel Vandoorne': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 7, 13, 13, 13, 13, 13, 13], 
        'Fernando Alonso': [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 10, 10, 10, 10, 10, 10, 10, 11, 15, 17], 
        'Kevin Magnussen': [0, 4, 4, 4, 4, 5, 5, 11, 11, 11, 11, 11, 11, 11, 11, 15, 15, 19, 19, 19], 
        'Lance Stroll': [0, 0, 0, 0, 0, 0, 2, 17, 18, 18, 18, 18, 24, 28, 32, 32, 32, 40, 40, 40], 
        'Daniel Ricciardo': [0, 12, 22, 22, 37, 52, 67, 92, 107, 117, 117, 132, 144, 162, 177, 192, 192, 192, 200, 200], 
        'Marcus Ericsson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Jolyon Palmer': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8], 
        'Romain Grosjean': [0, 0, 4, 4, 5, 9, 10, 10, 18, 18, 18, 24, 24, 26, 26, 28, 28, 28, 28, 28], 
        'Pascal Wehrlein': [0, 0, 0, 0, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 
        'Jenson Button': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Paul di Resta': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Pierre Gasly': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Brendon Hartley': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Sebastian Vettel': 'Ferrari', 'Lewis Hamilton': 'Mercedes', 'Valtteri Bottas': 'Mercedes', 
                      'Kimi Räikkönen': 'Ferrari', 'Max Verstappen': 'Red Bull Racing TAG Heuer', 'Felipe Massa': 'Williams Mercedes', 
                      'Sergio Perez': 'Force India Mercedes', 'Carlos Sainz': 'Renault', 'Daniil Kvyat': 'Toro Rosso', 
                      'Esteban Ocon': 'Force India Mercedes', 'Nico Hulkenberg': 'Renault', 'Antonio Giovinazzi': 'Sauber Ferrari', 
                      'Stoffel Vandoorne': 'McLaren Honda', 'Fernando Alonso': 'McLaren Honda', 'Kevin Magnussen': 'Haas Ferrari', 
                      'Lance Stroll': 'Williams Mercedes', 'Daniel Ricciardo': 'Red Bull Racing TAG Heuer', 'Marcus Ericsson': 'Sauber Ferrari', 
                      'Jolyon Palmer': 'Renault', 'Romain Grosjean': 'Haas Ferrari', 'Pascal Wehrlein': 'Sauber Ferrari', 
                      'Jenson Button': 'McLaren Honda', 'Paul di Resta': 'Williams Mercedes', 'Pierre Gasly': 'Toro Rosso', 'Brendon Hartley': 'Toro Rosso'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing TAG Heuer': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Honda': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Haas Ferrari': 'Haas', 
              'Toro Rosso': 'Toro Rosso', 
              'Williams Mercedes': 'Williams', 
              'Renault': 'Renault'}


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


raceLocations = ["Australia", "China", "Bahrain", "Russia", "Spain",
                 "Monaco", "Canada", "Azerbaijan", "Austria", "Great Britain",
                 "Hungary", "Belgium", "Italy", "Singapore", "Malaysia",
                 "Japan", "United States", "Mexico", "Brazil", "Abu Dhabi"]

