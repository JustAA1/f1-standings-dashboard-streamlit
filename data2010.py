year = 2010
data = {'Fernando Alonso': [25, 37, 37, 49, 67, 75, 79, 94, 98, 98, 123, 141, 141, 166, 191, 206, 231, 246, 252], 
        'Felipe Massa': [18, 33, 39, 41, 49, 61, 67, 67, 67, 67, 85, 97, 109, 124, 128, 128, 143, 143, 144], 
        'Lewis Hamilton': [15, 23, 31, 49, 49, 59, 84, 109, 127, 145, 157, 157, 182, 182, 182, 192, 210, 222, 240], 
        'Sebastian Vettel': [12, 12, 37, 45, 60, 78, 78, 90, 115, 121, 136, 151, 151, 163, 181, 206, 206, 231, 256], 
        'Nico Rosberg': [10, 20, 35, 50, 50, 56, 66, 74, 75, 90, 94, 94, 102, 112, 122, 122, 122, 130, 142], 
        'Michael Schumacher': [8, 9, 9, 10, 22, 22, 34, 34, 34, 36, 38, 38, 44, 46, 46, 54, 66, 72, 72], 
        'Jenson Button': [6, 31, 35, 60, 70, 70, 88, 106, 121, 133, 143, 147, 147, 165, 177, 189, 189, 199, 214], 
        'Mark Webber': [4, 6, 24, 28, 53, 78, 93, 103, 103, 128, 136, 161, 179, 187, 202, 220, 220, 238, 242], 
        'Vitantonio Liuzzi': [2, 8, 8, 8, 8, 10, 10, 12, 12, 12, 12, 12, 13, 13, 13, 13, 21, 21, 21], 
        'Rubens Barrichello': [1, 5, 5, 5, 7, 7, 7, 7, 19, 29, 29, 30, 30, 31, 39, 41, 47, 47, 47], 
        'Robert Kubica': [0, 18, 30, 40, 44, 59, 67, 73, 83, 83, 89, 89, 104, 108, 114, 114, 124, 126, 136], 
        'Adrian Sutil': [0, 0, 10, 10, 16, 20, 22, 23, 31, 35, 35, 35, 45, 45, 47, 47, 47, 47, 47], 
        'Jaime Alguersuari': [0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5], 
        'Nico Hulkenberg': [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 10, 10, 16, 17, 17, 18, 22, 22], 
        'Heikki Kovalainen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sebastien Buemi': [0, 0, 0, 0, 0, 1, 1, 5, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8], 
        'Jarno Trulli': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Pedro de la Rosa': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6], 
        'Bruno Senna': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Timo Glock': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Vitaly Petrov': [0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 7, 17, 19, 19, 19, 19, 19, 19, 27], 
        'Kamui Kobayashi': [0, 0, 0, 0, 0, 0, 1, 1, 7, 15, 15, 17, 21, 21, 21, 27, 31, 32, 32], 
        'Lucas di Grassi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Karun Chandhok': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sakon Yamamoto': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Nick Heidfeld': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 6, 6], 
        'Christian Klien': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Fernando Alonso': 'Ferrari', 'Felipe Massa': 'Ferrari', 'Lewis Hamilton': 'McLaren Mercedes', 
                      'Sebastian Vettel': 'RBR Renault', 'Nico Rosberg': 'Mercedes', 'Michael Schumacher': 'Mercedes', 
                      'Jenson Button': 'McLaren Mercedes', 'Mark Webber': 'RBR Renault', 'Vitantonio Liuzzi': 'Force India Mercedes', 
                      'Rubens Barrichello': 'Williams Cosworth', 'Robert Kubica': 'Renault', 'Adrian Sutil': 'Force India Mercedes', 
                      'Jaime Alguersuari': 'STR Ferrari', 'Nico Hulkenberg': 'Williams Cosworth', 'Heikki Kovalainen': 'Lotus Cosworth', 
                      'Sebastien Buemi': 'STR Ferrari', 'Jarno Trulli': 'Lotus Cosworth', 'Pedro de la Rosa': 'Sauber Ferrari', 
                      'Bruno Senna': 'HRT Cosworth', 'Timo Glock': 'Virgin Cosworth', 'Vitaly Petrov': 'Renault', 'Kamui Kobayashi': 'Sauber Ferrari', 
                      'Lucas di Grassi': 'Virgin Cosworth', 'Karun Chandhok': 'HRT Cosworth', 'Sakon Yamamoto': 'HRT Cosworth', 
                      'Nick Heidfeld': 'Sauber Ferrari', 'Christian Klien': 'HRT Cosworth'}


# can add more teams as I add more past data
teamChange = {'RBR Renault': "Red Bull", 
              'Ferrari': "Ferrari", 
              'McLaren Mercedes': "McLaren", 
              'Mercedes': "Mercedes", 
              'Lotus Cosworth': "Lotus", 
              'Force India Mercedes': "Force India", 
              'STR Ferrari': "Toro Rosso", 
              'HRT Cosworth': "HRT", 
              'Sauber Ferrari': "Sauber", 
              'Williams Cosworth': "Williams",
              'Virgin Cosworth': "Virgin",
              'Renault': "Renault"}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {"Red Bull": "#1310cf", 
                     "Ferrari": "#EF1A2D", 
                     "McLaren": "#C0C0C0", 
                     "Mercedes": "#00A19B", 
                     "Lotus": "#A39064", 
                     "Force India": "#EE8663", 
                     "Toro Rosso": "#A39064", 
                     "HRT": "#8B0000", 
                     "Sauber": "#FFA500", 
                     "Williams": "#00A0DE",
                     "Virgin": "#cc0000",
                     "Renault": "#FFF500"}
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


raceLocations = ["Bahrain", "Australia", "Malaysia", "China", "Spain",
                 "Monaco", "Turkey", "Canada", "Europe", "Great Britain",
                 "Germany", "Hungary", "Belgium", "Italy", "Singapore",
                 "Japan", "South Korea", "Brazil", "Abu Dhabi"]

