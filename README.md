## Prerequisites

### 1. FFmpeg
This app requires **FFmpeg** to process and convert audio/video downloads.
* **Windows:** Download FFmpeg from the official site, extract it, and add the `bin` folder to your System `PATH`.
* **Linux:** `sudo apt install ffmpeg`

### 2. Python Dependencies
This app requires **Flet v0.28.3** specifically.

Install all required packages with:
```bash
pip install -r requirements.txt
```

# Media-Fetch: YouTube Downloader

## Project Overview
Media-Fetch is a cross-platform desktop application built with Python and the Flet UI framework. It acts as a graphical wrapper around the powerful `yt-dlp` library, allowing users to effortlessly download media from YouTube in both MP3 and MP4 formats. 

This project showcases the ability to integrate external command-line tools into a modern, asynchronous graphical interface, handling background processes and dynamic UI updates.

## Tech Stack & Skills Demonstrated
*   **Python:** Core application logic and asynchronous task management.
*   **Flet:** Building a modern, Flutter-based desktop GUI entirely in Python.
*   **yt-dlp:** Extracting and downloading media from YouTube.
*   **Asynchronous Programming (`asyncio`):** Running non-blocking background tasks for UI animations.
*   **File System Operations (`os`):** Managing directories and file paths for downloads.

## Key Features
*   **Format Selection:** Seamlessly switch between downloading audio (MP3) or video (MP4) using a segmented control button.
*   **Customizable Quality:** Users can specify the exact audio bitrate (e.g., 192, 320) for MP3 downloads.
*   **Dynamic UI & Animations:** 
    *   Animated text banners indicating current app state (Downloading, Successful, Error).
    *   Asynchronous background tasks that cycle UI colors (`colorsys`) and animate elements without freezing the main application thread.
*   **Dark/Light Mode:** Built-in theme toggling for user preference.
*   **Custom Directory Selection:** Integrated file picker allowing users to choose exactly where their media is saved.
*   **Keyboard Shortcuts:** Navigate the app quickly using `Ctrl+T` (Toggle Theme) and `Ctrl+R` (Refresh App State).

## Technical Highlights
*   **Asynchronous UI Updates:** Utilizes `asyncio.sleep()` within infinite loops (`colcyc`, `txtcyc`) deployed via `page.run_task()` to create smooth UI animations that run concurrently with the main application logic.
*   **Robust Error Handling:** Wraps the `yt-dlp` extraction process in a `try/except` block, ensuring the GUI gracefully handles invalid URLs or download failures without crashing, providing clear visual feedback to the user.
*   **Dictionary-Driven Configuration:** Dynamically constructs the complex `yt-dlp` option dictionaries based on user selections (Format, Bitrate) from the GUI.

