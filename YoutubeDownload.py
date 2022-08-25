import sys
from pytube import YouTube

count_argv = len(sys.argv)

if count_argv == 1 or count_argv > 3:
    sys.exit('Error!!! \nFirst arg - link on Youtube video \nSecond arg - id_tag for download \nOnly one or two args is require')

if count_argv == 2:
    link = sys.argv[1]
    yt = YouTube(link)
    print(yt.streams)
elif count_argv == 3:
    link = sys.argv[1]
    id_tag = sys.argv[2]
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(id_tag)
    stream.download()