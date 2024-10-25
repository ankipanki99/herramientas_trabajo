# v4 - Optimized for Lenovo Laptop Blankis (Optimized by Claude 3.5)

This version of the script has been optimized specifically for use on a Lenovo laptop (Blankis model). It includes streamlined functionalities to efficiently extract and transcribe video content, providing users with an easy-to-use interactive interface.

## Features

- **System Resource Monitoring**: Monitors CPU and RAM usage during the transcription process to ensure efficient performance.
- **Audio Extraction**: Extracts audio from video files and converts it into WAV format for transcription.
- **Basic Transcription**: Uses the Whisper model to perform basic transcription of the audio, supporting multiple video formats.
- **Result Saving**: Saves the transcription result in a text file with the same name as the original video file.
- **Simple User Interface**: Allows the user to input a folder path, select a video, and initiate the transcription process.

## How to Use

1. **Run the Script**: Execute the script in your Python environment. Ensure all dependencies are installed (Whisper, MoviePy, psutil).
2. **Load the Whisper Model**: The script automatically loads the Whisper "medium" model, which balances speed and accuracy.
3. **Select Folder**: Input the path of the folder containing the video files to be transcribed.
4. **Choose Video**: The script lists all available video files in the specified folder. Select the video by entering its corresponding number.
5. **View System Status**: The script provides CPU and RAM usage updates during the transcription process, helping monitor system performance.
6. **Save Transcription**: The transcription is saved in a text file with the same name as the original video in the same directory.

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
- **main()**: Manages the overall flow, including selecting folders, listing available videos, and handling user interactions.

## Notes

- This version was optimized using Claude 3.5, ensuring efficient resource utilization on Lenovo laptops.

- This version is optimized specifically for the Lenovo Blankis laptop, focusing on efficient resource usage.
- The Whisper model used in this script is "medium". You may adjust the model size based on your system capabilities and requirements.
- The interface is simple, aiming for usability without advanced features. It's suitable for users who want straightforward transcription without extensive configuration.

## License

This project is licensed under the MIT License.

