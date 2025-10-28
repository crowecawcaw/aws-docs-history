# Testing Your Setup by Using Veritas NetBackup

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Veritas NetBackup. In this topic, you can find basic
documentation on how to configure the NetBackup application for a Tape Gateway and perform
a backup and restore operation.

For detailed information about how to use NetBackup, see the [Veritas Services and Operations Readiness Tools
(SORT)](https://sort.veritas.com/documents "https://sort.veritas.com/documents") page on the Veritas website.

For more information about compatible backup applications, see [Supported third-party backup
applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

###### Topics

- [Configuring NetBackup Storage
  Devices](#configure-netback-storage-devices "#configure-netback-storage-devices")
- [Backing Up Data to a Tape](#GettingStarted-backup-data-VTL "#GettingStarted-backup-data-VTL")
- [Archiving the Tape](#GettingStarted-archiving-tapes-vtl "#GettingStarted-archiving-tapes-vtl")
- [Restoring Data from the Tape](#restore-data-vtl "#restore-data-vtl")

## Configuring NetBackup Storage

Devices

After you have connected the virtual tape library (VTL) devices to the Windows client,
you configure Veritas NetBackup storage to recognize your devices. For information about
how to connect VTL devices to the Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

###### To configure NetBackup to use storage devices on your Tape Gateway

1. Open the NetBackup Administration Console as an administrator.
2. Choose **Configure Storage Devices** to open the Device
   Configuration wizard.
3. Choose **Next**. The NetBackup application detects your
   computer as a device host.
4. In the **Device Hosts** column, select your computer, and
   then choose **Next**. The NetBackup application scans your
   computer for devices and discovers all devices.
5. In the **Scanning Hosts** page, choose
   **Next**, and then choose **Next**. The
   NetBackup application finds all 10 tape drives and the medium changer on your
   computer.
6. In the **Backup Devices** window, choose
   **Next**.
7. In the **Drag and Drop Configuration** window, verify that
   your medium changer is selected, and then choose **Next.**
8. In the dialog box that appears, choose **Yes** to save the
   configuration on your computer. The NetBackup application updates the device
   configuration.
9. When the update is completed, choose **Next** to make the
   devices available to the NetBackup application.
10. In the **Finished!** window, choose
    **Finish**.

###### To verify your devices in the NetBackup application

1. In the NetBackup Administration Console, expand the **Media and Device
   Management** node, and then expand the **Devices**
   node. Choose **Drives** to display all the tape drives.
2. In the **Devices** node, choose **Robots**
   to display all your medium changers. In the NetBackup application, the medium
   changer is called a _robot_.
3. In the **All Robots** pane, open the context (right-click)
   menu for **TLD(0)** (that is, your robot), and then choose
   **Inventory Robot**.
4. In the **Robot Inventory** window, verify that your host is
   selected from the **Device-Host** list located in the
   **Select robot** category.
5. Verify that your robot is selected from the **Robot**
   list.
6. In the **Robot Inventory** window, select **Update
   volume configuration**, select **Preview
   changes**, select **Empty media access port prior to
   update**, and then choose **Start**.

The process then inventories your medium changer and virtual tapes in the
NetBackup Enterprise Media Management (EMM) database. NetBackup stores media
information, device configuration, and tape status in the EMM. 7. In the **Robot Inventory** window, choose
**Yes** once the inventory is complete. Choosing
**Yes** here updates the configuration and moves virtual
tapes found in import/export slots to the virtual tape library. 8. Close the **Robot Inventory** window. 9. In the **Media** node, expand the **Robots**
node and choose **TLD(0)** to show all virtual tapes that are
available to your robot (medium changer).

###### Note

If you have previously connected other devices to the NetBackup
application, you might have multiple robots. Make sure that you select the
right robot.

Now that you have connected your devices and made them available to your backup
application, you are ready to test your gateway. To test your gateway, you back up data
onto the virtual tapes you created and archive the tapes.

## Backing Up Data to a Tape

You test the Tape Gateway setup by backing up data onto your virtual tapes.

###### Note

- You should back up only a small amount of data for this Getting Started
  exercise, because there are costs associated with storing, archiving, and
  retrieving data. For pricing information, see [Pricing](https://aws.amazon.com/storagegateway/pricing "https://aws.amazon.com/storagegateway/pricing") on the Storage Gateway detail
  page.
- If your Tape Gateway restarts for any reason during an ongoing backup
  job, the backup job will be suspended. The suspended backup job will resume
  automatically when your gateway finishes restarting.

###### To create a volume pool

A _volume pool_ is a collection of virtual tapes to use for a
backup.

1. Start the NetBackup Administration Console.
2. Expand the **Media** node, open the context (right-click)
   menu for **Volume Pool**, and then choose
   **New**. The **New Volume Pool** dialog
   box appears.
3. For **Name**, type a name for your volume pool.
4. For **Description**, type a description for the volume pool,
   and then choose **OK**. The volume pool you just created is
   added to the volume pool list.

The following screenshot shows a list of volume pools.

###### To add virtual tapes to a volume pool

1. Expand the **Robots** node, and select the
   **TLD(0)** robot to display the virtual tapes this robot is
   aware of.

If you have previously connected a robot, your Tape Gateway robot might have
a different name. 2. From the list of virtual tapes, open the context (right-click) menu for the
tape you want to add to the volume pool, and choose **Change**
to open the **Change Volumes** dialog box. 3. For **Volume Pool**, choose **New
pool**. 4. For **New pool**, select the pool you just created, and then
choose **OK**.

You can verify that your volume pool contains the virtual tape that you just
added by expanding the **Media** node and choosing your volume
pool.

###### To create a backup policy

The backup policy specifies what data to back up, when to back it up, and which
volume pool to use.

1. Choose your **Master Server** to return to the Veritas
   NetBackup console.
2. Choose **Create a Policy** to open the **Policy
   Configuration Wizard** window.
3. Select **File systems, databases, applications**, and choose
   **Next**.
4. For **Policy Name**, type a name for your policy and verify
   that **MS-Windows** is selected from the **Select the
   policy type** list, and then choose
   **Next**.
5. In the **Client List** window, choose
   **Add**, type the host name of your computer in the
   **Name** column, and then choose **Next**.
   This step applies the policy you are defining to `localhost` (your
   client computer).
6. In the **Files** window, choose **Add**, and
   then choose the folder icon.
7. In the **Browse** window, browse to the folder or files you
   want to back up, choose **OK**, and then choose
   **Next**.
8. In the **Backup Types** window, accept the defaults, and then
   choose **Next**.

###### Note

If you want to initiate the backup yourself, select **User
Backup**. 9. In the **Frequency and Retention** window, select the
frequency and retention policy you want to apply to the backup. For this
exercise, you can accept all of the defaults and choose**Next**. 10. In the **Start** window, select **Off
hours**, and then choose **Next**. This selection
specifies that your folder should be backed up during off hours only. 11. In the **Policy Configuration** wizard, choose
**Finish**.

The policy runs the backups according to the schedule. You can also perform a manual
backup at any time, which we do in the next step.

###### To perform a manual backup

1. On the navigation pane of the NetBackup console, expand the
   **NetBackup Management** node.
2. Expand the **Policies** node.
3. Open the context (right-click) menu for your policy, and choose
   **Manual Backup**.
4. In the **Manual Backup** window, select a schedule, select a
   client, and then choose **OK**.
5. In the **Manual Backup Started** dialog box that appears,
   choose **OK**.
6. On the navigation pane, choose **Activity Monitor** to view
   the status of your backup in the **Job ID** column.

To find the barcode of the virtual tape where NetBackup wrote the file data during the
backup, look in the **Job Details** window as described in the
following procedure. You need this barcode in the procedure in the next section, where
you archive the tape.

###### To find the barcode of a tape

1. In **Activity Monitor**, open the context (right-click) menu
   for the identifier of your backup job in the **Job ID** column,
   and then choose **Details**.
2. In the **Job Details** window, choose the **Detailed
   Status** tab.
3. In the **Status** box, locate the media ID. For example, an
   entry in the status report might read `media id 87A222`. This ID
   helps you determine which tape you have written data to.

You have now successfully deployed a Tape Gateway, created virtual tapes, and backed
up your data. Next, you can archive the virtual tapes and retrieve them from the
archive.

## Archiving the Tape

When you archive a tape, Tape Gateway moves the tape from your gateway’s virtual tape
library (VTL) to the archive, which provides offline storage. You initiate tape archival
by ejecting the tape using your backup application.  

###### To archive a virtual tape

1. In the NetBackup Administration console, expand the **Media and Device
   Management** node, and expand the **Media**
   node.
2. Expand **Robots** and choose **TLD**(0).
3. Open the context (right-click) menu for the virtual tape you want to archive,
   and choose **Eject Volume From Robot**.
4. In the **Eject Volumes** window, make sure the
   **Media ID** matches the virtual tape you want to eject,
   and then choose **Eject**.
5. In the dialog box, choose **Yes**.

When the eject process is completed, the status of the tape in the
**Eject Volumes** dialog box indicates that the eject
succeeded. 6. Choose **Close** to close the **Eject
Volumes** window. 7. In the Storage Gateway console, verify the status of the tape you are archiving in the
gateway's VTL. It can take some time to finish uploading data to AWS. During
this time, the ejected tape is listed in the gateway's VTL with the status
**IN TRANSIT TO VTS**. When archiving starts, the status is
**ARCHIVING**. Once data upload has completed, the ejected
tape is no longer listed in the VTL but is archived in
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. 8. To verify that the virtual tape is no longer listed in your gateway, choose
your gateway, and then choose **VTL Tape Cartridges**. 9. In the navigation pane of the Storage Gateway console, choose
**Tapes**. Verify that your archived tape's status is
**ARCHIVED**.

## Restoring Data from the Tape

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape to a Tape Gateway. For instructions, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use the Backup, Archive, and Restore software installed with the Veritas
   NetBackup application. This process is the same as restoring data from physical
   tapes. For instructions, see [Veritas Services and Operations Readiness Tools (SORT)](https://sort.veritas.com/documents "https://sort.veritas.com/documents") on the
   Veritas website.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
