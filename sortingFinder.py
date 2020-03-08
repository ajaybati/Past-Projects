import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class myFinderHandler(FileSystemEventHandler):
    def on_modified(self, events):
        for file_name in os.listdir(folder_to_track):
            type = os.path.splitext(file_name)[-1].lower()
            if type == ".pdf" or type == ".png" or type==".jpg":
                new_destination = ""
                src = folder_to_track + "/" + file_name
                if type==".png" or type==".jpg":
                    new_destination += folder_destination + "/Screenshots/"+file_name
                elif type == ".pdf":
                    new_destination += folder_destination+ "/PDF/" + file_name
                os.rename(src, new_destination)
            else:
                continue



folder_to_track = "/Users/ajaybati/Desktop"
folder_destination = "/Users/ajaybati/Desktop


event_handler = myFinderHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
