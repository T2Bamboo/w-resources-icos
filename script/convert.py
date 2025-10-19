from PIL import Image
import os

def convert_all_to_png(input_folder, size=None):
    output_folder = os.path.join(input_folder, "converted")
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        if not os.path.isfile(input_path):
            continue

        try:
            with Image.open(input_path) as img:
                if size:
                    img = img.resize(size, Image.LANCZOS)

                base_name, _ = os.path.splitext(file_name)
                output_path = os.path.join(output_folder, f"{base_name}.png")

                img.save(output_path, "PNG")
                print(f"✅ {file_name} → {output_path} (size={img.size})")
        except Exception as e:
            print(f"⚠️ {file_name}: {e}")

    print(f"\n🎉 done: {output_folder}")


if __name__ == "__main__":
    # convert_all_to_png("generative", size=(32, 32)) 
    convert_all_to_png("w", size=(32, 32)) 

