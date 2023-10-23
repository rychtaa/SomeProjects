""" Create dictionaries for each city 
with monthly rainfall data for 2022 """
rainfallData = {
    "Eindhoven": {
        "January": 65,
        "February": 55,
        "March": 50,
        "April": 40,
        "May": 60,
        "June": 60,
        "July": 75,
        "August": 75,
        "September": 60,
        "October": 60,
        "November": 70,
        "December": 75
    },
    "Tilburg": {
        "January": 70,
        "February": 70,
        "March": 65,
        "April": 55,
        "May": 70,
        "June": 75,
        "July": 85,
        "August": 85,
        "September": 70,
        "October": 70,
        "November": 70,
        "December": 80
    },
    "Breda": {
        "January": 70,
        "February": 70,
        "March": 60,
        "April": 55,
        "May": 70,
        "June": 75,
        "July": 85,
        "August": 85,
        "September": 70,
        "October": 70,
        "November": 70,
        "December": 80
    },
    "Den Bosch": {
        "January": 70,
        "February": 70,
        "March": 60,
        "April": 55,
        "May": 65,
        "June": 70,
        "July": 85,
        "August": 85,
        "September": 70,
        "October": 70,
        "November": 70,
        "December": 80
    },
    "Helmond": {
        "January": 70,
        "February": 70,
        "March": 65,
        "April": 55,
        "May": 70,
        "June": 75,
        "July": 85,
        "August": 85,
        "September": 70,
        "October": 70,
        "November": 70,
        "December": 80
    }
}

# Create a dictionary to store quarterly rainfall for each city
quarterlyRainfall = {}

# Loop through each city in the rainfallData dictionary

for city, monthlyData in rainfallData.items():
    # Initialize variables to store quarterly rainfall totals
    q1Total = 0
    q2Total = 0
    q3Total = 0
    q4Total = 0

    # Loop through the months in the monthlyData dictionary
    for month , rainfall in monthlyData.items():
        if month in ["Januaray", "February", "March"]:
            q1Total += rainfall
        elif month in ["April", "May", "June"]:
            q2Total += rainfall
        elif month in ["July", "August", "September"]:
            q3Total += rainfall
        elif month in ["October", "November", "December"]:
            q4Total += rainfall

    # Store the quarterly totals for the current city
    quarterlyRainfall[city] = {
        "Q1": q1Total,
        "Q2": q2Total,
        "Q3": q3Total,
        "Q4": q4Total
    }

# Users input
while True:
    # Ask user to input a city or 'q' to quit
    userInput = input("\nEnter a city name from Nord Brabant or 'q' to quit: ")
    
    # print("Choose from: Eindhoven, Tilburg, Breda, Den Bosch, Helmond")

    # Check if the user wants to quit
    if userInput.lower() == "q":
        print("Goodbye!")
        break
    
    # Standardize the user input and convert to lowercase for case-insensitive comparison
    userInput = userInput.strip().title()

    # Check if entered city in one of the five cities in NB
    if userInput in rainfallData:
        
        # Display the requested city' monthly rainfall data
        print("\n------------------------------")
        print("---------- Rainfall ----------")
        print("------------------------------")
        print(f"\nMonthly rainfall data for {userInput}: ")
        for month, rainfall in rainfallData[userInput].items():
            print(f"{month:10}: {rainfall} mm")

        # Display the requested city's qurterly rainfall data
        print(f"\nQuarterly rainfall data for {userInput}: ")
        for quarter, rainfall in quarterlyRainfall[userInput].items():
            print(f"{quarter}: {rainfall} mm")

        """   # Calculate and display yearly rainfall !!!!----> HAVE A LOOK IN rainfallnotes.txt
        yearlyRainfall = sum(monthlyData.values())
        print(f"\nYearly rainfall in {userInput} in 2022 was {yearlyRainfall} mm")
        """

    else:
        print("\nInvalid city. Please enter city from Nord Brabant or 'q' to quit")
        
