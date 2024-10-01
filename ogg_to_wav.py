import os
import subprocess
from pydub import AudioSegment

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def convert_ogg_to_wav(input_dir):
    # Check if ffmpeg is installed
    if not check_ffmpeg():
        print("Error: ffmpeg is not installed or not in the system PATH.")
        print("Please install ffmpeg and make sure it's accessible from the command line.")
        print("You can install ffmpeg in Linux with 'sudo apt-get install ffmpeg'")
        return

    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Directory '{input_dir}' does not exist.")
        return

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".ogg"):
            ogg_path = os.path.join(input_dir, filename)
            wav_path = os.path.join(input_dir, filename[:-4] + ".wav")

            try:
                # Load the .ogg file
                audio = AudioSegment.from_ogg(ogg_path)

                # Export as .wav
                audio.export(wav_path, format="wav")

                print(f"Converted: {filename} -> {filename[:-4]}.wav")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    input_directory = "./mevoices/temih/"
    convert_ogg_to_wav(input_directory)
