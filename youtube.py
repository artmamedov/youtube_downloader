from pytube import YouTube
import os

def download_url(video_url):
    yt = YouTube(video_url)
    ys = yt.streams.filter(only_audio=True).first()
    dir = os.getcwd()
    if not os.path.exists(dir+'/downloads/'):
        os.mkdir(dir+'/downloads/')
    print("Downloading...")
    output = ys.download(dir+'/downloads/')
    print(dir+'downloads/')
    # save the file
    base, ext = os.path.splitext(output)
    new_file = base + '.mp3'
    os.rename(output, new_file)
    # result of success
    print(yt.title + " has been successfully downloaded.")

if __name__=='__main__':
    video_url = "https://www.youtube.com/watch?v=M9N11omUlNM"
    download_url(video_url)
