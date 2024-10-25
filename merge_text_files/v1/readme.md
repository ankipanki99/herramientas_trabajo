# Merger v1 - Basic Version

This is a basic script to merge all `.txt` files in a given directory into a single output text file. It provides a simple way for users to combine multiple text files in a specified folder.

## Features

- **Directory Input**: Prompts the user to input the directory containing the `.txt` files.
- **Directory Verification**: Checks if the provided directory is valid.
- **File Detection and Sorting**: Detects all `.txt` files in the directory, sorts them, and prepares them for merging.
- **Automatic Output Naming**: Creates a logical name for the output file based on the number of `.txt` files merged.
- **Output File Creation**: Combines all the `.txt` files into a single output file, adding a newline between each file.

## How to Use

1. **Run the Script**: Execute the script in your Python environment.
2. **Input Directory Path**: You will be prompted to enter the path to the directory containing your `.txt` files.
3. **Merging Process**: The script will verify if the directory is valid and if it contains `.txt` files.
4. **Output**: If successful, the script will create a new merged file in the same directory with a name like `archivos_unidos_X_archivos.txt` (where `X` is the number of `.txt` files).

## Requirements

- **Python 3.6+**

## Example Usage

```sh
Please enter the path of the directory where your text files are located: /path/to/your/directory
Files successfully merged into: /path/to/your/directory/archivos_unidos_3_archivos.txt
```

## Notes

- The script adds a newline character between the contents of each file for readability. You may remove or modify this line if not required.
- The output file will be saved in the same directory as the input files.

## License

This project is licensed under the MIT License.

