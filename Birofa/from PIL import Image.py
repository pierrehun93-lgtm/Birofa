from PIL import Image
import os

input_folder = "D:/Weblap/Birofa/Pictures/Stair"
output_folder = "D:/Weblap/Birofa/Pictures/Stair/Optimized"

print("Input folder:", input_folder)
print("Exists:", os.path.exists(input_folder))

os.makedirs(output_folder, exist_ok=True)

files = os.listdir(input_folder)
print("Files found:", len(files))
print(files)

for filename in files:
    print("Checking:", filename)

    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        print("Processing:", filename)

        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        w, h = img.size

        if w > 1200:
            new_height = int((1200 / w) * h)
            img = img.resize((1200, new_height), Image.LANCZOS)

        output_path = os.path.join(output_folder, filename)
        img.save(output_path, optimize=True, quality=80)

        print("Saved:", output_path)

print("Done")