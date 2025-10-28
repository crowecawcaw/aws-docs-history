# Testing your setup by using Microsoft System Center DPM

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Microsoft System Center Data Protection Manager (DPM).
In this topic, you can find basic documentation on how to configure the DPM backup
application for a Tape Gateway and perform a backup and restore operation.

For detailed information about how to use DPM, see the [DPM documentation](http://technet.microsoft.com/en-us/library/hh758173.aspx "http://technet.microsoft.com/en-us/library/hh758173.aspx")
on the Microsoft System Center website. For more information about compatible backup
applications, see [Supported third-party backup
applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

###### Topics

- [Configuring DPM to Recognize VTL
  Devices](#dpm-configure-software "#dpm-configure-software")
- [Importing a Tape into DPM](#dpm-Import-tapes "#dpm-Import-tapes")
- [Writing Data to a Tape in DPM](#dpm-write-data-to-tape "#dpm-write-data-to-tape")
- [Archiving a Tape by Using DPM](#dpm-archive-tape "#dpm-archive-tape")
- [Restoring Data from a Tape Archived in DPM](#dpm-restore-tape "#dpm-restore-tape")

## Configuring DPM to Recognize VTL

Devices

After you have connected the virtual tape library (VTL) devices to the Windows client,
you configure DPM to recognize your devices. For information about how to connect VTL
devices to the Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

By default, the DPM server does not recognize Tape Gateway devices. To configure the
server to work with the Tape Gateway devices, you perform the following tasks:

1. Update the device drivers for the VTL devices to expose them to the DPM
   server.
2. Manually map the VTL devices to the DPM tape library.

###### To update the VTL device drivers

- In Device Manager, update the driver for the medium changer. For instructions,
  see [Updating the Device Driver for Your Medium
  Changer](resource_vtl-devices.md#update-vtl-device-driver "resource_vtl-devices.md#update-vtl-device-driver").

You use the DPMDriveMappingTool to map your tape drives to the DPM tape
library.

###### To map tape drives to the DPM server tape library

1. Create at least one tape for your gateway. For information on how to do this
   on the console, see [Creating
   Tapes](GettingStartedCreateTapes.md "GettingStartedCreateTapes.md").
2. Import the tape into the DPM library. For information on how to do this, see
   [Importing a Tape into DPM](#dpm-Import-tapes "#dpm-Import-tapes").
3. If the DPMLA service is running, stop it by opening a command terminal and
   typing the following on the command line.

`net stop DPMLA` 4. Locate the following file on the DPM server: `%ProgramFiles%\System
 Center\DPM\DPM\Config\DPMLA.xml`.

###### Note

The directory path might change depending on your version of System Center
or DPM.

If this file exists, the DPMDriveMappingTool overwrites it. If you want to
preserve your original file, create a backup copy. 5. Open a command terminal, change the directory to `%ProgramFiles%\System Center\DPM\DPM\Bin`, and run the following
command.

###### Note

The directory path might change depending on your version of System Center
or DPM.

```

                        `C:\Microsoft System Center\DPM\DPM\bin>DPMDriveMappingTool.exe`

```

The output for the command looks like the following.

```
                       `Performing Device Inventory ...
Mapping Drives to Library ...
Adding Standalone Drives ...
Writing the Map File ...
Drive Mapping Completed Successfully.`

```

## Importing a Tape into DPM

You are now ready to import tapes from your Tape Gateway into the DPM backup
application library.

###### To import tapes into the DPM backup application library

1. On the DPM server, open the Management Console, choose
   **Rescan**, and then choose **Refresh**.
   The Management Console displays your medium changer and tape drives.
2. Open the context (right-click) menu for the media changer in the
   **Library** section, and then choose **Add tape
   (I/E port)** to add a tape to the **Slots**
   list.

###### Note

The process of adding tapes can take several minutes to complete.

The tape label appears as **Unknown**, and the tape is not
usable. For the tape to be usable, you must identify it. 3. Open the context (right-click) menu for the tape you want to identify, and
then choose **Identify unknown tape**.

###### Note

The process of identifying tapes can take a few seconds or a few
minutes.

If the tapes don’t display barcodes correctly, you need to change the
media changer driver to Sun/StorageTek Library. For more information, see
[Displaying Barcodes for Tapes in Microsoft System
Center DPM](resource_vtl-devices.md#enable-barcode "resource_vtl-devices.md#enable-barcode").

When identification is complete, the tape label changes to
**Free**. That is, the tape is free for data to be written
to it.

## Writing Data to a Tape in DPM

You write data to a Tape Gateway virtual tape by using the same protection procedures
and policies you do with physical tapes. You create a protection group and add the data
you want to back up, and then back up the data by creating a recovery point. For
detailed information about how to use DPM, see the [DPM
documentation](http://technet.microsoft.com/en-us/library/jj628070.aspx "http://technet.microsoft.com/en-us/library/jj628070.aspx") on the Microsoft System Center website.

By default, the capacity of a tape is 30GB. When you backup data that is larger than a
tape's capacity, a device I/O error occurs. If the position where the error occurred is
larger than the size of the tape, Microsoft DPM treats the error as an indication of end
of tape. If the position where the error occurred is less than the size of the tape, the
backup job fails. To resolve the issue, change the `TapeSize` value in the
registry entry to match the size of your tape. For information about how to do this, see
[Error ID:
30101](https://technet.microsoft.com/en-us/library/ff634181.aspx "https://technet.microsoft.com/en-us/library/ff634181.aspx") at the Microsoft System Center.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will fail. To complete the failed backup job, you must resubmit
it.

## Archiving a Tape by Using DPM

When you archive a tape, Tape Gateway moves the tape from the DPM tape library to
offline storage. You begin tape archival by removing the tape from the slot using your
backup application—that is, DPM.

###### To archive a tape in DPM

1. Open the context (right-click) menu for the tape you want to archive, and then
   choose **Remove tape (I/E port)**.
2. In the dialog box that appears, choose **Yes**. Doing this
   ejects the tape from the medium changer's storage slot and moves the tape into
   one of the gateway's I/E slots. When a tape is moved into the gateway's I/E
   slot, it is immediately sent for archiving.
3. On the Storage Gateway console, choose your gateway, and then choose **VTL
   Tape Cartridges** and verify the status of the virtual tape you are
   archiving.

The archiving process can take some time to complete. The initial status of
the tape is shown as **IN TRANSIT TO VTS**. When archiving
starts, the status changes to **ARCHIVING**. When archiving is
completed, the tape is no longer listed in the VTL.

## Restoring Data from a Tape Archived in DPM

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions,
   see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use the DPM backup application to restore the data. You do this by creating a
   recovery point, as you do when restoring data from physical tapes. For
   instructions, see [Recovering
   Client Computer Data](http://technet.microsoft.com/en-us/library/hh757887.aspx "http://technet.microsoft.com/en-us/library/hh757887.aspx") on the DPM website.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
