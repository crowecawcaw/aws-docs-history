# Testing your setup by using NovaStor DataCenter

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using NovaStor DataCenter/Network. In this topic, you can find
basic documentation on how to configure the NovaStor DataCenter/Network backup application
for a Tape Gateway and perform backup and restore operations. For detailed information
about how to use NovaStor DataCenter/Network, refer to the NovaStor DataCenter/Network
documentation.

## Setting Up NovaStor DataCenter/Network

After you have connected your virtual tape library (VTL) devices to your Microsoft
Windows client, you configure the NovaStor software to recognize your devices. For
information about how to connect VTL devices to your Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

NovaStor DataCenter/Network requires drivers from the driver manufacturers. You can
use the Windows drivers, but you must first deactivate other backup applications.

## Configuring NovaStor DataCenter/Network to Work with

VTL Devices

When configuring your VTL devices to work with NovaStor DataCenter/Network, you might
see an error message that reads `External Program did not exit correctly`.
This issue requires a workaround, which you need to perform before you continue.

You can prevent the issue by creating the workaround before you start configuring your
VTL devices. For information about how to create the workaround, see [Resolving an "External Program Did Not Exit
Correctly" Error](#novastor-workaround "#novastor-workaround").

###### To configure NovaStor DataCenter/Network to work with VTL devices

1. In the NovaStor DataCenter/Network Admin console, choose **Media
   Management**, and then choose **Storage
   Management**.
2. In the **Storage Targets** menu, open the context menu
   (right-click) for **Media Management Servers**, choose
   **New**, and choose **OK** to create and
   prepopulate a **storage** node.

If you see an error message that says `External Program did not exit
 correctly`, resolve the issue before you continue. This issue requires
a workaround. For information about how to resolve this issue, see [Resolving an "External Program Did Not Exit
Correctly" Error](#novastor-workaround "#novastor-workaround").

###### Important

This error occurs because the element assignment range from AWS Storage Gateway
for storage drives and tape drives exceeds the number that NovaStor
DataCenter/Network allows. 3. Open the context (right-click) menu for the **storage** node
that was created, and choose **New Library**. 4. Choose the library server from the list. The library list is automatically
populated. 5. Name the library and choose **OK**. 6. Choose the library to display all the properties of the Storage Gateway virtual
tape library. 7. In the **Storage Targets** menu, expand **Backup
Servers**, open the context (right-click) menu for the server, and
choose **Attach Library**. 8. In the **Attach Library** dialog box that appears, choose the
**LTO5** media type, and then choose
**OK**. 9. Expand **Backup Servers** to see the Storage Gateway virtual
tape library and the library partition that shows all the mounted tape
drives.

## Creating a Tape Pool

A tape pool is dynamically created in the NovaStor DataCenter/Network software and so
doesn't contain a fixed number of media. A tape pool that needs a tape gets it from its
scratch pool. A _scratch pool_ is a reservoir of tapes
that are freely available for one or more tape pools to use. A tape pool returns to the
scratch pool any media that have exceeded their retention times and that are no longer
needed.

Creating a tape pool is a three-step task:

1. You create a scratch pool.
2. You assign tapes to the scratch pool.
3. You create a tape pool.

###### To create a scratch pool

1. In the left navigation menu, choose the **Scratch Pools**
   tab.
2. Open the context (right-click) menu for **Scratch Pools**,
   and choose **Create Scratch Pool**.
3. In the **Scratch Pools** dialog box, name your scratch pool,
   and then choose your media type.
4. Choose **Label Volume**, and create a low water mark for the
   scratch pool. When the scratch pool is emptied down to the low water mark, a
   warning appears.
5. In the warning dialog box that appears, choose **OK** to
   create the scratch pool.

###### To assign tapes to a scratch pool

1. In the left navigation menu, choose **Tape Library
   Management**.
2. Choose the **Library** tab to see your library's
   inventory.
3. Choose the tapes that you want to assign to the scratch pool. Make sure that
   the tapes are set to the correct media type.
4. Open the context (right-click) menu for the library and choose **Add
   to Scratch Pool**.

You now have a filled scratch pool that you can use for tape pools.

###### To create a tape pool

1. From the left navigation menu, choose **Tape Library
   Management**.
2. Open the context (right-click) menu for the **Media Pools**
   tab and choose **Create Media Pool**.
3. Name the media pool and choose **Backup Server**.
4. Choose a library partition for the media pool.
5. Choose the scratch pool that you want the pool to get the tapes from.
6. For **Schedule**, choose **Not
   Scheduled**.

## Configuring Media Import and Export to Archive

Tapes

NovaStor DataCenter/Network can use import/export slots if they are part of the media
changer.

For an export, NovaStor DataCenter/Network must know which tapes are going to be
physically taken out of the library.

For an import, NovaStor DataCenter/Network recognizes tape media that are exported in
the tape library and offers to import them all, either from a data slot or an export
slot. Your Tape Gateway archives tapes in the offline storage
(S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive).

###### To configure media import and export

1. Navigate to **Tape Library Management**, choose a server for
   **Media Management Server**, and then choose
   **Library**.
2. Choose the **Off-site Locations** tab.
3. Open the context (right-click) menu for the white area, and choose
   **Add** to open a new panel.
4. In the panel, type `S3 Glacier Flexible Retrieval` or
   `S3 Glacier Deep Archive` and add an optional
   description in the text box.

## Backing Up Data to Tape

You create a backup job and write data to a virtual tape by using the same procedures
that you do with physical tapes. For detailed information about how to back up data
using the NovaStor software, see [Documentation NovaStor DataCenter/Network](https://dcmanual.novastor.com/help-html/dc/en/StartBackupJob.html "https://dcmanual.novastor.com/help-html/dc/en/StartBackupJob.html").

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will fail, and the tape will become unwriteable. You can archive the tape
or continue to read data from it. To complete the failed backup job, you must
resubmit it on a new tape.

## Archiving a Tape

When you archive a tape, a Tape Gateway ejects the tape from the tape drive to the
storage slot. It then exports the tape from the slot to the archive by using your backup
application—that is, NovaStor DataCenter/Network.

###### To archive a tape

1. In the left navigation menu, choose **Tape Library
   Management**.
2. Choose the **Library** tab to see the library's
   inventory.
3. Highlight the tapes you want to archive, open the context (right-click) menu
   for the tapes, and choose your off-site archive location.

The archiving process can take some time to complete. The initial status of the tape
appears as **IN TRANSIT TO VTS**. When archiving starts, the status
changes to **ARCHIVING**. When archiving is completed, the tape is no
longer listed in the VTL.

In NovaStor DataCenter/Network, verify that the tape is no longer in the storage
slot.

In the navigation pane of the Storage Gateway console, choose **Tapes**.
Verify that your archived tape's status is **ARCHIVED**.

## Restoring Data from an Archived and

Retrieved Tape

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions,
   see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use the NovaStor DataCenter/Network software to restore the data. You do this
   by refreshing the mail slot and moving each tape you want to retrieve into an
   empty slot, as you do when restoring data from physical tapes. For information
   about restoring data, see [Documentation NovaStor DataCenter/Network](https://dcmanual.novastor.com/help-html/dc/en/RestoretheExample.html "https://dcmanual.novastor.com/help-html/dc/en/RestoretheExample.html").

## Writing Several Backup Jobs to a Tape Drive at the Same

Time

In the NovaStor software, you can write several jobs to a tape drive at the same time
using the multiplexing feature. This feature is available when a multiplexer is
available for a media pool. For information about how to use multiplexing, see [Documentation NovaStor DataCenter/Network](https://dcmanual.novastor.com/help-html/dc/en/DefineBackupDestinationandSchedu.html "https://dcmanual.novastor.com/help-html/dc/en/DefineBackupDestinationandSchedu.html").

## Resolving an "External Program Did Not Exit

Correctly" Error

When configuring your VTL devices to work with NovaStor DataCenter/Network, you might
see an error message that reads `External Program did not exit correctly`.
This error occurs because the element assignment range from Storage Gateway for storage drives
and tape drives exceeds the number that NovaStor DataCenter/Network allows.

Storage Gateway returns 3200 storage and import/export slots, which is more than the 2400
limit that NovaStor DataCenter/Network allows. To resolve this issue, you add a
configuration file that activates the NovaStor software to limit the number of storage
and import/export slots and preconfigures the element assignment range.

###### To apply the workaround for an "external program did not exit correctly"

error

1. Navigate to the Tape folder on your computer where you installed the NovaStor
   software.
2. In the Tape folder, create a text file and name it
   `hijacc.ini`.
3. Copy the following content, paste it into `hijacc.ini`
   file, and save the file.

```
port:12001
san:no
define: A3B0S0L0
*DRIVES: 10
*FIRST_DRIVE: 10000
*SLOTS: 200
*FIRST_SLOT: 20000
*HANDLERS: 1
*FIRST_HANDLER: 0
*IMP-EXPS: 30
*FIRST_IMP-EXP: 30000
```

4. Add and attach the library to the media management server.
5. Move a tape from the import/export slot into the library by using the
   following command. Replace the example library name with the name of the library
   in your deployment.

`C:\Program Files\NovaStor\DataCenter\Hitback\tape\ophijacc.exe -c
 `VTL-ec2amaz-uko8jfj-ec2amaz-uko8jfj.lcfg`` 6. Attach the library to the backup server. 7. In the NovaStor software, import all the tapes from import/export slots into
the library.
