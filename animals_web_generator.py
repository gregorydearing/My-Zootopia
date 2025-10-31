import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_text(animals_data):
    """Generates a formatted string with animal information"""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("type")

        if name:
            output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if locations and len(locations) > 0:
            output += f"Location: {locations[0]}\n"
        if animal_type:
            output += f"Type: {animal_type}\n"
        output += "\n"  # blank line between animals

    return output


def main():
    # Step 1: Load the data
    animals_data = load_data("animals_data.json")

    # Step 2: Generate text block with animal info
    animals_text = generate_animals_text(animals_data)

    # Step 3: Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Step 4: Replace placeholder with animal text
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    # Step 5: Write the new HTML to a file
    with open("animals.html", "w") as output_file:
        output_file.write(final_html)

    print("✅ animals.html generated successfully!")


if __name__ == "__main__":
    main()

