def get_input(prompt, valid_options):
    """Prompt user for input and ensure it's valid."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_gardening_advice(season, plant_type):
    """Generate gardening advice based on user input."""
    
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
    }

    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
    }

    return season_advice.get(season, "No advice for this season.") + plant_advice.get(plant_type, "No advice for this type of plant.")

def main():
    """Run the gardening advice program."""
    print("Welcome to the Gardening Advice Program!")
    
    season = get_input("Enter the season (summer/winter): ", {"summer", "winter"})
    plant_type = get_input("Enter the type of plant (flower/vegetable): ", {"flower", "vegetable"})

    advice = get_gardening_advice(season, plant_type)
    print("\nGardening Advice:")
    print(advice)
    
main()
# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
