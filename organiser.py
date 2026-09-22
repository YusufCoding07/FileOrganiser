from pathlib import Path

CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",

    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives"
}


def get_unique_destination(destination):
    """Create a unique filename if the destination already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organise_folder(folder):
    """Organise the files inside the selected folder."""

    if not folder.exists():
        print("Error: That folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The selected path is not a folder.")
        return

    moved_count = 0
    skipped_count = 0

    for item in folder.iterdir():

        # Ignore folders
        if not item.is_file():
            continue

        extension = item.suffix.lower()
        category = CATEGORIES.get(extension)

        # Unknown file type
        if category is None:
            print(f"Skipped: {item.name} (unknown file type)")
            skipped_count += 1
            continue

        # Create category folder if needed
        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        # Work out where the file should go
        destination = category_folder / item.name

        # Prevent overwriting an existing file
        destination = get_unique_destination(destination)

        # Move the file
        item.rename(destination)

        print(f"Moved: {item.name} -> {category}/")
        moved_count += 1

    print()
    print("Organisation complete!")
    print(f"Files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")


def main():
    """Ask the user which folder they want to organise."""

    folder_input = input("Enter the folder path to organise: ").strip()

    folder = Path(folder_input)

    organise_folder(folder)


if __name__ == "__main__":
    main()
