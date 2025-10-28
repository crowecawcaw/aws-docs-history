# Mounting volumes on Linux clients

We recommend that the volumes you want to mount with Linux clients have a
security style setting of `UNIX` or `mixed`. For more
information, see [Managing FSx for ONTAP volumes](managing-volumes.md "managing-volumes.md").

###### Note

By default, FSx for ONTAP NFS mounts are `hard` mounts. To ensure a
smooth failover in the event that one occurs, we recommend that you use the
default `hard` mount option.

###### To mount an ONTAP volume on a Linux client

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Create or select an Amazon EC2 instance running Amazon Linux 2 that is in the same VPC
   as the file system.

For more information on launching an EC2 Linux instance, see [Step 1: Launch an instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance") in the
_Amazon EC2 User Guide_. 3. Connect to your Amazon EC2 Linux instance. For more information, see [Connect to your
Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the
_Amazon EC2 User Guide_. 4. Open a terminal on your EC2 instance using secure shell (SSH), and log in
with the appropriate credentials. 5. Create a directory on the EC2 instance for mounting the SVM volume as
follows:

```
sudo mkdir /fsx
```

6. Mount the volume to the directory you just created using the following
   command:

```
sudo mount -t nfs `svm-dns-name`:/`volume-junction-path` /fsx
```

The following example uses sample values.

```
sudo mount -t nfs svm-01234567890abdef0.fs-01234567890abcdef1.fsx.us-east-1.amazonaws.com:/vol1 /fsx
```

You can also use the SVM's IP address instead of its DNS name. We recommend using the DNS name to mount clients to second-generation file
systems because it helps ensure that your clients are balanced across your file system's high-availability (HA) pairs.

```
sudo mount -t nfs 198.51.100.1:/vol1 /fsx
```

###### Note

For second-generation file systems, the parallel NFS (pNFS) protocol is enabled by default and is used by default for any clients mounting
volumes with NFS v4.1 or greater.

## Using /etc/fstab to mount

automatically on instance reboot

To automatically remount your FSx for ONTAP volume when an Amazon EC2 Linux instance
reboots, use the `/etc/fstab` file. The
`/etc/fstab` file contains information about file
systems. The command `mount -a`, which runs during instance start-up,
mounts the file systems listed in `/etc/fstab`.

###### Note

FSx for ONTAP file systems do not support automatic mounting using
`/etc/fstab` on Amazon EC2 Mac instances.

###### Note

Before you can update the `/etc/fstab` file of your EC2
instance, make sure that you already created your FSx for ONTAP file system.
For more information, see [Creating file systems](creating-file-systems.md "creating-file-systems.md").

###### To update the /etc/fstab file on your EC2 instance

1.  Connect to your EC2 instance:

        * To connect to your instance from a computer running macOS or
         Linux, specify the .pem file for your SSH command. To do this,
         use the `-i` option and the path to your private
         key.
        * To connect to your instance from a computer running Windows,
         you can either use MindTerm or PuTTY. To use PuTTY, install it
         and convert the .pem file to a .ppk file.

    For more information, see the following topics in the
    _Amazon EC2 User Guide_:

        * [Connecting to your Linux instance using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md")
        * [Connecting to your Linux
         instance from Windows using PuTTY](../../../AWSEC2/latest/UserGuide/putty.md "../../../AWSEC2/latest/UserGuide/putty.md")

2.  Create a local directory that will be used to mount the SVM
    volume.

```
sudo mkdir /fsx
```

3. Open the `/etc/fstab` file in an editor of your
   choice.
4. Add the following line to the `/etc/fstab` file.
   Insert a tab character between each parameter. It should appear as one
   line with no line breaks.

```
`svm-dns-name`:`volume-junction-path` /fsx nfs nfsvers=`version`,defaults 0 0
```

You can also use the IP address of volume's SVM. The last three
parameters indicate NFS options (which we set to default), dumping of
file system and filesystem check (these are typically not used so we set
them to 0). 5. Save the changes to the file. 6. Now mount the file share using the following command. The next time
the system starts, the folder will be mounted automatically.

```
sudo mount /fsx
sudo mount `svm-dns-name`:`volume-junction-path`
```

Your EC2 instance is now configured to mount the ONTAP volume whenever it
restarts.
