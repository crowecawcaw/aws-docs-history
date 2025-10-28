# Testing Your Setup by Using Bacula Enterprise

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using Bacula Enterprise. In this topic, you can find basic
documentation on how to configure the Bacula version 10 backup application for a
Tape Gateway and perform backup and restore operations. For detailed information about how
to use Bacula, see [Bacula
Systems Manuals and Documentation](https://www.baculasystems.com/bacula-systems-documentation-datasheet "https://www.baculasystems.com/bacula-systems-documentation-datasheet") or contact Bacula Systems.

###### Note

Bacula is only supported on Linux.

## Setting Up Bacula Enterprise

After you have connected your virtual tape library (VTL) devices to your Linux client,
you configure the Bacula software to recognize your devices. For information about how
to connect VTL devices to your client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

###### To set up Bacula

1. Get a licensed copy of the Bacula Enterprise backup software from Bacula
   Systems.
2. Install the Bacula Enterprise software on your on-premises or in-cloud
   computer.

For information about how to get the installation software, see [Enterprise Backup for Amazon S3 and Storage Gateway](https://www.baculasystems.com/corporate-data-backup-software-solutions/enterprise-backup-for-amazon-s3 "https://www.baculasystems.com/corporate-data-backup-software-solutions/enterprise-backup-for-amazon-s3"). For additional
installation guidance, see the Bacula whitepaper [Using Cloud Services and Object Storage with Bacula Enterprise
Edition](https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf "https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf").

## Configuring Bacula to Work with VTL Devices

Next, configure Bacula to work with your VTL devices. Following, you can find basic
configuration steps.

###### To configure Bacula

1. Install the Bacula Director and the Bacula Storage daemon. For instructions,
   see chapter 7 of the [Using Cloud Services and Object Storage with Bacula Enterprise
   Edition](https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf "https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf") Bacula white paper.
2. Connect to the system that is running Bacula Director and configure the iSCSI
   initiator. To do so, use the script provided in step 7.4 in the [Using Cloud Services and Object Storage with Bacula Enterprise
   Edition](https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf "https://www.baculasystems.com/wp-content/uploads/ObjectStorage_Bacula_Enterprise.pdf") Bacula whitepaper.
3. Configure the storage devices. Use the script provided in the Bacula
   whitepaper discussed preceding.
4. Configure the local Bacula Director, add storage targets, and define media
   pools for your tapes. Use the script provided in the Bacula whitepaper discussed
   preceding.

## Backing Up Data to Tape

1. Create tapes in the Storage Gateway console. For information on how to create
   tapes, see [Creating
   Tapes](GettingStartedCreateTapes.md "GettingStartedCreateTapes.md").
2. Transfer tapes from the I/E slot to the storage slot by using the following
   command.

`/opt/bacula/scripts/mtx-changer`

For example, the following command transfers tapes from I/E slot 1601 to
storage slot 1.

`/opt/bacula/scripts/mtx-changer transfer 1601 1` 3. Launch the Bacula console by using the following command.

`/opt/bacula/bin/bconsole`

###### Note

When you create and transfer a tape to Bacula, use the Bacula console
(bconsole) command `update slots storage=VTL` so that Bacula
knows about the new tapes that you created. 4. Label the tape with the barcode as the volume name or label by using the
following bconsole command.

`label storage=VTL pool=pool.VTL barcodes === label the tapes with the
 barcode as the volume name / label` 5. Mount the tape by using the following command.

`mount storage=VTL slot=1 drive=0` 6. Create a backup job that uses the media pools you created, and then write data
to the virtual tape by using the same procedures that you do with physical
tapes. 7. Unmount the tape from the Bacula console by using the following
command.

`umount storage=VTL slot=1 drive=0`

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will fail, and the tape status in Bacula Enterprise will change to
**FULL**. If you know the tape has not been fully utilized, you
can manually change the tape status back to **APPEND** and continue
the backup job using the same tape. You can also continue the job on a different
tape if other tapes in **APPEND** status are available.

## Archiving a Tape

When all backup jobs for a particular tape are done and you can archive the tape, use
the mtx-changer script to move the tape from the storage slot to the I/E slot. This
action is similar to the eject action in other backup applications.

###### To archive a tape

1. Transfer the tape from the storage slot to the I/E slot by using the
   `/opt/bacula/scripts/mtx-changer` command.

For example, the following command transfers a tape from the storage slot 1 to
I/E slot 1601.

`/opt/bacula/scripts/mtx-changer transfer 1 1601` 2. Verify that the tape is archived in the offline storage
(S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive) and that the
tape has the status **Archived**.

## Restoring Data from an Archived and

Retrieved Tape

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions,
   see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Restore your data by using the Bacula software:
   1. Import the tapes into the storage slot by using the
      `/opt/bacula/scripts/mtx-changer` command to transfer
      tapes from the I/E slot.

   For example, the following command transfers tapes from I/E slot 1601
   to storage slot 1.

   `/opt/bacula/scripts/mtx-changer transfer 1601 1` 2. Use the Bacula console to update the slots, and then mount the
   tape. 3. Run the restore command to restore your data. For instructions, see
   the Bacula documentation.
