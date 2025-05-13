import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def display_image(title, image):
    """Display an image using matplotlib"""
    plt.figure(figsize=(8, 6))
    
    # Convert BGR to RGB for matplotlib if it's a color image
    if len(image.shape) == 3:
        display_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        display_img = image
        
    plt.imshow(display_img, cmap='gray' if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_image(title, image):
    """Save an image to disk"""
    # Create 'output' directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Save the image
    filename = os.path.join('output', f'{title.lower().replace(" ", "_")}.jpg')
    cv2.imwrite(filename, image)
    print(f"Saved {filename}")

def create_sample_image():
    """Create a sample image with shapes"""
    # Create a black image
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    
    # Draw shapes
    # Green rectangle
    cv2.rectangle(img, (100, 50), (300, 200), (0, 255, 0), -1)
    # Red circle
    cv2.circle(img, (450, 100), 80, (0, 0, 255), -1)
    # Blue triangle
    pts = np.array([[250, 300], [150, 400], [350, 400]], np.int32)
    cv2.fillPoly(img, [pts], (255, 0, 0))
    
    return img

def process_image(image):
    """Apply various image processing operations"""
    # Process original image
    display_image('Original Image', image)
    save_image('Original Image', image)
    
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image('Grayscale Image', gray)
    save_image('Grayscale Image', gray)
    
    # 2. Apply Gaussian blur
    blurred = cv2.GaussianBlur(image, (7, 7), 0)
    display_image('Blurred Image', blurred)
    save_image('Blurred Image', blurred)
    
    # 3. Edge detection using Canny
    edges = cv2.Canny(gray, 100, 200)
    display_image('Edge Detection', edges)
    save_image('Edge Detection', edges)
    
    # 4. Binary thresholding
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    display_image('Binary Threshold', threshold)
    save_image('Binary Threshold', threshold)
    
    # 5. HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    display_image('HSV Color Space', hsv)
    save_image('HSV Color Space', hsv)

def main():
    try:
        print("Starting image processing...")
        print("Images will be displayed and saved.")
        
        # Create and process sample image
        image = create_sample_image()
        process_image(image)
        
        print("\nImage processing completed successfully!")
        print("All images have been saved in the 'output' directory.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        plt.close('all')  # Clean up all matplotlib windows

if __name__ == "__main__":
    main()
