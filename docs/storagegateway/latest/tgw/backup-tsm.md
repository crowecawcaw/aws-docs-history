# Testing Your Setup by Using IBM Data Protect

You can back up your data to virtual tapes, archive the tapes, and manage your virtual
tape library (VTL) devices by using IBM Data Protect with AWS Storage Gateway. (IBM Data Protect was
formerly known as Tivoli Storage Manager.)

This topic contains basic information about how to configure the IBM Data Protect backup
software for a Tape Gateway. It also includes basic information about performing backup and
restore operations with IBM Data Protect. For more information about how to administer IBM
Data Protect backup software, refer to the IBM Data Protect documentation.

The IBM Data Protect backup software supports AWS Storage Gateway on the following operating
systems.

- **Microsoft Windows Server**
- **Red Hat Linux**
  For information about IBM Data Protect supported devices for Windows, see [IBM Data Protect (formerly Tivoli
  Storage Manager) Supported Devices for AIX, HP-UX, Solaris, and Windows](https://www.ibm.com/support/pages/node/716993 "https://www.ibm.com/support/pages/node/716993").

For information about IBM Data Protect supported devices for Linux, see [IBM Data Protect (formerly Tivoli
Storage Manager) Supported Devices for Linux](https://www.ibm.com/support/pages/node/716987 "https://www.ibm.com/support/pages/node/716987").

###### Topics

- [Setting Up IBM Data Protect](#tsm-setup "#tsm-setup")
- [Configuring IBM Data Protect to Work with VTL
  Devices](#tsm-configure "#tsm-configure")
- [Writing Data to a Tape in IBM Data
  Protect](#tsm-write-data-to-tape "#tsm-write-data-to-tape")
- [Restoring Data from a Tape Archived in IBM Data
  Protect](#tsm-restore-tape "#tsm-restore-tape")

## Setting Up IBM Data Protect

After you connect your VTL devices to your client, you configure the IBM Data Protect
software to recognize them. For more information about connecting VTL devices to your
client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

###### To set up IBM Data Protect

1. Get a licensed copy of the IBM Data Protect software from IBM.
2. Install the IBM Data Protect software on your on-premises environment or
   in-cloud Amazon EC2 instance. For more information, see IBM's [Installing and upgrading](https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.common/t_installing_upgrading.html "https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.common/t_installing_upgrading.html") documentation for IBM Data Protect.

For more information about configuring IBM Data Protect software, see [Configuring AWS
Tape Gateway virtual tape libraries for an IBM Data Protect
server](https://www.ibm.com/support/pages/node/6326793 "https://www.ibm.com/support/pages/node/6326793").

## Configuring IBM Data Protect to Work with VTL

Devices

Next, configure IBM Data Protect to work with your VTL devices. You can configure IBM
Data Protect to work with VTL devices on Microsoft Windows Server or Red Hat
Linux.

### Configuring IBM Data Protect for

Windows

For complete instructions on how to configure IBM Data Protect on Windows, see
[Tape Device Driver-W12 6266 for Windows 2012](https://datacentersupport.lenovo.com/us/en/products/storage/tape-and-backup/ts2240/6160/downloads/ds502099 "https://datacentersupport.lenovo.com/us/en/products/storage/tape-and-backup/ts2240/6160/downloads/ds502099") on the Lenovo website.
Following is basic documentation on the process.

###### To configure IBM Data Protect for Microsoft Windows

1. Get the correct driver package for your media changer. For the tape-device
   driver, IBM Data Protect requires version W12 6266 for Windows 2012. For
   instructions on how to get the drivers, see [Tape Device Driver-W12 6266 for Windows 2012](https://datacentersupport.lenovo.com/us/en/products/storage/tape-and-backup/ts2240/6160/downloads/ds502099 "https://datacentersupport.lenovo.com/us/en/products/storage/tape-and-backup/ts2240/6160/downloads/ds502099") on the Lenovo
   website.

###### Note

Make sure that you install the "non-exclusive" set of drivers. 2. On your computer, open **Computer Management**,
expand **Media Changer devices**, and verify that the
media changer type is listed as **IBM 3584 Tape
Library**. 3. Ensure that the barcode for any tape in the virtual tape library is eight
characters or less. If you try to assign your tape a barcode that is longer
than eight characters, you get this error message: `"Tape barcode
 is too long for media changer"`. 4. Ensure that all your tape drives and media changer appear in IBM Data
Protect. To do so, use the following command:
`\Tivoli\TSM\server>tsmdlst.exe`

### Configure IBM Data Protect for Linux

Following is basic documentation on configuring IBM Data Protect to work with VTL
devices on Linux.

###### To configure IBM Data Protect for Linux

1. Go to [IBM Fix
   Central](https://www.ibm.com/support/fixcentral/ "https://www.ibm.com/support/fixcentral/") on the IBM Support website, and choose **Select
   product**.
2. For **Product Group**, choose **System
   Storage**.
3. For **Select from System Storage**, choose **Tape
   systems**.
4. For **Tape systems**, choose **Tape drivers and
   software**.
5. For **Select from Tape drivers and software**, choose
   **Tape device drivers**.
6. For **Platform**, choose your operating system and choose
   **Continue**.
7. Choose the device driver version that you want to download. Then follow
   the instructions on the **Fix Central** download page to
   download and configure IBM Data Protect.
8. Ensure that the barcode for any tape in the virtual tape library is eight
   characters or less. If you try to assign your tape a barcode that is longer
   than eight characters, you get this error message: `"Tape barcode
is too long for media changer"`.

## Writing Data to a Tape in IBM Data

Protect

You write data to a Tape Gateway virtual tape by using the same procedure and backup
policies that you do with physical tapes. Create the necessary configuration for backup
and restore jobs. For more information about configuring IBM Data Protect, see [Overview of administration tasks](https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.admin/t_administer_solution.html "https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.admin/t_administer_solution.html") for IBM Data Protect.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job might fail. If the backup job fails, the tape status in IBM Data Protect
changes to **ReadOnly**. If you know the tape has not been fully
utilized, you can manually change the tape status back to
**ReadWrite**, and either resume or resubmit the backup job
using the same tape. IBM Data Protect might continue the failed backup job on a
different tape if other tapes in **ReadWrite** status are
available.

## Restoring Data from a Tape Archived in IBM Data

Protect

Restoring your archived data is a two-step process.

###### To restore data from an archived tape

1. Retrieve the archived tape from archive to a Tape Gateway. For instructions,
   see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Restore the data by using the IBM Data Protect backup software. You do this by
   creating a recovery point, as you do when restoring data from physical tapes.
   For more information about configuring IBM Data Protect, see [Overview of administration tasks](https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.admin/t_administer_solution.html "https://www.ibm.com/support/knowledgecenter/en/SSEQVQ_8.1.10/srv.admin/t_administer_solution.html") for IBM Data Protect.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
