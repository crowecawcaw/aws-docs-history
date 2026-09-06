

# Create the VHD
<a name="create-vhd"></a>

A VHD is a single file that when mounted to the operating system is treated like a hard disk. The VHD can be mounted as a drive letter, to a folder path, or both. When the VHD is mounted, you can treat it as you would any other hard disk, including installing your application or copying files to it that your user will need.

To create the app block, you will need to create the VHD, install your applications to it, then detach it. Once detached you can test your VHD on another PC, an EC2 instance, or an WorkSpaces Applications image builder to validate the applications work as expected. Once completed, upload to an Amazon S3 bucket in your account and create the app block.

**Note**  
This page describes using a VHD to deliver your application; however, the WorkSpaces Applications streaming instance will download any object from Amazon S3. The object you store in Amazon S3 can also be a zip file, application installer, or the application executable itself. You can use the setup script to configure it correctly on the streaming instance before a user launches their application.  
The WorkSpaces Applications streaming instance waits up to 120 seconds for the VHD to complete downloading before the setup script runs. If the VHD does not complete downloading within this duration, the download stops, and the setup script will not run.   
We recommend a maximum size of 1.5 gigabyte for the VHD. You might be able to reduce the size of the VHD by compressing. You must use the setup script to decompress it before mounting it, because the file needs to be fully downloaded from Amazon S3 before it can be mounted and the application is launched. Larger VHDs increase the time it takes for the application to launch and the streaming session to begin.

**To create a VHD for Microsoft Windows**

1. From a Windows PC or Windows Amazon Elastic Compute Cloud (Amazon EC2) instance, open a command prompt with administrative privileges.

1. Launch the Microsoft **diskpart** utility by entering the following command:

   **diskpart**

1. Create the unformatted and uninitialized VHD file by entering the following command, where {{<maximum file size>}} is the size of the VHD file, in MB:

   **create vdisk file=C:\\path\\to\\new\\file.vhdx maximum={{<maximum file size>}} type=expandable **

1. Select the newly created VHD by entering the following command:

   **select vdisk file=C:\\path\\to\\new\\file.vhdx**

1. Attach the newly created VHD by entering the following command:

   **attach vdisk**

1. Initialize the newly created VHD by entering the following command:

   **convert mbr**

1. Create the primary partition spanning the entire VHD by entering the following command:

   **create partition primary**

1. Format the newly created partition by entering the following command:

   **format fs=ntfs quick**

1. You can mount your newly created VHD to an unused drive letter, a folder path on the root volume, or both.

   To mount a drive letter, enter: **assign letter={{<unused drive letter>}}**

   To mount a folder, enter: **assign mount={{C:\\path\\to\\empty\\folder\\to\\mount\\}}**
**Note**  
To mount to a folder path, the folder must already exist and must be empty.

1. You can now install your application to the VHD, using either the drive letter or the folder mount path chosen in step 9.

After you finish installing your application(s) to the VHD, you need to detach it before you can safely upload it to an Amazon S3 bucket.

**To detach a VHD for Microsoft Windows**

1. Launch the Microsoft diskpart utility by entering the following command:

   **diskpart**

1. Select the VHD by entering the following command:

   **select vdisk file={{C:\\path\\to\\new\\file.vhdx}}**

1. Detach the VHD by entering the following command:

   **detach vdisk**

1. The VHD has now been detached, and can be tested on another Windows PC, Amazon EC2 instance, or an WorkSpaces Applications image builder.

**To create a VHD for Linux**

1. Open a terminal:
   + For Ubuntu Pro 24.04 LTS: Use EC2 instance, or WorkSpaces powered by Ubuntu Pro

1. Create the unformatted and uninitialized VHD file:

   **dd if=/dev/zero of={{<name of file>}} bs={{<size of VHD>}} count=1**

1. Add a file system to the created VHD by entering the following command:

   **sudo mkfs -t ext4 {{<name of file>}}**
**Note**  
You might see a message stating that the file is not a block special device. You can select to proceed anyway.

1. Create an empty folder to use for the mount point by entering the following command:

   **sudo mkdir {{/path/to/mount/point}}**

1. Mount the newly created VHD to a file system path by running the following command:

   **sudo mount -t auto -o loop {{<name of file>}} {{/path/to/mount/point}}**

1. You can now install your application to the VHD using the folder mount path chosen in step 4.
**Note**  
The default permissions for files and folders created on the VHD can prevent non-administrator users from launching applications or reading files. Validate the permissions and change them, if necessary.

After you finish installing your application(s) to the VHD, you need to detach it before you can safely upload it to an Amazon S3 bucket.

**To detach a VHD for Linux**

1. Open a terminal session, and enter the following command:

   **sudo umount {{/path/to/mount/point}}**

1. The VHD has now been detached, and can be tested on another Ubuntu Pro 24.04 LTS Amazon EC2 instance or Ubuntu WorkSpaces Personal.