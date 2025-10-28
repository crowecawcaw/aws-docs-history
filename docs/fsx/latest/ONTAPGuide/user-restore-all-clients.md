# Restoring files from snapshots

Using the snapshots on your Amazon FSx file system, you can quickly restore
previous versions of individual files or folders.

If you use Linux and macOS clients, you can view snapshots in the `.snapshot` directory at
the root of a volume. If you use Windows clients, you can view snapshots in the `Previous Versions` tab
of Windows Explorer (when right-clicking on a file or folder).

###### To restore a file from a snapshot (Linux and macOS clients)

1. If the original file still exists and you do not want it overwritten by the file in a snapshot,
   then use your Linux or macOS client to rename the original file or move it to a different directory.
2. In the `.snapshot` directory, locate the snapshot that contains the version of the file
   that you want to restore.
3. Copy the file from the `.snapshot` directory to the directory in which the file
   originally existed.

###### To restore a file from a snapshot (Windows clients)

Users on Windows clients can restore files to previous versions using the familiar Windows File Explorer interface.

1. To restore a file, users choose the file to restore, then choose **Restore previous
   versions** from the context (right-click) menu.
2. Users can then view and restore a previous version from the **Previous Versions** list.
   Data in snapshots is read-only. If you want to make modifications to files and folders
   listed in the
   **Previous
   Versions** tab, you must save a copy of the files and folders that you want to modify
   to a writable location and make modifications to the copies.
