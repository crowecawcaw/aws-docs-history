

# Mounting volumes to access data
<a name="mounting-volumes"></a>

The primary way to access data on your file system is through mounting individual volumes from an Amazon EC2 instance. This section provides details on how to configure your file system to automatically remount volumes on an Amazon EC2 instance when the instance reboots, and tips for mounting a volume to maximize your file systems overall performance. For detailed instructions on how to mount a volume to a Linux, macOS, or Windows client, see [Step 2: Mount your file system from an Amazon EC2 instance](getting-started.md#getting-started-step2).

**Topics**
+ [Automatically mounting file systems on reboot for Linux instances](#mount-fs-auto-mount-update-fstab)
+ [Additional mounting options to maximize file system performance](#additional-mounting-options)

## Automatically mounting file systems on reboot for Linux instances
<a name="mount-fs-auto-mount-update-fstab"></a>

You can use the `/etc/fstab` file, which contains information about your file systems, to automatically remount your volumes on an Amazon EC2 Linux instance when the instance reboots. The command `mount -a`, which runs during instance start-up, mounts the file systems listed in `/etc/fstab`.

**Note**  
FSx for OpenZFS file systems do not support automatic mounting using `/etc/fstab` on Amazon EC2 Mac instances.

**To automatically mount your file system on reboot**

1. Connect to your EC2 instance:
   + To connect to your instance from a computer running macOS or Linux, specify the .pem file for your SSH command. To do this, use the `-i` option and the path to your private key.
   + To connect to your instance from a computer running Windows, you can use either MindTerm or PuTTY. To use PuTTY, install it and convert the .pem file to a .ppk file.

   For more information, see the following topics in the *Amazon EC2 User Guide*:
   +  [Connecting to your Linux instance using SSH](AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html)
   +  [Connecting to your Linux instance from Windows using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) 

1. Create a local directory that will be used to mount the FSx for OpenZFS volume.

   ```
   sudo mkdir /fsx
   ```

1. Open the `/etc/fstab` file in an editor of your choice.

1. Add the following line to the `/etc/fstab` file. Insert a tab character between each parameter. It should appear as one line with no line breaks.

   ```
   {{filesystem-dns-name}}:{{volume-path}} /{{localpath}} nfs vers={{nfs-version}},defaults 0 0
   ```

   The last three parameters indicate NFS options (which we set to default), dumping of file system and filesystem check (these are typically not used so we set them to 0).

1. Save the changes to the file.

1. Test the fstab entry by using the mount command with the `fake` `all` `verbose` options.

   ```
   sudo mount -fav
                           {{fs-dns-name}}:/{{vol_path}}      : successfully mounted
   ```

   Now mount the volume using the following command. The next time the EC2 instance restarts, the volume will be mounted automatically.

   ```
   sudo mount /{{localpath}}
   sudo mount {{filessystem-dns-name}}:/{{volume-path}}
   ```

Your EC2 instance is now configured to mount the FSx for OpenZFS volume whenever it restarts.

## Additional mounting options to maximize file system performance
<a name="additional-mounting-options"></a>

You can also include the following options when mounting a volume to improve your file system's overall performance.
+ `rsize=1048576` – Sets the maximum number of bytes of data that the NFS client can receive for each network READ request. This value applies when reading data from a file on an FSx for OpenZFS volume. We recommend that you use the largest size possible, 1048576. Due to lower memory capacity on file systems with 64 MBps and 128 MBps of provisioned throughput, these file systems will only accept a maximum rsize of 262144 and 524288 bytes, respectively.
+ `wsize=1048576` – Sets the maximum number of bytes of data that the NFS client can send for each network WRITE request. This value applies when writing data to a file on an FSx for OpenZFS volume. We recommend that you use the largest size possible, 1048576. Due to lower memory capacity on file systems with 64 MBps and 128 MBps of provisioned throughput, these file systems will only accept a maximum wsize of 262144 and 524288 bytes, respectively.
+ `timeo=600` – Sets the timeout value that the NFS client uses to wait for a response before it retries an NFS request to 600 deciseconds (60 seconds).
+ `_netdev` – When present in `/etc/fstab`, prevents the client from attempting to mount the FSx for OpenZFS volume until the network has been enabled.

The following example uses sample values.

```
sudo mount -t nfs -o rsize=1048576,wsize=1048576,timeo=600 fs-01234567890abcdef1.fsx.us-east-1.amazonaws.com:/fsx/vol1 /fsx
```