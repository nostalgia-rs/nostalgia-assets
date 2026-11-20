from PIL import Image
from os import walk

def get_first_pixel_hex(image_path):
  with Image.open(image_path) as img:
    # Convert to RGB to ensure a consistent (R, G, B) tuple
    rgb_img = img.convert("RGB")

    # Get the RGB values of the top-left pixel at (0, 0)
    r, g, b = rgb_img.getpixel((0, 0))

    # Format the RGB values into a hex string
    return f"#{r:02x}{g:02x}{b:02x}"


# Example usage
for root, dirs, files in walk("./pokemon"):
    # print(f"Current folder: {root}")
    # print(f"Subfolders: {dirs}")
    # print(f"Files: {files}")
    # print("-" * 20)
    for file in files:
        if file.endswith((".png", ".jpg", ".jpeg")):
            image_path = f"{root}/{file}"

            img = Image.open(image_path).convert("RGB")
            quantized = img.quantize(colors=16).convert("RGB")

            colors = quantized.getcolors(maxcolors=16)
            sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)

            count, second_dominant_rgb = sorted_colors[1]
            hex_color = "#{:02x}{:02x}{:02x}".format(*second_dominant_rgb).upper()

            # hex_color = get_first_pixel_hex(image_path)
            file_name = file.split("/")[-1].split(".")[0]
            print(f"{file_name},{hex_color}")
