year = 2009
data = {'Jenson Button': [10, 20, 26, 36, 46, 56, 66, 69, 73, 75, 77, 77, 85, 89, 90, 94, 100], 
        'Rubens Barrichello': [8, 12, 17, 21, 29, 37, 37, 43, 46, 46, 56, 58, 68, 71, 73, 74, 79], 
        'Jarno Trulli': [6, 11, 11, 17, 17, 17, 22, 24, 24, 25, 25, 25, 25, 25, 33, 33, 35], 
        'Lewis Hamilton': [0, 2, 5, 10, 10, 10, 10, 10, 10, 20, 28, 28, 28, 38, 44, 50, 50], 
        'Timo Glock': [5, 11, 13, 15, 15, 15, 16, 16, 16, 19, 19, 19, 19, 27, 27, 27, 27], 
        'Fernando Alonso': [4, 4, 4, 5, 9, 11, 11, 11, 13, 13, 16, 16, 20, 26, 26, 26, 26], 
        'Nico Rosberg': [3, 4, 4, 4, 5, 8, 12, 16, 21, 26, 30, 31, 31, 31, 35, 35, 35], 
        'Sebastien Buemi': [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6], 
        'Sebastien Bourdais': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
        'Adrian Sutil': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5], 
        'Nick Heidfeld': [0, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 14, 16, 16, 19, 19, 23], 
        'Giancarlo Fisichella': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8], 
        'Mark Webber': [0, 3, 11, 11, 17, 21, 29, 37, 47, 53, 53, 53, 53, 53, 53, 63, 71], 
        'Sebastian Vettel': [0, 0, 10, 18, 23, 23, 29, 39, 47, 47, 47, 53, 54, 59, 69, 74, 84], 
        'Robert Kubica': [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 3, 8, 8, 9, 9, 17, 17], 
        'Kimi Räikkönen': [0, 0, 0, 3, 3, 9, 9, 10, 10, 18, 24, 34, 40, 40, 45, 48, 48], 
        'Felipe Massa': [0, 0, 0, 0, 3, 8, 11, 16, 22, 22, 22, 22, 22, 22, 22, 22, 22], 
        'Nelson Piquet': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Kazuki Nakajima': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Heikki Kovalainen': [0, 0, 4, 4, 4, 4, 4, 4, 5, 9, 14, 17, 20, 22, 22, 22, 22], 
        'Jaime Alguersuari': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Romain Grosjean': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Luca Badoer': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Vitantonio Liuzzi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Kamui Kobayashi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Jenson Button': 'Brawn Mercedes', 'Rubens Barrichello': 'Brawn Mercedes', 'Jarno Trulli': 'Toyota', 
                      'Lewis Hamilton': 'McLaren Mercedes', 'Timo Glock': 'Toyota', 'Fernando Alonso': 'Renault', 
                      'Nico Rosberg': 'Williams Toyota', 'Sebastien Buemi': 'STR Ferrari', 'Sebastien Bourdais': 'STR Ferrari', 
                      'Adrian Sutil': 'Force India Mercedes', 'Nick Heidfeld': 'Sauber BMW', 'Giancarlo Fisichella': 'Ferrari', 
                      'Mark Webber': 'RBR Renault', 'Sebastian Vettel': 'RBR Renault', 'Robert Kubica': 'Sauber BMW', 
                      'Kimi Räikkönen': 'Ferrari', 'Felipe Massa': 'Ferrari', 'Nelson Piquet': 'Renault', 
                      'Kazuki Nakajima': 'Williams Toyota', 'Heikki Kovalainen': 'McLaren Mercedes', 
                      'Jaime Alguersuari': 'STR Ferrari', 'Romain Grosjean': 'Renault', 'Luca Badoer': 'Ferrari', 
                      'Vitantonio Liuzzi': 'Force India Mercedes', 'Kamui Kobayashi': 'Toyota'}

# can add more teams as I add more past data
teamChange = {'McLaren Mercedes': 'McLaren', 
              'Williams Toyota': 'Williams', 
              'Sauber BMW': 'Sauber', 
              'Force India Mercedes': 'Force India', 
              'STR Ferrari': 'Toro Rosso',
              'Brawn Mercedes': 'Brawn', 
              'RBR Renault': 'Red Bull', 
              'Renault': 'Renault',
              'Toyota': 'Toyota',
              'Ferrari': 'Ferrari'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'McLaren': '#C0C0C0',  # Silver
                     'Williams': '#00A0DE',  # Blue
                     'Sauber': '#638CB3',  # White
                     'Force India': '#F9A602',  # Orange
                     'Toro Rosso': '#A39064',  # Dark Blue
                     'Brawn': '#DFFF00',  # White
                     'Red Bull': '#1310cf',  # Dark Blue
                     'Renault': '#FFD800',  # Yellow
                     'Toyota': '#58595B',  # Red
                     'Ferrari': '#EF1A2D'}  # Ferrari Red
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


raceLocations = ["Australia", "Malaysia", "China", "Bahrain", 
                 "Spain", "Monaco", "Turkey", "Great Britain", 
                 "Germany", "Hungary", "Europe", "Belgium", 
                 "Italy", "Singapore", "Japan", "Brazil", "Abu Dhabi"]

