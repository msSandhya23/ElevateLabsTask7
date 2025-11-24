import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), keep_aspect=True):
    """
    Resize all images in a folder and save them to output_folder.

    :param input_folder: Folder containing original images
    :param output_folder: Folder to save resized images
    :param size: Target (width, height)
    :param keep_aspect: Preserve aspect ratio if True
    """

    # Create output directory if missing
    os.makedirs(output_folder, exist_ok=True)

    # Supported image formats
    valid_ext = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_ext):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    if keep_aspect:
                        img.thumbnail(size)
                    else:
                        img = img.resize(size)

                    img.save(output_path)
                    print(f"Resized: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    resize_images(
        input_folder="input_images",
        output_folder="output_images",
        size=(800, 800),      # Customize your target size
        keep_aspect=True      # Change to False to ignore aspect ratio
    )
