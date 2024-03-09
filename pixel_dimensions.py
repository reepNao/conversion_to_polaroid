from PIL import Image

def get_image_dimensions(file_path):
    try:
        image = Image.open(file_path)

        width, height = image.size
        return width, height
    except Exception as e:
        print(f"Hata: {e}")
        return None, None