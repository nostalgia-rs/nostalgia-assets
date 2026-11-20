from PIL import Image
from os import walk


# Example usage
for root, dirs, files in walk("./pride"):
    # print(f"Current folder: {root}")
    # print(f"Subfolders: {dirs}")
    # print(f"Files: {files}")
    # print("-" * 20)
    for file in files:
        if file.endswith((".png")):
            image_path = f"{root}/{file}"

            with Image.open(image_path) as img:
                rgb_img = img.convert("RGB")
                # Save as JPG
                new_image_path = image_path.rsplit('.', 1)[0] + '.jpg'
                rgb_img.save(new_image_path, quality=95)
                file_name = file.split("/")[-1].split(".")[0]
