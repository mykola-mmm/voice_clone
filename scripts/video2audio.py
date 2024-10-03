import os
import argparse
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_mp4_to_wav(input_folder):
    # Get the parent directory of the input folder
    parent_dir = os.path.dirname(input_folder)
    
    # Create the output folder
    output_folder = os.path.join(parent_dir, "../video2audio")
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    mp4_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]
    for filename in tqdm(mp4_files, desc="Converting files", unit="file"):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_folder, output_filename)
        
        # Convert MP4 to WAV
        video = VideoFileClip(input_path)
        audio = video.audio
        audio.write_audiofile(output_path, logger=None)
        
        # Close the video and audio objects
        audio.close()
        video.close()
    
    print(f"Converted {len(mp4_files)} files")

def main():
    parser = argparse.ArgumentParser(description="Convert MP4 videos to WAV audio files")
    parser.add_argument("input_folder", help="Path to the folder containing MP4 videos")
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_folder):
        print("Error: The specified input folder does not exist.")
        return
    
    convert_mp4_to_wav(args.input_folder)
    print("Conversion completed.")

if __name__ == "__main__":
    main()