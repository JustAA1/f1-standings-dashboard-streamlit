year = 2007
data = {'Kimi Räikkönen': [10, 16, 22, 22, 23, 27, 32, 42, 52, 52, 60, 68, 74, 84, 90, 100, 110], 
        'Fernando Alonso': [8, 18, 22, 28, 38, 40, 48, 50, 58, 68, 73, 79, 89, 95, 95, 103, 109], 
        'Lewis Hamilton': [6, 14, 22, 30, 38, 48, 58, 64, 70, 70, 80, 84, 92, 97, 107, 107, 109], 
        'Nick Heidfeld': [5, 10, 15, 15, 18, 26, 26, 30, 33, 36, 42, 47, 52, 56, 56, 58, 61], 
        'Giancarlo Fisichella': [4, 7, 8, 8, 13, 13, 13, 16, 17, 17, 17, 17, 17, 17, 21, 21, 21], 
        'Felipe Massa': [3, 7, 17, 27, 33, 33, 39, 47, 51, 59, 59, 69, 69, 77, 80, 86, 94], 
        'Nico Rosberg': [2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 7, 9, 12, 15, 15, 15, 20], 
        'Ralf Schumacher': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5], 
        'Jarno Trulli': [0, 2, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8], 
        'Heikki Kovalainen': [0, 1, 1, 3, 3, 8, 12, 12, 14, 15, 16, 19, 21, 22, 30, 30, 30], 
        'Rubens Barrichello': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Takuma Sato': [0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
        'Mark Webber': [0, 0, 0, 0, 0, 0, 2, 2, 2, 8, 8, 8, 8, 10, 10, 10, 10], 
        'Vitantonio Liuzzi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3], 
        'Jenson Button': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 6, 6], 
        'Anthony Davidson': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Adrian Sutil': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
        'Alexander Wurz': [0, 0, 0, 0, 2, 8, 8, 8, 8, 13, 13, 13, 13, 13, 13, 13, 13], 
        'David Coulthard': [0, 0, 0, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 13, 14, 14], 
        'Robert Kubica': [0, 0, 3, 8, 12, 12, 12, 17, 22, 24, 28, 29, 33, 33, 35, 35, 39], 
        'Scott Speed': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Christijan Albers': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sebastian Vettel': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6], 
        'Markus Winkelhock': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Sakon Yamamoto': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Kazuki Nakajima': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Kimi Räikkönen': 'Ferrari', 'Fernando Alonso': 'McLaren Mercedes', 'Lewis Hamilton': 'McLaren Mercedes', 
                      'Nick Heidfeld': 'Sauber BMW', 'Giancarlo Fisichella': 'Renault', 'Felipe Massa': 'Ferrari', 
                      'Nico Rosberg': 'Williams Toyota', 'Ralf Schumacher': 'Toyota', 'Jarno Trulli': 'Toyota', 
                      'Heikki Kovalainen': 'Renault', 'Rubens Barrichello': 'Honda', 'Takuma Sato': 'Super Aguri Honda', 
                      'Mark Webber': 'Red Bull Renault', 'Vitantonio Liuzzi': 'STR Ferrari', 'Jenson Button': 'Honda', 
                      'Anthony Davidson': 'Super Aguri Honda', 'Adrian Sutil': 'Spyker Ferrari', 'Alexander Wurz': 'Williams Toyota', 
                      'David Coulthard': 'Red Bull Renault', 'Robert Kubica': 'Sauber BMW', 'Scott Speed': 'STR Ferrari', 
                      'Christijan Albers': 'Spyker Ferrari', 'Sebastian Vettel': 'STR Ferrari', 'Markus Winkelhock': 'Spyker Ferrari', 
                      'Sakon Yamamoto': 'Spyker Ferrari', 'Kazuki Nakajima': 'Williams Toyota'}

# can add more teams as I add more past data
teamChange = {'McLaren Mercedes': 'McLaren', 
              'Williams Toyota': 'Williams', 
              'Sauber BMW': 'Sauber', 
              'Spyker Ferrari': 'Spyker', 
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
                     'Spyker': '#EE8663',  # Orange
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
                 "Monaco", "Canada", "United States", "France", 
                 "Great Britain", "Europe", "Hungary", "Turkey", 
                 "Italy", "Belgium", "Japan", "China", "Brazil"]

