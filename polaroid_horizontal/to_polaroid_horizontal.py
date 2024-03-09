from PIL import Image, ImageOps
from datetime import datetime
import os

from pixel_dimensions import *
from image_cut import *

def apply_polaroid_effect(input_path, output_folder, polaroid_size, frame_sizes=(150, 100, 150, 250)):
    #right, top, left, bottom frame sizes

    image = Image.open(input_path)#resmi açar
    grayscale_image = image.convert("L")#resmi gri tonlamalı yapar
    polaroid_image = ImageOps.expand(grayscale_image, border=frame_sizes, fill='white')#beyaz arka plana sahip polaroid resmi oluşturur
    polaroid_image = polaroid_image.resize(polaroid_size)#tekrar boyutlandırır
    timestamp = datetime.now().strftime("%H%M%S")

    output_filename = os.path.join(output_folder, f"output_polaroid_{timestamp}.jpg")#resmin adını oluşturur
    polaroid_image.save(output_filename)#resmi kaydede
    print(f"Polaroid image saved to: {output_filename}")

if __name__ == "__main__":
    input_image = "reverend mother 2.jpg"
    cropped_folder = "cropped_folder"
    if not os.path.exists(cropped_folder):
        os.makedirs(cropped_folder)

    input_path = crop_and_resize_image(input_image, cropped_folder)
    output_folder = "output_folder"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    width, height = get_image_dimensions(input_path)
    image_dimensions = (width, height)
    apply_polaroid_effect(input_path, output_folder, image_dimensions)

    try:
        os.remove(input_path)
    except Exception as e:
        print(f"Error: {e}")