# Cache eviction

Files can be evicted (released) from the cache to free up space for new files. Releasing a
file retains the file listing and metadata, but removes the local copy of that file's
contents. You can't release a file if it's in use or if it hasn't been exported to a linked
data repository. There are two methods to release files:

- Automatic cache eviction releases files automatically when the cache begins
  to fill up.
- Manual release using HSM commands to release files.

###### Important

Both methods only release files that are in the archived state. You must first export the
files to your linked data repository using HSM commands, as described in [Exporting files using HSM commands](exporting-files-hsm.md "exporting-files-hsm.md").

## Automatic cache eviction

Amazon File Cache automatically manages the cache storage capacity by releasing the less
recently used files on your cache when the cache begins to fill up. Automatic cache eviction
is enabled by default when you create a cache using the File Cache console, AWS CLI, or the
AWS API.

## Releasing files using HSM commands

You can manually release individual files from your cache using the following commands:

- To release one or more files from your cache if you are the file owner:

```
lfs hsm_release `file1 file2 ...`
```

- To release one or more files from your cache if you're not the file owner:

```
sudo lfs hsm_release `file1 file2 ...`
```

The `hsm_release` command can only release regular files as defined by POSIX.
You cannot release sockets, symbolic links, block devices, character devices, or named pipes.
To identify whether a file is a regular file, use the `test -f` command on that file.
