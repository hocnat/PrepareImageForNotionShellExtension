# PrepareImageForNotionShellExtension

Shell extension that prepares an image for upload by copying and optionally compressing it based on user-defined settings

[![License](https://img.shields.io/github/license/hocnat/PrepareImageForNotionShellExtension)](https://github.com/hocnat/PrepareImageForNotionShellExtension/blob/main/LICENSE)

## Motivation

[Notion imposes a 5MB file size limit on image uploads](https://www.notion.com/help/images-files-and-media). High-resolution screenshots and photos frequently exceed this limit, requiring a manual workflow to compress them before they can be used. This typically involves using an external tool to reduce the file size and save a new version of the image.

This project automates these steps by adding a `Prepare for Notion` command to the Windows context menu. A single right-click creates a new, optimized image file in a user-configured folder, ready for immediate upload.

## Usage

Follow these steps to set up the script and add the custom command to your context menu.

### Prerequisites

Before you begin, ensure you have the following set up.

#### Python and dependencies

The script requires Python to run.

1. **Install Python**: If you don't have it already, download and install Python from the [official website](https://www.python.org/downloads/).
2. **Install required package**: This script depends on the `Pillow` library for image processing. You can install it using `pip`, Python's package installer. Open your terminal or command prompt and run:
   ```shell
   pip install Pillow
   ```

#### Notion Desktop App (Optional)

For the context menu item to have the official Notion icon, you need the Notion Desktop App installed. If you don't have it, the command will still work, but it will appear without an icon.

### Get the code

Clone this repository to your local machine using the following command:

```shell
git clone https://github.com/hocnat/PrepareImageForNotionShellExtension.git
cd PrepareImageForNotionShellExtension
```

### Configuration (Required)

Before the script can work, you must configure it with your specific paths.

#### Configure the script

You must tell the script where to save the prepared images.

1. Open the `prepare_image_for_notion.py` file in a text editor.
2. Find the `CONFIGURATION` section at the top.
3. **Update the target folder path**:
   * Find the line `DOWNLOADS_FOLDER_PATH = "..."`.
   * Replace the placeholder path with the **absolute path** to your desired folder.
   * **IMPORTANT**: In the script, you must replace every single backslash `\` with a double backslash `\\`.
4. **Adjust the target file size (Optional)**: By default, the limit is `5.0` MB. You can change the value in `TARGET_SIZE_MB = 5.0` if needed.

#### Configure the registry file

The registry file tells Windows how to run the script. You must ensure the paths in it are correct.

1. Open the `add_prepare_image_for_notion_action.reg` file in a text editor.
2. **Update the Python Path**: For maximum reliability, provide the full path to your Python installation.
   * Look for the line that starts with `@=`.
   * Replace `C:\\Path\\To\\Your\\pythonw.exe` with the actual path to `pythonw.exe` on your system.
   * **To find the path:** Open a command prompt and type `where.exe pythonw.exe`.
3. **Update the Script Path**:
   * The file assumes you have cloned this repository to `C:\dev\PrepareImageForNotionShellExtension`.
   * If you have placed the project in a different directory, you **must** update the path `\"C:\\dev\\PrepareImageForNotionShellExtension\\prepare_image_for_notion.py\"` to match its actual location.
4. **Update the Icon Path (Optional)**:
   * Look for the line starting with `"Icon"=`.
   * Replace `YourUsername` with your actual Windows username to ensure the path to `Notion.exe` is correct.

### Installation

To add the "Prepare for Notion" command to your right-click menu, simply run the registry file.

1. Navigate to the folder where you cloned the repository.
2. Double-click the `add_prepare_image_for_notion_action.reg` file.
3. Windows will show a security warning. Click `Run`, then `Yes`, and finally `OK` to confirm that the information has been added to the registry.

The command is now installed.

### How to use

1. Find any image file on your computer that you want to upload to Notion.
2. Right-click the file.

    > **💡 Note for Windows 11 Users:**
    > On Windows 11, custom context menu commands are often hidden in the "Show more options" menu. To bypass this and open the classic context menu directly, hold down the **`Shift`** key while you right-click the file. The "Prepare for Notion" command will then be immediately visible.

3. Select `Prepare for Notion` from the context menu.
4. A new, optimized version of the image (named `..._notion.jpg`) will instantly appear in the folder you specified during configuration.
   * If the original image was already under the size limit, a simple copy is created.
   * If it was too large, it is compressed to fit the limit.
5. Upload the new file to Notion.

## Troubleshooting

**Problem:** The command does nothing, or a window flashes briefly and disappears.

This usually means the script is failing silently. The command is set up to run with `pythonw.exe`, which hides all output and error messages for a seamless experience. To see what's going wrong, you need to temporarily switch to `python.exe`.

1. **Open the registry file** (`add_prepare_image_for_notion_action.reg`) in a text editor.
2. **Find the command line** (it starts with `@=`).
3. **Change `pythonw.exe` to `python.exe`** in the path.
4. **Save the file** and double-click it again to update the registry.
5. Now, when you run the command from the context menu, a black console window will appear and show any error messages from the script. This will tell you exactly what needs to be fixed (e.g., a wrong path in the configuration).
6. Once you have fixed the issue, change it back to `pythonw.exe` to hide the window again.

## Used tools

* [Python](https://www.python.org/) - Python Software Foundation - *Python Software Foundation License*
  * The core programming language for the script.
* [Pillow](https://pillow.readthedocs.io/en/latest/) - Jeffrey A. Clark and contributors - *MIT-CMU License*
    * Image processing library used for resizing and compressing images.
* [Windows Registry](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry) - Microsoft
  * Used to add the custom command to the Windows Explorer context menu.
* [Gemini](https://gemini.google.com) - Google
  * Used as a development assistant for creating the script and writing documentation.

## License

[MIT License](https://github.com/hocnat/PrepareImageForNotionShellExtension/blob/main/LICENSE) Copyright 2025 © [hocnat](https://github.com/hocnat)