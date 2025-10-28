# Move, rename, or delete files or directories

on the remote server

###### Topics

- [Move or rename files or directories on the remote
  SFTP server](#move-remote-file "#move-remote-file")
- [Delete files or directories on the remote SFTP
  server](#delete-remote-file "#delete-remote-file")

## Move or rename files or directories on the remote

SFTP server

You can use an SFTP connector to move or rename files and directories on a remote
SFTP server. Note that the remote server needs to support these operations for
successful processing using connectors.

Some common use cases are as follows.

- A remote server generates or receives a new file every hour, with the same
  filename but a different timestamp. To keep the main folder up to date (so
  that it contains only the latest file), you can use a connector to move
  older files to an archived folder.
- You use a connector to list all of the files in a remote directory, then
  transfer all of the files to your local storage. You can then use a
  connector to move the files to an archived folder on the remote
  server.

You must use a `StartRemoteMove` call for each file or directory you
want to process, as the command takes a single source and destination file or
directory as arguments. However, you can accelerate performance by having your
connectors create concurrent sessions with remote servers that support concurrent
sessions from the same user, and move/rename up to 5 files in parallel.

The following example moves a file on the remote SFTP server from
`/source/folder/sourceFile` to `/destination/targetFile`,
and returns a unique identifier for the operation.

```
aws transfer --connector-id c-AAAA1111BBBB2222C start-remote-move \
   --source-path /source/folder/sourceFile --target-path /destination/targetFile
```

###### Note

For the move/rename operations, Transfer Family uses the standard `SFTP
 SSH_FXP_RENAME` command to do the move/rename operation.

## Delete files or directories on the remote SFTP

server

You can use an SFTP connector to delete files or directories on a remote SFTP
server. Note that the remote server needs to support these operations for successful
processing using connectors.

###### Note

Delete operations for remote directories are only supported for empty
directories.

Some common use cases are as follows.

- You use a connector to retrieve a file from a remote SFTP server, store it
  in your Amazon S3 bucket, then encrypt it. Finally, you can use a connector to
  delete the unencrypted file on the remote server.
- You use a connector to list all of the files in a remote directory, then
  transfer all of the files to your local storage. You can then use a
  connector to delete all of the files that you transferred. You could also
  delete the remote directory if you prefer.

You must use a `StartRemoteDelete` call for each file or directory you
want to delete, as the command takes a single file or directory as an argument.
However, you can accelerate performance by having your connectors create concurrent
sessions with remote servers that support concurrent sessions from the same user,
and delete up to 5 files/directories in parallel.

The following example deletes a file on the remote SFTP server in the path
`/delete/folder/deleteFile`, and returns a unique identifier for the
operation.

```
aws transfer start-remote-delete --connector-id c-AAAA1111BBBB2222C \
   --delete-path /delete/folder/deleteFile
```

###### Note

For the delete operation, Transfer Family uses the standard `SSH_FXP_REMOVE`
command to delete a file, and `SSH_FXP_RMDIR` to delete a
directory.
