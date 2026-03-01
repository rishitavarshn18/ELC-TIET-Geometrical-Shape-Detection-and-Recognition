"""
Softy Shape Detection - Detect and recognize shapes in softy ice cream image
Techniques: Contour detection, vertex counting, shape approximation
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def detect_shape(contour):
    """Detect shape based on number of vertices"""
    shape = "unidentified"
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    vertices = len(approx)
    
    if vertices == 3:
        shape = "triangle"
    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        shape = "square" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
    elif vertices == 5:
        shape = "pentagon"
    elif vertices == 6:
        shape = "hexagon"
    elif vertices > 6:
        shape = "circle"
    
    return shape, vertices

def analyze_softy_shapes(image_path):
    """Analyze and detect shapes in softy image"""
    print(f"\n{'='*60}")
    print(f"SOFTY SHAPE DETECTION ANALYSIS")
    print(f"{'='*60}")
    print(f"Processing: {image_path}")
    
    # Load image
    image = cv2.imread(str(image_path))
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    original = image.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Binary threshold
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    
    # Morphological operations
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Edge detection
    edges = cv2.Canny(morph, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours and detect shapes
    result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    shape_counts = {}
    
    print(f"\nDetected {len(contours)} contours")
    print(f"\n{'Shape':<15} {'Vertices':<10} {'Area':<12} {'Perimeter':<12}")
    print("-" * 60)
    
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 500:  # Filter small contours
            shape, vertices = detect_shape(contour)
            perimeter = cv2.arcLength(contour, True)
            
            # Count shapes
            shape_counts[shape] = shape_counts.get(shape, 0) + 1
            
            # Draw contour and label
            cv2.drawContours(result, [contour], -1, (0, 255, 0), 3)
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(result, shape, (cX - 30, cY), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            
            print(f"{shape:<15} {vertices:<10} {area:<12.2f} {perimeter:<12.2f}")
    
    print(f"\n{'='*60}")
    print("SHAPE SUMMARY:")
    for shape, count in shape_counts.items():
        print(f"  {shape.capitalize()}: {count}")
    print(f"{'='*60}\n")
    
    # Visualization
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Softy Shape Detection Analysis', fontsize=16, fontweight='bold')
    
    axes[0, 0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(gray, cmap='gray')
    axes[0, 1].set_title('Grayscale')
    axes[0, 1].axis('off')
    
    axes[0, 2].imshow(blurred, cmap='gray')
    axes[0, 2].set_title('Gaussian Blur')
    axes[0, 2].axis('off')
    
    axes[1, 0].imshow(thresh, cmap='gray')
    axes[1, 0].set_title('Binary Threshold')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(edges, cmap='gray')
    axes[1, 1].set_title('Edge Detection')
    axes[1, 1].axis('off')
    
    axes[1, 2].imshow(result)
    axes[1, 2].set_title(f'Detected Shapes ({len(contours)} contours)')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Process softy image
    image_path = Path("images/softy.jpg")
    if image_path.exists():
        analyze_softy_shapes(image_path)
    else:
        print(f"Error: Image not found at {image_path}")
