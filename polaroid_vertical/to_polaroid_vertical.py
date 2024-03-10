from PIL import Image, ImageOps
from datetime import datetime
import os

from pixel_dimensions import *

def apply_polaroid_effect(input_path, output_folder, polaroid_size, frame_sizes=(150, 75, 150, 200)):
    # right, top, left, bottom frame sizes

    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    polaroid_image = ImageOps.expand(grayscale_image, border=frame_sizes, fill='white')
    polaroid_image = polaroid_image.resize(polaroid_size)
    timestamp = datetime.now().strftime("%H%M%S")

    output_filename = os.path.join(output_folder, f"output_polaroid_{timestamp}.jpg")
    polaroid_image.save(output_filename)
    print(f"Polaroid image saved to: {output_filename}")
    return polaroid_image  # apply_polaroid_effect fonksiyonu artık polaroid resmini döndürüyor.

def adding_last_frame(polaroid_image, output_folder, frame_sizes=(3, 3, 3, 3)):
    # right, top, left, bottom frame sizes
    polaroid_with_frame = ImageOps.expand(polaroid_image, border=frame_sizes, fill='black')
    timestamp = datetime.now().strftime("%H%M%S")
    output_filename = os.path.join(output_folder, f"output_polaroid_{timestamp}.jpg")
    polaroid_with_frame.save(output_filename)
    print(f"Last framed polaroid image saved to: {output_filename}")

if __name__ == "__main__":
    input_image = "lea seydoux f.jpg"
    output_folder = "output_folder"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    width, height = get_image_dimensions(input_image)
    image_dimensions = (width, height)
    polaroid_image = apply_polaroid_effect(input_image, output_folder, image_dimensions)
    adding_last_frame(polaroid_image, output_folder)
