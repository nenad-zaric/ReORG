import os
import magic
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(source):
            if '.crdownload' in file or '.tmp' in file or '.part' in file:
                print('Waiting for download to finish...')
                time.sleep(5)
                continue
            source_file_path = source + '/' + file
            try:
                file_type = magic.from_file(source_file_path, mime=True)
                destination_file_path = source + '/' + file_type
                try:
                    os.makedirs(destination_file_path)
                except FileExistsError:
                    pass
                destination_file_path = destination_file_path + '/' + file
                os.replace(source_file_path,destination_file_path)
                print(destination_file_path+' reorganized')
            except:
                pass
            
source = os.path.join(os.path.expanduser('~'), 'Downloads')
print(source)
event_handler = CustomHandler()
observer = Observer()
observer.schedule(event_handler, source, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
