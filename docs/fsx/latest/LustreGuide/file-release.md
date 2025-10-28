# Releasing files

Release data repository tasks release file data from your FSx for Lustre file system
to free up space for new files. Releasing a file retains the file listing and metadata,
but removes the local copy of that file's contents. If a user or application accesses
a released file, the data is automatically and transparently loaded back onto your
file system from your linked Amazon S3 bucket.

###### Note

Release data repository tasks are not available on FSx for Lustre 2.10 file systems.

The parameters **File system paths to release**
and **Minimum duration since last access** determine which files will be released.

- **File system paths to release**: Specifies the path
  from which files will be released.
- **Minimum duration since last access**: Specifies
  the duration, in days, such that any file not accessed in that duration should be
  released. The duration since a file was last accessed is calculated by taking the
  difference between the release task create time and the last time a file was accessed
  (maximum value of `atime`, `mtime`, and `ctime`).
  Files will only be released along the file path if they have been exported to S3
  and have a duration since last access that is greater than the minimum duration since
  last access value. Providing a minimum duration since last access of `0`
  days will release files independent of their duration since last access.

###### Note

The use of wildcards to include or exclude files for release is not supported.

Release data repository tasks will only release data from files that have already
been exported to a linked S3 data repository. You can export data to S3 using either
the automatic export feature, an export data repository task, or HSM commands. To verify
that a file has been exported to your data repository, you can run the following command.
A return value of `states: (0x00000009) exists archived` indicates that the
file has successfully been exported.

```
sudo lfs hsm_state `path/to/export/file`
```

###### Note

You must run the HSM command as the root user or using `sudo`.

To release file data on a regular interval, you can schedule a recurring release
data repository task using Amazon EventBridge Scheduler. For more information, see [Getting started with EventBridge Scheduler](../../../scheduler/latest/UserGuide/getting-started.md "../../../scheduler/latest/UserGuide/getting-started.md")
in the _Amazon EventBridge Scheduler User Guide_.

###### Topics

- [Using data repository tasks to release files](release-files-task.md "release-files-task.md")
