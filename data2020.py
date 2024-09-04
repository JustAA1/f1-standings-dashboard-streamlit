year = 2020
data = {'Valtteri Bottas': [25, 43, 58, 58, 73, 89, 107, 117, 135, 161, 161, 179, 197, 197, 201, 205, 223], 
        'Charles Leclerc': [18, 18, 18, 33, 45, 45, 45, 45, 49, 57, 63, 75, 85, 97, 98, 98, 98], 
        'Lando Norris': [16, 26, 26, 36, 38, 39, 45, 57, 65, 65, 65, 65, 69, 74, 86, 87, 97], 
        'Lewis Hamilton': [12, 37, 63, 88, 107, 132, 157, 164, 190, 205, 230, 256, 282, 307, 332, 332, 347], 
        'Carlos Sainz': [10, 13, 15, 15, 15, 23, 23, 41, 41, 41, 51, 59, 65, 75, 85, 97, 105], 
        'Sergio Perez': [8, 16, 22, 22, 22, 32, 33, 34, 44, 56, 68, 74, 82, 100, 100, 125, 125], 
        'Pierre Gasly': [6, 6, 6, 12, 12, 14, 18, 43, 43, 45, 53, 63, 63, 63, 71, 71, 75], 
        'Esteban Ocon': [4, 4, 4, 12, 16, 16, 26, 30, 30, 36, 36, 40, 40, 40, 42, 60, 62], 
        'Antonio Giovinazzi': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4], 
        'Sebastian Vettel': [1, 1, 9, 10, 10, 16, 16, 16, 17, 17, 17, 18, 18, 33, 33, 33, 33], 
        'Nicholas Latifi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Daniil Kvyat': [0, 1, 1, 1, 2, 2, 2, 4, 10, 14, 14, 14, 26, 26, 26, 32, 32], 
        'Alexander Albon': [0, 12, 22, 26, 36, 40, 48, 48, 63, 64, 64, 64, 64, 70, 85, 93, 105], 
        'Kimi Räikkönen': [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4], 
        'George Russell': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3], 
        'Romain Grosjean': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2], 
        'Kevin Magnussen': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        'Lance Stroll': [0, 6, 18, 20, 28, 40, 42, 57, 57, 57, 57, 57, 57, 59, 59, 74, 75], 
        'Daniel Ricciardo': [0, 4, 8, 20, 20, 20, 33, 41, 53, 63, 78, 80, 95, 96, 102, 112, 119], 
        'Max Verstappen': [0, 15, 33, 52, 77, 95, 110, 110, 110, 128, 147, 162, 162, 170, 189, 189, 214], 
        'Nico Hulkenberg': [0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 10, 10, 10, 10, 10, 10, 10], 
        'Jack Aitken': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Pietro Fittipaldi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Valtteri Bottas': 'Mercedes', 'Charles Leclerc': 'Ferrari', 
                      'Lando Norris': 'McLaren Renault', 'Lewis Hamilton': 'Mercedes', 
                      'Carlos Sainz': 'McLaren Renault', 'Sergio Perez': 'Racing Point BWT Mercedes', 
                      'Pierre Gasly': 'AlphaTauri Honda', 'Esteban Ocon': 'Renault', 
                      'Antonio Giovinazzi': 'Alfa Romeo Racing Ferrari', 'Sebastian Vettel': 'Ferrari', 
                      'Nicholas Latifi': 'Williams Mercedes', 'Daniil Kvyat': 'AlphaTauri Honda', 
                      'Alexander Albon': 'Red Bull Racing Honda', 'Kimi Räikkönen': 'Alfa Romeo Racing Ferrari', 
                      'George Russell': 'Williams Mercedes', 'Romain Grosjean': 'Haas Ferrari', 
                      'Kevin Magnussen': 'Haas Ferrari', 'Lance Stroll': 'Racing Point BWT Mercedes', 
                      'Daniel Ricciardo': 'Renault', 'Max Verstappen': 'Red Bull Racing Honda', 
                      'Nico Hulkenberg': 'Racing Point BWT Mercedes', 'Jack Aitken': 'Williams Mercedes', 
                      'Pietro Fittipaldi': 'Haas Ferrari'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Honda': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Renault': 'McLaren', 
              'Racing Point BWT Mercedes': 'Racing Point', 
              'Alfa Romeo Racing Ferrari': 'Alfa Romeo', 
              'Haas Ferrari': 'Haas', 
              'AlphaTauri Honda': 'AlphaTauri', 
              'Williams Mercedes': 'Williams', 
              'Renault': 'Renault'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Racing Point': '#F363B9', 
                     'Alfa Romeo': '#A50F2D', 
                     'Haas': '#F7F5EC', 
                     'AlphaTauri': '#20394C',
                     'Williams': '#00A0DE', 
                     'Renault': '#FFF500'}
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


raceLocations = ["Austria", "Styria", "Hungary", "Great Britain", 
                 "70th Anniversary", "Spain", "Belgium", "Italy", 
                 "Tuscany", "Russia", "Eifel", "Portugal", 
                 "Imola", "Turkey", "Bahrain", "Sakhir", "Abu Dhabi"]

