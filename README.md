# Geometrical Shape Detection and Recognition

A complete image analysis project for detecting and recognizing geometric shapes using OpenCV, NumPy, and Matplotlib.

## Project Overview

This project implements geometric shape detection and recognition using computer vision techniques. It can identify various shapes including triangles, squares, rectangles, pentagons, hexagons, and circles from images.

## Project Structure

```
ELC-TIET-Geometrical-Shape-Detection-and-Recognition/
├── images/                          # Input images for analysis
│   ├── 4shapes.jpg
│   ├── cookie2.jpg
│   ├── env.jpg
│   ├── globe.jpg
│   └── softy.jpg
├── scripts/                         # Python scripts (one per image)
│   ├── 4shapes_detection.py
│   ├── cookie_detection.py
│   ├── env_detection.py
│   ├── globe_detection.py
│   └── softy_detection.py
├── notebooks/                       # Jupyter notebooks (one per image)
│   ├── 4shapes_detection.ipynb
│   ├── cookie_detection.ipynb
│   ├── env_detection.ipynb
│   ├── globe_detection.ipynb
│   └── softy_detection.ipynb
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

## Features

### Geometric Shape Detection
- **Detects shapes:** Triangle, Square, Rectangle, Pentagon, Hexagon, Circle
- **Techniques used:**
  - Contour detection
  - Vertex counting
  - Shape approximation
  - Morphological operations
  - Edge detection (Canny)
  - Gaussian blur for noise reduction

### Analysis Capabilities
- Shape classification based on vertices
- Area and perimeter calculation
- Aspect ratio analysis
- Visual annotations with labels
- Statistical summary of detected shapes

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ELC-TIET-Geometrical-Shape-Detection-and-Recognition.git
cd ELC-TIET-Geometrical-Shape-Detection-and-Recognition
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Using Python Scripts

Each image has its own dedicated script. Run any of these:

```bash
# For 4shapes.jpg
python scripts/4shapes_detection.py

# For cookie2.jpg
python scripts/cookie_detection.py

# For env.jpg
python scripts/env_detection.py

# For globe.jpg
python scripts/globe_detection.py

# For softy.jpg
python scripts/softy_detection.py
```

Each script will:
- Load its specific image
- Apply preprocessing steps
- Detect and classify shapes
- Display visualization with 6 subplots
- Print statistical summary

### Using Jupyter Notebooks

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open any notebook from the `notebooks/` folder:
   - `4shapes_detection.ipynb` - For 4shapes.jpg
   - `cookie_detection.ipynb` - For cookie2.jpg
   - `env_detection.ipynb` - For env.jpg
   - `globe_detection.ipynb` - For globe.jpg
   - `softy_detection.ipynb` - For softy.jpg

3. Run cells sequentially to:
   - Load and display the specific image
   - Apply preprocessing techniques step-by-step
   - Detect and classify shapes interactively
   - Visualize results with detailed explanations

## Dependencies

- **opencv-contrib-python** (>=4.5.0) - Computer vision operations
- **numpy** (>=1.19.0) - Numerical computations
- **matplotlib** (>=3.3.0) - Visualization
- **Pillow** (>=8.0.0) - Image processing
- **jupyter** (>=1.0.0) - Notebook interface
- **notebook** (>=6.0.0) - Jupyter notebook server

## Image Processing Pipeline

1. **Load Image** - Read input image from file
2. **Grayscale Conversion** - Convert to single channel
3. **Gaussian Blur** - Reduce noise (5x5 kernel)
4. **Binary Threshold** - Separate foreground/background
5. **Morphological Operations** - Clean up binary image
6. **Edge Detection** - Canny edge detector
7. **Contour Detection** - Find shape boundaries
8. **Shape Classification** - Identify based on vertices
9. **Visualization** - Display results with annotations

## Shape Detection Logic

| Shape | Vertices | Additional Criteria |
|-------|----------|-------------------|
| Triangle | 3 | - |
| Square | 4 | Aspect ratio ≈ 1.0 |
| Rectangle | 4 | Aspect ratio ≠ 1.0 |
| Pentagon | 5 | - |
| Hexagon | 6 | - |
| Circle | >6 | High vertex count |

## Output Information

For each detected shape, the system provides:
- Shape name (triangle, square, etc.)
- Number of vertices
- Area (in pixels²)
- Perimeter (in pixels)
- Visual annotation on image

## Examples

### Available Images

1. **4shapes.jpg** - Contains multiple geometric shapes (triangles, squares, circles, etc.)
2. **cookie2.jpg** - Cookie or circular objects for shape detection
3. **env.jpg** - Envelope with rectangular shapes
4. **globe.jpg** - Globe with circular and curved shapes
5. **softy.jpg** - Soft serve ice cream with organic shapes

### Input/Output

Each script and notebook:
- **Input:** Specific image from `images/` folder
- **Processing:** 6-step visualization (original → grayscale → blur → threshold → edges → result)
- **Output:** 
  - Console output with shape statistics
  - Matplotlib visualization with detected shapes labeled
  - Shape summary (count of each shape type)

## Troubleshooting

### No shapes detected
- Adjust threshold values in the script
- Check image contrast and lighting
- Ensure shapes are clearly visible

### Too many false detections
- Increase minimum area filter (default: 500 pixels)
- Adjust Canny edge detection parameters
- Modify shape approximation epsilon value

## Course Information

**Project:** Geometrical Shape Detection and Recognition  
**Institution:** Thapar Institute of Engineering & Technology (TIET)  
**Department:** Electronics & Communication Engineering (ELC)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available for educational purposes.

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This project is designed for educational purposes to demonstrate computer vision techniques for shape detection and recognition.
CodeSpace Repository For ELC ECE Activity 2026
