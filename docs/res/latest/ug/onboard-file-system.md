

# Onboard a file system
<a name="onboard-file-system"></a>

**Note**  
To successfully onboard a file system, it must share the same VPC and at least one of your RES subnets. You must also ensure you have the security group configured properly so your VDIs have access to the file system's contents.

1.  Choose **Onboard File System**. 

1. Select a file system from the drop down. The modal will expand with additional detail entries.  
![Select file system](http://docs.aws.amazon.com/res/latest/ug/images/res-selectfilesystem.jpg)

1. Enter file system details.
**Note**  
By default, administrators and project owners have the ability to choose a home filesystem when creating a new project, which cannot be edited afterwards.  
File systems intended to be used as home directories on projects must be onboarded by setting their **Mount Directory** path to `/home`. This will populate the onboarded filesystem on the home directory filesystem dropdown options. This feature helps to keep the data isolated across projects since only users associated with the project will have access to the filesystem through their VDIs. VDIs will mount the filesystem at the mount point selected during onboarding of a filesystem.

1. Choose **Submit**.   
![Select file system](http://docs.aws.amazon.com/res/latest/ug/images/res-filesystemdetails.jpg)

## Multiple volumes from a single ONTAP file system
<a name="onboard-multiple-ontap-volumes"></a>

RES supports onboarding multiple volumes from a single for NetApp ONTAP file system. This allows administrators to organize data across separate volumes within the same ONTAP file system while making each volume independently available to projects.

To onboard additional volumes from an ONTAP file system that is already onboarded:

1. Choose **Onboard File System**.

1. Select the same ONTAP file system from the drop down.

1. In the **Volume** field, select a different volume from the file system.

1. Specify a unique **Mount Directory** for this volume.

1. Choose **Submit**.

**Note**  
Each volume from the same ONTAP file system must be onboarded with a unique mount directory. Volumes can be independently assigned to different projects.