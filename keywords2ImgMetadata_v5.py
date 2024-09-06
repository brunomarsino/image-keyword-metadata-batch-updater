import os
import subprocess

# Path to the folder containing the images and txt files
image_folder = '/Users/brunomarsino/Documents/judson_ai_training/quick test sep 6'

# Supported image extensions
supported_extensions = ['.jpg', '.jpeg', '.png']

def update_image_keywords(image_path, keywords):
    # Prepare the ExifTool command, adding each keyword as a separate argument
    command = ['/usr/local/bin/exiftool', '-overwrite_original']
    
    # Add each keyword as a separate flag
    for keyword in keywords:
        command.append('-IPTC:Keywords={}'.format(keyword))
    
    command.append(image_path)
    
    # Run the ExifTool command
    subprocess.run(command)

def process_images_in_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Check if the file is an image
        if os.path.splitext(file)[1].lower() in supported_extensions:
            # Check if the corresponding txt file exists
            txt_file = os.path.splitext(file)[0] + '.txt'
            txt_file_path = os.path.join(folder_path, txt_file)
            
            if os.path.exists(txt_file_path):
                # Read the keywords from the txt file
                with open(txt_file_path, 'r') as f:
                    keywords = [kw.strip() for kw in f.read().split(';')]
                
                # Update the image metadata with the keywords
                update_image_keywords(file_path, keywords)
                print(f'Updated {file} with keywords from {txt_file}')
            else:
                print(f'No corresponding txt file for {file}')

# Run the process on the image folder
process_images_in_folder(image_folder)
