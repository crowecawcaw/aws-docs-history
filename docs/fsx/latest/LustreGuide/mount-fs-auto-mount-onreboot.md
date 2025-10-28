# Mounting your Amazon FSx file system

automatically

You can update the `/etc/fstab` file in your Amazon EC2 instance after you connect to
the instance for the first time so that it mounts your Amazon FSx file system each time it reboots.

## Using /etc/fstab to

mount FSx for Lustre automatically

To automatically mount your Amazon FSx file system directory when the Amazon EC2 instance
reboots, you can use the `fstab` file. The `fstab`
file contains information about file systems. The command `mount -a`, which runs
during instance startup, mounts the file systems listed in the `fstab`
file.

###### Note

- Before you can update the `/etc/fstab` file of your EC2 instance,
  make sure that you've already created your Amazon FSx file system. For more information,
  see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") in the
  Getting Started exercise.
- For EFA-enabled file systems, configuring systemd is a pre-requisite. For more information,
  see [Quick setup](configure-efa-clients.md#quick-setup "configure-efa-clients.md#quick-setup").

###### To update the /etc/fstab file in your EC2 instance

1. Connect to your EC2 instance, and open the `/etc/fstab` file in
   an editor.
2. Add the following line to the `/etc/fstab` file.

Mount the Amazon FSx for Lustre file system to the directory that you created. Use the following command
and replace the following:

    * Replace ``/fsx`` with the directory that you want to mount
     your Amazon FSx file system to.
    * Replace ``file_system_dns_name`` with the
     actual file system's DNS name.
    * Replace ``mountname`` with the file system's mount name.
     This mount name is returned in the `CreateFileSystem` API operation
     response. It's also returned in the response of the
     **describe-file-systems** AWS CLI command, and the `DescribeFileSystems` API operation.

**For non-EFA file systems:**

```
`file_system_dns_name`@tcp:/`mountname` `/fsx` lustre defaults,relatime,flock,_netdev,x-systemd.automount,x-systemd.requires=network.service 0 0
```

**For EFA-enabled file systems:**

```
`file_system_dns_name`@tcp:/`mountname` `/fsx` lustre defaults,relatime,flock,_netdev,x-systemd.automount,x-systemd.requires=configure-efa-fsx-lustre-client.service,x-systemd.after=configure-efa-fsx-lustre-client.service 0 0
```

###### Warning

Use the `_netdev` option, used to identify network file systems, when
mounting your file system automatically. If `_netdev` is missing, your EC2
instance might stop responding. This result is because network file systems need to be
initialized after the compute instance starts its networking. For more information,
see [Automatic mounting fails and the instance is
unresponsive](mount-troubleshooting.md#lustre-automount-fails "mount-troubleshooting.md#lustre-automount-fails"). 3. Save the changes to the file.

Your EC2 instance is now configured to mount the Amazon FSx file system whenever it
restarts.

###### Note

In some cases, your Amazon EC2 instance might need to start regardless of the status of
your mounted Amazon FSx file system. In these cases, add the `nofail` option to your
file system's entry in your `/etc/fstab` file.

The fields in the line of code that you added to the `/etc/fstab`
file do the following.

| Field                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``file_system_dns_name`@tcp:/`                                                                                                           | The DNS name for your Amazon FSx file system, which identifies the file system. You can get this name from the console or programmatically from the AWS CLI or an AWS SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `mountname`                                                                                                                              | The mount name for the file system. You can get this name from the console or programmatically from the AWS CLI using the **describe-file-systems** command or the AWS API or SDK using the `DescribeFileSystems` operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `/fsx`                                                                                                                                   | The mount point for the Amazon FSx file system on your EC2 instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `lustre`                                                                                                                                 | The type of file system, Amazon FSx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `mount options`                                                                                                                          | Mount options for the file system, presented as a comma-separated list of the following options: <br>• `defaults` – This value tells the operating system to use the default mount options. You can list the default mount options after the file system has been mounted by viewing the output of the `mount` command. <br>• `relatime` – This option maintains `atime` (inode access times) data, but not for each time that a file is accessed. With this option enabled, `atime` data is written to disk only if the file has been modified since the `atime` data was last updated (`mtime`), or if the file was last accessed more than a certain amount of time ago (one day by default). If you want to turn off inode access time updates, use the `noatime` mount option instead. <br>• `flock` – mounts your file system with file locking enabled. If you don't want file locking enabled, use the `noflock` mount option instead. <br>• `_netdev` – The value tells the operating system that the file system resides on a device that requires network access. This option prevents the instance from mounting the file system until the network has been enabled on the client. |
| `x-systemd.automount,x-systemd.requires=network.service`                                                                                 | These options for non-EFA file systems ensure that the auto mounter does not run until the network connectivity is online. NoteFor Amazon Linux 2023 and Ubuntu 22.04 and higher, use the `x-systemd.requires=systemd-networkd-wait-online.service` option instead of the `x-systemd.requires=network.service` option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `x-systemd.automount,x-systemd.requires=configure-efa-fsx-lustre-client.service,x-systemd.after=configure-efa-fsx-lustre-client.service` | These options for EFA-enabled file systems ensure that the auto mounter does not run until after EFA client configuration completes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `0`                                                                                                                                      | A value that indicates whether the file system should be backed up by `dump`. For Amazon FSx, this value should be `0`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `0`                                                                                                                                      | A value that indicates the order in which `fsck` checks file systems at boot. For Amazon FSx file systems, this value should be `0` to indicate that `fsck` should not run at startup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
