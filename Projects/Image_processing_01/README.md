# Image Processing Application

A Python-based image processing application that provides various operations to manipulate and analyze images.

## Features

- Load and display images
- Save processed images
- Image operations:
  - Invert colors
  - Crop images
  - Resize images
  - Rotate images
  - Swap color channels
  - Display histograms

## Requirements

- Python 3.8 or higher
- Required packages:
  - PIL (Pillow)
  - numpy
  - matplotlib

## Installation

1. Clone or download this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python test_photoshop.py
   ```

2. Menu Options:
   - 1: Load image - Enter image path or filename
   - 2: Display image - Show the current image
   - 3: Save image - Save processed image to file
   - 4: Invert colors - Invert the colors of the image
   - 5: Crop image - Crop using coordinates
   - 6: Resize image - Change image dimensions
   - 7: Rotate image - Rotate by specified angle
   - 8: Swap color channels - Change RGB channel order
   - 9: Show histogram - Display color distribution
   - 0: Exit program

## Example Usage

```python
# Load an image
1. Select option 1
2. Enter image path (e.g., "img.jpg" or full path)

# Display the image
3. Select option 2 to view the image

# Process the image
4. Choose any operation (options 3-9)
5. Follow the prompts for each operation

# Save the result
6. Select option 3
7. Enter output filename
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)

## Error Handling

The application includes robust error handling for:
- File not found
- Invalid file formats
- Invalid operations
- Input validation

## Project Structure

- `test_photoshop.py`: Main program with user interface
- `photoshop.py`: Core image processing class and functions
- `README.md`: Project documentation (this file)

## Tips

- Images should be in the same directory as the program or use full path
- For crop operation, coordinates are in format: left, top, right, bottom
- For channel swapping, use numbers 0 (R), 1 (G), 2 (B)
- Press Enter to close image display window 