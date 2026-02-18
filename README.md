## simple File Manager Automation Tool – User Guide

This tool allows you to automatically create folders and files using a simple command syntax inside Python.

---

## 1. How to Run the Tool

1. Make sure Python is installed on your computer.
2. Download the script.
3. Open your terminal or command prompt
4. Navigate to the folder where the script is saved, or just open the file by double click.
5. Run the script (cmd):

```
simflan.py
```

6. The program will ask for:

   * Base path
   * Command input

---

## 2. Base Path

The base path is the root directory where all folders and files will be created.

Example:

```
E:/my_folder
```

All generated folders and files will be created inside this directory.

---

## 3. Command Syntax

The tool supports several special symbols and commands.

---

### A. Create Nested Folders Using Comma (,)

Use a comma to create folders inside the previous folder.

Example:

```
moments, family, friends
```

Result:

```
E:/my_folder/moments/family/friends
```

Each comma means “go inside the previous folder”.

---

### B. Create Separate Folders Using Dot (.)

Use a dot to create folders at the same level (parallel folders).

Example:

```
moments. family. friends
```

Result:

```
E:/my_folder/moments
E:/my_folder/family
E:/my_folder/friends
```

Each dot means “create a new folder in the base path”.

---

### C. Create a File in a Specific Folder (-f)

Use `-f` followed by:

```
-f folder_name file_name
```

Example:

```
-f family note.txt
```

Result:

```
E:/my folder/family/note.txt
```

If the folder does not exist, it will be created automatically.

---

### D. Create a Folder Inside a Specific Folder (-in)

Use `-in` followed by:

```
-in target_folder .new_folder
```

Example:

```
-in teman .rizal
```

Result:

```
E:/my_folder/friends/jack
```

The dot before the new folder name is required by the current script format.

---

## 4. Example Full Session

Input:

Base path:

```
E:/my_folder
```

Command:

```
image, family -f family note.txt -in family .archive
```

This will:

1. Create nested folder: `image/family`
2. Create file: `family/note.txt`
3. Create subfolder: `family/archive`

---

## 5. Important Notes

* Folder and file names must not contain invalid system characters.
* Paths must exist or be valid for your operating system.
* The script does not currently support spaces inside folder names unless modified.

---

This tool is designed for fast manual structure creation using compact text commands.
