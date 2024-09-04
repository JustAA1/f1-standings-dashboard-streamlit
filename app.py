import streamlit as st
from streamlit_echarts import st_echarts

def titlePage():
    # Basic Information Section
    st.header("Welcome to the F1 Standings Dashboard!")
    st.write("""
    This app provides up-to-date and historical standings for the Formula 1 Drivers and Constructors Championships, 
    allowing you to explore how your favorite drivers and teams are performing or how they have performed historically. 
    The dashboard offers various visualizations and insights to help you understand the points distribution and trends across the races for a particular season.

    ### Key Features:
    - **Real-time Standings**: Get the latest updates on this season's Drivers' and Constructors' Championship standings.
    - **Interactive Charts**: Visualize the points earned by each team and driver over the course of the season.
    - **Historical Data**: Dive into past seasons to see how teams and drivers have performed historically. 
        * Currently supports 2007-2024 with more seasons on the way!
    - **Customizable**: Easily switch between Drivers' and Constructors' Championship standings.
    """)

    # Create two columns
    col1, col2 = st.columns([3, 2])

    with col1:
        st.write("""
        ### How to use the dashboard:
        - Use the sidebar to select the year and championship you want to view.
        - The dashboard will automatically update to show the standings for the selected year and championship.
        - You can hover over the points to see the exact points and the change from the previous race.
        """)

    with col2:
        st.image("https://i.postimg.cc/3RQzm9yg/Screenshot-2024-09-01-at-13-00-13.png", caption="Dashboard Preview", use_column_width=True)


# sidebar title
st.sidebar.title("F1 Standings")
# year selection in sidebar
option = st.sidebar.selectbox(
    "Select year:",
    ("2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007"),
    index=None,
    placeholder="Select year...",
)

# pick between drivers and constructors
selection = st.sidebar.radio(
    "Select championship:",
    ["Drivers", "Constructors"],
    disabled=(option is None)  # Disable if no year is selected
)

if option == "2024":
    import data2024 as f1Data
elif option == "2023":
    import data2023 as f1Data
elif option == "2022":
    import data2022 as f1Data
elif option == "2021":
    import data2021 as f1Data
elif option == "2020":
    import data2020 as f1Data
elif option == "2019":
    import data2019 as f1Data
elif option == "2018":
    import data2018 as f1Data
elif option == "2017":
    import data2017 as f1Data
elif option == "2016":
    import data2016 as f1Data
elif option == "2015":
    import data2015 as f1Data
elif option == "2014":
    import data2014 as f1Data
elif option == "2013":
    import data2013 as f1Data
elif option == "2012":
    import data2012 as f1Data
elif option == "2011":
    import data2011 as f1Data
elif option == "2010":
    import data2010 as f1Data
elif option == "2009":
    import data2009 as f1Data
elif option == "2008":
    import data2008 as f1Data
elif option == "2007":
    import data2007 as f1Data
else:
    titlePage()


def constructorsStandings():
    st.title("F1 Constructors Standings")

    f1Data2 = {
        "teamsWithPoints": f1Data.teamsWithPoints,
        "raceLocations": f1Data.raceLocations
    }

    # Create datasets for each team
    datasets = [
        {
            "id": f"dataset_{team}",
            "source": [[i, points, f1Data2["raceLocations"][i], f"(+{change})"] for i, points, change in zip(range(len(points_list[0])), points_list[0], points_list[1])]
        }
        for team, points_list in f1Data2["teamsWithPoints"].items()
    ]

    # Create series configuration for each team
    seriesList = [
        {
            "type": "line",
            "datasetId": f"dataset_{team}",
            "showSymbol": True,
            "name": team,
            "endLabel": {
                "show": True,
                "formatter": "{@[1]}" + f" - {team}",
                "fontSize": 12,  # Increase font size
                "textBorderColor": f1Data.teamWithHexColors[team],  # Add text border color (black in this example)
                "textBorderWidth": 2,  # Add text border width
                "color": "black",
            },
            "labelLayout": {"moveOverlap": "shiftY"},
            "emphasis": {"focus": "series"},
            "encode": {
                "x": 0,  # Index of the x-values in the dataset (Race #)
                "y": 1,  # Index of the y-values in the dataset (Points)
                "tooltip": [1, 3]
            },
            "itemStyle": {
                "color": f1Data.teamWithHexColors[team]
            }
        }
        for team in f1Data2["teamsWithPoints"].keys()
    ]

    # Configure the chart options
    option = {
        "animationDuration": 500,
        "dataset": datasets,  # Use the datasets created above
        "title": {"text": f"Year: {f1Data.year}"},
        "tooltip": {
            "trigger": "axis",
        },
        "xAxis": {
            "type": "category",
            "nameLocation": "middle",
            "axisLabel": {
                "rotate": 45,  # Rotate labels 45 degrees
                "formatter": "{value}",  # Custom format for labels
                "fontSize": 11,  # Font size
                "fontWeight": "bold"  # Font weight
            },
            "data": f1Data2["raceLocations"]  # Set x-axis labels (categories)
        },
        #"xAxis": {"type": "category", "name": "Race #", "nameLocation": "middle"},
        "yAxis": {"name": "Points"},
        "grid": {"right": 100},
        "series": seriesList,
    }
    
    # Render the chart
    st_echarts(options=option, height="550px")

