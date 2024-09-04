year = 2008
data = {'Lewis Hamilton': [10, 14, 14, 20, 28, 38, 38, 38, 48, 58, 62, 70, 76, 78, 84, 84, 94, 98], 
        'Nick Heidfeld': [8, 11, 16, 16, 20, 20, 28, 28, 36, 41, 41, 41, 49, 53, 56, 56, 60, 60], 
        'Nico Rosberg': [6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 17, 17, 17, 17], 
        'Fernando Alonso': [5, 6, 6, 6, 9, 9, 9, 10, 13, 13, 18, 18, 23, 28, 38, 48, 53, 61], 
        'Heikki Kovalainen': [4, 10, 14, 14, 14, 15, 15, 20, 24, 28, 38, 43, 43, 51, 51, 51, 51, 53], 
        'Kazuki Nakajima': [3, 3, 3, 5, 5, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9], 
        'Sebastien Bourdais': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4], 
        'Kimi Räikkönen': [1, 11, 19, 29, 35, 35, 35, 43, 48, 51, 57, 57, 57, 57, 57, 63, 69, 75], 
        'Robert Kubica': [0, 8, 14, 19, 24, 32, 42, 46, 46, 48, 49, 55, 58, 64, 64, 72, 75, 75], 
        'Timo Glock': [0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 13, 15, 15, 15, 20, 20, 22, 25], 
        'Takuma Sato': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Nelson Piquet': [0, 0, 0, 0, 0, 0, 0, 2, 2, 10, 13, 13, 13, 13, 13, 18, 19, 19], 
        'Felipe Massa': [0, 0, 10, 18, 28, 34, 38, 48, 48, 54, 54, 64, 74, 77, 77, 79, 87, 97], 
        'David Coulthard': [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8], 
        'Jarno Trulli': [0, 5, 8, 9, 9, 9, 12, 18, 20, 20, 22, 26, 26, 26, 26, 30, 30, 31], 
        'Adrian Sutil': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sebastian Vettel': [0, 0, 0, 0, 0, 4, 5, 5, 5, 6, 6, 9, 13, 23, 27, 30, 30, 35], 
        'Jenson Button': [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
        'Mark Webber': [0, 2, 4, 8, 10, 15, 15, 18, 18, 18, 18, 18, 19, 20, 20, 21, 21, 21], 
        'Giancarlo Fisichella': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Anthony Davidson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Rubens Barrichello': [0, 0, 0, 0, 0, 3, 5, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Lewis Hamilton': 'McLaren Mercedes', 'Nick Heidfeld': 'Sauber BMW', 'Nico Rosberg': 'Williams Toyota', 
                      'Fernando Alonso': 'Renault', 'Heikki Kovalainen': 'McLaren Mercedes', 'Kazuki Nakajima': 'Williams Toyota', 
                      'Sebastien Bourdais': 'STR Ferrari', 'Kimi Räikkönen': 'Ferrari', 'Robert Kubica': 'Sauber BMW', 
                      'Timo Glock': 'Toyota', 'Takuma Sato': 'Super Aguri Honda', 'Nelson Piquet': 'Renault', 
                      'Felipe Massa': 'Ferrari', 'David Coulthard': 'Red Bull Renault', 'Jarno Trulli': 'Toyota', 
                      'Adrian Sutil': 'Force India Ferrari', 'Sebastian Vettel': 'STR Ferrari', 'Jenson Button': 'Honda', 
                      'Mark Webber': 'Red Bull Renault', 'Giancarlo Fisichella': 'Force India Ferrari', 
                      'Anthony Davidson': 'Super Aguri Honda', 'Rubens Barrichello': 'Honda'}

# can add more teams as I add more past data
teamChange = {'McLaren Mercedes': 'McLaren', 
              'Williams Toyota': 'Williams', 
              'Sauber BMW': 'Sauber', 
              'Force India Ferrari': 'Force India', 
              'STR Ferrari': 'Toro Rosso',
              'Honda': 'Honda', 
              'Super Aguri Honda': 'Super Aguri', 
              'Red Bull Renault': 'Red Bull', 
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
                     'Honda': '#61D1A6',  # White
                     'Super Aguri': '#8B0000',  # White
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


raceLocations = ["Australia", "Malaysia", "Bahrain", "Spain", 
                 "Turkey", "Monaco", "Canada", "France", 
                 "Great Britain", "Germany", "Hungary", "Europe", 
                 "Belgium", "Italy", "Singapore", "Japan", "China", "Brazil"]

