# Make instance store volume available for use on an EC2 instance

After you launch an instance with attached instance store volumes, you must mount the
volumes before you can access them.

You can format volumes with the file system of your choice after you launch your
instance.

###### To make an instance store volume available on Linux

1. Connect to the instance using an SSH client. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. Use the `df -h` command to view the volumes that are formatted and
   mounted.

```
`$` `df -h`
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.8G   72K  3.8G   1% /dev
tmpfs           3.8G     0  3.8G   0% /dev/shm
/dev/nvme0n1p1  7.9G  1.2G  6.6G  15% /
```

3. Use the `lsblk` to view any volumes that were mapped at launch but
   not formatted and mounted.

```
`$` `lsblk`
NAME          MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
nvme0n1       259:1    0    8G  0 disk
├─nvme0n1p1   259:2    0    8G  0 part /
└─nvme0n1p128 259:3    0    1M  0 part
nvme1n1       259:0    0 69.9G  0 disk
```

4.  To format and mount an instance store volume that was mapped only, do the
    following:

        1. Create a file system on the device using the `mkfs` command.



        ```
        `$` `sudo mkfs -t xfs` `/dev/nvme1n1`
        ```
        2. Create a directory on which to mount the device using the `mkdir`
         command.



        ```
        `$` `sudo mkdir` `/data`
        ```
        3. Mount the device on the newly created directory using the `mount`
         command.



        ```
        `$` `sudo mount` `/dev/nvme1n1 /data`
        ```

    For Windows instances, we reformat the instance store volumes with the NTFS file system.

You can view the instance store volumes using Windows Disk Management. For more information,
see [List non-NVMe disks](windows-list-disks.md#windows-disks "windows-list-disks.md#windows-disks").

###### To manually mount an instance store volume

1. Choose **Start**, enter **Computer Management**,
   and then press **Enter**.
2. In left-hand panel, choose **Disk Management**.
3. If you are prompted to initialize the volume, choose the volume to initialize, select the
   required partition type depending on your use case, and then choose
   **OK**.
4. In the list of volumes, right-click the volume to mount, and then choose
   **New Simple Volume**.
5. On the wizard, choose **Next**.
6. On the Specify Volume Size screen, choose **Next** to use the
   maximum volume size. Alternatively, choose a volume size that is between the
   minimum and maximum disk space.
7. On the Assign a Drive Letter or Path screen, do one of the following, and choose
   **Next**.
   - To mount the volume with a drive letter, choose **Assign
     the following drive letter** and then choose the drive letter to use.
   - To mount the volume as a folder, choose **Mount in the
     following empty NTFS folder** and then choose
     **Browse** to create or select the folder to use.
   - To mount the volume without a drive letter or path, choose
     **Do not assign a drive letter or drive path**.

8. On the Format Partition screen, specify whether or not to format the volume. If you choose to
   format the volume, choose the required file system and unit size, and specify a volume label.
9. Choose **Next**, **Finish**.
