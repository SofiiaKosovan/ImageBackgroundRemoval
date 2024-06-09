from rembg import remove
from PIL import Image

input_path = '/Users/skosovan/Documents/couple.jpg'
output_path = '/Users/skosovan/Documents/couple_wb.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
