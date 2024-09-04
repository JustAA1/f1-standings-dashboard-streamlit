year = 2013
data = {'Kimi Räikkönen': [25, 31, 49, 67, 85, 86, 88, 98, 116, 134, 134, 134, 149, 167, 177, 183, 183, 183, 183], 
        'Fernando Alonso': [18, 18, 43, 47, 72, 78, 96, 111, 123, 133, 151, 169, 187, 195, 207, 207, 217, 227, 242], 
        'Sebastian Vettel': [15, 40, 52, 77, 89, 107, 132, 132, 157, 172, 197, 222, 247, 272, 297, 322, 347, 372, 397], 
        'Felipe Massa': [12, 22, 30, 30, 45, 45, 49, 57, 57, 61, 67, 79, 87, 89, 90, 102, 106, 106, 112], 
        'Lewis Hamilton': [10, 25, 40, 50, 50, 62, 77, 89, 99, 124, 139, 141, 151, 161, 161, 169, 175, 187, 189], 
        'Mark Webber': [8, 26, 26, 32, 42, 57, 69, 87, 93, 105, 115, 130, 130, 130, 148, 148, 166, 181, 199], 
        'Adrian Sutil': [6, 6, 6, 6, 6, 16, 17, 23, 23, 23, 25, 25, 26, 26, 26, 28, 29, 29, 29], 
        'Paul di Resta': [4, 4, 8, 20, 26, 28, 34, 36, 36, 36, 36, 36, 36, 36, 36, 40, 48, 48, 48], 
        'Jenson Button': [2, 2, 12, 13, 17, 25, 25, 25, 33, 39, 47, 48, 54, 58, 60, 60, 60, 61, 73], 
        'Romain Grosjean': [1, 9, 11, 26, 26, 26, 26, 26, 41, 49, 53, 57, 57, 72, 87, 102, 114, 132, 132], 
        'Sergio Perez': [0, 2, 2, 10, 12, 12, 12, 12, 16, 18, 18, 18, 22, 23, 23, 33, 35, 41, 49], 
        'Jean-Eric Vergne': [0, 1, 1, 1, 1, 5, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13], 
        'Esteban Gutierrez': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6], 
        'Valtteri Bottas': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4], 
        'Jules Bianchi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Charles Pic': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Max Chilton': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Giedo van der Garde': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Daniel Ricciardo': [0, 0, 6, 6, 7, 7, 7, 11, 11, 11, 12, 18, 18, 18, 18, 19, 19, 19, 20], 
        'Nico Rosberg': [0, 12, 12, 14, 22, 47, 57, 82, 84, 84, 96, 104, 116, 122, 126, 144, 159, 161, 171], 
        'Pastor Maldonado': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Nico Hulkenberg': [0, 4, 5, 5, 5, 5, 5, 6, 7, 7, 7, 17, 19, 31, 39, 39, 39, 47, 51], 
        'Heikki Kovalainen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Kimi Räikkönen': 'Lotus Renault', 'Fernando Alonso': 'Ferrari', 'Sebastian Vettel': 'Red Bull Racing Renault', 
                      'Felipe Massa': 'Ferrari', 'Lewis Hamilton': 'Mercedes', 'Mark Webber': 'Red Bull Racing Renault', 
                      'Adrian Sutil': 'Force India Mercedes', 'Paul di Resta': 'Force India Mercedes', 'Jenson Button': 'McLaren Mercedes', 
                      'Romain Grosjean': 'Lotus Renault', 'Sergio Perez': 'McLaren Mercedes', 'Jean-Eric Vergne': 'STR Ferrari', 
                      'Esteban Gutierrez': 'Sauber Ferrari', 'Valtteri Bottas': 'Williams Renault', 'Jules Bianchi': 'Marussia Cosworth', 
                      'Charles Pic': 'Caterham Renault', 'Max Chilton': 'Marussia Cosworth', 'Giedo van der Garde': 'Caterham Renault', 
                      'Daniel Ricciardo': 'STR Ferrari', 'Nico Rosberg': 'Mercedes', 'Pastor Maldonado': 'Williams Renault', 
                      'Nico Hulkenberg': 'Sauber Ferrari', 'Heikki Kovalainen': 'Lotus Renault'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Renault': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Lotus Renault': 'Lotus', 
              'STR Ferrari': 'Toro Rosso', 
              'Williams Renault': 'Williams', 
              'Marussia Cosworth': 'Marussia',
              'Caterham Renault': 'Caterham'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#C0C0C0', 
                     'Force India': '#F363B9', 
                     'Sauber': '#1d45aa', 
                     'Toro Rosso': '#A39064',
                     'Williams': '#00A0DE', 
                     'Marussia': '#d82f20',
                     'Lotus': '#86995B',
                     'Caterham': '#005030'}
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
                 "Monaco", "Canada", "Great Britain", "Germany", "Hungary",
                 "Belgium", "Italy", "Singapore", "Korea", "Japan",
                 "India", "Abu Dhabi", "United States", "Brazil"]

