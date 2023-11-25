from aeneas.executetask import ExecuteTask
from aeneas.task import Task

# create Task object
config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
task = Task(config_string=config_string)
task.audio_file_path_absolute = "audio.mp3"
task.text_file_path_absolute = "page.xhtml"
task.sync_map_file_path_absolute = "syncmap.json"

# process Task
ExecuteTask(task).execute()

# output sync map to file
task.output_sync_map_file()
