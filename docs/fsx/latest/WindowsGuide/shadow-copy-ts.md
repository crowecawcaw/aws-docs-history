# Troubleshooting shadow copies

There are a number of potential causes when shadow copies are missing or inaccessible,
as described in the following section.

###### Topics

- [Oldest shadow copies are missing](#w2aac22c11c37b7 "#w2aac22c11c37b7")
- [All of my shadow copies are missing](#w2aac22c11c37b9 "#w2aac22c11c37b9")
- [Cannot create Amazon FSx backups or access shadow copies on a recently restored or updated file
  system](#w2aac22c11c37c11 "#w2aac22c11c37c11")

## Oldest shadow copies are missing

The oldest shadow copies are deleted in either of these situations:

- If you have 500 shadow copies, the next shadow copy replaces the oldest shadow copy, regardless
  of the remaining allocated storage volume space for shadow copies.
- If the maximum shadow copy storage amount configured is reached, the next shadow copy replaces one or
  more of the oldest shadow copies, even if you have fewer than 500 shadow copies.

Both results are expected behavior. If you have insufficient storage allocated for
shadow copies, consider increasing the storage you have allocated.

## All of my shadow copies are missing

Having insufficient I/O performance capacity
on your file system (for example, because you're using HDD storage, because the
HDD storage has run out of burst capacity, or because the throughput capacity is
insufficient) can cause all shadow copies to be deleted by Windows Server because it
is unable to maintain the shadow copies with the available I/O performance capacity.
Consider the following recommendations to help prevent this problem:

- If you're using HDD storage, use the Amazon FSx console or Amazon FSx API to switch to using SSD storage. For more information, see [Managing your file system's storage type](managing-storage-configuration.md#managing-storage-type "managing-storage-configuration.md#managing-storage-type").
- Increase the file system's throughput capacity to a value three times
  your expected workload.
- Make sure that your file system has at least 320 MB of free space, in addition to the maximum
  shadow copy storage amount configured.
- Schedule shadow copies when you expect your file system to be idle.

For more information, see
[File system recommendations for shadow copies](shadow-copies-fsxW.md#shadow-cpy-config-recommend "shadow-copies-fsxW.md#shadow-cpy-config-recommend").

## Cannot create Amazon FSx backups or access shadow copies on a recently restored or updated file

system

This is expected behavior. Amazon FSx rebuilds the shadow-copy state on a recently restored file system and does not allow
access to shadow copies or backups while the rebuilding is still in progress.