def driverStandings():
    st.title("F1 Drivers Standings")

    f1Data2 = {
        "driverData": f1Data.driverData,
        "raceLocations": f1Data.raceLocations
    }

    # Create datasets for each team
    datasets = [
        {
            "id": f"dataset_{driver}",
            "source": [[i, points, f1Data2["raceLocations"][i], f"(+{change})"] for i, points, change in zip(range(len(points_list[0])), points_list[0], points_list[1])]
        }
        for driver, points_list in f1Data2["driverData"].items()
    ]

    # Create series configuration for each team
    seriesList = [
        {
            "type": "line",
            "datasetId": f"dataset_{driver}",
            "showSymbol": True,
            "name": driver,
            "endLabel": {
                "show": False,
                "formatter": "{@[1]}" + f" - {driver}",
                #"color": f1Data.teamWithHexColors[f1Data.driverTeamData[driver]],
            },
            "labelLayout": {"moveOverlap": "shiftY"},
            "emphasis": {"focus": "series"},
            "encode": {
                "x": 0,  # Index of the x-values in the dataset (Race #)
                "y": 1,  # Index of the y-values in the dataset (Points)
                "tooltip": [1, 3]
            },
            "itemStyle": {
                "color": f1Data.teamWithHexColors[f1Data.driverTeamData[driver]]
            }
        }
        for driver in f1Data2["driverData"].keys()
    ]

    # Configure the chart options
    option = {
        "animationDuration": 500,
        "dataset": datasets,  # Use the datasets created above
        "title": {"text": f"Year: {f1Data.year}"},
        "tooltip": {
            "show": True,
            "trigger": "item",
        },
        "xAxis": {
            "type": "category",
            "nameLocation": "middle",
            "axisLabel": {
                "rotate": 45,  # Rotate labels 45 degrees
                "formatter": "{value}",  # Custom format for labels
                "fontSize": 10,  # Font size
                "fontWeight": "bold"  # Font weight
            },
            "data": f1Data2["raceLocations"]  # Set x-axis labels (categories)
        },
        #"xAxis": {"type": "category", "name": "Race #", "nameLocation": "middle"},
        "yAxis": {"name": "Points"},
        "grid": {"right": 100},
        "series": seriesList,
    }

    # Get the most recent points for each driver
    current_standings = {driver: points[0][-1] for driver, points in f1Data2["driverData"].items()}
    
    # Sort drivers by points in descending order
    sorted_drivers = sorted(current_standings.items(), key=lambda x: x[1], reverse=True)
    
    # Create two columns: one for the chart, one for the leaderboard
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Render the chart
        st_echarts(options=option, height="565px", width="115%")
    
    with col2:
        # Display the leaderboard
        for position, (driver, points) in enumerate(sorted_drivers, 1):
            team_color = f1Data.teamWithHexColors[f1Data.driverTeamData[driver]]
            driverSplit = driver.split()
            driver_name = f"{driverSplit[0][0]}. {driverSplit[-1]}" if driver != "Zhou Guanyu" else "G. Zhou"
            st.markdown(
                f"<div style='display: flex; align-items: center;'>"
                f"<div style='background-color: {team_color}; width: 10px; height: 10px; margin-right: 5px;'></div>"
                f"<span style='font-weight: bold;'>{position}: {driver_name}</span>"
                f"<span style='margin-left: auto; margin-right: -10px;'>{points}</span>"
                f"</div>",
                unsafe_allow_html=True
            )

# Render the selected page
if selection == "Drivers" and option:
    driverStandings()
elif selection == "Constructors" and option:
    constructorsStandings()

