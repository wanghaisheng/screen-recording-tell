from bs4 import BeautifulSoup
import requests

# Function to fetch HTML content of a webpage
def fetch_webpage(url):
    response = requests.get(url)
    return response.text

# Function to find HTML elements by coordinates
def find_elements_by_coordinates(html_content, coordinates):
    soup = BeautifulSoup(html_content, 'html.parser')
    matched_elements = []

    for coords, label, confidence in coordinates:
        x_coords = [int(coord[0]) for coord in coords]
        y_coords = [int(coord[1]) for coord in coords]

        # Find elements using CSS selectors or other methods
        # Example: finding elements with matching attributes or dimensions
        for element in soup.find_all(True):
            if 'style' in element.attrs:
                style = element['style']
                if all(str(x) in style for x in x_coords) and all(str(y) in style for y in y_coords):
                    matched_elements.append((element, label, confidence))
                    break  # assuming each rectangle corresponds to only one element

    return matched_elements

# Example usage
if __name__ == "__main__":
    url = 'https://example.com'
    html_content = fetch_webpage(url)
    
    input_data = [
        [[[9.0, 2.0], [321.0, 11.0], [318.0, 102.0], [6.0, 93.0]], '正品促销', '0.7986101984977723'],
        [[[70.0, 98.0], [251.0, 98.0], [251.0, 125.0], [70.0, 125.0]], '大桶装更划算', '0.7368737288883754']
        # Add more entries as needed
    ]
    
    matched_elements = find_elements_by_coordinates(html_content, input_data)
    
    for element, label, confidence in matched_elements:
        print(f"Label: {label}, Confidence: {confidence}")
        print("Element found:", element)
        print("Element HTML:", element.prettify())  # Print HTML of the element
        print("--------------------")
