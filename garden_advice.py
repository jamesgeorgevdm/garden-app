def get_input(prompt, valid_options):
    """Prompt user for input and ensure it's valid."""
    while True:
        user_input = input(prompt).strip().lower() # Normalize input
        if user_input in valid_options:
            return user_input # Returns if valid input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}") # Invalidation response providing valid_options

def get_gardening_advice(season, plant_type):
    """Generate gardening advice based on user input."""
    
    # Dictionary to store advice based on season and plant type
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
    }

    # Dictionary to store advice based on plant type
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
    }

    return season_advice.get(season, "No advice for this season.") + plant_advice.get(plant_type, "No advice for this type of plant.")

def main():
    """Run the gardening advice program."""
    print("Welcome to the Gardening Advice Program!")
    
    # Prompt user for season and plant type
    season = get_input("Enter the season (summer/winter): ", {"summer", "winter"}) # Includes valid seasons
    plant_type = get_input("Enter the type of plant (flower/vegetable): ", {"flower", "vegetable"}) # Includes valid plant types

    # Get gardening advice based on user input
    advice = get_gardening_advice(season, plant_type)

    # Display the advice to the user
    print("\nGardening Advice:")
    print(advice)

# Run the main function to start the program
main()

