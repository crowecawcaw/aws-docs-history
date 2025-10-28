# Testing Your Setup by Using Commvault

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Commvault. In this topic, you can find basic
documentation on how to configure the Commvault backup application for a Tape Gateway,
perform a backup archive, and retrieve your data from archived tapes. For detailed
information about how to use Commvault, refer to the Commvault documentation.

###### Topics

- [Configuring Commvault to Work with VTL
  Devices](#commvault-configure-software "#commvault-configure-software")
- [Creating a Storage Policy and a
  Subclient](#commvault-prepare-tapes "#commvault-prepare-tapes")
- [Backing Up Data to a Tape in Commvault](#commvault-backup-data "#commvault-backup-data")
- [Archiving a Tape in Commvault](#commvault-archive-tape "#commvault-archive-tape")
- [Restoring Data from a Tape](#commvault-restore-data "#commvault-restore-data")

## Configuring Commvault to Work with VTL

Devices

After you connect the VTL devices to the Windows client, you configure Commvault to
recognize them. For information about how to connect VTL devices to the Windows client,
see [Connecting your VTL devices to a Windows
client](ConfiguringiSCSIClient-vtl.md "ConfiguringiSCSIClient-vtl.md").

The Commvault backup application doesn't automatically recognize VTL devices. You
must manually add devices to expose them to the Commvault backup application and then
discover the devices.

###### To configure Commvault

1. In the CommCell console main menu, choose **Storage**, and
   then choose **Expert Storage Configuration** to open the
   **Select MediaAgents** dialog box.
2. Choose the available media agent you want to use, choose
   **Add**, and then choose **OK**.
3. In the **Expert Storage Configuration** dialog box, choose
   **Start**, and then choose **Detect/Configure
   Devices**.
4. Leave the **Device Type** options selected, choose
   **Exhaustive Detection**, and then choose
   **OK**.
5. In the **Confirm Exhaustive Detection** confirmation box,
   choose **Yes**.
6. In the **Device Selection** dialog box, choose your library
   and all its drives, and then choose **OK**. Wait for your
   devices to be detected, and then choose **Close** to close the
   log report.
7. Right-click your library, choose **Configure**, and then
   choose **Yes**. Close the configuration dialog box.
8. In the **Does this library have a barcode reader?** dialog
   box, choose **Yes**, and then for device type, choose
   **IBM ULTRIUM V5**.
9. In the CommCell browser, choose **Storage Resources**, and
   then choose **Libraries** to see your tape library.
10. To see your tapes in your library, open the context (right-click) menu for
    your library, and then choose **Discover Media**,
    **Media location**, **Media
    Library**.
11. To mount your tapes, open the context (right-click) menu for your media, and
    then choose **Load**.

## Creating a Storage Policy and a

Subclient

Every backup and restore job is associated with a storage policy and a subclient
policy.

A storage policy maps the original location of the data to your media.

###### To create a storage policy

1. In the CommCell browser, choose **Policies**.
2. Open the context (right-click) menu for **Storage Policies**,
   and then choose **New Storage Policy**.
3. In the Create Storage Policy wizard, choose **Data Protection and
   Archiving**, and then choose **Next**.
4. Type a name for **Storage Policy Name**, and then choose
   **Incremental Storage Policy**. To associate this storage
   policy with incremental loads, choose one of the options. Otherwise, leave the
   options unchecked, and then choose **Next**.
5. In the **Do you want to Use Global Deduplication Policy?**
   dialog box, choose your **Deduplication** preference, and then
   choose **Next**.
6. From **Library for Primary Copy**, choose your VTL library,
   and then choose **Next**.
7. Verify that your media agent settings are correct, and then choose
   **Next**.
8. Verify that your scratch pool settings are correct, and then choose
   **Next**.
9. Configure your retention policies in **iData Agent Backup
   data**, and then choose **Next**.
10. Review the encryption settings, and then choose
    **Next**.
11. To see your storage policy, choose **Storage
    Policies**.

You create a subclient policy and associate it with your storage policy. A subclient
policy allows you to configure similar file system clients from a central template, so
that you don't have to set up many similar file systems manually.

###### To create a subclient policy

1. In the CommCell browser, choose **Client Computers**, and
   then choose your client computer. Choose **File System**, and
   then choose **defaultBackupSet**.
2. Right-click **defaultBackupSet**, choose **All
   Tasks**, and then choose **New Subclient**.
3. In the **Subclient** properties box, type a name in
   **SubClient Name**, and then choose
   **OK**.
4. Choose **Browse**, navigate to the files that you want to
   back up, choose **Add**, and then close the dialog box.
5. In the **Subclient** property box, choose the
   **Storage Device** tab, choose a storage policy from
   **Storage policy**, and then choose
   **OK**.
6. In the **Backup Schedule** window that appears, associate the
   new subclient with a backup schedule.
7. Choose **Do Not Schedule** for one time or on-demand backups,
   and then choose **OK**.

You should now see your subclient in the **defaultBackupSet**
tab.

## Backing Up Data to a Tape in Commvault

You create a backup job and write data to a virtual tape by using the same procedures
you use with physical tapes. For more information, refer to the Commvault
documentation.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job might fail. In some cases, you can select an option to resume the failed
job. Otherwise, you must submit a new job. If Commvault marks the tape as unusable
after a job fails, you must reload the tape into the drive to continue writing to
it. If multiple tapes are available, Commvault might continue the failed backup job
on a different tape.

## Archiving a Tape in Commvault

You start the archiving process by ejecting the tape. When you archive a tape,
Tape Gateway moves the tape from the tape library to offline storage. Before you eject
and archive a tape, you might want to first check the content on the tape.

###### To archive a tape

1. In the CommCell browser, choose **Storage Resources**,
   **Libraries**, and then choose **Your
   library**. Choose **Media By Location**, and then
   choose **Media In Library**.
2. Open the context (right-click) menu for the tape you want to archive, choose
   **All Tasks**, choose **Export**, and then
   choose **OK**.

The archiving process can take some time to complete. The initial status of the tape
appears as **IN TRANSIT TO VTS**. When archiving starts, the status
changes to **ARCHIVING**. When archiving is completed, the tape is no
longer listed in the VTL.

In the Commvault software, verify that the tape is no longer in the storage
slot.

In the navigation pane of the Storage Gateway console, choose **Tapes**.
Verify that your archived tape's status is **ARCHIVED**.

## Restoring Data from a Tape

You can restore data from a tape that has never been archived and retrieved, or from a
tape that has been archived and retrieved. For tapes that have never been archived and
retrieved (nonretrieved tapes), you have two options to restore the data:

- Restore by subclient
- Restore by job ID

###### To restore data from a nonretrieved tape by subclient

1. In the CommCell browser, choose **Client Computers**, and
   then choose your client computer. Choose **File System**, and
   then choose **defaultBackupSet.**
2. Open the context (right-click) menu for your subclient, choose
   **Browse and Restore**, and then choose **View
   Content**.
3. Choose the files you want to restore, and then choose **Recover All
   Selected**.
4. Choose **Home**, and then choose **Job
   Controller** to monitor the status of your restore job.

###### To restore data from a nonretrieved tape by job ID

1. In the CommCell browser, choose **Client Computers**, and
   then choose your client computer. Right-click **File System**,
   choose **View**, and then choose **Backup
   History**.
2. In the **Backup Type** category, choose the type of backup
   jobs you want, and then choose **OK**. A tab with the history
   of backup jobs appears.
3. Find the **Job ID** you want to restore, right-click it, and
   then choose **Browse and Restore**.
4. In the **Browse and Restore Options** dialog box, choose
   **View Content**.
5. Choose the files that you want to restore, and then choose **Recover
   All Selected**.
6. Choose **Home**, and then choose **Job
   Controller** to monitor the status of your restore job.

###### To restore data from an archived and retrieved tape

1. In the CommCell browser, choose **Storage Resources**, choose
   **Libraries**, and then choose **Your
   library**. Choose **Media By Location**, and then
   choose **Media In Library**.
2. Right-click the retrieved tape, choose **All Tasks**, and
   then choose **Catalog.**
3. In the **Catalog Media** dialog box, choose **Catalog
   only**, and then choose **OK**.
4. Choose **CommCell Home**, and then choose **Job
   Controller** to monitor the status of your restore job.
5. After the job succeeds, open the context (right-click) menu for your tape,
   choose **View**, and then choose **View Catalog
   Contents**. Take note of the **Job ID** value for
   use later.
6. Choose **Recatalog/Merge**. Make sure that **Merge
   only** is chosen in the **Catalog Media** dialog
   box.
7. Choose **Home**, and then choose **Job
   Controller** to monitor the status of your restore job.
8. After the job succeeds, choose **CommCell Home**, choose
   **Control Panel**, and then choose
   **Browse/Search/Recovery**.
9. Choose **Show aged data during browse and recovery**, choose
   **OK**, and then close the **Control
   Panel**.
10. In the CommCell browser, right-click **Client Computers**,
    and then choose your client computer. Choose **View**, and then
    choose **Job History**.
11. In the **Job History Filter** dialog box, choose
    **Advanced**.
12. Choose **Include Aged Data**, and then choose
    **OK**.
13. In the **Job History** dialog box, choose
    **OK** to open the **history of jobs**
    tab.
14. Find the job that you want to restore, open the context (right-click) menu for
    it, and then choose **Browse and Restore**.
15. In the **Browse and Restore** dialog box, choose
    **View Content**.
16. Choose the files that you want to restore, and then choose **Recover
    All Selected.**
17. Choose **Home**, and then choose **Job
    Controller** to monitor the status of your restore job.
