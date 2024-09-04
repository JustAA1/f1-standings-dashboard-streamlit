year = 2021
data = {'Lewis Hamilton': [25, 44, 69, 94, 101, 101, 119, 138, 150, 177, 195, 202.5, 221.5, 221.5, 246.5, 256.5, 275.5, 293.5, 318.5, 343.5, 369.5, 387.5], 
        'Max Verstappen': [18, 43, 61, 80, 105, 105, 131, 156, 182, 185, 187, 199.5, 224.5, 226.5, 244.5, 262.5, 287.5, 312.5, 332.5, 351.5, 369.5, 395.5], 
        'Valtteri Bottas': [16, 16, 32, 47, 47, 47, 59, 74, 92, 108, 108, 108, 123, 141, 151, 177, 185, 185, 203, 203, 218, 226], 
        'Lando Norris': [12, 27, 37, 41, 56, 66, 76, 86, 101, 113, 113, 113, 114, 132, 139, 145, 149, 150, 151, 153, 154, 160], 
        'Sergio Perez': [10, 10, 22, 32, 44, 69, 84, 96, 104, 104, 104, 104, 108, 118, 120, 135, 150, 165, 178, 190, 190, 190], 
        'Charles Leclerc': [8, 20, 28, 40, 40, 52, 52, 58, 62, 80, 80, 82, 92, 104, 104, 116, 128, 138, 148, 152, 158, 159], 
        'Daniel Ricciardo': [6, 14, 16, 24, 24, 26, 34, 34, 40, 50, 50, 56, 56, 83, 95, 95, 105, 105, 105, 105, 115, 115], 
        'Carlos Sainz': [4, 14, 14, 20, 38, 42, 42, 50, 60, 68, 83, 83.5, 89.5, 97.5, 112.5, 116.5, 122.5, 130.5, 139.5, 145.5, 149.5, 164.5], 
        'Yuki Tsunoda': [2, 2, 2, 2, 2, 8, 8, 9, 9, 10, 18, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20, 32], 
        'Lance Stroll': [1, 5, 5, 5, 9, 9, 10, 14, 14, 18, 18, 18, 18, 24, 24, 26, 26, 26, 26, 34, 34, 34], 
        'Kimi Räikkönen': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 6, 6, 6, 10, 10, 10, 10, 10, 10, 10], 
        'Antonio Giovinazzi': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3], 
        'Esteban Ocon': [0, 2, 8, 10, 12, 12, 12, 12, 12, 14, 39, 42, 44, 45, 45, 46, 46, 46, 50, 60, 72, 74], 
        'George Russell': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 13, 13, 15, 16, 16, 16, 16, 16, 16, 16, 16], 
        'Sebastian Vettel': [0, 0, 0, 0, 10, 28, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 36, 42, 42, 43, 43, 43], 
        'Mick Schumacher': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Pierre Gasly': [0, 6, 7, 8, 16, 31, 37, 37, 39, 39, 49, 53, 65, 65, 65, 73, 73, 85, 91, 91, 99, 109], 
        'Nicholas Latifi': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
        'Fernando Alonso': [0, 1, 5, 5, 5, 13, 17, 19, 20, 26, 38, 38, 46, 50, 58, 58, 58, 60, 62, 77, 77, 81], 
        'Nikita Mazepin': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        'Robert Kubica': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
data = dict(sorted(data.items(), key=lambda item: item[1][-1], reverse=True))

# saving time not waiting for data
tempDriverTeamData = {'Lewis Hamilton': 'Mercedes', 'Max Verstappen': 'Red Bull Racing Honda', 
                      'Valtteri Bottas': 'Mercedes', 'Lando Norris': 'McLaren Mercedes', 
                      'Sergio Perez': 'Red Bull Racing Honda', 'Charles Leclerc': 'Ferrari', 
                      'Daniel Ricciardo': 'McLaren Mercedes', 'Carlos Sainz': 'Ferrari', 
                      'Yuki Tsunoda': 'AlphaTauri Honda', 'Lance Stroll': 'Aston Martin Mercedes', 
                      'Kimi Räikkönen': 'Alfa Romeo Racing Ferrari', 'Antonio Giovinazzi': 'Alfa Romeo Racing Ferrari', 
                      'Esteban Ocon': 'Alpine Renault', 'George Russell': 'Williams Mercedes', 
                      'Sebastian Vettel': 'Aston Martin Mercedes', 'Mick Schumacher': 'Haas Ferrari', 
                      'Pierre Gasly': 'AlphaTauri Honda', 'Nicholas Latifi': 'Williams Mercedes', 
                      'Fernando Alonso': 'Alpine Renault', 'Nikita Mazepin': 'Haas Ferrari', 
                      'Robert Kubica': 'Alfa Romeo Racing Ferrari'}

# can add more teams as I add more past data
teamChange = {'Red Bull Racing Honda': 'Red Bull', 
              'Ferrari': 'Ferrari', 
              'Mercedes': 'Mercedes', 
              'McLaren Mercedes': 'McLaren', 
              'Aston Martin Mercedes': 'Aston Martin', 
              'Alfa Romeo Racing Ferrari': 'Alfa Romeo', 
              'Haas Ferrari': 'Haas', 
              'AlphaTauri Honda': 'AlphaTauri', 
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
                     'Haas': '#F7F5EC', 
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


raceLocations = ["Bahrain", "Imola", "Portugal", "Spain", "Monaco", "Azerbaijan", 
                 "France", "Styria", "Austria", "Great Britain", "Hungary", "Belgium", "Netherlands", 
                 "Monza", "Russia", "Turkey", "United States", "Mexico", "Brazil", 
                 "Qatar", "Saudi Arabia", "Abu Dhabi"]


#print(driverData)
