from PIL import Image
from datetime import datetime
import os

def crop_and_resize_image(input_path, cropped_folder):
    try:
        # Resmi aç
        image = Image.open(input_path)

        # Resmin genişliğini ve yüksekliğini al
        width, height = image.size

        # Genişliği dörde bölerek yeni genişliği hesapla
        new_width = width // 4

        # Kırpma sınırları (left, top, right, bottom)
        crop_left = new_width  # Sol kenarı dörtte birine kadar olan genişlik
        crop_top = 0
        crop_right = width - new_width  # Sağ kenarı dörtte birine kadar olan genişlik
        crop_bottom = height

        # Resmi kırp
        cropped_image = image.crop((crop_left, crop_top, crop_right, crop_bottom))

        # Kırpılmış resmin adını oluştur
        timestamp = datetime.now().strftime("%H%M%S")
        output_filename = f"cropped_image_{timestamp}.jpg"

        # Çıkış klasörünü ve dosya yolunu birleştirerek kaydet
        output_path = os.path.join(cropped_folder, output_filename)
        cropped_image.save(output_path)
    except Exception as e:
        print(f"Error: {e}")

# Kullanım örneği
input_path = "reverend mother 2.jpg"
cropped_folder = "cropped_folder"

crop_and_resize_image(input_path, cropped_folder)
