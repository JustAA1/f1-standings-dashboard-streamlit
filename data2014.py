year = 2014
data = {'Nico Rosberg': [25, 43, 61, 79, 97, 122, 140, 165, 165, 190, 202, 220, 238, 238, 256, 274, 292, 317, 317], 
        'Daniel Ricciardo': [0, 0, 12, 24, 39, 54, 79, 83, 98, 106, 131, 156, 166, 181, 193, 199, 214, 214, 226], 
        'Kevin Magnussen': [18, 20, 20, 20, 20, 21, 23, 29, 35, 37, 37, 37, 38, 39, 39, 49, 53, 55, 55], 
        'Jenson Button': [15, 23, 23, 23, 23, 31, 43, 43, 55, 59, 60, 68, 72, 72, 82, 94, 94, 106, 116], 
        'Fernando Alonso': [12, 24, 26, 41, 49, 61, 69, 79, 87, 97, 115, 121, 121, 133, 133, 141, 149, 157, 159], 
        'Valtteri Bottas': [10, 14, 18, 24, 34, 34, 40, 55, 73, 91, 95, 110, 122, 122, 130, 145, 155, 156, 171], 
        'Nico Hulkenberg': [8, 18, 28, 36, 37, 47, 57, 59, 63, 69, 69, 70, 70, 72, 76, 76, 76, 80, 88], 
        'Kimi Räikkönen': [6, 6, 7, 11, 17, 17, 18, 19, 19, 19, 27, 39, 41, 45, 45, 47, 47, 53, 54], 
        'Jean-Eric Vergne': [4, 4, 4, 4, 4, 4, 8, 8, 9, 9, 11, 11, 11, 19, 21, 21, 22, 22, 22], 
        'Daniil Kvyat': [2, 3, 3, 4, 4, 4, 4, 4, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8], 
        'Sergio Perez': [1, 1, 16, 18, 20, 20, 20, 28, 28, 29, 29, 33, 39, 45, 46, 47, 47, 47, 53], 
        'Adrian Sutil': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Esteban Gutierrez': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Max Chilton': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Jules Bianchi': [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
        'Romain Grosjean': [0, 0, 0, 0, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 
        'Pastor Maldonado': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 
        'Marcus Ericsson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sebastian Vettel': [0, 15, 23, 33, 45, 45, 60, 60, 70, 82, 88, 98, 106, 124, 139, 143, 149, 159, 163], 
        'Lewis Hamilton': [0, 25, 50, 75, 100, 118, 118, 136, 161, 176, 191, 191, 216, 241, 266, 291, 316, 334, 359], 
        'Felipe Massa': [0, 6, 12, 12, 12, 18, 18, 30, 30, 30, 40, 40, 55, 65, 71, 71, 83, 98, 116], 
        'Kamui Kobayashi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Andre Lotterer': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Will Stevens': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Nico Rosberg': 'Mercedes', 'Daniel Ricciardo': 'Red Bull Racing Renault', 'Kevin Magnussen': 'McLaren Mercedes', 
                      'Jenson Button': 'McLaren Mercedes', 'Fernando Alonso': 'Ferrari', 'Valtteri Bottas': 'Williams Mercedes', 
                      'Nico Hulkenberg': 'Force India Mercedes', 'Kimi Räikkönen': 'Ferrari', 'Jean-Eric Vergne': 'STR Renault', 
                      'Daniil Kvyat': 'STR Renault', 'Sergio Perez': 'Force India Mercedes', 'Adrian Sutil': 'Sauber Ferrari', 
                      'Esteban Gutierrez': 'Sauber Ferrari', 'Max Chilton': 'Marussia Ferrari', 'Jules Bianchi': 'Marussia Ferrari', 
                      'Romain Grosjean': 'Lotus Renault', 'Pastor Maldonado': 'Lotus Renault', 'Marcus Ericsson': 'Caterham Renault', 
                      'Sebastian Vettel': 'Red Bull Racing Renault', 'Lewis Hamilton': 'Mercedes', 'Felipe Massa': 'Williams Mercedes', 
                      'Kamui Kobayashi': 'Caterham Renault', 'Andre Lotterer': 'Caterham Renault', 'Will Stevens': 'Caterham Renault'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Renault': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Force India Mercedes': 'Force India', 
              'Sauber Ferrari': 'Sauber', 
              'Lotus Renault': 'Lotus', 
              'STR Renault': 'Toro Rosso', 
              'Williams Mercedes': 'Williams', 
              'Marussia Ferrari': 'Marussia',
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

raceLocations = ["Australia", "Malaysia", "Bahrain", "China", "Spain",
                 "Monaco", "Canada", "Austria", "Great Britain", "Germany",
                 "Hungary", "Belgium", "Italy", "Singapore", "Japan",
                 "Russia", "United States", "Brazil", "Abu Dhabi"]

