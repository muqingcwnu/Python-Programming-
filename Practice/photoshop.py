import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from typing import Tuple, Optional

class Photoshop:
    def __init__(self):
        """Initialize the Photoshop class"""
        self.image = None
        self.filename = None

    def load_image(self, filepath: str) -> bool:
        """Load an image from the specified filepath"""
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Image file not found: {filepath}")
            
            self.image = Image.open(filepath)
            self.filename = os.path.basename(filepath)
            print(f"Successfully loaded image: {self.filename}")
            return True
        except Exception as e:
            print(f"Error loading image: {str(e)}")
            return False

    def save_image(self, output_path: str) -> bool:
        """Save the current image to the specified path"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to save")
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Convert numpy array back to PIL Image if necessary
            if isinstance(self.image, np.ndarray):
                self.image = Image.fromarray(self.image)
            
            self.image.save(output_path)
            print(f"Successfully saved image to: {output_path}")
            return True
        except Exception as e:
            print(f"Error saving image: {str(e)}")
            return False

    def display_image(self, title: str = None) -> None:
        """Display the current image using matplotlib"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to display")

            plt.figure(figsize=(10, 8))
            
            # Convert PIL Image to numpy array if necessary
            if isinstance(self.image, Image.Image):
                img_array = np.array(self.image)
            else:
                img_array = self.image

            # Handle different image types
            if len(img_array.shape) == 3:
                if img_array.shape[2] == 4:  # RGBA image
                    plt.imshow(img_array[:, :, :3])
                else:
                    plt.imshow(img_array)
            else:
                plt.imshow(img_array, cmap='gray')
                
            if title:
                plt.title(title)
            plt.axis('off')
            plt.tight_layout()
            plt.draw()
            plt.pause(0.1)  # Small pause to ensure window displays
            input("Press Enter to continue...")  # Wait for user input
            plt.close()  # Close the window after user input
        except Exception as e:
            print(f"Error displaying image: {str(e)}")

    def invert_colors(self) -> bool:
        """Invert the colors of the current image"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to invert")

            # Convert PIL Image to numpy array if necessary
            if isinstance(self.image, Image.Image):
                self.image = np.array(self.image)

            # Invert the colors
            self.image = 255 - self.image
            print("Successfully inverted image colors")
            return True
        except Exception as e:
            print(f"Error inverting colors: {str(e)}")
            return False

    def crop_image(self, box: Tuple[int, int, int, int]) -> bool:
        """Crop the image using the specified box coordinates (left, top, right, bottom)"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to crop")

            # Convert numpy array to PIL Image if necessary
            if isinstance(self.image, np.ndarray):
                self.image = Image.fromarray(self.image)

            self.image = self.image.crop(box)
            print("Successfully cropped image")
            return True
        except Exception as e:
            print(f"Error cropping image: {str(e)}")
            return False

    def resize_image(self, size: Tuple[int, int]) -> bool:
        """Resize the image to the specified dimensions (width, height)"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to resize")

            # Convert numpy array to PIL Image if necessary
            if isinstance(self.image, np.ndarray):
                self.image = Image.fromarray(self.image)

            self.image = self.image.resize(size, Image.Resampling.LANCZOS)
            print(f"Successfully resized image to {size}")
            return True
        except Exception as e:
            print(f"Error resizing image: {str(e)}")
            return False

    def rotate_image(self, angle: float) -> bool:
        """Rotate the image by the specified angle in degrees"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to rotate")

            # Convert numpy array to PIL Image if necessary
            if isinstance(self.image, np.ndarray):
                self.image = Image.fromarray(self.image)

            self.image = self.image.rotate(angle, expand=True)
            print(f"Successfully rotated image by {angle} degrees")
            return True
        except Exception as e:
            print(f"Error rotating image: {str(e)}")
            return False

    def swap_channels(self, order: Optional[Tuple[int, int, int]] = None) -> bool:
        """Swap color channels of the image. Default order is RGB to BGR"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to swap channels")

            # Convert PIL Image to numpy array if necessary
            if isinstance(self.image, Image.Image):
                self.image = np.array(self.image)

            if len(self.image.shape) != 3:
                raise ValueError("Image must be in color (3 channels) to swap channels")

            if order is None:
                order = (2, 1, 0)  # Default RGB to BGR

            self.image = self.image[:, :, order]
            print("Successfully swapped image channels")
            return True
        except Exception as e:
            print(f"Error swapping channels: {str(e)}")
            return False

    def show_histogram(self) -> None:
        """Display the histogram of the image"""
        try:
            if self.image is None:
                raise ValueError("No image loaded to show histogram")

            # Convert PIL Image to numpy array if necessary
            if isinstance(self.image, Image.Image):
                img_array = np.array(self.image)
            else:
                img_array = self.image

            plt.figure(figsize=(12, 6))

            if len(img_array.shape) == 3:  # Color image
                colors = ('r', 'g', 'b')
                for i, color in enumerate(colors):
                    histogram = plt.hist(img_array[:,:,i].ravel(), 
                                      bins=256, range=(0, 256), 
                                      color=color, alpha=0.5)
                plt.title("Color Histogram")
            else:  # Grayscale image
                plt.hist(img_array.ravel(), bins=256, range=(0, 256), 
                        color='gray', alpha=0.7)
                plt.title("Grayscale Histogram")

            plt.xlabel("Pixel Intensity")
            plt.ylabel("Frequency")
            plt.show()
        except Exception as e:
            print(f"Error showing histogram: {str(e)}")

    def process_image(self, operation: str, **kwargs) -> bool:
        """Process the image based on the specified operation"""
        operations = {
            'load': lambda: self.load_image(kwargs.get('filepath')),
            'save': lambda: self.save_image(kwargs.get('output_path')),
            'display': lambda: self.display_image(),
            'invert': self.invert_colors,
            'crop': lambda: self.crop_image(kwargs.get('box')),
            'resize': lambda: self.resize_image(kwargs.get('size')),
            'rotate': lambda: self.rotate_image(kwargs.get('angle')),
            'swap': lambda: self.swap_channels(kwargs.get('order')),
            'histogram': self.show_histogram
        }

        if operation not in operations:
            print(f"Unknown operation: {operation}")
            return False

        return operations[operation]() 