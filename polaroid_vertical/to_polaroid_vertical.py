from PIL import Image, ImageOps
from datetime import datetime
import os

from pixel_dimensions import *

def apply_polaroid_effect(input_path, output_folder, polaroid_size, frame_sizes=(150, 75, 150, 200)):
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
    input_image = "lea seydoux f.jpg"
    output_folder = "output_folder"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    width, height = get_image_dimensions(input_image)
    image_dimensions = (width, height)
    apply_polaroid_effect(input_image, output_folder, image_dimensions)
