import yt_dlp

DOWNLOAD_DIR = "/Users/ibe/PycharmProjects/YTDownload/downloaded_videos"

url = input("Enter the YouTube URL: ").strip()

try:
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "format":"bestvideo/best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nDownload complete. Saved to:", DOWNLOAD_DIR)

except Exception as e:
    print("\nAn error occurred:", str(e))

