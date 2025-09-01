
# -------------------------------------------
# Day 01 - Band Name Generator 🎸
# -------------------------------------------
# This project generates a fun band name by
# combining the name of a city and a pet.
# It's a beginner-level project to practice:
# - Taking user input
# - String concatenation / f-strings
# - Writing clean, reusable code
# -------------------------------------------

def band_name_generator():
    """
    Generate the band name based on the city and pet name
    provided by the user.
    :return: None
    """
    print("Welcome to the Band Name Generator")

    # Ask user to provide the city he/she grew up in
    city = input("What's the name of the city you grew up in?\n")
    # Ask user to provide his/her pet name
    pet = input("What's your pet's name?\n")
    # Printing the band name by combining the
    # city and pet using the F string
    print(f"Your band name could be {city} {pet}")

# This file runs only when it is executed directly (not imported as a module)
if __name__ == "__main__":
    band_name_generator()