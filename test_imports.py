try:
    import numpy as np
    print("NumPy version:", np.__version__)
except ImportError as e:
    print("Failed to import NumPy:", e)

try:
    import pandas as pd
    print("Pandas version:", pd.__version__)
except ImportError as e:
    print("Failed to import Pandas:", e)

try:
    import matplotlib
    print("Matplotlib version:", matplotlib.__version__)
except ImportError as e:
    print("Failed to import Matplotlib:", e)

try:
    import cv2
    print("OpenCV version:", cv2.__version__)
except ImportError as e:
    print("Failed to import OpenCV:", e)

print("\nAll imports completed successfully!") 