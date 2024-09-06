# Image Metadata Batch Updater

A Python script that uses ExifTool to batch update image keywords from corresponding text files. The script automatically overwrites existing keywords in the image metadata with the new ones provided in the `.txt` files.

## Features
- Supports `.jpg`, `.jpeg`, and `.png` image formats.
- Reads keywords from `.txt` files with the same name as the images.
- Replaces existing image metadata keywords with the new ones from the text files.
- Automatically removes backup files with `_original` created by ExifTool.
- Ensures keywords are added as individual list entries (no spaces before or after).

## Requirements

- Python 3.x
- [ExifTool](https://exiftool.org/) (installed via Homebrew or manually)

### Python Libraries:
- None required (uses Python’s built-in `subprocess` module).

### Installing ExifTool (macOS/Linux):
```bash
brew install exiftool

## Usage

1. Place the images and corresponding `.txt` files in the same folder. Each `.txt` file should contain the keywords for the image, separated by a semicolon (`;`).
   - Example:
     - `image1.jpg`
     - `image1.txt` containing: `Gothic tracery; Liturgical; Radiating halo; Saint depiction`
2. Run the script to update the keywords.

## Running the Script:

python3 script.py

## Sample Output

Updated image1.jpg with keywords from image1.txt
Updated image2.png with keywords from image2.txt

## Example .txt File:

The text file should have keywords separated by semicolons, like:

Gothic tracery; Liturgical; Radiating halo; Saint depiction

## License

This project is licensed under the MIT License - see the LICENSE file for details.

