year = 2012
data = {'Jenson Button': [25, 25, 43, 43, 45, 45, 45, 49, 50, 68, 76, 101, 101, 119, 131, 131, 141, 153, 163, 188], 
        'Sebastian Vettel': [18, 18, 28, 53, 61, 73, 85, 85, 100, 110, 122, 140, 140, 165, 190, 215, 240, 255, 273, 281], 
        'Lewis Hamilton': [15, 30, 45, 49, 53, 63, 88, 88, 92, 92, 117, 117, 142, 142, 152, 153, 165, 165, 190, 190], 
        'Mark Webber': [12, 24, 36, 48, 48, 73, 79, 91, 116, 120, 124, 132, 132, 132, 134, 152, 167, 167, 167, 179], 
        'Fernando Alonso': [10, 35, 37, 43, 61, 76, 86, 111, 129, 154, 164, 164, 179, 194, 194, 209, 227, 245, 260, 278], 
        'Kamui Kobayashi': [8, 8, 9, 9, 19, 19, 21, 21, 21, 33, 33, 33, 35, 35, 50, 50, 50, 58, 58, 60], 
        'Kimi Räikkönen': [6, 16, 16, 34, 49, 51, 55, 73, 83, 98, 116, 131, 141, 149, 157, 167, 173, 198, 206, 207], 
        'Sergio Perez': [4, 22, 22, 22, 22, 22, 37, 39, 39, 47, 47, 47, 65, 66, 66, 66, 66, 66, 66, 66], 
        'Daniel Ricciardo': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 6, 7, 9, 9, 10, 10, 10], 
        'Paul di Resta': [1, 7, 7, 15, 15, 21, 21, 27, 27, 27, 27, 28, 32, 44, 44, 44, 44, 46, 46, 46], 
        'Jean-Eric Vergne': [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 12, 12, 16], 
        'Nico Rosberg': [0, 0, 25, 35, 41, 59, 67, 75, 75, 76, 77, 77, 83, 93, 93, 93, 93, 93, 93, 93], 
        'Pastor Maldonado': [0, 0, 4, 4, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 33, 33, 33, 43, 45, 45], 
        'Timo Glock': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Charles Pic': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Bruno Senna': [0, 8, 14, 14, 14, 15, 15, 16, 18, 18, 24, 24, 25, 25, 25, 25, 26, 30, 31, 31], 
        'Felipe Massa': [0, 0, 0, 2, 2, 10, 11, 11, 23, 23, 25, 35, 47, 51, 69, 81, 89, 95, 107, 122], 
        'Heikki Kovalainen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Vitaly Petrov': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Michael Schumacher': [0, 1, 1, 2, 2, 2, 2, 17, 23, 29, 29, 35, 43, 43, 43, 43, 43, 43, 43, 49], 
        'Romain Grosjean': [0, 0, 8, 23, 35, 35, 53, 53, 61, 61, 76, 76, 76, 82, 82, 88, 90, 90, 96, 96], 
        'Nico Hulkenberg': [0, 2, 2, 2, 3, 7, 7, 17, 17, 19, 19, 31, 31, 31, 37, 45, 49, 49, 53, 63], 
        'Pedro de la Rosa': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Narain Karthikeyan': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        "Jerome d'Ambrosio": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Jenson Button': 'McLaren Mercedes', 'Sebastian Vettel': 'Red Bull Racing Renault', 'Lewis Hamilton': 'McLaren Mercedes', 
                      'Mark Webber': 'Red Bull Racing Renault', 'Fernando Alonso': 'Ferrari', 'Kamui Kobayashi': 'Sauber Ferrari', 
                      'Kimi Räikkönen': 'Lotus Renault', 'Sergio Perez': 'Sauber Ferrari', 'Daniel Ricciardo': 'STR Ferrari', 
                      'Paul di Resta': 'Force India Mercedes', 'Jean-Eric Vergne': 'STR Ferrari', 'Nico Rosberg': 'Mercedes', 
                      'Pastor Maldonado': 'Williams Renault', 'Timo Glock': 'Marussia Cosworth', 'Charles Pic': 'Marussia Cosworth', 
                      'Bruno Senna': 'Williams Renault', 'Felipe Massa': 'Ferrari', 'Heikki Kovalainen': 'Caterham Renault',
                      'Vitaly Petrov': 'Caterham Renault', 'Michael Schumacher': 'Mercedes', 'Romain Grosjean': 'Lotus Renault', 
                      'Nico Hulkenberg': 'Force India Mercedes', 'Pedro de la Rosa': 'HRT Cosworth', 
                      'Narain Karthikeyan': 'HRT Cosworth', "Jerome d'Ambrosio": 'Lotus Renault'}


# can add more teams as I add more past data
teamChange = {'Red Bull Racing Renault': "Red Bull", 
              'Ferrari': "Ferrari", 
              'McLaren Mercedes': "McLaren", 
              'Caterham Renault': "Caterham", 
              'Mercedes': "Mercedes", 
              'Lotus Renault': "Lotus", 
              'Force India Mercedes': "Force India", 
              'Marussia Cosworth': "Marussia", 
              'STR Ferrari': "Toro Rosso", 
              'HRT Cosworth': "HRT", 
              'Sauber Ferrari': "Sauber", 
              'Williams Renault': "Williams"}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {"Red Bull": "#1310cf", 
                     "Ferrari": "#EF1A2D", 
                     "McLaren": "#C0C0C0", 
                     "Caterham": "#005030", 
                     "Mercedes": "#00A19B", 
                     "Lotus": "#A39064", 
                     "Force India": "#EE8663", 
                     "Marussia": "#d82f20", 
                     "Toro Rosso": "#A39064", 
                     "HRT": "#8B0000", 
                     "Sauber": "#FFA500", 
                     "Williams": "#00A0DE"}
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
                 "Monaco", "Canada", "Europe", "Great Britain", "Germany",
                 "Hungary", "Belgium", "Italy", "Singapore", "Japan",
                 "South Korea", "India", "Abu Dhabi", "United States", "Brazil"]

