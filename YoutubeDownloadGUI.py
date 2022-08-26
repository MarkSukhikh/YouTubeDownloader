import sys
from pytube import YouTube
import dearpygui.dearpygui as dpg

link = ''

def check_streams_callback(sender, data):
    global link, new_checkbox
    yt = YouTube(link)
    streams = yt.streams
    for i in streams:
        stream_str = str(i)
        id_tag = stream_str[15: 18]
        id_tag = id_tag.replace('"','')
        new_checkbox = dpg.add_checkbox(label=i, before="download_button", tag=id_tag)
        


def save_link_callback(sender, data):
    global link
    link = str(data)

def download_stream_callback(sender, data):
    pass

dpg.create_context()
dpg.create_viewport(title='Youtube downloader', width=600, height=300)

with dpg.window(tag="pw", label="Youtube downloader"):
    dpg.add_text("Insert link below, check the streams and download!")
    dpg.add_text("Paste Youtube link here:")
    dpg.add_input_text(default_value="https://", callback=save_link_callback)
    dpg.add_button(label="Click here to check the streams", callback=check_streams_callback)
    dpg.add_button(label="Download stream", callback=download_stream_callback, tag="download_button", show=False)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("pw", True)
dpg.start_dearpygui()
dpg.destroy_context()




# count_argv = len(sys.argv)

# if count_argv == 1 or count_argv > 3:
#     sys.exit('Error!!! \nFirst arg - link on Youtube video \nSecond arg - id_tag for download \nOnly one or two args is require')

# if count_argv == 2:
#     link = sys.argv[1]
#     yt = YouTube(link)
#     print(yt.streams)
# elif count_argv == 3:
#     link = sys.argv[1]
#     id_tag = sys.argv[2]
#     yt = YouTube(link)
#     stream = yt.streams.get_by_itag(id_tag)
#     stream.download()