import sublime, sublime_plugin
import subprocess
import threading

DEBUG = False

# Base rsync command template: rsync -arv <local> <remote>
base_cmd = "rsync -arv {0} {1}"

class SyncOnSaveCommand(sublime_plugin.EventListener):
    def on_post_save(self, view):
        """ Sync directory containing the current directory after saving. """
        synced_dirs = sublime.load_settings("SyncOnSave.sublime-settings").get("synced_dirs")

        file_name = view.file_name()

        for synced_dir in synced_dirs.keys():
            if file_name.startswith(synced_dir):
                # Current file is in a synced directory.
                remote = synced_dirs[synced_dir]["remote"]
                cmd = base_cmd.format(synced_dir, remote)

                if DEBUG:
                    print cmd

                # Execute rsync in a new thread, to avoid noticeable network lag on save.
                thread = threading.Thread(target=subprocess.call, args=(cmd,), kwargs={"shell": True})
                thread.daemon = True
                thread.start()


