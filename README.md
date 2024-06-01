# Image to ASCII Converter

## Overview

This project converts an image of a Porsche Taycan into ASCII art and saves the result in a text file. The project is implemented in Python, utilizing the Python Imaging Library (PIL) for image processing.

## Features

- Converts a given image to ASCII art.
- Saves the ASCII art to a text file.
- Simple and easy to use.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pillow (Python Imaging Library)

You can install the required library using pip:

```bash
pip install Pillow
```

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/image-to-ascii-converter.git
   cd image-to-ascii-converter
   ```

2. **Add the Image**

   Place the image of the Porsche Taycan (e.g., `porche_taycan.jpg`) in the project directory.

3. **Run the Script**

   Execute the script to convert the image to ASCII art and save it to a text file:

   ```bash
   python convert_to_ascii.py
   ```

4. **Output**

   The ASCII art will be saved to a file named `output.txt` in the project directory.

## Example Code

Below is the main code for converting the image to ASCII art:

```python
from PIL import Image
import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,. "[::-1]
chararray = list(chars)
charlen = len(chararray)
interval = charlen / 256

text_file = open("output.txt", "w")

im = Image.open("porche_taycan.jpg")
print(im.format, im.size, im.mode)

def getChar(inputInt):
    return chararray[math.floor(inputInt * interval)]

width, height = im.size
ScaleFactor = 0.2
im = im.resize((int(ScaleFactor * width), int(ScaleFactor * height * 8 / 18)), Image.NEAREST)

width, height = im.size
pixels = im.load()

for i in range(height):
    for j in range(width):
        r, g, b = pixels[j, i]
        h = int(r / 3 + g / 3 + b / 3)
        pixels[j, i] = (h, h, h)
        text_file.write(getChar(h))
    text_file.write('\n')
```

## Project Structure

```
image-to-ascii-converter/
├── convert_to_ascii.py
├── porche_taycan.jpg
└── output.txt
```

- `convert_to_ascii.py`: The main script to convert the image to ASCII art.
- `porche_taycan.jpg`: The image file of the Porsche Taycan (add your own image here).
- `output.txt`: The output file containing the ASCII art.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README provides an overview of the project, instructions for setup and usage, and an example to get you started. Enjoy converting images to ASCII art!
