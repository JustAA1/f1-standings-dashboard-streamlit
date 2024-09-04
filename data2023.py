year = 2023
data = {'Max Verstappen': [25, 44, 69, 93, 119, 144, 170, 195, 229, 255, 281, 314, 339, 364, 374, 400, 433, 466, 491, 524, 549, 575], 
         'Sergio Perez': [18, 43, 54, 87, 105, 105, 117, 126, 148, 156, 171, 189, 201, 219, 223, 223, 224, 240, 240, 258, 273, 285], 
         'Fernando Alonso': [15, 30, 45, 60, 75, 93, 99, 117, 131, 137, 139, 149, 168, 170, 170, 174, 183, 183, 183, 198, 200, 206], 
         'Carlos Sainz': [12, 20, 20, 34, 44, 48, 58, 68, 82, 83, 87, 92, 102, 117, 142, 150, 153, 171, 183, 192, 200, 200], 
         'Lewis Hamilton': [10, 20, 38, 48, 56, 69, 87, 102, 106, 121, 133, 148, 156, 164, 180, 190, 194, 201, 220, 226, 232, 234], 
         'Lance Stroll': [8, 8, 20, 27, 27, 27, 35, 37, 44, 44, 45, 47, 47, 47, 47, 47, 53, 53, 63, 73, 74, 74], 
         'George Russell': [6, 18, 18, 28, 40, 50, 65, 65, 72, 82, 90, 99, 99, 109, 109, 115, 132, 143, 151, 156, 160, 175], 
         'Valtteri Bottas': [4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 10, 10, 10, 10, 10, 10], 
         'Pierre Gasly': [2, 4, 4, 4, 8, 14, 15, 15, 16, 16, 16, 22, 37, 37, 45, 46, 46, 56, 56, 62, 62, 62], 
         'Alexander Albon': [1, 1, 1, 1, 1, 1, 1, 7, 7, 11, 11, 11, 15, 21, 21, 21, 23, 25, 27, 27, 27, 27], 
         'Yuki Tsunoda': [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 8, 8, 13, 13, 17], 
         'Logan Sargeant': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
         'Kevin Magnussen': [0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3], 
         'Nyck de Vries': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         'Nico Hulkenberg': [0, 0, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
         'Zhou Guanyu': [0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6], 
         'Lando Norris': [0, 0, 8, 10, 10, 12, 12, 12, 24, 42, 60, 69, 75, 79, 97, 115, 136, 159, 169, 195, 195, 205], 
         'Esteban Ocon': [0, 4, 4, 4, 6, 21, 25, 29, 31, 31, 31, 35, 36, 36, 36, 38, 44, 44, 45, 46, 58, 58], 
         'Charles Leclerc': [0, 6, 6, 28, 34, 42, 42, 54, 72, 74, 80, 99, 99, 111, 123, 135, 145, 151, 166, 170, 188, 206], 
         'Oscar Piastri': [0, 0, 4, 4, 4, 5, 5, 5, 5, 17, 27, 34, 36, 36, 42, 57, 83, 83, 87, 87, 89, 97], 
         'Daniel Ricciardo': [0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
         'Liam Lawson': [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Max Verstappen': 'Red Bull Racing Honda RBPT', 'Sergio Perez': 'Red Bull Racing Honda RBPT', 
                      'Fernando Alonso': 'Aston Martin Aramco Mercedes', 'Carlos Sainz': 'Ferrari', 
                      'Lewis Hamilton': 'Mercedes', 'Lance Stroll': 'Aston Martin Aramco Mercedes', 
                      'George Russell': 'Mercedes', 'Valtteri Bottas': 'Alfa Romeo Ferrari', 
                      'Pierre Gasly': 'Alpine Renault', 'Alexander Albon': 'Williams Mercedes', 
                      'Yuki Tsunoda': 'AlphaTauri Honda RBPT', 'Logan Sargeant': 'Williams Mercedes', 
                      'Kevin Magnussen': 'Haas Ferrari', 'Nyck de Vries': 'AlphaTauri Honda RBPT', 
                      'Nico Hulkenberg': 'Haas Ferrari', 'Zhou Guanyu': 'Alfa Romeo Ferrari', 
                      'Lando Norris': 'McLaren Mercedes', 'Esteban Ocon': 'Alpine Renault', 
                      'Charles Leclerc': 'Ferrari', 'Oscar Piastri': 'McLaren Mercedes', 
                      'Daniel Ricciardo': 'AlphaTauri Honda RBPT', 'Liam Lawson': 'AlphaTauri Honda RBPT'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Honda RBPT': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Aston Martin Aramco Mercedes': 'Aston Martin', 
              'Alfa Romeo Ferrari': 'Alfa Romeo', 
              'Haas Ferrari': 'Haas', 
              'AlphaTauri Honda RBPT': 'AlphaTauri', 
              'Williams Mercedes': 'Williams', 
              'Alpine Renault': 'Alpine'}


# data to be used (including "data")
# can add more teams probably (with more years)
teamWithHexColors = {'Red Bull': '#1310cf', 
                     'Ferrari': '#EF1A2D', 
                     'Mercedes': '#00A19B', 
                     'McLaren': '#FF8000', 
                     'Aston Martin': '#09826e', 
                     'Alfa Romeo': '#A50F2D', 
                     'Haas': '#9c091d', 
                     'AlphaTauri': '#20394C',
                     'Williams': '#00A0DE', 
                     'Alpine': '#0e62c2'}
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


raceLocations = ["Bahrain", "Saudi Arabia", "Australia", "Azerbaijan", "Miami", "Monaco", 
                 "Spain", "Canada", "Austria", "Great Britain", "Hungary", "Belgium", "Netherlands", 
                 "Monza", "Singapore", "Japan", "Qatar", "United States", "Mexico", "Brazil", 
                 "Las Vegas", "Abu Dhabi"]


#print(driverData)
