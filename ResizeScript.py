from PIL import Image
import os

def resize_images(input_folder, output_folder, size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image
        if filename.endswith('.bmp'):
            # Open the image
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Convert to grayscale if necessary
                if img.mode != 'L':
                    img = img.convert('L')
                
                # Resize the image
                img_resized = img.resize(size)
                
                # Save the resized image
                img_resized.save(os.path.join(output_folder, filename))

# Define input and output folders
input_folder = 'rawFolder'
output_folder = 'resized'

# Define the size to resize the images to
size = (128, 128)

# Resize the images
resize_images(input_folder, output_folder, size)

print("Images resized successfully!")
