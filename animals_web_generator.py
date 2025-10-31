import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_html(animals_data):
    """Generates HTML card items for each animal"""
    output = ""
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("type")

        output += '<li class="cards__item">\n'

        if name:
            output += f'  <div class="card__title">{name}</div>\n'

        output += '  <p class="card__text">\n'
        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'
        if locations and len(locations) > 0:
            output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
        if animal_type:
            output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
        output += '  </p>\n'

        output += '</li>\n\n'

    return output




def main():
    animals_data = load_data("animals_data.json")
    animals_html = generate_animals_html(animals_data)

    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as output_file:
        output_file.write(final_html)

    print("✅ animals.html updated with styled cards!")


if __name__ == "__main__":
    main()