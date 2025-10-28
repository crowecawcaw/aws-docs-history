# Mounting from an Amazon Elastic Compute Cloud

instance

You can mount your file system from an Amazon EC2 instance.

###### To mount your file system from Amazon EC2

1. Connect to your Amazon EC2 instance.
2. Make a directory on your FSx for Lustre file system for the mount point with the following command.

```
$ sudo mkdir -p /fsx
```

3. Mount the Amazon FSx for Lustre file system to the directory that you created. Use the following
   command and replace the following items:
   - Replace `file_system_dns_name` with the actual file
     system's DNS name.
   - Replace `mountname` with the file system's mount name.
     This mount name is returned in the `CreateFileSystem` API operation
     response. It's also returned in the response of the
     **describe-file-systems** AWS CLI command, and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.

```
sudo mount -t lustre -o relatime,flock `file_system_dns_name`@tcp:/`mountname` /fsx
```

This command mounts your file system with two options, `-o relatime` and
`flock`:

    * `relatime` – While the `atime` option maintains
     `atime` (inode access times) data for each time a file is accessed, the
     `relatime` option also maintains `atime` data, but not for
     each time that a file is accessed. With the `relatime` option enabled,
     `atime` data is written to disk only if the file has been modified since
     the `atime` data was last updated (`mtime`), or if the file was
     last accessed more than a certain amount of time ago (6 hours by default).
     Using either the `relatime` or `atime` option will optimize the
     [file release](file-release.md "file-release.md") processes.


    ###### Note

    If your workload requires precise access time accuracy, you can mount with the
     `atime` mount option. However, doing so can impact workload performance
     by increasing the network traffic required to maintain precise access time values.

    If your workload does not require metadata access time, using the `noatime`
     mount option to disable updates to access time can provide a performance gain. Be aware that
     `atime` focused processes like file release or releasing data validity will be
     inaccurate in their release.
    * `flock` – Enables file locking for your file system. If you
     don't want file locking enabled, use the `mount` command without
     `flock`.

4. Verify that the mount command was successful by listing the contents of the directory to which you mounted the file system, /mnt/fsx by using the following
   command.

```
`$` `ls /fsx`
import-path  lustre
$
```

You can also use the `df` command, following.

```
`$` df
Filesystem                    1K-blocks    Used  Available Use% Mounted on
devtmpfs                        1001808       0    1001808   0% /dev
tmpfs                           1019760       0    1019760   0% /dev/shm
tmpfs                           1019760     392    1019368   1% /run
tmpfs                           1019760       0    1019760   0% /sys/fs/cgroup
/dev/xvda1                      8376300 1263180    7113120  16% /
123.456.789.0@tcp:/`mountname` 3547698816   13824 3547678848   1% /fsx
tmpfs                            203956       0     203956   0% /run/user/1000

```

The results show the Amazon FSx file system mounted on /fsx.
