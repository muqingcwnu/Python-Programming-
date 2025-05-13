import numpy as np
from PIL import Image, ImageDraw

# Create a new image with a white background
width = 400
height = 300
image = Image.new('RGB', (width, height), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw some shapes
# Red rectangle
draw.rectangle([50, 50, 150, 100], fill='red')

# Blue circle
draw.ellipse([200, 100, 300, 200], fill='blue')

# Green triangle
draw.polygon([(150, 200), (100, 250), (200, 250)], fill='green')

# Save the image
image.save('sample.jpg')
print("Sample image created: sample.jpg") 