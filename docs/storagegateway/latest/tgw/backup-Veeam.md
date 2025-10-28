# Testing your setup by using Veeam Backup and

Replication

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Veeam Backup & Replication. In this topic, you can
find basic documentation on how to configure the Veeam Backup & Replication software for
a Tape Gateway and perform a backup and restore operation. For detailed information about
how to use the Veeam software, refer to the Veeam Backup & Replication documentation.
For more information about compatible backup applications, see [Supported third-party backup
applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

###### Topics

- [Configuring Veeam to Work with VTL
  Devices](#veeam-configure-software "#veeam-configure-software")
- [Importing a Tape into Veeam](#veeam-Import-tapes "#veeam-Import-tapes")
- [Backing Up Data to a Tape in Veeam](#veeam-write-data-to-tape "#veeam-write-data-to-tape")
- [Archiving a Tape by Using Veeam](#veeam-archive-tape "#veeam-archive-tape")
- [Restoring Data from a Tape Archived in
  Veeam](#veeam-restore-tape "#veeam-restore-tape")

## Configuring Veeam to Work with VTL

Devices

After you have connected your virtual tape library (VTL) devices to the Windows
client, you configure Veeam Backup & Replication to recognize your devices. For
information about how to connect VTL devices to the Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

### Updating VTL Device Drivers

To configure the software to work with Tape Gateway devices, you update the
device drivers for the VTL devices to expose them to the Veeam software and then
discover the VTL devices. In Device Manager, update the driver for the medium
changer. For instructions, see [Updating the Device Driver for Your Medium
Changer](resource_vtl-devices.md#update-vtl-device-driver "resource_vtl-devices.md#update-vtl-device-driver").

### Discovering VTL Devices

You must use native SCSI commands instead of a Windows driver to discover your
tape library if your media changer is unknown. For detailed instructions, see [Tape Libraries](https://helpcenter.veeam.com/docs/backup/vsphere/managing_library.html "https://helpcenter.veeam.com/docs/backup/vsphere/managing_library.html").

###### To discover VTL devices

1. In the Veeam software, choose **Tape Infrastructure**.
   When the Tape Gateway is connected, virtual tapes are listed in the
   **Tape Infrastructure** tab.
2. Expand the **Tape** tree to see your tape drives and
   medium changer.
3. Expand the medium changer tree. If your tape drives are mapped to the
   medium changer, the drives appear under **Drives**.
   Otherwise, your tape library and tape drives appear as separate devices.

If the drives are not mapped automatically, follow the [instructions on the Veeam
website](http://www.veeam.com/kb1842 "http://www.veeam.com/kb1842") to map the drives.

## Importing a Tape into Veeam

You are now ready to import tapes from your Tape Gateway into the Veeam backup
application library.

###### To import a tape into the Veeam library

1. Open the context (right–click) menu for the medium changer, and choose
   **Import** to import the tapes to the I/E slots.
2. Open the context (right–click) menu for the medium charger, and choose
   **Inventory Library** to identify unrecognized tapes. When
   you load a new virtual tape into a tape drive for the first time, the tape is
   not recognized by the Veeam backup application. To identify the unrecognized
   tape, you inventory the tapes in the tape library.

## Backing Up Data to a Tape in Veeam

Backing data to a tape is a two-step process:

1. You create a media pool and add the tape to the media pool.
2. You write data to the tape.

You create a media pool and write data to a virtual tape by using the same procedures
you do with physical tapes. For detailed information about how to back up data, see the
[Getting Started with Tapes](https://helpcenter.veeam.com/docs/backup/vsphere/getting_started_with_tapes.html "https://helpcenter.veeam.com/docs/backup/vsphere/getting_started_with_tapes.html") in the Veeam Help Center.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will fail. To complete the failed backup job, you must resubmit
it.

## Archiving a Tape by Using Veeam

When you archive a tape, Tape Gateway moves the tape from the Veeam tape library to
the offline storage. You begin tape archival by ejecting from the tape drive to the
storage slot and then exporting the tape from the slot to the archive by using your
backup application—that is, the Veeam software.

###### To archive a tape in the Veeam library

1. Choose **Tape Infrastructure**, and choose the media pool
   that contains the tape you want to archive.
2. Open the context (right–click) menu for the tape that you want to archive, and
   then choose **Eject Tape**.
3. For **Ejecting tape**, choose **Close**. The
   location of the tape changes from a tape drive to a slot.
4. Open the context (right–click) menu for the tape again, and then choose
   **Export**. The status of the tape changes from
   **Tape drive** to **Offline**.
5. For **Exporting tape**, choose **Close**.
   The location of the tape changes from **Slot** to
   **Offline**.
6. On the Storage Gateway console, choose your gateway, and then choose **VTL
   Tape Cartridges** and verify the status of the virtual tape you are
   archiving.

The archiving process can take some time to complete. The initial status of
the tape appears as **IN TRANSIT TO VTS**. When archiving
starts, the status changes to **ARCHIVING**. When archiving is
completed, the tape is no longer listed in the VTL but is archived in
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive.

## Restoring Data from a Tape Archived in

Veeam

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions,
   see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use the Veeam software to restore the data. You do this by creating a
   restoring a folder file, as you do when restoring data from physical tapes. For
   instructions, see [Restoring Files from Tape](https://helpcenter.veeam.com/docs/backup/vsphere/restore_files_from_tapes.html "https://helpcenter.veeam.com/docs/backup/vsphere/restore_files_from_tapes.html") in the Veeam Help Center.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
