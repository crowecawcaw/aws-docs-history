# Mounting a file share on an Amazon EC2 Linux instance

You can mount an FSx for Windows File Server file share on an Amazon EC2 Linux instance that is either
joined to your Active Directory or not joined to access your FSx for Windows File Server file system.

###### Note

- The following commands specify parameters such as SMB protocol, caching, and read
  and write buffer size as examples only. Parameter choices for the Linux `cifs` command,
  as well as the Linux kernel version used, can impact throughput and latency for network operations
  between the client and the Amazon FSx file system. For more information, see `cifs`
  documentation for the Linux environment you are using.
- Linux clients do not support automatic DNS-based failover. For more information, see
  [Failover experience on Linux clients](high-availability-multiAZ.md#linux-failover "high-availability-multiAZ.md#linux-failover").

1. If you don't already have a running EC2 Linux instance joined to your Microsoft Active Directory, see [Manually join a Linux
   instance](../../../directoryservice/latest/admin-guide/join_linux_instance.md "../../../directoryservice/latest/admin-guide/join_linux_instance.md") in the _AWS Directory Service Administration Guide_ for the instructions to do so.
2. Connect to your EC2 Linux instance. For more information, see [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
   in the _Amazon EC2 User Guide_.
3. Run the following command to install the `cifs-utils` package. This
   package is used to mount network file systems like Amazon FSx on Linux.

```
`$` `sudo yum install cifs-utils`
```

4. Create the mount point directory `/mnt/fsx`. This is where
   you will mount the Amazon FSx file system.

```
`$` `sudo mkdir -p /mnt/fsx`
```

5. Authenticate with kerberos using the following command.

```
`$` `kinit`
```

6. Mount the file share with the following command.

```
`$` `sudo mount -t cifs //`file_system_dns_name`/`file_share` `mount_point` --verbose -o vers=`SMB_version`,sec=krb5,cruid=`ad_user`,rsize=`CIFSMaxBufSize`,wsize=`CIFSMaxBufSize`,cache=none`,ip=`preferred-file-server-Ip`
```

You can find the DNS name on the [Amazon FSx
console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx") by choosing **Windows File Server**,
**Network & security**. Or, you can find them in the response
of `CreateFileSystem` or `DescribeFileSystems` API
operation.

    * For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the
     following.



    ```
    fs-0123456789abcdef0.`ad-domain`.com
    ```
    * For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file
     system, the DNS name looks like the following.



    ```
    amznfsxaa11bb22.`ad-domain`.com
    ```

Replace `CIFSMaxBufSize` with the largest value allowed by your kernel.
Run the following command to get this value.

```
`$` modinfo cifs | grep CIFSMaxBufSize
`parm: CIFSMaxBufSize:Network buffer size (not including header). Default: 16384 Range: 8192 to 130048 (uint)`
```

The output shows that the maximum buffer size is 130048. 7. Verify that the file system is mounted by running the following command, which
returns only file systems of the Common Internet File System (CIFS) type.

```
$ `mount -l -t cifs`
`//fs-0123456789abcdef0/share on /mnt/fsx type cifs (rw,relatime,vers=`SMB_version`,sec=krb5,cache=`cache_mode`,username=user1@CORP.NETWORK.COM,uid=0,noforceuid,gid=0,noforcegid,addr=192.0.2.0,file_mode=0755,dir_mode=0755,soft,nounix,serverino,mapposix,rsize=1048576,wsize=1048576,echo_interval=60,actimeo=1)`
```

The mount command used in this procedure does the following at the given points:

- `//`file_system_dns_name`/`file_share`` – Specifies the DNS name and share of the
  file system to mount.
- `mount_point` – The directory on the EC2 instance
  that you are mounting the file system to.
- `-t cifs vers=`SMB_version`` – Specifies the type of file system as CIFS
  and the SMB protocol version. Amazon FSx for Windows File Server supports SMB versions 2.0 through 3.1.1.
- `sec=krb5` – Specifies to use Kerberos version 5 for authentication.
- `cache=`cache_mode``– Sets the cache mode. This option
for CIFS cache can impact performance, and you should test which settings work best (and review
Linux documentation) for your kernel and workload. Options`strict`and`none`are recommended, because`loose` can cause data inconsistency due to the looser protocol
  semantics.
- `cruid=`ad_user`` – Sets the uid of the
  owner of the credentials cache to the AD directory administrator.
- `/mnt/fsx` – Specifies the mount
  point for the Amazon FSx file share on your EC2 instance.
- `rsize=`CIFSMaxBufSize`,wsize=`CIFSMaxBufSize`– Specifies the read
and write buffer size as the maximum allowed by the CIFS protocol. Replace`CIFSMaxBufSize``with the largest value allowed by your kernel. 
Determine the`CIFSMaxBufSize` by running the following command.

```
`$` modinfo cifs | grep CIFSMaxBufSize
`parm: CIFSMaxBufSize:Network buffer size (not including header). Default: 16384 Range: 8192 to 130048 (uint)`
```

The output shows that the maximum buffer size is 130048.

- `ip=`preferred-file-server-Ip`` – Sets
  the destination IP address to that of the file system's preferred file
  server.

You can retrieve the file system's preferred file server IP address as follows:

    + Using the Amazon FSx console, on the **Network & security** tab of the
     **File system details** page.
    + In the response of the `describe-file-systems` CLI command or the
     equivalent [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API command.

The following procedure mounts an Amazon FSx file share to an Amazon EC2 Linux instance that is
not joined to your Active Directory (AD). For an EC2 Linux instance that is not joined to your AD, you can only mount an
FSx for Windows File Server file share by using its private IP address. You can get the file system's
private IP address using the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx"), on
the **Network & security** tab, in **Preferred File Server IP Address**.

This example uses NTLM authentication. To do
this, you mount the file system as a user that is a member of the Microsoft Active
Directory domain that the FSx for Windows File Server file system is joined to. The credentials for the
user account are provided in a text file that you create on your EC2 instance,
`creds.txt`. This file contains the user name, password, and domain
for the user.

```
`$` `cat creds.txt`
`username=user1
password=Password123
domain=EXAMPLE.COM`
```

###### To launch and configure the Amazon Linux EC2 instance

1. Launch an Amazon Linux EC2 instance using the [Amazon EC2
   console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2"). For more information, see [Launch an
   instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_.
2. Connect to your Amazon Linux EC2 instance. For more information, see [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
   in the _Amazon EC2 User Guide_.
3. Run the following command to install the `cifs-utils` package. This
   package is used to mount network file systems like Amazon FSx on Linux.

```
`$` `sudo yum install cifs-utils`
```

4. Create the mount point `/mnt/fsxx` where you plan to mount
   the Amazon FSx file system.

```
`$` `sudo mkdir -p /mnt/fsx`
```

5. Create the `creds.txt` credentials file in the
   `/home/ec2-user` directory, using the format shown
   previously.
6. Set the `creds.txt` file permissions so that only you (the
   owner) can read and write to the file by running the following command.

```
`$` `chmod 700 creds.txt`
```

###### To mount the file system

1. You mount a file share not joined to your Active Directory by using its private IP address.
   You can get the file system's private IP address using the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx"), on the **Network &
   security** tab, in the **Preferred File Server IP Address**.
2. Mount the file system using the following command:

```
`$` `sudo mount -t cifs //`file-system-IP-address`/`file_share` /mnt/fsx --verbose -o vers=`SMB_version`,sec=ntlmsspi,cred=/home/ec2-user/creds.txt,rsize=`CIFSMaxBufSize`,wsize=`CIFSMaxBufSize`,cache=none`
```

Replace `CIFSMaxBufSize` with the largest value allowed by your kernel.
Run the following command to get this value.

```
`$` modinfo cifs | grep CIFSMaxBufSize
`parm: CIFSMaxBufSize:Network buffer size (not including header). Default: 16384 Range: 8192 to 130048 (uint)`
```

The output shows that the maximum buffer size is 130048. 3. Verify that the file system is mounted by running the following command, which
returns only CIFS file systems.

```
`$` `mount -l -t cifs`
`//`file-system-IP-address`/`file_share` on /mnt/fsx type cifs (rw,relatime,vers=`SMB_version`,sec=ntlmsspi,cache=`cache_mode`,username=user1,domain=CORP.EXAMPLE.COM,uid=0,noforceuid,gid=0,noforcegid,addr=192.0.2.0,file_mode=0755,dir_mode=0755,soft,nounix,serverino,mapposix,rsize=1048576,wsize=1048576,echo_interval=60,actimeo=1)`
```

The mount command used in this procedure does the following at the given points:

- `//`file-system-IP-address`/`file_share`` – Specifies the IP address and share of the
  file system you're mounting.
- `-t cifs vers=`SMB_version`` – Specifies the type of file system as CIFS
  and the SMB protocol version. Amazon FSx for Windows File Server supports SMB versions 2.0 through 3.1.1.
- `sec=ntlmsspi` – Specifies to use NT LAN Manager Security Support Provider
  Interface (NTLMSSPI) for authentication.
- `cache=`cache_mode``– Sets the cache mode. This option
for CIFS cache can impact performance, and you should test which settings work best (and review
Linux documentation) for your kernel and workload. Options`strict`and`none`are recommended, because`loose` can cause data inconsistency due to the looser protocol
  semantics.
- `cred=/home/ec2-user/creds.txt` – Specifies where to get the user credentials.
- `/mnt/fsx` – Specifies the mount
  point for the Amazon FSx file share on your EC2 instance.
- `rsize=`CIFSMaxBufSize`,wsize=`CIFSMaxBufSize`– Specifies the read
and write buffer size as the maximum allowed by the CIFS protocol. Replace`CIFSMaxBufSize``with the largest value allowed by your kernel. 
Determine the`CIFSMaxBufSize` by running the following command.

```
`$` modinfo cifs | grep CIFSMaxBufSize
`parm: CIFSMaxBufSize:Network buffer size (not including header). Default: 16384 Range: 8192 to 130048 (uint)`
```
