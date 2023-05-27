# Function that takes a YouTube video URL and downloads it
# into the current directory as an mp4 file
def download_youtube_video(url):
    from pytube import YouTube
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Downloaded: " + yt.title + " into " + yt.filename + ".mp4"