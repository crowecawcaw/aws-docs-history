# Step A: Get ready to migrate an AWS Elemental Conductor File

cluster

## Read the essential notes

Refer to the essential notes in the [AWS Elemental Conductor File Release Notes](../../../elemental-onprem/latest/pdf/elemental_server_conductor_file_release_notes_2.18.0.md "../../../elemental-onprem/latest/pdf/elemental_server_conductor_file_release_notes_2.18.0.md") to identify key changes to
the behavior of the Conductor File and worker nodes.

###### Important

Make sure that you have the latest version of the Release Notes. If you
downloaded the file more than a few days ago, we recommend that you download it
again.

## Modify your automation system for

HTTPS

After a node has been migrated, it uses HTTPS. By default, the nodes are set up
with self-signed certificates. Make sure of the following points:

- You might need to change your automation system to use HTTPS.

## Verify installer type

The software installer that you use depends on whether you have GPU-accelerated
software type, or CPU-only.

To determine whether you have a GPU-accelerated or CPU-only system, run the
following command:

**lspci | grep NVIDIA**

If the output is empty, your system is CPU-only.

If the output is similar to the following, your system is GPU-accelerated:

```
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
VGA compatible controller: NVIDIA Corporation GM204GL [Tesla M60] (rev a1)
```

## Create a boot USB drive

On Dell hardware, you have the option to install RHEL 9 by using a boot USB drive
or by using or iDRAC (for Dell). (Note that SuperMicro hardware, you can only
install RHEL 9 by using IPMI.)

If you want to use a boot USB drive with Dell, you should make the drive now. You
might want to make several drives, depending on how many people will be performing
the migration tasks. For instructions, see [Create a boot USB drive](migrate-topic-create-boot.md "migrate-topic-create-boot.md").

## Verify space on each node

As part of the upgrade, you create a backup of the data on each node. You must
make sure that you have enough free space for the backup. Follow these
guidelines:

- The backup for a freshly kickstarted and licensed appliance generates a
  small backup directory andB zipped version of the backup
  (`<hostname>_lifeboat-archive.zip`).
- Your configuration will generate larger files because of the data that you
  create, so review available space before starting.
- Check the contents of the `/home` partion, and clear
  out old files, unnecessary files, and old installers.
