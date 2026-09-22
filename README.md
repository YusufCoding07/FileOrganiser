# File Organiser

A Python file organisation tool that automatically sorts files into folders based on their file extensions.

## Features

* Organises files by type
* Supports images, documents, audio, videos, code and archives
* Creates category folders automatically
* Handles uppercase and lowercase file extensions
* Skips unsupported file types
* Prevents files from being overwritten when duplicate filenames exist
* Shows a summary of files moved and skipped
* Allows the user to choose which folder to organise

## Categories

| File Types                              | Folder    |
| --------------------------------------- | --------- |
| `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` | Images    |
| `.pdf`, `.doc`, `.docx`, `.txt`         | Documents |
| `.mp3`, `.wav`, `.flac`                 | Audio     |
| `.mp4`, `.mov`, `.avi`                  | Videos    |
| `.py`, `.js`, `.html`, `.css`, `.java`  | Code      |
| `.zip`, `.rar`, `.7z`                   | Archives  |

## How It Works

The program checks each file in the selected folder and gets its file extension.

It then uses a dictionary to match the extension to a category.

For example:

```text
photo.jpg
    ↓
.jpg
    ↓
Images
    ↓
Images/photo.jpg
```

If a file type is not supported, the program skips it rather than causing an error.

If a file with the same name already exists in the destination folder, the program creates a unique filename instead.

For example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

## Requirements

* Python 3.11 or newer

## How to Run

Clone the repository and open the project folder in a terminal.

Run:

```bash
python organiser.py
```

Enter the path of the folder you want to organise when prompted.

Example:

```text
Enter the folder path to organise: test_folder
```

## Technologies Used

* Python
* pathlib
* Git
* GitHub

## Project Purpose

This project was created to practise Python programming, file handling, dictionaries, functions, error handling and automation.
