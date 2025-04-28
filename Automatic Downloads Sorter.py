import os, shutil

# Change the file path for the folder to be sorted (e.g. downloads folder)
folderToSort = r"path \ of \ folder \ to \ be \ sorted"

# Change each path for the folder in which items should be sorted into
sort_library = [
    {
        "folder": "Audio",
        "path": r"Audio \ path",
        "extensions": [ ".mp3", ".m4a", ".wav", ".aac", ".ogg", ".flac" ],
    },
    {
         "folder": "Compressed",
        "path": r"Compressed \ path",
        "extensions": [ ".zip", ".rar", ".7z", ".cab", ".tar", ".tar.gz", ".tgz", ".gz", ".iso" ],
    },
    {
        "folder": "Documents",
        "path": r"Documents \ path",
        "extensions": [ ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".rtf", ".odt", ".ods", ".odp", ".md", ".log" ],
    },
    {
        "folder": "Images",
        "path": r"Images \ path",
        "extensions": [ ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tif", ".tiff", ".svg", ".raw", ".cr2", ".nef", ".arw" ],
    },
    {
        "folder": "Programs",
        "path": r"Programs \ path",
        "extensions": [ ".exe", ".jar", ".app", ".msi", ".bat", ".sh", ".ps1", ".lnk", ".dll", ".sys" ],
    },
    {
        "folder": "Videos",
        "path": r"Videos \ path",
        "extensions": [ ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm" ],
    }
]

for file in os.listdir(folderToSort):
        for folder in sort_library:
            for extension in folder["extensions"]:
                if file.endswith(extension):
                    shutil.move(folderToSort+"\\"+file, folder["path"])

