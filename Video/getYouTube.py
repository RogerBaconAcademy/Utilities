from pytube import YouTube

def getYouTube(link:str, destinationFolder:str, extension='mp4', resolution='360p'):
    yt = YouTube(link)
    mp4_files = yt.streams.filter(file_extension=extension)
    mp4_369p_files = mp4_files.get_by_resolution(resolution)
    mp4_369p_files.download(destinationFolder)