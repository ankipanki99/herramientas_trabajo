# v3 - Claude Version with Additional Functions
# This version was created using Claude with additional functions.
# Features:
# - Monitoring CPU and RAM usage during transcription.
# - Extracting audio from video files.
# - Transcribing audio to text.
# - Saving the result in a text file.
# - Interactive interface to process videos, change folders, or exit.

import whisper
import moviepy.editor as mp
import os
import time
import psutil

def monitor_resources():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    return f"CPU: {cpu_percent}% | RAM: {memory.percent}% | Available RAM: {memory.available / (1024 * 1024 * 1024):.2f}GB"

def extract_audio_from_video(video_path, output_audio_path):
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')
        video.close()
    except Exception as e:
        print(f"Error extracting audio: {e}")
        raise e

def transcribe_video(video_path, model):
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    try:
        print("Starting transcription process...")
        print("System status:", monitor_resources())
        
        print("Extracting audio...")
        extract_audio_from_video(video_path, audio_path)
        print("Audio extracted successfully")
        
        print("Starting transcription...")
        start_time = time.time()
        
        result = model.transcribe(audio_path)
        
        duration = time.time() - start_time
        
        output_file = os.path.splitext(video_path)[0] + "_transcription.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"\nTranscription completed in {duration:.2f} seconds")
        print("Final system status:", monitor_resources())
        print(f"Transcription saved in: {output_file}")
        
    except Exception as e:
        print(f"Error in transcription: {e}")
        raise e
    finally:
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except:
                pass

def process_folder(folder_path, model):
    videos = [f for f in os.listdir(folder_path) 
              if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    
    if not videos:
        print("No videos found in this folder.")
        return True
    
    while True:
        print("\nAvailable videos:")
        for i, file in enumerate(videos, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("\nSelect the video number (0 to change folder): "))
            if choice == 0:
                return True
            if 1 <= choice <= len(videos):
                video_path = os.path.join(folder_path, videos[choice-1])
                transcribe_video(video_path, model)
            else:
                print("Invalid selection")
        except ValueError:
            print("Please enter a valid number")
        
        continuar = input("\nWhat would you like to do?\n"
                         "1: Process another video in the same folder\n"
                         "2: Change folder\n"
                         "3: Exit\n"
                         "Select an option (1/2/3): ").strip()
        
        if continuar == '2':
            return True
        elif continuar == '3':
            return False
        elif continuar != '1':
            print("Invalid option, continuing with the same folder...")

def main():
    try:
        print("Loading Whisper model...")
        model = whisper.load_model("medium")
        print("Model loaded successfully")
        
        last_path = None
        change_folder = True
        
        while True:
            if change_folder:
                if last_path:
                    print(f"\nLast used folder: {last_path}")
                    use_last = input("Do you want to use the same folder? (y/n): ").lower()
                    if use_last == 'y':
                        folder_path = last_path
                    else:
                        folder_path = input("Enter the new folder path: ").strip()
                else:
                    folder_path = input("Enter the folder path: ").strip()
                
                if folder_path.lower() == 'exit':
                    break
                    
                if not os.path.exists(folder_path):
                    print("Invalid path.")
                    continue
                
                last_path = folder_path
                
            change_folder = process_folder(folder_path, model)
            
            if not change_folder:
                break
                
    except Exception as e:
        print(f"Error in the program: {e}")
        raise e

if __name__ == "__main__":
    main()
