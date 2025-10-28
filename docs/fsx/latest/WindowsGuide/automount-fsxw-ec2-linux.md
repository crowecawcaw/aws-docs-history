# Automatically mount file shares on an Amazon EC2 Linux instance

You can automatically mount your FSx for Windows File Server file share to access your FSx for Windows File Server file system whenever the Amazon EC2 Linux
instance to which it's mounted reboots. To do so, add an entry to the
`/etc/fstab` file on the EC2 instance. The
`/etc/fstab` file contains information about file systems. The command
**mount -a**, which runs during instance startup, mounts the file systems
listed in the `/etc/fstab` file.

For an Amazon EC2 Linux instance that is _not_ joined to your Active Directory,
you can only mount an FSx for Windows File Server file share by using its private IP address. You can get the file
system's private IP address using the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx"),
on the **Network & security** tab, in **Preferred File Server
IP Address**.

The following procedure uses Microsoft NTLM authentication. You mount the file system as
a user that is a member of the Microsoft Active Directory domain to which the FSx for Windows File Server
file system is joined. You can retrieve the credentials for the user account from the
`creds.txt` file using the following command.

```
`$` `cat creds.txt`
`username=user1
password=Password123
domain=EXAMPLE.COM`
```

## To automatically mount a file share on an Amazon Linux

EC2 instance not joined to your Active Directory

###### To launch and configure the Amazon Linux EC2 instance

1. Launch an Amazon Linux EC2 instance using the [Amazon EC2
   console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2"). For more information, see [Launch an
   instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the _Amazon EC2 User Guide_.
2. Connect to your instance. For more information, see [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
   in the _Amazon EC2 User Guide_.
3. Run the following command to install the `cifs-utils` package. This
   package is used to mount network file systems like Amazon FSx on Linux.

```
`$` `sudo yum install cifs-utils`
```

4. Create the `/mnt/fsx` directory. This is where you will mount the Amazon FSx file system.

```
`$` `sudo mkdir /mnt/fsx`
```

5. Create the `creds.txt` credentials file in the `/home/ec2-user` directory.
6. Set the file permissions so that only you (the owner) can read the file by running
   the following command.

```
`$` sudo chmod 700 creds.txt
```

###### To automatically mount the file system

1. You automatically mount a file share not joined to your Active Directory by using its
   private IP address. You can get the file system's private IP address using the
   [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx"), on the **Network
   & security** tab, in **Preferred File Server IP Address**.
2. To automatically mount the file share using its private IP address,
   add the following line to the `/etc/fstab` file.

```
`//`file-system-IP-address`/`file_share` /mnt/fsx cifs vers=`SMB_version`,sec=ntlmsspi,cred=/home/ec2-user/creds.txt,rsize=`CIFSMaxBufSize`,wsize=`CIFSMaxBufSize`,cache=none 0 0`
```

Replace `CIFSMaxBufSize` with the largest value allowed by your kernel.
Run the following command to get this value.

```
`$` modinfo cifs | grep CIFSMaxBufSize
`parm: CIFSMaxBufSize:Network buffer size (not including header). Default: 16384 Range: 8192 to 130048 (uint)`
```

The output shows that the maximum buffer size is 130048. 3. Test the `fstab` entry by using the `mount` command with the
'fake' option in conjunction with the 'all' and 'verbose' options.

```
`$` `sudo mount -fav`
`home/ec2-user/fsx : successfully mounted`
```

4. To mount the file share, reboot the Amazon EC2 instance.
5. When the instance is available again, verify that the file system is mounted by running the following command.

```
`$` `sudo mount -l -t cifs`
`//`file-system-IP-address`/`file_share` on /mnt/fsx type cifs (rw,relatime,vers=`SMB_version`,sec=ntlmsspi,cache=`cache_code`,username=user1,domain=CORP.EXAMPLE.COM,uid=0,noforceuid,gid=0,noforcegid,addr=192.0.20.0,file_mode=0755,dir_mode=0755,soft,nounix,serverino,mapposix,rsize=1048576,wsize=1048576,echo_interval=60,actimeo=1)`
```

The line added to the `/etc/fstab` file in this procedure does the following at the given points:

    * `//`file-system-IP-address`/`file_share`` –
     Specifies the IP address and share of the Amazon FSx file system you're mounting.
    * `/mnt/fsx` – Specifies the mount point for the Amazon FSx file
     system on your EC2 instance.
    * `cifs vers=`SMB_version`` – Specifies the type of file system as
     CIFS and the SMB protocol version. Amazon FSx for Windows File Server supports SMB versions 2.0 through 3.1.1.
    * `sec=ntlmsspi` – Specifies using NT LAN Manager Security Support Provider
     Interface to facilitate NTLM challenge-response authentication.
    * `cache=`cache_mode`` – Sets the cache mode. This option
     for CIFS cache can impact performance, and you should test which settings work best (and review
     Linux documentation) for your kernel and workload. Options `strict` and `none`
     are recommended, because `loose` can cause data inconsistency due to the looser protocol
     semantics.
    * `cred=/home/ec2-user/creds.txt` – Specifies where to get the user credentials.
    * `_netdev` – Tells the operating system that the
     file system resides on a device that requires network access. Using this option
     prevents the instance from mounting the file system until the network service is
     enabled on the client.
    * `0` – Indicates that the file system should be backed up by
     `dump`, if it's a nonzero value. For Amazon FSx, this value should
     be `0`.
    * `0` – Specifies the order in which `fsck` checks file systems at
     boot. For Amazon FSx file systems, this value should be `0` to indicate
     that `fsck` shouldn't run at start up.
