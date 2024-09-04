year = 2019
data = {'Valtteri Bottas': [26, 44, 62, 87, 105, 120, 133, 151, 166, 184, 184, 188, 203, 221, 231, 249, 274, 289, 314, 314, 326], 
        'Lewis Hamilton': [18, 43, 68, 86, 112, 137, 162, 187, 197, 223, 225, 250, 268, 284, 296, 322, 338, 363, 381, 387, 413], 
        'Max Verstappen': [15, 27, 39, 51, 66, 78, 88, 100, 126, 136, 162, 181, 181, 185, 200, 212, 212, 220, 235, 260, 278], 
        'Sebastian Vettel': [12, 22, 37, 52, 64, 82, 100, 111, 123, 123, 141, 156, 169, 169, 194, 194, 212, 230, 230, 230, 240], 
        'Charles Leclerc': [10, 26, 36, 47, 57, 57, 72, 87, 105, 120, 120, 132, 157, 182, 200, 215, 223, 236, 249, 249, 264], 
        'Kevin Magnussen': [8, 8, 8, 8, 14, 14, 14, 14, 14, 14, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20, 20], 
        'Nico Hulkenberg': [6, 6, 6, 6, 6, 6, 12, 16, 16, 17, 17, 17, 21, 31, 33, 34, 34, 35, 37, 37, 37], 
        'Kimi Räikkönen': [4, 10, 12, 13, 13, 13, 13, 19, 21, 25, 25, 31, 31, 31, 31, 31, 31, 31, 31, 43, 43], 
        'Lance Stroll': [2, 2, 2, 4, 4, 4, 6, 6, 6, 6, 18, 18, 19, 19, 19, 19, 21, 21, 21, 21, 21], 
        'Daniil Kvyat': [1, 1, 1, 1, 3, 9, 10, 10, 10, 12, 27, 27, 33, 33, 33, 33, 34, 34, 34, 35, 37], 
        'Pierre Gasly': [0, 4, 13, 13, 21, 32, 36, 37, 43, 55, 55, 63, 65, 65, 69, 69, 75, 77, 77, 95, 95], 
        'Lando Norris': [0, 8, 8, 12, 12, 12, 12, 14, 22, 22, 22, 24, 24, 25, 31, 35, 35, 35, 41, 45, 49], 
        'Sergio Perez': [0, 1, 5, 13, 13, 13, 13, 13, 13, 13, 13, 13, 21, 27, 27, 33, 37, 43, 44, 46, 52], 
        'Alexander Albon': [0, 2, 3, 3, 3, 7, 7, 7, 7, 7, 15, 16, 26, 34, 42, 52, 64, 74, 84, 84, 92], 
        'Antonio Giovinazzi': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 3, 4, 4, 4, 4, 4, 14, 14], 
        'George Russell': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Robert Kubica': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Romain Grosjean': [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 
        'Daniel Ricciardo': [0, 0, 6, 6, 6, 8, 16, 16, 16, 22, 22, 22, 22, 34, 34, 34, 34, 38, 46, 54, 54], 
        'Carlos Sainz': [0, 0, 0, 6, 10, 18, 18, 26, 30, 38, 48, 58, 58, 58, 58, 66, 76, 76, 80, 95, 96]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Valtteri Bottas': 'Mercedes', 'Lewis Hamilton': 'Mercedes', 'Max Verstappen': 'Red Bull Racing Honda', 
                      'Sebastian Vettel': 'Ferrari', 'Charles Leclerc': 'Ferrari', 'Kevin Magnussen': 'Haas Ferrari', 
                      'Nico Hulkenberg': 'Renault', 'Kimi Räikkönen': 'Alfa Romeo Racing Ferrari', 'Lance Stroll': 'Racing Point BWT Mercedes', 
                      'Daniil Kvyat': 'Scuderia Toro Rosso Honda', 'Pierre Gasly': 'Scuderia Toro Rosso Honda', 'Lando Norris': 'McLaren Renault', 
                      'Sergio Perez': 'Racing Point BWT Mercedes', 'Alexander Albon': 'Red Bull Racing Honda', 
                      'Antonio Giovinazzi': 'Alfa Romeo Racing Ferrari', 'George Russell': 'Williams Mercedes', 'Robert Kubica': 'Williams Mercedes', 
                      'Romain Grosjean': 'Haas Ferrari', 'Daniel Ricciardo': 'Renault', 'Carlos Sainz': 'McLaren Renault'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Honda': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Renault': 'McLaren', 
              'Racing Point BWT Mercedes': 'Racing Point', 
              'Alfa Romeo Racing Ferrari': 'Alfa Romeo', 
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
                     'Racing Point': '#F363B9', 
                     'Alfa Romeo': '#A50F2D', 
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
                 "Russia", "Japan", "Mexico", "United States", "Brazil", 
                 "Abu Dhabi"]

