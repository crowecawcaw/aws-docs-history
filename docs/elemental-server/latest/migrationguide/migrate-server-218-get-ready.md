

# Step A: Get ready for AWS Elemental Server migration
<a name="migrate-server-218-get-ready"></a>

## Read the essential notes
<a name="migrate-server-218-essential-notes"></a>

Refer to the essential notes in the [AWS Elemental Server Release Notes](https://docs.aws.amazon.com/elemental-onprem/latest/pdf/elemental_server_conductor_file_release_notes_2.18.0.pdf) to identify key changes to the behavior of AWS Elemental Server.

## Modify your automation system for HTTPS
<a name="migrate-server-218--automation-system"></a>

After a node has been migrated, it uses HTTPS. By default, the nodes are set up with self-signed certificates. Make sure of the following points:
+ You might need to change your automation system to use HTTPS.

## Verify installer type
<a name="migrate-server-218-verify-cpu"></a>

Use a software installer that aligns with your AWS Elemental Server type: GPU-accelerated or CPU-only. 

Use the same type of installer for your Conductor File. For example, if your AWS Elemental Server has a GPU, use the GPU installer for your Conductor File.

To determine whether you have a GPU-accelerated or CPU-only system, run the following command on your AWS Elemental Server: 

**lspci \| grep NVIDIA**

If the output is empty, your system is CPU-only.

If the output is similar to the following, your system is GPU-accelerated:

```
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
```

## Create a boot USB drive
<a name="migrate-server-218-boot"></a>

On Dell hardware, you have the option to install RHEL 9 by using a boot USB drive or by using iDRAC (for Dell). (Note that SuperMicro hardware, you can only install RHEL 9 by using IPMI.)

If you want to use a boot USB drive with Dell, you should make the drive now. You might want to make several drives, depending on how many people will be performing the migration tasks.

To create a boot drive, follow these steps:

1. Obtain the RHEL 9 `.iso` file from [AWS Elemental Software Download page](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads).

   Find the AWS Elemental product and version they are planning to use. The appropriate ISO file appears beside that version.

1. At your workstation, use a third-party utility (such as PowerISO or ISO2USB) to create a bootable USB drive from your `.iso` file. For help, see the knowledge base article [Creating Bootable Recovery (kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-CentOS-Elemental-v2-0-Windows-and-Apple-OS-X).

## Verify space on the node
<a name="migrate-server-218-memory"></a>

As part of the upgrade, you create a backup of the data on the node. You must make sure that you have enough free space for the backup. Follow these guidelines:
+ The backup for a freshly kickstarted and licensed appliance generates a small backup directory zipped version of the backup (`<hostname>_lifeboat-archive.zip`). 
+ Your configuration will generate larger files because of the data that you create, so review available space before starting. 
+ Check the contents of the `/home` partion, and clear out old files, unnecessary files, and old installers.