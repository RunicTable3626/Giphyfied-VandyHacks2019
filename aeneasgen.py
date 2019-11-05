#!/usr/bin/env python
# coding=utf-8

from aeneas.executetask import ExecuteTask
from aeneas.task import Task
def sync_map_generator(song_name):
# create Task object
    print('Creating sync map file...')
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = "C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/Songs/" + song_name +".wav"
    task.text_file_path_absolute = "C:/Users/jaysh/Desktop/VandyHacks/Hack Prototype/Lyrics/" + song_name +".txt"
    task.sync_map_file_path_absolute = u"output/"+ song_name + ".json"

    # process Task
    ExecuteTask(task).execute()

    # output sync map to file
    task.output_sync_map_file()
    print('Created sync map file')

