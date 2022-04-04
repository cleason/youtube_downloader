from pytube import YouTube

url = "https://www.youtube.com/watch?v=lvCCqkkweyw" 


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    
    
    print(f"Progression du téléchargement {int(percent)} %")
    

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("Titre: " + youtube_video.title)
print("Nombre de vues: ", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(" ", stream)
    
# stream = youtube_video.streams.get_by_itag(22)
stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement en cours...")
stream.download()
print("Téléchargement terminé")