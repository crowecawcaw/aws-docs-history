

# Testing your setup by using Quest NetVault Backup
<a name="backup-netvault"></a>

You can back up your data to virtual tapes, archive the tapes, and manage your virtual tape library (VTL) devices by using Quest (formerly Dell) NetVault Backup.

In this topic, you can find basic documentation on how to configure the Quest NetVault Backup application for a Tape Gateway and perform a backup and restore operation. 

For detailed information about how to use the Quest NetVault Backup application, see the Quest NetVault Backup – Administration Guide. For more information about compatible backup applications, see [Supported third-party backup applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl).

**Topics**
+ [Configuring Quest NetVault Backup to Work with VTL Devices](#netvault-configure-software)
+ [Backing Up Data to a Tape in the Quest NetVault Backup](#netvault-write-data-to-tape)
+ [Archiving a Tape by Using the Quest NetVault Backup](#netvault-archive-tape)
+ [Restoring Data from a Tape Archived in Quest NetVault Backup](#netvault-restore-tape)

## Configuring Quest NetVault Backup to Work with VTL Devices
<a name="netvault-configure-software"></a>

After you have connected the virtual tape library (VTL) devices to the Windows client, you configure Quest NetVault Backup to recognize your devices. For information about how to connect VTL devices to the Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md).

The Quest NetVault Backup application doesn't automatically recognize Tape Gateway devices. You must manually add the devices to expose them to the Quest NetVault Backup application and then discover the VTL devices.

### Adding VTL Devices
<a name="netvault-add-devices"></a>

**To add the VTL devices**

1. In Quest NetVault Backup, choose **Manage Devices** in the **Configuration** tab.

1. On the Manage Devices page, choose **Add Devices**.

1. In the Add Storage Wizard, choose **Tape library / media changer**, and then choose **Next**.

1. On the next page, choose the client machine that is physically attached to the library and choose **Next** to scan for devices.

1. If devices are found, they are displayed. In this case, your medium changer is displayed in the device box.

1. Choose your medium changer and choose **Next**. Detailed information about the device is displayed in the wizard.

1. On the Add Tapes to Bays page, choose **Scan For Devices**, choose your client machine, and then choose **Next**. 

   Quest NetVault Backup displays all of your drives, and the 10 bays to which you can add your drives. The bays are displayed one at a time.

1. Choose the drive you want to add to the bay that is displayed, and then choose **Next**.
**Important**  
When you add a drive to a bay, the drive and bay numbers must match. For example, if bay 1 is displayed, you must add drive 1. If a drive is not connected, leave its matching bay empty.

1. When your client machine appears, choose it, and then choose **Next**. The client machine can appear multiple times.

1. When the drives are displayed, repeat steps 7 through 9 to add all the drives to the bays.

1. In the **Configuration** tab, choose **Manage devices** and on the **Manage Devices** page, expand your medium changer to see the devices that you added.

## Backing Up Data to a Tape in the Quest NetVault Backup
<a name="netvault-write-data-to-tape"></a>

You create a backup job and write data to a virtual tape by using the same procedures you do with physical tapes. For detailed information about how to back up data, see the [Quest NetVault Backup - Administration Guide](https://support.quest.com/technical-documents/netvault-backup/12.4/administration-guide).

**Note**  
If your Tape Gateway restarts for any reason during an ongoing backup job, the backup job will fail. To complete the failed backup job, you must resubmit it.

## Archiving a Tape by Using the Quest NetVault Backup
<a name="netvault-archive-tape"></a>

When you archive a tape, a Tape Gateway ejects the tape from the tape drive to the storage slot. It then exports the tape from the slot to the archive by using your backup application—that is, the Quest NetVault Backup.

**To archive a tape in Quest NetVault Backup**

1. In the Quest NetVault Backup Configuration tab, choose and expand your medium changer to see your tapes.

1. Choose the settings icon for **Slots** to open the **Slots Browser** for the medium changer.

1. In the slots, choose the tape you want to archive, and then choose **Export**.

The archiving process can take some time to complete. The initial status of the tape appears as **IN TRANSIT TO VTS**. When archiving starts, the status changes to **ARCHIVING**. When archiving is completed, the tape is no longer listed in the VTL.

In the Quest NetVault Backup software, verify that the tape is no longer in the storage slot.

In the navigation pane of the Storage Gateway console, choose **Tapes**. Verify that your archived tape's status is **ARCHIVED**. 

## Restoring Data from a Tape Archived in Quest NetVault Backup
<a name="netvault-restore-tape"></a>

Restoring your archived data is a two-step process.

**To restore data from an archived tape**

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md).

1. Use the Quest NetVault Backup application to restore the data. You do this by creating a restoring a folder file, as you do when restoring data from physical tapes. For instructions on creating a restore job, see [Quest NetVault Backup - Administration Guide](https://support.quest.com/technical-documents/netvault-backup/12.4/administration-guide).

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl)