import re


def extract_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(r'coordinaten: \(([-\d.]+), ([-\d.]+)\)', line)
            if match:
                lat, lng = match.groups()
                coordinates.append((float(lat), float(lng)))
    return coordinates


def generate_js_array(coordinates):
    js_array = "var locations = [\n"
    for lat, lng in coordinates:
        js_array += f"    {{ lat: {lat}, lng: {lng} }},\n"
    js_array += "]"  # Close the array
    return js_array


if __name__ == "__main__":
    file_path = "leesbare_data_nlt.txt"  # Update with actual path if needed
    coords = extract_coordinates(file_path)
    js_code = generate_js_array(coords)

    with open("coordinates.js", "w", encoding="utf-8") as js_file:
        js_file.write(js_code)

    print("JavaScript file 'coordinates.js' generated successfully!")
