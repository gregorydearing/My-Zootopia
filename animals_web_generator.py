import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # Load the data from the JSON file
    animals_data = load_data("animals_data.json")

    # Iterate through each animal and print required fields
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        if animal_type:
            print(f"Type: {animal_type}")
        print()  # Empty line between animals


if __name__ == "__main__":
    main()
