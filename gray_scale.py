from PIL import Image

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)

input_path = "reverend mother 2.jpg"
output_filename = "output_grayscale.jpg"

convert_to_grayscale(input_path, output_filename)
