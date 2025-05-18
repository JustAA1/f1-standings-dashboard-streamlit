year = 2025

data = {'Lando Norris': [25, 44, 62, 77, 89, 115, 133], 
        'Max Verstappen': [18, 36, 61, 69, 87, 99, 124], 
        'George Russell': [15, 35, 45, 63, 73, 93, 99], 
        'Andrea Kimi Antonelli': [12, 22, 30, 30, 38, 48, 48], 
        'Alexander Albon': [10, 16, 18, 18, 20, 30, 40], 
        'Lance Stroll': [8, 10, 10, 10, 10, 14, 14], 
        'Nico Hulkenberg': [6, 6, 6, 6, 6, 6, 6], 
        'Charles Leclerc': [4, 8, 20, 32, 47, 53, 61], 
        'Oscar Piastri': [2, 34, 49, 74, 99, 131, 146], 
        'Lewis Hamilton': [1, 9, 15, 25, 31, 41, 53], 
        'Pierre Gasly': [0, 0, 0, 6, 6, 7, 7], 
        'Yuki Tsunoda': [0, 3, 3, 5, 5, 9, 10], 
        'Esteban Ocon': [0, 10, 10, 14, 14, 14, 14], 
        'Oliver Bearman': [0, 4, 5, 6, 6, 6, 6], 
        'Liam Lawson': [0, 0, 0, 0, 0, 0, 0], 
        'Gabriel Bortoleto': [0, 0, 0, 0, 0, 0, 0], 
        'Fernando Alonso': [0, 0, 0, 0, 0, 0, 0], 
        'Carlos Sainz': [0, 1, 1, 1, 5, 5, 9], 
        'Jack Doohan': [0, 0, 0, 0, 0, 0, 0], 
        'Isack Hadjar': [0, 0, 4, 4, 5, 5, 7],
        'Franco Colapinto': [0, 0, 0, 0, 0, 0, 0]}

data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

tempDriverTeamData = {'Max Verstappen': 'Red Bull Racing Honda RBPT', 'Liam Lawson': 'Red Bull Racing Honda RBPT', 
                      'Lewis Hamilton': 'Ferrari', 'Charles Leclerc': 'Ferrari', 'George Russell': 'Mercedes', 
                      'Lando Norris': 'McLaren Mercedes', 'Andrea Kimi Antonelli': 'Mercedes', 'Oscar Piastri': 'McLaren Mercedes', 
                      'Fernando Alonso': 'Aston Martin Aramco Mercedes', 'Lance Stroll': 'Aston Martin Aramco Mercedes', 
                      'Nico Hulkenberg': 'Kick Sauber Ferrari', 'Oliver Bearman': 'Haas Ferrari', 'Isack Hadjar': 'Racing Bulls Honda RBPT', 
                      'Yuki Tsunoda': 'Racing Bulls Honda RBPT', 'Alexander Albon': 'Williams Mercedes', 'Esteban Ocon': 'Haas Ferrari', 
                      'Jack Doohan': 'Alpine Renault', 'Pierre Gasly': 'Alpine Renault', 'Gabriel Bortoleto': 'Kick Sauber Ferrari', 
                      'Carlos Sainz': 'Williams Mercedes', 'Franco Colapinto': 'Alpine Renault'}

teamChange = {'Red Bull Racing Honda RBPT': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Aston Martin Aramco Mercedes': 'Aston Martin', 
              'Kick Sauber Ferrari': 'Kick Sauber', 
              'Haas Ferrari': 'Haas', 
              'Racing Bulls Honda RBPT': 'Racing Bulls', 
              'Williams Mercedes': 'Williams', 
              'Alpine Renault': 'Alpine'}

teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Aston Martin': '#09826e', 
                     'Kick Sauber': '#52E252', 
                     'Haas': '#9c091d', 
                     'Racing Bulls': '#0840fa', 
                     'Williams': '#00A0DE', 
                     'Alpine': '#cc00ff'}
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

numRaces = 7

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

raceLocations = ["Australia", "China", "Japan", "Bahrain", "Saudi Arabia", 
                 "Miami", "Imola", "Monaco", "Spain", "Canada", "Austria", 
                 "Great Britain", "Belgium", "Hungary", "Netherlands", "Monza", 
                 "Azerbaijan", "Singapore", "United States", "Mexico", "Brazil", 
                 "Las Vegas", "Qatar", "Abu Dhabi"][:numRaces]
