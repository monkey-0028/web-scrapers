from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=UJeSWbR6W04")
print(video.streams)