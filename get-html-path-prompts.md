You are tasked with extracting corresponding HTML code for each pair of coordinates from a given HTML document. You will be provided with two inputs: the HTML code and a list of coordinates with associated text and confidence scores.

First, here is the HTML code you will be working with:
<html_code>
{{HTML_CODE}}
</html_code>

Now, here is the list of coordinates and associated information:
<coordinates_list>
{{COORDINATES_LIST}}
</coordinates_list>

Your task is to process each item in the coordinates list and find the corresponding HTML code within the provided HTML document. Follow these steps:

1. For each item in the coordinates list:
   a. Extract the coordinates, text, and confidence score.
   b. Use the coordinates to locate the corresponding section in the HTML code.
   c. Extract the relevant HTML code that falls within or closest to the given coordinates.

2. Format your output as a list of dictionaries, where each dictionary contains:
   - 'coordinates': The original coordinates
   - 'text': The associated text
   - 'confidence': The confidence score
   - 'html': The extracted HTML code

3. If you cannot find a matching HTML section for a given set of coordinates, include an empty string for the 'html' key.

Here's an example of how your output should be formatted:

<output>
[
    {
        'coordinates': [[9.0, 2.0], [321.0, 11.0], [318.0, 102.0], [6.0, 93.0]],
        'text': '正品促销',
        'confidence': '0.7986101984977723',
        'html': '<div class="promotion">正品促销</div>'
    },
    {
        'coordinates': [[70.0, 98.0], [251.0, 98.0], [251.0, 125.0], [70.0, 125.0]],
        'text': '大桶装更划算',
        'confidence': '0.7368737288883754',
        'html': '<span class="offer">大桶装更划算</span>'
    }
]
</output>

If you encounter any errors or cannot process a particular item, include it in the output with an empty string for the 'html' key.

Process all items in the coordinates list and provide your complete output within <output> tags.
