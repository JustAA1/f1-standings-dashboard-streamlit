year = 2024

data = {'Max Verstappen': [26, 51, 51, 77, 110, 136, 161, 169, 194, 219, 237, 255, 265, 277, 295, 303, 313, 331, 354], 
        'Sergio Perez': [18, 36, 46, 64, 85, 103, 107, 107, 107, 111, 118, 118, 124, 131, 139, 143, 143, 144, 150], 
        'Carlos Sainz': [15, 15, 40, 55, 69, 83, 93, 108, 108, 116, 135, 146, 154, 162, 172, 184, 184, 190, 215], 
        'Charles Leclerc': [12, 28, 47, 59, 76, 98, 113, 138, 138, 148, 150, 150, 162, 177, 192, 217, 235, 245, 275], 
        'George Russell': [10, 18, 18, 24, 33, 37, 44, 54, 69, 81, 111, 111, 116, 116, 122, 128, 143, 155, 167], 
        'Lando Norris': [8, 12, 27, 37, 58, 83, 101, 113, 131, 150, 156, 171, 189, 199, 225, 241, 254, 279, 297], 
        'Lewis Hamilton': [6, 8, 8, 10, 19, 27, 35, 42, 55, 70, 85, 110, 125, 150, 154, 164, 166, 174, 177], 
        'Oscar Piastri': [4, 16, 28, 32, 38, 41, 53, 71, 81, 87, 112, 124, 149, 167, 179, 197, 222, 237, 247], 
        'Fernando Alonso': [2, 12, 16, 24, 31, 33, 33, 33, 41, 41, 41, 45, 45, 49, 50, 50, 58, 62, 62], 
        'Lance Stroll': [1, 1, 9, 9, 9, 9, 11, 11, 17, 17, 17, 23, 24, 24, 24, 24, 24, 24, 24], 
        'Zhou Guanyu': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Kevin Magnussen': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6, 6, 6, 8], 
        'Daniel Ricciardo': [0, 0, 0, 0, 0, 5, 5, 5, 9, 9, 11, 11, 11, 12, 12, 12, 12, 12, 12], 
        'Yuki Tsunoda': [0, 0, 6, 7, 7, 14, 15, 19, 19, 19, 19, 20, 22, 22, 22, 22, 22, 22, 22], 
        'Alexander Albon': [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 6, 12, 12, 12], 
        'Nico Hulkenberg': [0, 1, 3, 3, 4, 6, 6, 6, 6, 6, 14, 22, 22, 22, 22, 22, 22, 24, 29], 
        'Esteban Ocon': [0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5], 
        'Pierre Gasly': [0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 6, 6, 6, 6, 8, 8, 8, 8, 8], 
        'Valtteri Bottas': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Logan Sargeant': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Oliver Bearman': [0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7], 
        'Franco Colapinto': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 5], 
        'Liam Lawson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]}

data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

tempDriverTeamData = {'Max Verstappen': 'Red Bull Racing Honda RBPT', 'Sergio Perez': 'Red Bull Racing Honda RBPT', 
                      'Carlos Sainz': 'Ferrari', 'Charles Leclerc': 'Ferrari', 'George Russell': 'Mercedes', 
                      'Lando Norris': 'McLaren Mercedes', 'Lewis Hamilton': 'Mercedes', 'Oscar Piastri': 'McLaren Mercedes', 
                      'Fernando Alonso': 'Aston Martin Aramco Mercedes', 'Lance Stroll': 'Aston Martin Aramco Mercedes', 
                      'Zhou Guanyu': 'Kick Sauber Ferrari', 'Kevin Magnussen': 'Haas Ferrari', 'Daniel Ricciardo': 'RB Honda RBPT', 
                      'Yuki Tsunoda': 'RB Honda RBPT', 'Alexander Albon': 'Williams Mercedes', 'Nico Hulkenberg': 'Haas Ferrari', 
                      'Esteban Ocon': 'Alpine Renault', 'Pierre Gasly': 'Alpine Renault', 'Valtteri Bottas': 'Kick Sauber Ferrari', 
                      'Logan Sargeant': 'Williams Mercedes', 'Oliver Bearman': 'Haas Ferrari', 'Franco Colapinto': 'Williams Mercedes', 
                      'Liam Lawson': 'RB Honda RBPT'}

teamChange = {'Red Bull Racing Honda RBPT': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Aston Martin Aramco Mercedes': 'Aston Martin', 
              'Kick Sauber Ferrari': 'Kick Sauber', 
              'Haas Ferrari': 'Haas', 
              'RB Honda RBPT': 'RB', 
              'Williams Mercedes': 'Williams', 
              'Alpine Renault': 'Alpine'}

teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Aston Martin': '#09826e', 
                     'Kick Sauber': '#52E252', 
                     'Haas': '#9c091d', 
                     'RB': '#0840fa', 
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

numRaces = 19

delta = {key:value[1] for key, value in teamsWithPoints.items()}

driverDelta = {key:None for key in data}
for driver in data:
    points = data[driver]
    tempDelta = [points[0]]
    for i in range(len(points) - 1):
        tempDelta.append(points[i+1] - points[i])
    driverDelta[driver] = tempDelta


numRaces = numRaces
driverData = data
driverDelta = driverDelta

driverData = {key:[value1, value2] for key, value1, value2 in zip(driverData, driverData.values(), driverDelta.values())}


raceLocations = ["Bahrain", "Saudi Arabia", "Australia", "Japan", "China", 
                 "Miami", "Imola", "Monaco", "Canada", "Spain", "Austria", 
                 "Great Britain", "Hungary", "Belgium", "Netherlands", "Monza", 
                 "Azerbaijan", "Singapore", "United States", "Mexico", "Brazil", 
                 "Las Vegas", "Qatar", "Abu Dhabi"][:numRaces]


#print(driverData)
