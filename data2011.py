year = 2011
data = {'Sebastian Vettel': [25, 50, 68, 93, 118, 143, 161, 186, 204, 216, 234, 259, 284, 309, 324, 349, 374, 374, 392], 
        'Lewis Hamilton': [18, 22, 47, 59, 77, 85, 85, 97, 109, 134, 146, 146, 158, 168, 178, 196, 202, 227, 227], 
        'Vitaly Petrov': [15, 15, 17, 21, 21, 21, 31, 31, 31, 32, 32, 34, 34, 34, 36, 36, 36, 36, 37], 
        'Fernando Alonso': [12, 20, 26, 41, 51, 69, 69, 87, 112, 130, 145, 157, 172, 184, 202, 212, 227, 245, 257], 
        'Mark Webber': [10, 22, 37, 55, 67, 79, 94, 109, 124, 139, 149, 167, 167, 182, 194, 209, 221, 233, 258], 
        'Jenson Button': [8, 26, 38, 46, 61, 76, 101, 109, 109, 109, 134, 149, 167, 185, 210, 222, 240, 255, 270], 
        'Sergio Perez': [0, 0, 0, 0, 2, 2, 2, 2, 8, 8, 8, 8, 8, 9, 13, 13, 14, 14, 14], 
        'Kamui Kobayashi': [0, 6, 7, 8, 9, 19, 25, 25, 25, 27, 27, 27, 27, 27, 27, 27, 27, 28, 30], 
        'Felipe Massa': [6, 16, 24, 24, 24, 24, 32, 42, 52, 62, 70, 74, 82, 84, 90, 98, 98, 108, 118], 
        'Sebastien Buemi': [4, 4, 4, 6, 6, 7, 8, 8, 8, 8, 12, 12, 13, 13, 13, 15, 15, 15, 15], 
        'Adrian Sutil': [2, 2, 2, 2, 2, 8, 8, 10, 10, 18, 18, 24, 24, 28, 28, 28, 30, 34, 42], 
        'Paul di Resta': [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8, 12, 20, 20, 21, 21, 23, 27], 
        'Jaime Alguersuari': [0, 0, 0, 0, 0, 0, 4, 8, 9, 9, 10, 10, 16, 16, 16, 22, 26, 26, 26], 
        'Nick Heidfeld': [0, 15, 15, 21, 25, 29, 29, 30, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34], 
        'Jarno Trulli': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        "Jerome d'Ambrosio": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Timo Glock': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Rubens Barrichello': [0, 0, 0, 0, 0, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
        'Nico Rosberg': [0, 0, 10, 20, 26, 26, 26, 32, 40, 46, 48, 56, 56, 62, 63, 67, 75, 83, 89], 
        'Heikki Kovalainen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Michael Schumacher': [0, 2, 6, 6, 14, 14, 26, 26, 28, 32, 32, 42, 52, 52, 60, 60, 70, 76, 76], 
        'Pastor Maldonado': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Vitantonio Liuzzi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Narain Karthikeyan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Pedro de la Rosa': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Daniel Ricciardo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Karun Chandhok': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Bruno Senna': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Sebastian Vettel': 'Red Bull Racing Renault', 'Lewis Hamilton': 'McLaren Mercedes', 'Vitaly Petrov': 'Renault', 
                      'Fernando Alonso': 'Ferrari', 'Mark Webber': 'Red Bull Racing Renault', 'Jenson Button': 'McLaren Mercedes', 
                      'Sergio Perez': 'Sauber Ferrari', 'Kamui Kobayashi': 'Sauber Ferrari', 'Felipe Massa': 'Ferrari', 
                      'Sebastien Buemi': 'STR Ferrari', 'Adrian Sutil': 'Force India Mercedes', 'Paul di Resta': 'Force India Mercedes', 
                      'Jaime Alguersuari': 'STR Ferrari', 'Nick Heidfeld': 'Renault', 'Jarno Trulli': 'Lotus Renault', 
                      "Jerome d'Ambrosio": 'Virgin Cosworth', 'Timo Glock': 'Virgin Cosworth', 'Rubens Barrichello': 'Williams Cosworth', 
                      'Nico Rosberg': 'Mercedes', 'Heikki Kovalainen': 'Lotus Renault', 'Michael Schumacher': 'Mercedes', 
                      'Pastor Maldonado': 'Williams Cosworth', 'Vitantonio Liuzzi': 'HRT Cosworth', 'Narain Karthikeyan': 
                      'HRT Cosworth', 'Pedro de la Rosa': 'Sauber Ferrari', 'Daniel Ricciardo': 'HRT Cosworth', 
                      'Karun Chandhok': 'Lotus Renault', 'Bruno Senna': 'Renault'}


# can add more teams as I add more past data
teamChange = {'Red Bull Racing Renault': "Red Bull", 
              'Ferrari': "Ferrari", 
              'McLaren Mercedes': "McLaren", 
              'Caterham Renault': "Caterham", 
              'Mercedes': "Mercedes", 
              'Lotus Renault': "Lotus", 
              'Force India Mercedes': "Force India", 
              'Renault': "Renault", 
              'STR Ferrari': "Toro Rosso", 
              'HRT Cosworth': "HRT", 
              'Sauber Ferrari': "Sauber", 
              'Williams Cosworth': "Williams",
              'Virgin Cosworth': "Virgin"}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {"Red Bull": "#1310cf", 
                     "Ferrari": "#EF1A2D", 
                     "McLaren": "#C0C0C0", 
                     "Caterham": "#005030", 
                     "Mercedes": "#00A19B", 
                     "Lotus": "#A39064", 
                     "Force India": "#EE8663", 
                     "Renault": "#FFF500", 
                     "Toro Rosso": "#A39064", 
                     "HRT": "#8B0000", 
                     "Sauber": "#FFA500", 
                     "Williams": "#00A0DE",
                     "Virgin": "#cc0000"}
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


raceLocations = ["Australia", "Malaysia", "China", "Turkey", "Spain",
                 "Monaco", "Canada", "Europe", "Great Britain", "Germany",
                 "Hungary", "Belgium", "Italy", "Singapore", "Japan",
                 "South Korea", "India", "Abu Dhabi", "Brazil"]

