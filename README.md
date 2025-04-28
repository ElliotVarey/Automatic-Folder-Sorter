📂 Automatic Folder Sorter
A simple Python script that automatically organizes files from a folder (like your Downloads folder) into categorized subfolders based on file types.
I built this tool to keep my Downloads folder clean and structured without needing to manually sort files every day.

✨ Features
Sorts files into categories like Audio, Compressed, Documents, Images, Programs, and Videos.

Easy to configure: just update folder paths and file types in a single place.

Lightweight — no external Python packages required.

Helps maintain a neat and organized file system automatically.

🛠 How It Works
The script checks each file in the target folder, compares its extension against a pre-defined list, and moves it to the correct destination folder.

Example Categories:

Category	Extensions
Audio	.mp3, .wav, .flac, etc.
Compressed	.zip, .rar, .7z, etc.
Documents	.pdf, .docx, .txt, etc.
Images	.jpg, .png, .gif, .svg, etc.
Programs	.exe, .jar, .bat, .msi, etc.
Videos	.mp4, .avi, .mov, etc.
(You can customize or expand these easily.)

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/automatic-folder-sorter.git
Navigate into the project directory:

bash
Copy
Edit
cd automatic-folder-sorter
⚙️ Setup
Edit the Script:

Set the folderToSort variable to the folder you want to organize (e.g., your Downloads folder).

Update each path in the sort_library list to where you want the files to be moved.

Example:

python
Copy
Edit
folderToSort = r"C:\Users\YourName\Downloads"

sort_library = [
    {
        "folder": "Documents",
        "path": r"C:\Users\YourName\Downloads\Documents",
        "extensions": [".pdf", ".docx", ".txt"],
    },
    # Other categories...
]
Run the script:

bash
Copy
Edit
python folder_sorter.py
That's it!
All matching files will be moved into the appropriate folders.

📝 Customization
You can add more folders or file types by editing the sort_library list:

python
Copy
Edit
{
    "folder": "Ebooks",
    "path": r"C:\Users\YourName\Downloads\Ebooks",
    "extensions": [".epub", ".mobi", ".azw3"],
}
Simply append new dictionaries with folder, path, and extensions to the sort_library list.

🙋‍♂️ Why I Built This
My Downloads folder was constantly a mess with documents, videos, programs, and random images piling up.
I built this automatic folder sorter to save time, reduce clutter, and improve my productivity — no more manual file moving!

📜 License
This project is licensed under the MIT License.
