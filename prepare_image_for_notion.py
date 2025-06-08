import os
import sys
import shutil
from PIL import Image

# --- CONFIGURATION ---
# 1. Set the target file size in Megabytes (MB).
TARGET_SIZE_MB = 5.0

# 2. Set the absolute path to your target folder.
# IMPORTANT: Use double backslashes (\\) in the path!
# Example: "C:\\Users\\YourUsername\\Downloads"
DOWNLOADS_FOLDER_PATH = "A:\\Downloads"
# --- END OF CONFIGURATION ---


# Convert megabytes to bytes for file size comparison
TARGET_SIZE_BYTES = TARGET_SIZE_MB * 1024 * 1024


def prepare_image_for_notion(input_path):
    """
    Prepares an image file for a Notion upload based on user configuration.
    """
    print(f"--- Starting script for: '{input_path}' ---")

    if not os.path.isfile(input_path):
        print(f"ERROR: Input path is not a valid file.")
        return

    try:
        img = Image.open(input_path)
    except (IOError, SyntaxError):
        print(f"ERROR: Input is not a valid image file. Aborting.")
        return

    # Use the configured folder path directly
    target_folder = DOWNLOADS_FOLDER_PATH
    
    if not os.path.isdir(target_folder):
        print(f"ERROR: The configured target folder does not exist: '{target_folder}'")
        img.close()
        return

    base_name, extension = os.path.splitext(os.path.basename(input_path))
    
    # Decide to copy or compress
    if os.path.getsize(input_path) <= TARGET_SIZE_BYTES:
        output_path = os.path.join(target_folder, f"{base_name}_notion{extension}")
        shutil.copy2(input_path, output_path)
        print(f"SUCCESS: File copied to '{output_path}'")
        img.close()
        return

    # Compress the image
    print(f"LOG: File is larger than {TARGET_SIZE_MB}MB. Starting compression...")
    output_path = os.path.join(target_folder, f"{base_name}_notion.jpg")

    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    quality = 95
    quality_step = 5
    compression_success = False
    while quality > 10:
        try:
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            if os.path.getsize(output_path) <= TARGET_SIZE_BYTES:
                compression_success = True
                break
            quality -= quality_step
        except Exception as e:
            print(f"ERROR: Failed to save compressed image. Reason: {e}")
            break
            
    if compression_success:
        print(f"SUCCESS: File compressed to '{output_path}'")
    else:
        print(f"ERROR: Could not compress the file to the target size.")
    
    img.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            prepare_image_for_notion(sys.argv[1])
        except Exception as e:
            # This general catch is for unexpected errors during execution.
            # The error message will only be visible when running with python.exe.
            print(f"--- A CRITICAL UNHANDLED ERROR OCCURRED ---")
            print(e)