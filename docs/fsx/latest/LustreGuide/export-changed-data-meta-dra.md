# Exporting changes to the data

repository

You can export changes to data and POSIX metadata changes from your FSx for Lustre file
system to a linked data repository. Associated POSIX metadata includes ownership, permissions,
and timestamps.

To export changes from the file system, use one of the following methods.

- Configure your file system to automatically export new, changed, or deleted files
  to your linked data repository. For more information, see [Automatically export updates to your S3
  bucket](autoexport-data-repo-dra.md "autoexport-data-repo-dra.md").
- Use an on-demand export data repository task. For more information, see [Using data repository tasks to export changes](export-data-repo-task-dra.md "export-data-repo-task-dra.md")
  Automatic export and export data repository tasks cannot run at the same time.

###### Important

Automatic export will not synchronize the following metadata operations on your
file system with S3 if the corresponding objects are stored in S3 Glacier Flexible Retrieval:

- chmod
- chown
- rename
  When you turn on automatic export for a data repository association, your file system
  automatically exports file data and metadata changes as files are created, modified, or
  deleted. When you export files or directories using an export data repository task, your
  file system exports only data files and metadata that were created or modified since the
  last export.

Both automatic export and export data repository tasks export POSIX metadata.
For more information, see [POSIX metadata support for data
repositories](posix-metadata-support.md "posix-metadata-support.md").

###### Important

- To ensure that FSx for Lustre can export your data to your S3 bucket,
  it must be stored in a UTF-8 compatible format.
- S3 object keys have a maximum length of 1,024 bytes. FSx for Lustre
  will not export files whose corresponding S3 object key would be longer than
  1,024 bytes.

###### Note

All objects created by automatic export and export data repository tasks are written
using the S3 Standard storage class.

###### Topics

- [Automatically export updates to your S3
  bucket](autoexport-data-repo-dra.md "autoexport-data-repo-dra.md")
- [Using data repository tasks to export changes](export-data-repo-task-dra.md "export-data-repo-task-dra.md")
- [Exporting files using HSM
  commands](exporting-files-hsm.md "exporting-files-hsm.md")
