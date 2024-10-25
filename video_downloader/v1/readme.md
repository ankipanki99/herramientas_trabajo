# Downloader v1 - Basic Version

This is a basic script to download YouTube videos using the `yt_dlp` library. It allows users to choose the quality of the video to download and saves the video with a well-formatted filename.

## Features

- **YouTube Video Download**: Downloads videos from YouTube by allowing users to input the video URL.
- **Quality Selection**: Displays available quality options for the video and allows the user to choose which quality to download.
- **Recommended Quality**: Identifies a balanced quality option (360p, mp4, H.264, with audio) if available.
- **Formatted Filename**: Saves the downloaded video with a filename formatted as `YEARmonthday_video_title_uploader`.
- **User-Friendly Interface**: Prompts the user to enter the video URL and the output directory.

## How to Use

1. **Run the Script**: Execute the script in your Python environment.
2. **Input Video URL**: You will be prompted to enter the YouTube video URL.
3. **Choose Quality**: The script will display available quality options, and you can select which one to download.
4. **Specify Output Path**: You can specify a directory to save the video. If left empty, the video will be saved in the current directory.

## Requirements

- **Python 3.6+**
- **Dependencies**:
  - yt-dlp

Install dependencies using the following command:
```sh
pip install yt-dlp
```

## Script Breakdown

- **download_video(url, output_path)**: Downloads the YouTube video with the given URL, allowing the user to select the desired quality and save the file with a well-formatted name.
- **Quality Options**: Lists all available video quality options, including resolution, format, and codecs. A recommended quality (360p, mp4) is suggested if available.
- **Error Handling**: The script includes basic error handling to inform the user if something goes wrong during the download.

## Notes

- The script uses `yt-dlp` to extract information about the video and to handle the downloading process.
- The recommended quality is selected based on a balance between resolution, file size, and compatibility.
- Ensure that you have permission to download the content, as some videos may be protected by copyright.

## License

This project is licensed under the MIT License.

