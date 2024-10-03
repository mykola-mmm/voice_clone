import argparse
import shutil
import os

def merge_folders(source_folders, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for folder in source_folders:
        if not os.path.isdir(folder):
            print(f"Warning: {folder} is not a directory. Skipping.")
            continue

        for root, _, files in os.walk(folder):
            for file in files:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, folder)
                dst_path = os.path.join(output_folder, rel_path)

                # Create subdirectories if they don't exist
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                # Copy the file
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {src_path} -> {dst_path}")

def main():
    parser = argparse.ArgumentParser(description="Merge multiple folders into one output folder.")
    parser.add_argument("-m", "--merge", nargs="+", required=True, help="Source folders to merge")
    parser.add_argument("-o", "--output", required=True, help="Output folder")

    args = parser.parse_args()

    merge_folders(args.merge, args.output)
    print(f"Merge complete. All files copied to {args.output}")

if __name__ == "__main__":
    main()
