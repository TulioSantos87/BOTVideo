import yt_dlp
import uuid

def download_video(url):
    filename = f"video_{uuid.uuid4()}.mp4"

    ydl_opts = {
        'outtmpl': filename,
        'format': 'mp4',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return filename
