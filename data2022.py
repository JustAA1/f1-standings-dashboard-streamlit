year = 2022
data = {'Charles Leclerc': [26, 45, 71, 86, 104, 104, 116, 116, 126, 138, 170, 170, 178, 186, 201, 219, 237, 252, 267, 275, 290, 308], 
        'Carlos Sainz': [18, 33, 33, 38, 53, 65, 83, 83, 102, 127, 133, 144, 156, 171, 175, 187, 202, 202, 202, 212, 234, 246], 
        'Lewis Hamilton': [15, 16, 28, 28, 36, 46, 50, 62, 77, 93, 109, 127, 146, 146, 158, 168, 170, 180, 198, 216, 240, 240], 
        'George Russell': [12, 22, 37, 49, 59, 74, 84, 99, 111, 111, 128, 143, 158, 170, 188, 203, 203, 207, 218, 231, 265, 275], 
        'Kevin Magnussen': [10, 12, 12, 15, 15, 15, 15, 15, 15, 16, 22, 22, 22, 22, 22, 22, 22, 22, 24, 24, 25, 25], 
        'Valtteri Bottas': [8, 8, 12, 24, 30, 38, 40, 40, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 49, 49], 
        'Esteban Ocon': [6, 14, 20, 20, 24, 30, 30, 31, 39, 39, 52, 56, 58, 64, 66, 66, 66, 78, 78, 82, 86, 92], 
        'Yuki Tsunoda': [4, 4, 4, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12], 
        'Fernando Alonso': [2, 2, 2, 2, 2, 4, 10, 16, 18, 28, 29, 37, 41, 51, 59, 59, 59, 65, 71, 71, 81, 81], 
        'Zhou Guanyu': [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6], 
        'Mick Schumacher': [0, 0, 0, 0, 0, 0, 0, 0, 4, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
        'Lance Stroll': [0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 13, 13, 13, 13, 14, 18], 
        'Alexander Albon': [0, 0, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
        'Daniel Ricciardo': [0, 0, 8, 11, 11, 11, 11, 15, 15, 15, 17, 19, 19, 19, 19, 19, 29, 29, 29, 35, 35, 37], 
        'Lando Norris': [0, 6, 16, 35, 35, 39, 48, 50, 50, 58, 64, 70, 76, 76, 82, 88, 100, 101, 109, 111, 113, 122], 
        'Nicholas Latifi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
        'Nico Hulkenberg': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sergio Perez': [0, 12, 30, 54, 66, 85, 110, 129, 129, 147, 151, 163, 173, 191, 201, 210, 235, 253, 265, 280, 290, 305], 
        'Max Verstappen': [0, 25, 25, 59, 85, 110, 125, 150, 175, 181, 208, 233, 258, 284, 310, 335, 341, 366, 391, 416, 429, 454], 
        'Pierre Gasly': [0, 4, 6, 6, 6, 6, 6, 16, 16, 16, 16, 16, 16, 18, 18, 22, 23, 23, 23, 23, 23, 23], 
        'Sebastian Vettel': [0, 4, 4, 4, 5, 13, 13, 15, 15, 15, 16, 20, 20, 20, 24, 32, 36, 36, 36, 37, 37, 37], 
        'Nyck de Vries': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Charles Leclerc': 'Ferrari', 'Carlos Sainz': 'Ferrari', 
                      'Lewis Hamilton': 'Mercedes', 'George Russell': 'Mercedes', 
                      'Kevin Magnussen': 'Haas Ferrari', 'Valtteri Bottas': 'Alfa Romeo Ferrari', 
                      'Esteban Ocon': 'Alpine Renault', 'Yuki Tsunoda': 'AlphaTauri RBPT', 
                      'Fernando Alonso': 'Alpine Renault', 'Zhou Guanyu': 'Alfa Romeo Ferrari', 
                      'Mick Schumacher': 'Haas Ferrari', 'Lance Stroll': 'Aston Martin Aramco Mercedes', 
                      'Alexander Albon': 'Williams Mercedes', 'Daniel Ricciardo': 'McLaren Mercedes', 
                      'Lando Norris': 'McLaren Mercedes', 'Nicholas Latifi': 'Williams Mercedes', 
                      'Nico Hulkenberg': 'Aston Martin Aramco Mercedes', 'Sergio Perez': 'Red Bull Racing RBPT', 
                      'Max Verstappen': 'Red Bull Racing RBPT', 'Pierre Gasly': 'AlphaTauri RBPT', 
                      'Sebastian Vettel': 'Aston Martin Aramco Mercedes', 'Nyck de Vries': 'Williams Mercedes'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing RBPT': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Aston Martin Aramco Mercedes': 'Aston Martin', 
              'Alfa Romeo Ferrari': 'Alfa Romeo', 
              'Haas Ferrari': 'Haas', 
              'AlphaTauri RBPT': 'AlphaTauri', 
              'Williams Mercedes': 'Williams', 
              'Alpine Renault': 'Alpine'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Aston Martin': '#09826e', 
                     'Alfa Romeo': '#A50F2D', 
                     'Haas': '#F7F5EC', 
                     'AlphaTauri': '#20394C',
                     'Williams': '#00A0DE', 
                     'Alpine': '#0e62c2'}
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


raceLocations = ["Bahrain", "Saudi Arabia", "Australia", "Imola", "Miami", "Spain", 
                 "Monaco", "Azerbaijan", "Canada", "Great Britain", "Austria", "France", 
                 "Hungary", "Belgium", "Netherlands", "Monza", "Singapore", "Japan", 
                 "United States", "Mexico", "Brazil", "Abu Dhabi"]

