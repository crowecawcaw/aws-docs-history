# Step A: Get ready for Elemental Live migration

## Read the essential notes

Refer to the essential notes in the [current Release Notes](../../../elemental-live.md "../../../elemental-live.md") to identify key changes to the
behavior of Elemental Live.

###### Important

Make sure that you have the latest version of the Release Notes. If you
downloaded the file more than a few days ago, we recommend that you download it
again.

Follow the instructions in the Release Notes to prepare for these changes. Make a
note of all the decisions that you make, particularly:

- If you have Elemental Live nodes that have a Mellanox NIC, you must decide whether
  you will include the `–skip-mellanox` option in the install
  command on the node.
- If you have Elemental Live nodes that handle SMPTE 2110 inputs or outputs, you must
  a new license for each. The procedure for obtaining a new license is
  described in the essential notes.

## Modify your automation system for

HTTPS

After a node has been migrated, it uses HTTPS. By default, the nodes are set up
with self-signed certificates. Make sure of the following points:

- You might need to change your automation system to use HTTPS.
- In addition, if you decide not to provide custom certificates, use HTTPS
  with the `-k` option.

## Verify installer type

The software installer that you use depends on whether you have GPU-accelerated
software type, or CPU-only. To determine the type of software, look at any page on
the web interface of each worker node. At the top, look for these icons:

- CPU and GPU icons: the software is
  _GPU-accelerated_.
- CPU icon only: the software is _CPU-only_.

## Create a boot USB drive

On Dell hardware, you have the option to install RHEL 9 by using a boot USB drive
or by using or iDRAC (for Dell). (Note that SuperMicro hardware, you can only
install RHEL 9 by using IPMI.)

If you want to use a boot USB drive with Dell, you should make the drive now. You
might want to make several drives, depending on how many people will be performing
the migration tasks.

To create a boot drive, follow these steps:

1. Obtain the RHEL 9 `.iso` file from [AWS Elemental Software Download page](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads").

Find the AWS Elemental product and version they are planning to use. The
appropriate ISO file appears beside that version. 2. At your workstation, use a third-party utility (such as PowerISO or
ISO2USB) to create a bootable USB drive from your `.iso`
file. For help, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article
[Creating Bootable Recovery (kickstart)
Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").

## Obtain information

When you install RHEL 9, the _elemental_ password
will be reset to the global default value. When you install the AWS Elemental software, you
will need to enter this default password.

If your organization had previously kickstarted an AWS Elemental appliance, someone in
your organization might have the global default password. Note that this global
default password isn't the same as the unique default password that applied when you
first obtained the appliance.

If you need help finding the password, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the
Knowledge article [Unique passwords for AWS Elemental appliances](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Unique-passwords-for-AWS-Elemental-appliances "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Unique-passwords-for-AWS-Elemental-appliances") or open a case.

## Verify space on the node

As part of the upgrade, you create a backup of the data on the node. You must make
sure that you have enough free space for the backup. Follow these guidelines:

- The backup for a freshly kickstarted and licensed appliance generates a 5
  MB backup directory and a 2 MB zipped version of the backup
  (`<hostname>_lifeboat-archive.zip`).
- Your configuration will generate larger files because of the data that you
  create, so review available space before starting.
- Check the contents of the `/home` partition, and clear
  out old files, unnecessary files, and old installers.
