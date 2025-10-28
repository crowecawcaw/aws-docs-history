# Migrate data from CentOS

to AlmaLinux on Lightsail

Migrating from CentOS to AlmaLinux is a straightforward process by which you move data
from one instance in Lightsail to another. This topic outlines two options that you
can use to migrate your data.

For more information see the AlmaLinux documentation on the [_AlmaLinux Wiki_](https://wiki.almalinux.org/ "https://wiki.almalinux.org/")
site.

###### Contents

- [Prerequisites](amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-prerequisites "amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-prerequisites")
- [(Optional) Use
  secure copy (scp) to transfer files between instances](amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-scp "amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-scp")
- [(Optional)
  Move the block storage disk from the CentOS instance to the AlmaLinux
  instance](amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-copy-disk "amazon-lightsail-migrate-centos-to-almalinux.md#amazon-lightsail-migrate-centos-to-almalinux-copy-disk")

## Prerequisites

- If you haven't already, create an AlmaLinux Lightsail instance. For more
  information, see [Launch and set up an
  AlmaLinux instance on Lightsail](amazon-lightsail-quick-start-guide-almalinux.md "amazon-lightsail-quick-start-guide-almalinux.md").
- Create a snapshot of the disk you plan to move to your AlmaLinux instance.
  For more information, see [Create Lightsail block storage disk
  snapshots for backup or baseline](create-block-storage-disk-snapshot.md "create-block-storage-disk-snapshot.md").

## (Optional) Use

secure copy (scp) to transfer files between instances

You can securely transfer files from your CentOS instance to the new AlmaLinux
instance by using the secure copy command in Linux. For more information, see [Transfer files
between Linux instances on Lightsail using scp](amazon-lightsail-transfer-files-between-linux-instances.md "amazon-lightsail-transfer-files-between-linux-instances.md").

## (Optional)

Move the block storage disk from the CentOS instance to the AlmaLinux
instance

Use the following procedure to move a secondary block storage disk from your
CentOS instance bundle to the AlmaLinux bundle. You cannot detach the instance's
boot volume disk; the disk that contains the operating system. After you attach the
disk to your AlmaLinux instance, you need to connect to that instance and mount the
disk. For more information, see [Expand storage and
performance with Lightsail block storage disks](elastic-block-storage-and-ssd-disks-in-amazon-lightsail.md "elastic-block-storage-and-ssd-disks-in-amazon-lightsail.md").

If your CentOS instance is running, you will need to stop it before you can detach
the disk. For more information, see [Stop a running instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md#lightsail-instance-stop "lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md#lightsail-instance-stop").

1. From the **Storage** section of the Lightsail console,
   select the disk that you want to detach from your CentOS instance.

![The storage section in the Lightsail console.](images/lightsail-migrate-alma-01.png) 2. On the **Details** tab, choose
**Detach**.

![The disk details in the Lightsail console.](images/lightsail-migrate-alma-02.png) 3. From the disk **Details** page, choose the
**Attach to an instance** dropdown menu. Then choose
the name of your AlmaLinux instance.

![The attach disk dropdown menu in the Lightsail console.](images/lightsail-migrate-alma-03.png) 4. Choose **Attach**. 5. (Optional) You might need to connect to your AlmaLinux instance and mount
the disk before you can access its data. For more information, see [Connect to your instance to format and mount the disk](create-and-attach-additional-block-storage-disks-linux-unix.md#connect-to-linux-unix-instance-using-ssh-format-mount-disk "create-and-attach-additional-block-storage-disks-linux-unix.md#connect-to-linux-unix-instance-using-ssh-format-mount-disk").

###### Warning

The above link provides instructions for how to mount and format the attached
disk. **Do not format the disk** that you attached
to your AlmaLinux instance. Formatting it will permanently erase all information
stored on the disk.
