# Limitations

- For JupyterLab and Code Editor, large files over 15 MB cannot be directly uploaded to the shared folder. To upload large files,
  first upload them to any other folder (such as your local storage), then copy or move to the shared folder.
- When uploading files using `putObject` API to non-existent folder paths in shared storage,
  folders created indirectly may display incorrect timestamps - January 1, 1970 in JupyterLab's file browser. In the
  CodeEditor, the file metadata also shows the time stamp as January 1, 1970.
