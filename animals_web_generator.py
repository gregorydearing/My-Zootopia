import json
from typing import Dict, List, Any


def load_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load JSON data from the given file path.

    Returns:
        A list of animal dictionaries parsed from the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal: Dict[str, Any]) -> str:
    """
    Serialize a single animal object into an HTML list item.

    The function safely accesses nested fields (characteristics) and only
    emits fields that exist for that animal.
    """
    characteristics = animal.get("characteristics", {})
    name = animal.get("name")
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")

    locations = animal.get("locations", [])
    # Option: join all locations with ", " if there are many.
    location_text = None
    if locations:
        if isinstance(locations, list):
            location_text = ", ".join(locations)
        else:
            # fallback if locations is a single string
            location_text = str(locations)

    output = '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location_text:
        output += f'      <strong>Location:</strong> {location_text}<br/>\n'
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'

    output += '</li>\n\n'
    return output


def generate_animals_html(animals_data: List[Dict[str, Any]]) -> str:
    """
    Generate the full HTML block (list items) for all animals.
    """
    return "".join(serialize_animal(a) for a in animals_data)


def main() -> None:
    """
    Load the animals data, inject it into the HTML template, and write the
    resulting page to animals.html.
    """
    animals_data = load_data("animals_data.json")
    animals_html = generate_animals_html(animals_data)

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("✅ animals.html updated with styled cards!")


if __name__ == "__main__":
    main()
