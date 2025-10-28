# Testing your setup by using OpenText Data

Protector

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using OpenText Data Protector. In this topic, you can find
basic documentation on how to configure the OpenText Data Protector software for a
Tape Gateway and perform a backup and restore operation. For detailed information about how
to use the OpenText Data Protector software, see the OpenText Data Protector documentation.
For more information about compatible backup applications, see [Supported third-party backup
applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

###### Topics

- [Configuring OpenText Data Protector
  to Work with VTL Devices](#hpdataprotector-configure-software "#hpdataprotector-configure-software")
- [Preparing Virtual Tapes for Use with
  Data Protector](#hpdataprotector-prepare-tapes "#hpdataprotector-prepare-tapes")
- [Loading Tapes into a Media
  Pool](#hpdataprotector-load-tapes-into-media-pool "#hpdataprotector-load-tapes-into-media-pool")
- [Backing Up Data to a Tape](#hpdataprotector-backup-to-tape "#hpdataprotector-backup-to-tape")
- [Archiving a Tape](#hpdataprotector-archive-tape "#hpdataprotector-archive-tape")
- [Restoring Data from a Tape](#hpdataprotector-restore-tape "#hpdataprotector-restore-tape")

## Configuring OpenText Data Protector

to Work with VTL Devices

After you have connected the virtual tape library (VTL) devices to the client, you
configure OpenText Data Protector to recognize your devices. For information about how
to connect VTL devices to the client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

The OpenText Data Protector software doesn't automatically recognize Tape Gateway
devices. To have the software recognize these devices, manually add the devices and then
discover the VTL devices, as described following.

###### To add the VTL devices

1. In the OpenText Data Protector main window, choose the **Devices &
   Media** shelf in the list at top left.

Open the context (right-click) menu for **Devices**, and
choose **Add Device**. 2. On the **Add Device** tab, type a value for **Device
Name**. For **Device Type**, choose **SCSI
Library**, and then choose **Next**. 3. On the next screen, do the following:

    1. For **SCSI address of the library robotic**, select
     your specific address.
    2. For **Select what action Data Protector should take if the
     drive is busy**, choose "Abort" or your preferred action.
    3. Choose to activate these options:




    	* **Barcode reader support**
    	* **Automatically discover changed SCSI
    	 address**
    	* **SCSI Reserve/Release (robotic
    	 control)**
    4. Leave **Use barcode as medium label on
     initialization** clear (unchecked), unless your system
     requires it.
    5. Choose **Next** to continue.

4. On the next screen, specify the slots that you want to use with HP Data
   Protector. Use a hyphen ("-") between numbers to indicate a range of slots, for
   example 1–6. When you've specified slots to use, choose
   **Next**.
5. For the standard type of media used by the physical device, choose
   **LTO_Ultrium**, and then choose
   **Finish** to complete the setup.

Your tape library is now ready to use. To load tapes into it, see the next
section.

## Preparing Virtual Tapes for Use with

Data Protector

Before you can back up data to a virtual tape, you need to prepare the tape for use.
Doing this involves the following actions:

- Load a virtual tape into a tape library
- Load the virtual tape into a slot
- Create a media pool
- Load the virtual tape into media pool

In the following sections, you can find steps to guide you through this process.

### Loading Virtual Tapes into

a Tape Library

Your tape library should now be listed under **Devices**. If you
don't see it, press F5 to refresh the screen. When your library is listed, you can
load virtual tapes into the library.

###### To load virtual tapes into your tape library

1.  Choose the plus sign next to your tape library to display the nodes for
    robotics paths, drives, and slots.
2.  Open the context (right-click) menu for **Drives**,
    choose **Add Drive**, type a name for your tape, and then
    choose **Next** to continue.
3.  Choose the tape drive you want to add for **SCSI address of data
    drive**, choose **Automatically discover changed SCSI
    address**, and then choose **Next**.
4.  On the following screen, choose **Advanced**. The
    **Advanced Options** pop-up screen appears.
    1.  On the **Settings** tab, you should consider the
        following options:

            * **CRC Check** (to detect accidental data
             changes)
            * **Detect dirty drive** (to ensure the
             drive is clean before backup)
            * **SCSI Reserve/Release(drive)** (to avoid
             tape contention)

        For testing purposes, you can leave these options deactivated
        (unchecked).

    2.  On the **Sizes** tab, set the **Block
        size (kB)** to **Default (256)**.
    3.  Choose **OK** to close the advanced options
        screen, and then choose **Next** to
        continue.

5.  On the next screen, choose these options under **Device
    Policies**:
    - **Device may be used for restore**
    - **Device may be used as source device for object
      copy**

6.  Choose **Finish** to finish adding your tape drive to
    your tape library.

### Loading Virtual

Tapes into Slots

Now that you have a tape drive in your tape library, you can load virtual tapes
into slots.

###### To load a tape into a slot

1. In the tape library tree node, open the node labeled
   **Slots**. Each slot has a status represented by an
   icon:
   - A green tape means that a tape is already loaded into the
     slot.
   - A gray slot means that the slot is empty.
   - A cyan question mark means that the tape in that slot is not
     formatted.

2. For an empty slot, open the context (right-click) menu, and then choose
   **Enter**. If you have existing tapes, choose one to
   load into that slot.

### Creating a Media Pool

A _media pool_ is a logical group used to organize your tapes.
To set up tape backup, you create a media pool.

###### To create a media pool

1. In the **Devices & Media** shelf, open the tree node
   for **Media**, open the context (right-click) menu for the
   **Pools** node, and then choose **Add Media
   Pool**.
2. For **Pool name**, type a name.
3. For **Media Type**, choose
   **LTO_Ultrium**, and then choose
   **Next**.
4. On the following screen, accept the default values, and then choose
   **Next**.
5. Choose **Finish** to finish creating a media pool.

## Loading Tapes into a Media

Pool

Before you can back up data onto your tapes, you must load the tapes into the media
pool that you created.

###### To load a virtual tape into a media pool

1. On your tape library tree node, choose the **Slots** node.
2. Choose a loaded tape, one that has a green icon showing a loaded tape. Open
   the context (right-click) menu and choose **Format**, and then
   choose **Next**.
3. Choose the media pool you created, and then choose
   **Next**.
4. For **Medium Description**, choose **Use
   barcode**, and then choose **Next**.
5. For **Options**, choose **Force Operation**,
   and then choose **Finish**.

You should now see your chosen slot change from a status of unassigned (gray) to a
status of tape inserted (green). A series of messages appear to confirm that your media
is initialized.

At this point, you should have everything configured to begin using your virtual tape
library with Data Protector. To double-check that this is the case, use the following
procedure.

###### To verify that your tape library is configured for use

- Choose **Drives**, then open the context (right-click) menu
  for your drive, and choose **Scan**.

If your configuration is correct, a message confirms that your media was successfully
scanned.

## Backing Up Data to a Tape

When your tapes have been loaded into a media pool, you can back up data to
them.

###### To back up data to a tape

1. Choose **Backup** from the drop-down menu at the top-left
   corner of the window.
2. Expand the **Backup** navigation tree from the left
   pane.
3. Right-click on **Filesystem** to open the context menu, and
   then choose **Add Backup**.
4. On the **Create New Backup** screen, under
   **Filesystem**, choose **Blank File System
   Backup**, and then choose **OK**.
5. On the tree node that shows your host system, select the file system or file
   systems that you want to back up, and choose **Next** to
   continue.
6. Open the tree node for the tape library you want to use, open the context
   (right-click) menu for the tape drive you want to use, and then choose
   **Properties**.
7. Choose your media pool, choose **OK**, and then choose
   **Next**.
8. For the next three screens, accept the default settings and choose
   **Next**.
9. On the **Perform finishing steps in your backup/template
   design** screen, choose **Save as** to save this
   session. In the pop-up window, give the backup a name and assign it to the group
   where you want to save your new backup specification.
10. Choose **Start Interactive Backup**.

If the host system contains a database system, you can choose it as your target backup
system. The screens and selections are similar to the file-system backup just
described.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will fail, and the tape drive in Data Protector is marked as
**Dirty**. Data Protector also marks the tape quality as
**Poor**, and prevents writing to the tape. To continue reading
data from the tape, you must clean the drive and re-mount the tape. To complete the
failed backup job, you must resubmit it on a new tape.

## Archiving a Tape

When you archive a tape, Tape Gateway moves the tape from the tape library to the
offline storage. Before you eject and archive a tape, you might want to check the
content on it.

###### To check a tape's content before archiving it

1. Choose **Slots** and then choose the tape you want to check.
2. Choose **Objects** and check what content is on the
   tape.

When you have chosen a tape to archive, use the following procedure.

###### To eject and archive a tape

1. Open the context (right-click) menu for that tape, and choose
   **Eject**.
2. On the Storage Gateway console, choose your gateway, and then choose **VTL
   Tape Cartridges** and verify the status of the virtual tape you are
   archiving.

After the tape is ejected, it will be automatically archived in the offline storage
(S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive). The archiving process
can take some time to complete. The initial status of the tape is shown as **IN
TRANSIT TO VTS**. When archiving starts, the status changes to
**ARCHIVING**. When archiving is completed, the tape is no longer
listed in the VTL but is archived in S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive.

## Restoring Data from a Tape

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape to a Tape Gateway. For instructions, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use Data Protector to restore the data. This process is the same as restoring
   data from physical tapes.

To restore data from a tape, use the following procedure.

###### To restore data from a tape

1. Choose **Restore** from the drop-down menu at the top-left
   corner of the window.
2. Choose the file system or database system you want to restore from the left
   navigation tree. For the backup that you want to restore, make sure that the box
   is selected. Choose **Restore**.
3. In the **Start Restore Session** window, choose
   **Needed Media**. Choose **All media**,
   and you should see the tape originally used for the backup. Choose that tape,
   and then choose **Close**.
4. In the **Start Restore Session** window, accept the default
   settings, choose **Next**, and then choose
   **Finish**.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
