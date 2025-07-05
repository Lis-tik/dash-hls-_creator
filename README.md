# 📼 Python DASH Packager

**Python DASH Packager** is a Python tool that uses `ffmpeg` to convert input media files (MKV, MKA, MP4, etc.) into a ready-to-use DASH package with adaptive bitrate and a unified manifest.

---

## 🚀 Features

- 📂 Supports popular media formats: `.mkv`, `.mka`, `.mp4` and more.
- 🎵 Add multiple audio tracks.
- 💬 Add and edit subtitles.
- 🏷️ Edit metadata for audio tracks and subtitles (description, language, etc.).
- ⚙️ Converts everything into a DASH (MPEG-DASH) structure with a single manifest.
- 🔄 Generates streams with adaptive bitrate.

---

## 🧩 Dependencies

- Python >= 3.8
- [ffmpeg](https://ffmpeg.org/) — must be installed and added to your `PATH`
- [lxml](https://lxml.de/) — must be installed and added to your `PATH`


## 📦 Installation

```bash
# Clone the repository
git clone [repository](https://github.com/Lis-tik/dash-hls-_creator.git)
cd python-dash-packager


# Install dependencies
pip install lxml

#ffmpeg must be downloaded from the official website and added to your system's PATH, because the program runs commands using subprocess!
