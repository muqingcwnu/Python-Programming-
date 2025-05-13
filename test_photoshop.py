import os
from photoshop import Photoshop

def get_image_path():
    """Get image path from user"""
    # Show current directory
    current_dir = os.getcwd()
    print(f"\nCurrent directory: {current_dir}")
    
    # Show available image files
    print("\nAvailable images in current directory:")
    image_files = [f for f in os.listdir(current_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    if image_files:
        for file in image_files:
            print(f"  - {file}")
    else:
        print("  No image files found in current directory")
    
    # Get image path
    print("\nYou can either:")
    print("1. Enter just the image name if it's in the current directory (e.g., 'img.jpg')")
    print("2. Enter the full path (e.g., 'C:\\Users\\Pictures\\img.jpg')")
    image_path = input("\nEnter image name or path: ").strip()
    
    if not image_path:
        print("No path entered.")
        return None
    
    try:
        # If just filename is given, assume it's in the current directory
        if not os.path.dirname(image_path):
            image_path = os.path.join(current_dir, image_path)
        
        # Convert to absolute path and normalize it
        image_path = os.path.abspath(os.path.expanduser(image_path))
        
        # Check if file exists and is a file (not a directory)
        if not os.path.isfile(image_path):
            print(f"Error: File not found: {image_path}")
            print("Available images:", ', '.join(image_files))
            return None
        
        # Check if it's an image file
        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        if not image_path.lower().endswith(valid_extensions):
            print("Error: File must be an image (jpg, jpeg, png, bmp, or gif)")
            return None
        
        return image_path
        
    except Exception as e:
        print(f"Error processing path: {str(e)}")
        print("Please make sure the path is valid and you have permission to access it.")
        return None

def main():
    while True:  # Outer loop for multiple photos
        # Create an instance of the Photoshop class
        ps = Photoshop()
        
        while True:  # Inner loop for current photo operations
            print("\nImage Processing Menu:")
            print("1. Load image")
            print("2. Display image")
            print("3. Save image")
            print("4. Invert colors")
            print("5. Crop image")
            print("6. Resize image")
            print("7. Rotate image")
            print("8. Swap color channels")
            print("9. Show histogram")
            print("0. Exit")
            
            choice = input("\nEnter your choice (0-9): ")
            
            try:
                if choice == '0':
                    print("Exiting program...")
                    return  # Exit the entire program
                    
                elif choice == '1':
                    # Get image path from user
                    image_path = get_image_path()
                    if image_path:
                        if ps.process_image('load', filepath=image_path):
                            print(f"Image dimensions: {ps.image.size}")
                
                elif choice == '2':
                    ps.process_image('display')
                    continue  # Skip asking about new photo
                
                elif choice == '3':
                    output_path = input("Save as (e.g., output.jpg): ")
                    if output_path:
                        ps.process_image('save', output_path=output_path)
                
                elif choice == '4':
                    ps.process_image('invert')
                
                elif choice == '5':
                    print("Enter crop box coordinates (left, top, right, bottom):")
                    left = int(input("Left: "))
                    top = int(input("Top: "))
                    right = int(input("Right: "))
                    bottom = int(input("Bottom: "))
                    ps.process_image('crop', box=(left, top, right, bottom))
                
                elif choice == '6':
                    width = int(input("Enter new width: "))
                    height = int(input("Enter new height: "))
                    ps.process_image('resize', size=(width, height))
                
                elif choice == '7':
                    angle = float(input("Enter rotation angle in degrees: "))
                    ps.process_image('rotate', angle=angle)
                
                elif choice == '8':
                    print("Enter channel order (0=R, 1=G, 2=B) or press Enter for RGB->BGR:")
                    order = input("Order (e.g., '2,1,0'): ")
                    if order:
                        order = tuple(map(int, order.split(',')))
                        ps.process_image('swap', order=order)
                    else:
                        ps.process_image('swap')
                
                elif choice == '9':
                    ps.process_image('histogram')
                
                else:
                    print("Invalid choice! Please try again.")
                    continue  # Skip asking about new photo for invalid choice
                
                # Only ask about new photo for operations that modify the image
                if choice not in ['1', '2', '0'] and choice.isdigit():
                    another = input("\nDo you want to process another photo? (y/n): ").lower()
                    if another == 'y':
                        break  # Break inner loop to start fresh with new photo
                    elif another == 'n' and choice == '0':
                        return  # Exit program if user chose to exit
                
            except Exception as e:
                print(f"Error: {str(e)}")
                print("Please try again.")
                continue  # Skip asking about new photo on error

if __name__ == "__main__":
    main() 