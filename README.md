# SyncOnSave
Sublime Text 2 plugin that automatically syncs directories with a remote server when saving.

To install, simply copy this to your Sublime Text Packages directory. For every directory that you would like to sync with a remote server, simply add an entry to "synced_dirs" in SyncOnSave.sublime-settings. It should have the following form:

```
{
    "synced_dirs": {
        "/Users/person/path/to/local/dir/": {
            "remote": "cdfuser@something.com:/path/to/remote/dir/"
        }
    }
}```

In order for this plugin to work correctly, you must first setup your SSH account to recognize your SSH key, so that you can login without having to enter your password.
