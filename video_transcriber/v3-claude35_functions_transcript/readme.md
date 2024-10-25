# v3 - Claude Version with Additional Functions

This version of the script was created using Claude and includes several additional functionalities that enhance the transcription process, making it more interactive and user-friendly.

## Features

- **System Resource Monitoring**: Monitors CPU and RAM usage during the transcription process to provide real-time system status.
- **Audio Extraction**: Extracts audio from video files and converts it into WAV format for transcription.
- **Transcription**: Uses the Whisper model to transcribe audio to text, supporting multiple video formats.
- **Result Saving**: Saves the transcription result in a text file with the same name as the original video file.
- **Interactive Interface**: Provides an interactive interface for users to select videos, change folders, or exit the program.

## How to Use

1. **Run the Script**: Execute the script in your Python environment. Ensure all dependencies are installed (Whisper, MoviePy, psutil).
2. **Load the Whisper Model**: The script loads the Whisper model automatically. By default, it uses the "medium" model, which offers a balance between speed and accuracy.
3. **Select Folder**: You will be prompted to enter the folder path that contains the video files you wish to transcribe.
4. **Choose Video**: You can choose a specific video or process all videos in the folder. The interface allows you to easily navigate between available videos and folders.
5. **View System Status**: The script provides CPU and RAM usage updates during the transcription process, helping monitor system performance.
6. **Save Transcription**: The transcription is automatically saved in a text file in the same directory as the video.

## Requirements

- **Python 3.8+**
- **Dependencies**:
  - Whisper
  - MoviePy
  - psutil

Install dependencies using the following command:
```sh
pip install openai-whisper moviepy psutil
```

## Script Breakdown

- **monitor_resources()**: Monitors and returns the current CPU and RAM usage.
- **extract_audio_from_video(video_path, output_audio_path)**: Extracts audio from the specified video and saves it as a WAV file.
- **transcribe_video(video_path, model)**: Uses the Whisper model to transcribe the extracted audio and saves the transcription as a text file.
- **process_folder(folder_path, model)**: Lists available video files in the folder and provides options to transcribe selected videos.
- **main()**: Manages the overall flow, including loading the model, selecting folders, and handling user interactions.

## Notes

- This version is optimized for use on a Lenovo laptop, but it can be used on any machine with adequate system resources.
- The Whisper model used in this script is "medium". You may adjust the model size based on your system capabilities and requirements.
- Ensure that your system has sufficient RAM to handle the video and model processing effectively.

## License

This project is licensed under the MIT License.
