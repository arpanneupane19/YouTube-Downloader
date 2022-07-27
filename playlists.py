from pytube import YouTube
import os
import subprocess


class Downloader:
    def __init__(self, videos):
        self.videos = videos

    def download(self):
        count = 0
        for video in self.videos:
            vid = YouTube(str(video))
            stream = vid.streams.filter(only_audio=True).first()
            downloaded_video = stream.download()
            fname, ext = os.path.splitext(downloaded_video)
            subprocess.run(['ffmpeg', '-i', os.path.join(os.getcwd(),
                                                         fname+ext), os.path.join(os.getcwd(), fname+'.mp3')])
            os.remove(fname+ext)
            count += 1
            if count == 1:
                print(f"{count} video completed...")
            else:
                print(f"{count} videos completed...")

        print("Downloads complete!")


downloader = Downloader([
    'YOUTUBE LINK HERE',

])
downloader.download()
