# Quick Usage Guide

## Setup

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running Scripts

Each image has its own script:

```bash
python scripts/4shapes_detection.py      # Detects shapes in 4shapes.jpg
python scripts/cookie_detection.py       # Detects shapes in cookie2.jpg
python scripts/env_detection.py          # Detects shapes in env.jpg
python scripts/globe_detection.py        # Detects shapes in globe.jpg
python scripts/softy_detection.py        # Detects shapes in softy.jpg
```

## Running Notebooks

```bash
# Start Jupyter
jupyter notebook

# Then open any notebook:
# - notebooks/4shapes_detection.ipynb
# - notebooks/cookie_detection.ipynb
# - notebooks/env_detection.ipynb
# - notebooks/globe_detection.ipynb
# - notebooks/softy_detection.ipynb
```

## What Each Script Does

1. Loads the specific image
2. Converts to grayscale
3. Applies Gaussian blur
4. Binary thresholding
5. Morphological operations
6. Edge detection (Canny)
7. Contour detection
8. Shape classification
9. Displays 2x3 grid with all steps
10. Prints shape statistics

## Shape Detection Logic

- **Triangle** - 3 vertices
- **Square** - 4 vertices with aspect ratio ≈ 1.0
- **Rectangle** - 4 vertices with aspect ratio ≠ 1.0
- **Pentagon** - 5 vertices
- **Hexagon** - 6 vertices
- **Circle** - More than 6 vertices

## Output Format

### Console Output
```
============================================================
SHAPE DETECTION ANALYSIS
============================================================
Processing: images/4shapes.jpg

Detected 4 contours

Shape           Vertices   Area         Perimeter   
------------------------------------------------------------
triangle        3          5234.50      345.67
square          4          4567.00      270.45
circle          12         6789.23      292.11
rectangle       4          3456.78      234.56

============================================================
SHAPE SUMMARY:
  Triangle: 1
  Square: 1
  Circle: 1
  Rectangle: 1
============================================================
```

### Visual Output
- 2x3 subplot grid showing:
  1. Original image
  2. Grayscale
  3. Gaussian blur
  4. Binary threshold
  5. Edge detection
  6. Final result with labeled shapes

## Troubleshooting

### No shapes detected
- Adjust threshold value (line with `cv2.threshold`)
- Modify Canny edge parameters
- Change minimum area filter (default: 500 pixels)

### Too many false detections
- Increase minimum area: `if area > 1000:`
- Adjust shape approximation: `0.04 * peri` → `0.02 * peri`

### Image not loading
- Check image path is correct
- Ensure image is in `images/` folder
- Verify image format (.jpg or .png)

## Project Structure

```
├── images/          # 5 test images
├── scripts/         # 5 Python scripts (one per image)
├── notebooks/       # 5 Jupyter notebooks (one per image)
├── requirements.txt # Dependencies
└── README.md        # Full documentation
```

## Dependencies

- opencv-contrib-python (Computer vision)
- numpy (Numerical operations)
- matplotlib (Visualization)
- Pillow (Image processing)
- jupyter (Notebook interface)
