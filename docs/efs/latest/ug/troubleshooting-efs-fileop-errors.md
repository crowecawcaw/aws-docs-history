# Troubleshooting file operation

errors related to quotas

When you access EFS file systems, certain limits on the files in the file system
apply. Exceeding these limits causes file operation errors. For more information about file-based
limits in Amazon EFS, see [Amazon EFS quotas](limits.md "limits.md").

Following, you can find some common file
operation errors and the limits associated with each error.

###### Topics

- [Checking for open files and file locks](#check-open-files-locks "#check-open-files-locks")
- [Command fails with “Disk quota exceeded”
  error](#diskquotaerror "#diskquotaerror")
- [Command fails with "I/O error"](#ioerror "#ioerror")
- [Command fails with "File name is too long"
  error](#filenametoolong "#filenametoolong")
- [Command fails with "File not found" error](#filenotfound "#filenotfound")
- [Command fails with "Too many links" error](#hardlinkerror "#hardlinkerror")
- [Command fails with "File too large" error](#filesizeerror "#filesizeerror")

## Checking for open files and file locks

To troubleshoot file operation errors, you can check whether your client system has reached limits by examining open files and file locks on the EFS mount point:

- **Check open files** – Use your operating system's tools to list open files on the EFS mount path. This helps identify if you're approaching the open file limit. For example, on Linux you can use:

```
lsof <efs-mount-path>
```

- **Check file locks** – Use your system's lock monitoring tools to list files with locks on the EFS mount path. This helps identify if lock limits are being reached. For example, on Linux you can use:

```
lslocks | grep <efs-mount-path>
```

These commands will show you the current usage against EFS limits, helping you determine if file operation errors are related to reaching system or service limits.

## Command fails with “Disk quota exceeded”

error

Amazon EFS doesn't currently support user disk quotas. This error can occur if any of
the following limits have been exceeded:

- Up to 65,536 active users can have files open at the same time. A user
  account that is logged in multiple times counts as one active user.
- Up to 65,536 files can be open at once for an instance. Listing directory
  contents doesn't count as opening a file.
- Each unique mount on the client can acquire up to a total of 65,536 locks
  per connection.

###### Action to take

If you encounter this issue, you can resolve it by identifying which of the
preceding limits you are exceeding, and then making changes to meet that
limit. For more information, see [Quotas for NFS clients](limits.md#limits-client-specific "limits.md#limits-client-specific"). To check your current usage, see [Checking for open files and file locks](#check-open-files-locks "#check-open-files-locks").

## Command fails with "I/O error"

This error occurs when you encounter one of the following issues:

- More than 65,536 active user accounts for each instance have files open at
  once.

###### Action to take

If you encounter this issue, you can resolve it by meeting the
supported limit of open files on your instances. To do so, reduce the
number of active users that have files from your Amazon EFS file system open
simultaneously on your instances. To check your current usage, see [Checking for open files and file locks](#check-open-files-locks "#check-open-files-locks").

- The AWS KMS key encrypting your file system was deleted.

###### Action to take

If you encounter this issue, you can no longer decrypt the data that
was encrypted under that key, which means that data becomes
unrecoverable.

## Command fails with "File name is too long"

error

This error occurs when the size of a file name or its symbolic link (symlink) is
too long. File names have the following limits:

- A name can be up to 255 bytes long.
- A symlink can be up to 4080 bytes in size.

###### Action to take

If you encounter this issue, you can resolve it by reducing the size of your
file name or symlink length to meet the supported limits.

## Command fails with "File not found" error

This error occurs because some older 32-bit versions of Oracle E-Business suite use 32-bit
file I/O interfaces, and EFS uses 64-bit inode numbers. System calls
that may fail include `stat()` and `readdir()`.

###### Action to take

If you encounter this error, you can resolve it by using the **nfs.enable_ino64=0 kernel** boot option.
This option compresses the 64-bit EFS inode numbers
to 32 bits. Kernel boot options are handled differently for different Linux distributions.
On Amazon Linux, turn on this option by adding `nfs.enable_ino64=0 kernel` to the
`GRUB_CMDLINE_LINUX_DEFAULT` variable in `/etc/default/grub`.
Please consult your distribution for specific documentation on how to turn on kernel boot
options.

## Command fails with "Too many links" error

This error occurs when there are too many hard links to a file. You can have up to
177 hard links in a file.

###### Action to take

If you encounter this issue, you can resolve it by reducing the number of hard
links to a file to meet the supported limit.

## Command fails with "File too large" error

This error occurs when a file is too large. A single file can be up to
52,673,613,135,872 bytes (47.9 TiB) in size.

###### Action to take

If you encounter this issue, you can resolve it by reducing the size of a file
to meet the supported limit.
