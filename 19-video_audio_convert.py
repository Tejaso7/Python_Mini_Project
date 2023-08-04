import os

import pytube
from pytube import YouTube


def main():
    video_url = 'https://www.youtube.com/watch?v=W4sHmzMCo8s&ab_channel=JavedAli-Topic'

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    print(name)
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name + '.mkv'
    print(location)
    renametomp3 = path + name+ '.mp3'
    print(renametomp3)
    if os.name == 'nt':
        print('Inside')
        os.system('ren {0} {1}'.format(location, renametomp3))
    else:
        os.system('mv {0} {1}'.format(location, renametomp3))


if __name__ == '__main__':
    main()
