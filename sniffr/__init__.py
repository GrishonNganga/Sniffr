#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Grishon Ng'ang'a grishon.nganga01@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
WARNING! Still in its initial stages and may contain a lot of bugs. Use with caution.

Contribute -> 

'''

'''
Micro module uses watchdog library to monitor specified folder for file changes
and moves them to another folder specified.

'''

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import sys
import shutil
import os

class Sniffr(FileSystemEventHandler):

    def __init__(self, path_from, path_to):
        '''
        Monitor Folder for file changes and move the contents to another location.

        Usage:
        sniffer = Sniffer('folder-to-watch/', 'folder/to/move/files/to')
        sniffer.run()

        '''
        self.__path = path_from
        self.__event_handler = FileCreatedHandler(path_to)
        self.__event_observer = Observer()
        self.__keep_running = True
    
    def run(self):

        '''
        Call this method to start the sniffer.
        '''
        self.start()
        try:
            while self.__keep_running:
                time.sleep(1)
        except:
            pass
        

    def start(self):
        self.__event_observer.schedule(self.__event_handler, self.__path, recursive = False)
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()


class FileCreatedHandler(FileSystemEventHandler):

    '''
    Extends FileSystemEventHandler and override specific functionalities.

    1. on_creates() -> For file created evented on the specific folder.
    '''

    def __init__(self, path):
        self.__copy_to = path
        super().__init__()
    
    def on_created(self, event):

        '''
        Has all the functionality to move files to another location (Location specified on Sniffer())
        '''

        try:
            if os.path.isdir(self.__copy_to):
                shutil.copy(event.src_path, self.__copy_to)
                os.remove(event.src_path)
            else:
                os.mkdir(self.__copy_to)
                shutil.copy(event.src_path, self.__copy_to)
                os.remove(event.src_path)
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass
            
