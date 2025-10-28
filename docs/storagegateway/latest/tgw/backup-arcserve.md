# Testing your setup by using Arcserve Backup

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Arcserve Backup. In this topic, you can find basic
documentation to configure Arcserve Backup with a Tape Gateway and perform a backup and
restore operation. For detailed information about to use Arcserve Backup, refer to the
Arcserve Backup documentation.

###### Topics

- [Configuring Arcserve to Work with VTL
  Devices](#archServe-configure-software "#archServe-configure-software")
- [Loading Tapes into a Media Pool](#archServe-load-tapes "#archServe-load-tapes")
- [Backing Up Data to a Tape](#archServe-backup-data "#archServe-backup-data")
- [Archiving a Tape](#archServe-archive-tape "#archServe-archive-tape")
- [Restoring Data from a Tape](#archServe-restore-tape "#archServe-restore-tape")

## Configuring Arcserve to Work with VTL

Devices

After you have connected your virtual tape library (VTL) devices to your client, you
scan for your devices.

###### To scan for VTL devices

1. In the Arcserve Backup Manager, choose the **Utilities**
   menu.
2. Choose **Media Assure and Scan**.

## Loading Tapes into a Media Pool

When the Arcserve software connects to your gateway and your tapes become available,
Arcserve automatically loads your tapes. If your gateway is not found in the Arcserve
software, try restarting the tape engine in Arcserve.

###### To restart the tape engine

1. Choose **Quick Start**, choose
   **Administration**, and then choose
   **Device**.
2. On the navigation menu, open the context (right-click) menu for your gateway
   and choose an import/export slot.
3. Choose **Quick Import** and assign your tape to an empty
   slot.
4. Open the context (right-click) menu for your gateway and choose
   **Inventory/Offline Slots**.
5. Choose **Quick Inventory** to retrieve media information from
   the database.

If you add a new tape, you need to scan your gateway for the new tape to have it
appear in Arcserve. If the new tapes don't appear, you must import the
tapes.

###### To import tapes

1. Choose the **Quick Start** menu, choose **Back
   up**, and then choose **Destination tap**.
2. Choose your gateway, open the context (right-click) menu for one tape, and
   then choose **Import/Export Slot**.
3. Open the context (right-click) menu for each new tape and choose
   **Inventory**.
4. Open the context (right-click) menu for each new tape and choose
   **Format**.

Each tape's barcode now appears in your Storage Gateway console, and each tape is ready
to use.

## Backing Up Data to a Tape

When your tapes have been loaded into Arcserve, you can back up data. The backup
process is the same as backing up physical tapes.

###### To back up data to a tape

1. From the **Quick Start** menu, open the restore a backup
   session.
2. Choose the **Source** tab, and then choose the file system or
   database system that you want to back up.
3. Choose the **Schedule** tab and choose the repeat method you
   want to use.
4. Choose the **Destination** tab and then choose the tape you
   want to use. If the data you are backing up is larger than the tape can hold,
   Arcserve prompts you to mount a new tape.
5. Choose **Submit** to back up your data.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job might fail. To complete the failed backup job, you must resubmit
it.

## Archiving a Tape

When you archive a tape, your Tape Gateway moves the tape from the tape library to
the offline storage. Before you eject and archive a tape, you might want to check the
content on it.

###### To archive a tape

1. From the **Quick Start** menu, open the restore a backup
   session.
2. Choose the **Source** tab, and then choose the file system or
   database system you want to back up.
3. Choose the **Schedule** tab and choose the repeat method you
   want to use.
4. Choose your gateway, open the context (right-click) menu for one tape, and
   then choose **Import/Export Slot**.
5. Assign a mail slot to load the tape. The status in the Storage Gateway console
   changes to **Archive**. The archive process might take some
   time.

The archiving process can take some time to complete. The initial status of the tape
appears as **IN TRANSIT TO VTS**. When archiving starts, the status
changes to **ARCHIVING**. When archiving is completed, the tape is no
longer listed in the VTL but is archived in S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive.

## Restoring Data from a Tape

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape to a Tape Gateway. For instructions, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use Arcserve to restore the data. This process is the same as restoring data
   from physical tapes. For instructions, refer to the Arcserve Backup
   documentation.

To restore data from a tape, use the following procedure.

###### To restore data from a tape

1. From the **Quick Start** menu, open the restore a restore
   session.
2. Choose the **Source** tab, and then choose the file system or
   database system you want to restore.
3. Choose the **Destination** tab and accept the default
   settings.
4. Choose the **Schedule** tab, choose the repeat method that
   you want to use, and then choose **Submit**.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
