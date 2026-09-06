

# Initializing and formatting your volume
<a name="format-volume"></a>

After you use the iSCSI initiator in your client to connect to your volumes, you initialize and format your volume.

**Topics**
+ [Initializing and formatting your volume on Microsoft Windows](#format-windows)
+ [Initializing and formatting your volume on Red Hat Enterprise Linux](#format-rhel)

## Initializing and formatting your volume on Microsoft Windows
<a name="format-windows"></a>

Use the following procedure to initialize and format your volume on Windows.<a name="GettingStartedAccessVolumesFormatting"></a>

**To initialize and format your storage volume**

1. Start **diskmgmt.msc** to open the **Disk Management** console.

1. In the **Initialize Disk** dialog box, initialize the volume as a **MBR (Master Boot Record)** partition. When selecting the partition style, you should take into account the type of volume you are connecting to—cached or stored—as shown in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/format-volume.html)

1. Create a simple volume:

   1. Bring the volume online to initialize it. All the available volumes are displayed in the disk management console. 

   1. Open the context (right-click) menu for the disk, and then choose **New Simple Volume**.
**Important**  
Be careful not to format the wrong disk. Check to make sure that the disk you are formatting matches the size of the local disk you allocated to the gateway VM and that it has a status of **Unallocated**. 

   1. Specify the maximum disk size.

   1. Assign a drive letter or path to your volume, and format the volume by choosing **Perform a quick format**.
**Important**  
We strongly recommend using **Perform a quick format** for cached volumes. Doing so results in less initialization I/O, smaller initial snapshot size, and the fastest time to a usable volume. It also avoids using cached volume space for the full format process.
**Note**  
The time that it takes to format the volume depends on the size of the volume. The process might take several minutes to complete.

## Initializing and formatting your volume on Red Hat Enterprise Linux
<a name="format-rhel"></a>

Use the following procedure to initialize and format your volume on Red Hat Enterprise Linux (RHEL).

**To initialize and format your storage volume**

1. Change directory to the `/dev` folder.

1. Run the `sudo cfdisk` command.

1. Identify your new volume by using the following command. To find new volumes, you can list the partition layout of your volumes.

   `$ lsblk`

   An "unrecognized volumes label" error for the new unpartitioned volume appears.

1. Initialize your new volume. When selecting the partition style, you should take into account the size and type of volume you are connecting to—cached or stored—as shown in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/format-volume.html)

   For an MBR partition, use the following command: `sudo parted /dev/{{your volume}} mklabel msdos`

   For a GPT partition, use the following command: `sudo parted /dev/{{your volume}} mklabel gpt`

1. Create a partition by using the following command.

   `sudo parted -a opt /dev/{{your volume}} mkpart primary {{file system}} 0% 100%`

1. Assign a drive letter to the partition and create a file system by using the following command.

   `sudo mkfs -L datapartition /dev/{{your volume}}`

1. Mount the file system by using the following command.

    `sudo mount -o defaults /dev/{{your volume}} /mnt/{{your directory}}` 