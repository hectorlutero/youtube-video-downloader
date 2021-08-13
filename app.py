from pytube import YouTube

youtube_url = YouTube('https://www.youtube.com/watch?v=7BXJIjfJCsA')

stream = youtube_url.streams.get_by_itag(22)
stream.download()
