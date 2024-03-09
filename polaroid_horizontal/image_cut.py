from PIL import Image
from datetime import datetime
import os

from pixel_dimensions import *

def crop_and_resize_image(input_path, cropped_folder):
    try:
        image = Image.open(input_path)
        width, height = get_image_dimensions(input_path)
        new_width = width // 4
        # Kırpma sınırları (left, top, right, bottom)
        crop_left = new_width  #sol kenarı dörtte birine kadar olan genişlik
        crop_top = 0
        crop_right = width - new_width  #sağ kenarı dörtte birine kadar olan genişlik
        crop_bottom = height

        #resmi belirtilen pikseller kadar kırpma işlemi
        cropped_image = image.crop((crop_left, crop_top, crop_right, crop_bottom))

        #kırpılmış resmin adını oluştur
        timestamp = datetime.now().strftime("%H%M%S")
        output_filename = f"cropped_image_{timestamp}.jpg"

        # çıkış klasörünü ve dosya yolunu birleştirerek kaydet
        output_path = os.path.join(cropped_folder, output_filename)
        cropped_image.save(output_path)
        return output_path
    except Exception as e:
        print(f"Error: {e}")
        return None