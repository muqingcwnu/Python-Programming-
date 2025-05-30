import os
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Global variable to keep track of image in memory
current_image = None
current_df = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- TABULAR DATA PROCESSING ---
def tabular_data_processing(df):
    while True:
        print("\n--- Tabular Data Processing ---")
        print("1. View first few rows")
        print("2. Display Data Info")
        print("3. Summary Statistics")
        print("4. Drop rows with NaN")
        print("5. Filter by Condition")
        print("6. Filter by Range")
        print("7. Filter by Text Matching")
        print("8. Filter Missing Values")
        print("9. Filter with Regex")
        print("10. Top/Bottom N Rows")
        print("11. Group & Aggregate")
        print("12. Sort Data")
        print("13. Save Processed Data")
        print("14. Generate Histogram")
        print("15. Normalize Data")
        print("16. Correlation Matrix")
        print("17. Pivot Table")
        print("18. Merge with CSV")
        print("19. (Future) Image to CSV")
        print("M. Main Menu")
        print("0. Exit")

        choice = input("Choose an option: ").strip().lower()

        try:
            if choice == '1':
                print(df.head())
            elif choice == '2':
                print(df.info())
            elif choice == '3':
                print(df.describe())
            elif choice == '4':
                df = df.dropna()
                print("NaN rows dropped.")
            elif choice == '5':
                condition = input("Enter condition (e.g., `column > 10`): ")
                print(df.query(condition))
            elif choice == '6':
                col = input("Column name: ")
                min_v = float(input("Min value: "))
                max_v = float(input("Max value: "))
                print(df[(df[col] >= min_v) & (df[col] <= max_v)])
            elif choice == '7':
                col = input("Column: ")
                text = input("Text to match: ")
                print(df[df[col].str.contains(text, na=False)])
            elif choice == '8':
                col = input("Column name: ")
                print(df[df[col].isnull()])
            elif choice == '9':
                col = input("Column: ")
                pattern = input("Regex: ")
                print(df[df[col].str.match(pattern, na=False)])
            elif choice == '10':
                top_bottom = input("top or bottom? ").lower()
                n = int(input("How many rows? "))
                print(df.head(n) if top_bottom == 'top' else df.tail(n))
            elif choice == '11':
                col = input("Group by column: ")
                func = input("Aggregation function (mean, sum, etc.): ")
                print(df.groupby(col).agg(func))
            elif choice == '12':
                col = input("Sort by column: ")
                print(df.sort_values(by=col))
            elif choice == '13':
                path = input("Save path: ")
                df.to_csv(path, index=False)
                print(f"Saved to {path}")
            elif choice == '14':
                col = input("Column to plot: ")
                df[col].plot(kind='hist', bins=20, alpha=0.7)
                plt.title(f"Histogram of {col}")
                plt.show()
            elif choice == '15':
                cols = input("Columns to normalize (comma separated): ").split(',')
                df[cols] = df[cols].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
                print("Data normalized.")
            elif choice == '16':
                print(df.corr())
            elif choice == '17':
                index_col = input("Pivot index column: ")
                print(df.pivot_table(index=index_col))
            elif choice == '18':
                merge_path = input("CSV path to merge with: ")
                merge_df = pd.read_csv(merge_path)
                df = pd.merge(df, merge_df)
                print("Merged successfully.")
            elif choice == '19':
                print("This feature is under development.")
            elif choice == 'm':
                break
            elif choice == '0':
                print("Exiting. Bye!")
                exit()
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"Error: {e}")

# --- IMAGE PROCESSING ---
def photoshop_operations():
    global current_image
    while True:
        print("\n Welcome to Photoshop Operations!")
        print("Choose an operation:")
        print("1. Invert Colors")
        print("2. Crop Image")
        print("3. Resize Image")
        print("4. Rotate Image")
        print("5. Swap Color Channels")
        print("6. Display Histogram")
        print("7. Save Image")
        print("M. Main Menu")
        print("0. Exit")

        choice = input("Choose an option: ").strip().lower()

        try:
            if choice == '1':
                current_image = invert_colors(current_image)
            elif choice == '2':
                l = int(input("Left: "))
                t = int(input("Top: "))
                r = int(input("Right: "))
                b = int(input("Bottom: "))
                current_image = crop_image(current_image, (l, t, r, b))
            elif choice == '3':
                w = int(input("Width: "))
                h = int(input("Height: "))
                current_image = resize_image(current_image, (w, h))
            elif choice == '4':
                angle = int(input("Angle: "))
                current_image = rotate_image(current_image, angle)
            elif choice == '5':
                current_image = swap_color_channels(current_image)
            elif choice == '6':
                display_histogram(current_image)
            elif choice == '7':
                path = input("Save image path: ")
                current_image.save(path)
                print(f"Image saved to {path}")
            elif choice == 'm':
                break
            elif choice == '0':
                print("Exiting. Bye!")
                exit()
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"Error: {e}")

# --- IMAGE HELPER FUNCTIONS ---
def load_image(path):
    global current_image
    try:
        img = Image.open(path)
        img.show()
        current_image = img
    except Exception as e:
        print(f"Error loading image: {e}")

def invert_colors(img):
    img = ImageOps.invert(img.convert("RGB"))
    img.show()
    return img

def crop_image(img, box):
    img = img.crop(box)
    img.show()
    return img

def resize_image(img, size):
    img = img.resize(size)
    img.show()
    return img

def rotate_image(img, angle):
    img = img.rotate(angle)
    img.show()
    return img

def swap_color_channels(img):
    np_img = np.array(img)
    swapped = np_img[..., ::-1]
    img = Image.fromarray(swapped)
    img.show()
    return img

def display_histogram(img):
    np_img = np.array(img)
    colors = ['r', 'g', 'b']
    for i, col in enumerate(colors):
        hist, bins = np.histogram(np_img[..., i], bins=256, range=(0, 255))
        plt.plot(bins[:-1], hist, color=col)
    plt.title("Color Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend(colors)
    plt.show()

# --- MAIN MENU ---
def main():
    global current_df
    while True:
        print("Hi, Welcome to the Data & Image Processing Tool!")
        print("Please choose an option:")
        print(" Want to process tabular Data ? Choose 1")
        print("Want to process an Image? Choose 2")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            path = input("CSV path: ").strip()
            try:
                current_df = pd.read_csv(path)
                print("CSV loaded.")
                tabular_data_processing(current_df)
            except Exception as e:
                print(f"CSV Error: {e}")
        elif choice == '2':
            path = input("Image path: ").strip()
            load_image(path)
            if current_image:
                photoshop_operations()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 0.")

# --- RUN SCRIPT ---
if __name__ == "__main__":
    main()
