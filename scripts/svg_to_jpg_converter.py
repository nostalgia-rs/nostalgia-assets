"""Make sure to run `brew install cairo` before running this script."""
from PIL import Image
from os import walk
from cairosvg import svg2png
from io import BytesIO



def svg_to_jpg(svg_path, jpg_path, width=1200, quality=92, bg="white"):
    """Source: https://www.svggenie.com/blog/svg-to-jpg-convert-guide"""
    png_bytes = svg2png(
        url=svg_path,
        output_width=width,
        output_height=None,  # preserves aspect ratio
    )

    img = Image.open(BytesIO(png_bytes))

    # JPG cannot store alpha — composite onto background
    background = Image.new("RGB", img.size, bg)
    background.paste(img, mask=img.split()[3] if img.mode == "RGBA" else None)

    background.save(jpg_path, "JPEG", quality=quality, optimize=True)

# Example usage
for root, dirs, files in walk("./pride"):
    # print(f"Current folder: {root}")
    # print(f"Subfolders: {dirs}")
    # print(f"Files: {files}")
    # print("-" * 20)
    for file in files:
        if file.endswith((".svg")):
            image_path = f"{root}/{file}"

            svg_to_jpg(image_path, image_path.rsplit('.', 1)[0] + '.jpg', width=1200, quality=92)

