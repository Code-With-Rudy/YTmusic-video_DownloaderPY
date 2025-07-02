# YouTube Video & Audio Downloader

A Python script to download YouTube videos and extract audio using `yt-dlp`. Features an interactive menu and supports both video downloads and audio extraction in multiple formats.

## 🚀 Features

- **Download full videos** in the best available quality (MP4 preferred)
- **Extract audio to MP3** with customizable quality (requires FFmpeg)
- **Download audio in original format** (WebM/M4A) without FFmpeg
- **Get video information** without downloading
- **Interactive command-line interface**
- **Custom output directories**
- **Cross-platform support** (Windows, macOS, Linux)
- **Robust error handling** and URL validation

## 📋 Requirements

- Python 3.6+
- `yt-dlp` library
- `ffmpeg` (optional, for MP3 conversion)

## 🛠️ Installation

### 1. Clone the repository
```bash
https://github.com/Code-With-Rudy/YTmusic-video_DownloaderPY.git
cd youtube-downloader
```

### 2. Install Python dependencies
```bash
pip install yt-dlp
```

### 3. Install FFmpeg (Optional - for MP3 conversion)

#### Windows:
```powershell
# Using winget
winget install ffmpeg

# Or using Chocolatey
choco install ffmpeg
```

#### macOS:
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

## 🚀 Usage

### Interactive Mode
Run the script and follow the interactive menu:

```bash
# Windows
python youtube_downloader.py

# macOS/Linux
python3 youtube_downloader.py
```

### Menu Options:
1. **Download Video** - Downloads video in best available quality
2. **Download Audio (MP3)** - Extracts and converts audio to MP3 (requires FFmpeg)
3. **Download Audio (Original)** - Downloads audio in original format (no FFmpeg needed)
4. **Get Video Info** - Shows video details without downloading
5. **Exit** - Quit the program


## 📁 Output Structure

Downloaded files are saved to the specified directory (default: `./downloads/`) with the following naming convention:
```
downloads/
├── Video_Title.mp4
├── Audio_Title.mp3
└── Audio_Title.webm
```

## 🔧 Configuration

### Custom Output Directory
When prompted, you can specify a custom download directory, or press Enter to use the default `./downloads` folder.

### Audio Quality Settings
The script downloads audio at 192 kbps MP3 quality by default. You can modify this in the `download_audio()` function:

```python
'preferredquality': '320',  # For higher quality
```


## ❌ Troubleshooting

### Common Issues:

#### FFmpeg not found error:
```
ERROR: Postprocessing: ffprobe and ffmpeg not found
```
**Solution:** Install FFmpeg or use Option 3 (Original format) which doesn't require FFmpeg.

#### Permission denied error:
**Solution:** Run terminal/command prompt as administrator, or choose a different output directory.

#### URL not supported:
**Solution:** Ensure you're using a valid YouTube URL. Private or age-restricted videos may not be downloadable.

### FFmpeg Installation Verification:
```bash
ffmpeg -version
```
If this command works, FFmpeg is properly installed.

## ⚖️ Legal Disclaimer

This tool is for educational purposes only. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws. Only download content you have permission to download or that is available under appropriate licenses.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The core library that powers this downloader
- [FFmpeg](https://ffmpeg.org/) - For audio/video processing capabilities



## 🔗 Links
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [FFmpeg Download](https://ffmpeg.org/download.html)

---

⭐ **Star this repository if you found it helpful!**

---
```
CODE WITH RUDY - Rudranil Goswami
```
- [linkedin](https://www.linkedin.com/in/rudranil-goswami-a94298329/) - Visit Profile
---
