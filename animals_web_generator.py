import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_html(animals_data):
    """Generates HTML list items for each animal"""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("type")

        # Begin list item
        output += '<li class="cards__item">\n'

        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations and len(locations) > 0:
            output += f"Location: {locations[0]}<br/>\n"
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        # End list item
        output += "</li>\n\n"

    return output



def main():
    # Step 1: Load the data
    animals_data = load_data("animals_data.json")

    # Step 2: Generate HTML block with animal info
    animals_html = generate_animals_html(animals_data)

    # Step 3: Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Step 4: Replace placeholder with animal HTML
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Step 5: Write the new HTML file
    with open("animals.html", "w") as output_file:
        output_file.write(final_html)

    print("✅ animals.html updated with HTML cards!")

if __name__ == "__main__":
    main()