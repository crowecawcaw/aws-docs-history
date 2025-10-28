# POSIX metadata support for data

repositories

Amazon FSx for Lustre automatically transfers Portable Operating System Interface (POSIX)
metadata for files, directories, and symbolic links (symlinks) when importing and exporting
data to and from a linked data repository on Amazon S3. When you export changes in your file system
to its linked data repository, FSx for Lustre also exports POSIX metadata changes as S3 object
metadata. This means that if another FSx for Lustre file system imports the same files from S3,
the files will have the same POSIX metadata in that file system, including ownership and
permissions.

FSx for Lustre imports only S3 objects that have POSIX-compliant object keys, such as the
following.

```
mydir/
mydir/myfile1
mydir/mysubdir/
mydir/mysubdir/myfile2.txt
```

FSx for Lustre stores directories and symlinks as separate objects in the linked data
repository on S3, For directories, FSx for Lustre creates an S3 object with a key name that
ends with a slash ("/"), as follows:

- The S3 object key `mydir/` maps to the FSx for Lustre directory `mydir/`.
- The S3 object key `mydir/mysubdir/` maps to the FSx for Lustre directory `mydir/mysubdir/`.
  For symlinks, FSx for Lustre uses the following Amazon S3 schema:

- **S3 object key** – The path to the link,
  relative to the FSx for Lustre mount directory
- **S3 object data** – The target path of this
  symlink
- **S3 object metadata** – The metadata for the
  symlink
  FSx for Lustre stores POSIX metadata, including ownership, permissions, and timestamps for
  files, directories, and symbolic links, in S3 objects as follows:

- `Content-Type` – The HTTP entity header used to indicate the media
  type of the resource for web browsers.
- `x-amz-meta-file-permissions` – The file type and permissions in
  the format `<octal file type><octal permission mask>`, consistent
  with `st_mode` in the [Linux stat(2) man page](https://man7.org/linux/man-pages/man2/lstat.2.html "https://man7.org/linux/man-pages/man2/lstat.2.html").

###### Note

FSx for Lustre doesn't import or retain `setuid` information.

- `x-amz-meta-file-owner` – The owner user ID (UID) expressed as an
  integer.
- `x-amz-meta-file-group` – The group ID (GID) expressed as an
  integer.
- `x-amz-meta-file-atime` – The last-accessed time in nanoseconds
  since the beginning of the Unix epoch. Terminate the time value with `ns`;
  otherwise FSx for Lustre interprets the value as milliseconds.
- `x-amz-meta-file-mtime` – The last-modified time in nanoseconds
  since the beginning of the Unix epoch. Terminate the time value with `ns`;
  otherwise, FSx for Lustre interprets the value as milliseconds.
- `x-amz-meta-user-agent` – The user agent, ignored during FSx for Lustre
  import. During export, FSx for Lustre sets this value to `aws-fsx-lustre`.
  When importing objects from S3 that don't have associated POSIX permissions,
  the default POSIX permission that FSx for Lustre assigns to a file is `755`.
  This permission allows read and execute access for all users and write access for
  the owner of the file.

###### Note

FSx for Lustre doesn't retain any user-defined custom metadata on S3 objects.
