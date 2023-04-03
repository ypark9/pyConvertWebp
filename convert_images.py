import os
from PIL import Image

def convert_images_to_jpg_or_png(folder_path, output_format='jpeg'):
    # Get a list of all the files in the folder
    files = os.listdir(folder_path)
    # Loop through each file in the folder
    for file in files:
        # Check if the file is a WebP image
        if file.lower().endswith('.webp'):
            # Open the image using PIL
            image_path = os.path.join(folder_path, file)
            with Image.open(image_path) as im:
                # Determine the output filename and format
                output_filename = os.path.splitext(file)[0] + '.' + output_format
                output_path = os.path.join(folder_path, output_filename)
                # Convert the image to the desired format
                if output_format == 'jpeg':
                    im.convert('RGB').save(output_path, 'JPEG')
                elif output_format == 'png':
                    im.save(output_path, 'PNG')
