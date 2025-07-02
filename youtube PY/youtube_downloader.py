import os
import sys
from pathlib import Path
import yt_dlp

def download_video(url, output_path="./downloads"):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Prefer mp4, fallback to best available
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'restrictfilenames': True,  # Avoid special characters in filenames
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Video download completed successfully!")
            
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return False
    
    return True

def download_audio(url, output_path="./downloads", convert_to_mp3=True):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'restrictfilenames': True,
    }
    
    if convert_to_mp3:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from: {url}")
            ydl.download([url])
            if convert_to_mp3:
                print("Audio download and conversion completed successfully!")
            else:
                print("Audio download completed successfully!")
            
    except Exception as e:
        error_msg = str(e)
        if "ffmpeg" in error_msg.lower() or "ffprobe" in error_msg.lower():
            print(f"FFmpeg not found. Trying to download without conversion...")
            return download_audio(url, output_path, convert_to_mp3=False)
        else:
            print(f"Error downloading audio: {error_msg}")
            return False
    
    return True

def download_audio_raw(url, output_path="./downloads"):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'restrictfilenames': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio (original format) from: {url}")
            ydl.download([url])
            print("Audio download completed successfully!")
            
    except Exception as e:
        print(f"Error downloading audio: {str(e)}")
        return False
    
    return True

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Unknown'),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown')
            }
    except Exception as e:
        print(f"Error getting video info: {str(e)}")
        return None

def main():
    print("=== YouTube Video/Audio Downloader ===")
    print()
    
    while True:
        print("\nOptions:")
        print("1. Download Video")
        print("2. Download Audio (MP3 - requires FFmpeg)")
        print("3. Download Audio (Original format - no FFmpeg needed)")
        print("4. Get Video Info")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue
            
        url = input("Enter YouTube URL: ").strip()
        
        if not url:
            print("Please enter a valid URL.")
            continue
        # Basic URL validation for YouTube
        if not any(domain in url for domain in ['youtube.com', 'youtu.be', 'm.youtube.com']):
            print("Please enter a valid YouTube URL.")
            continue
            
        if choice == '1':
            output_dir = input("Enter output directory (press Enter for './downloads'): ").strip()
            if not output_dir:
                output_dir = "./downloads"
            download_video(url, output_dir)
            
        elif choice == '2':
            output_dir = input("Enter output directory (press Enter for './downloads'): ").strip()
            if not output_dir:
                output_dir = "./downloads"
            download_audio(url, output_dir, convert_to_mp3=True)
            
        elif choice == '3':
            output_dir = input("Enter output directory (press Enter for './downloads'): ").strip()
            if not output_dir:
                output_dir = "./downloads"
            download_audio_raw(url, output_dir)
            
        elif choice == '4':
            info = get_video_info(url)
            if info:
                print(f"\n--- Video Information ---")
                print(f"Title: {info['title']}")
                print(f"Uploader: {info['uploader']}")
                print(f"Duration: {info['duration']} seconds")
                print(f"Views: {info['view_count']:,}")
                print(f"Upload Date: {info['upload_date']}")

def quick_download_video(url, output_path="./downloads"):
    return download_video(url, output_path)

def quick_download_audio(url, output_path="./downloads"):
    return download_audio(url, output_path)

if __name__ == "__main__":
    main()