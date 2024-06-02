import os
from PIL import Image
import numpy as np

def center_and_resize_image(image_path, output_path, resize_factor=0.7):
    # Load the image
    image = Image.open(image_path).convert('L')
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Find the bounding box of the non-white (non-255) pixels
    non_white_pixels = np.where(image_array < 255)
    min_row, max_row = np.min(non_white_pixels[0]), np.max(non_white_pixels[0])
    min_col, max_col = np.min(non_white_pixels[1]), np.max(non_white_pixels[1])
    
    # Crop the image to the bounding box
    cropped_image = image_array[min_row:max_row+1, min_col:max_col+1]
    
    # Resize the cropped image to 70% of its original size
    cropped_image_pil = Image.fromarray(cropped_image)
    new_size = (int(cropped_image_pil.size[0] * resize_factor), int(cropped_image_pil.size[1] * resize_factor))
    resized_image_pil = cropped_image_pil.resize(new_size, Image.LANCZOS)
    resized_image = np.array(resized_image_pil)
    
    # Calculate the padding needed to center the resized image
    resized_height, resized_width = resized_image.shape
    top_padding = (128 - resized_height) // 2
    bottom_padding = 128 - resized_height - top_padding
    left_padding = (128 - resized_width) // 2
    right_padding = 128 - resized_width - left_padding
    
    # Create a new 128x128 image with a white background
    centered_image_array = np.full((128, 128), 255, dtype=np.uint8)
    
    # Paste the resized image into the center of the new image
    centered_image_array[
        top_padding:top_padding+resized_height, 
        left_padding:left_padding+resized_width
    ] = resized_image
    
    # Convert the numpy array back to an image
    centered_image = Image.fromarray(centered_image_array)
    
    # Save the centered image
    centered_image.save(output_path)

# Paths to the directories
input_dir = 'Haa-old'
output_dir = 'Haa-centered6'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process all BMP images in the input directory with resizing
resize_factor = 0.7  # Resize the image to 70% of its original size
for filename in os.listdir(input_dir):
    if filename.endswith('.bmp'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        center_and_resize_image(input_path, output_path, resize_factor)
