import os
import magic
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(source):
            if '.crdownload' in file:
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
            except IsADirectoryError:
                pass
            
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

source = get_download_path()
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
