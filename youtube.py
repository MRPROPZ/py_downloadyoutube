from pytube import YouTube

link = "https://www.youtube.com/watch?v=zpUgpBaT5kI"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()