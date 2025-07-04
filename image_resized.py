import os
from PIL import Image

# 📁 Source and output folders
SOURCE_FOLDER = 'input_images'
OUTPUT_FOLDER = 'resized_images'
NEW_SIZE = (800, 800)  # Resize to 800x800

def resize_and_convert_images():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for file_name in os.listdir(SOURCE_FOLDER):
        try:
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp')):
                img_path = os.path.join(SOURCE_FOLDER, file_name)
                with Image.open(img_path) as img:
                    img = img.resize(NEW_SIZE)
                    new_name = os.path.splitext(file_name)[0] + '.png'
                    img.save(os.path.join(OUTPUT_FOLDER, new_name), 'PNG')
                    print(f"[✔] Processed: {file_name}")
        except Exception as e:
            print(f"[✘] Failed: {file_name} → {e}")

if __name__ == "__main__":
    resize_and_convert_images()
