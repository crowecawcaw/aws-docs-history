# Working with VTL Devices

When activating your Tape Gateway, you select your backup application from the list and
use the appropriate medium changer. If your backup application is not listed, you choose
**Other** and then choose the medium changer that works with backup
application. For a list of recommended media changers for supported backup applications, see
[https://docs.aws.amazon.com/storagegateway/latest/tgw/Requirements.html#requirements-backup-sw-for-vtl](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

Your Tape Gateway setup provides the following iSCSI devices, which you select when
activating your gateway.

**Medium changers:**

- AWS-Gateway-VTL – This device is provided with the gateway.
- STK-L700 – This device emulation is provided with the gateway.
  **Tape drives:**

- IBM-ULT3580-TD5—This device emulation is provided with the gateway.

###### Topics

- [Selecting a Medium Changer After Gateway
  Activation](#change-mediumchanger-vtl "#change-mediumchanger-vtl")
- [Updating the Device Driver for Your Medium
  Changer](#update-vtl-device-driver "#update-vtl-device-driver")
- [Displaying Barcodes for Tapes in Microsoft System
  Center DPM](#enable-barcode "#enable-barcode")

## Selecting a Medium Changer After Gateway

Activation

After your gateway is activated, you can choose to select a different medium changer
type.

###### To select a different medium changer type after gateway activation

1. Stop any related jobs that are running in your backup software.
2. On the Windows server, open the iSCSI initiator properties window.
3. Choose the **Targets** tab to display the discovered
   targets.
4. On the Discovered targets pane, choose the medium changer you want to change,
   choose **Disconnect**, and then choose **OK**.
5. On the Storage Gateway console, choose **Gateways** from the
   navigation pane, and then choose the gateway whose medium changer you want to
   change.
6. Choose the **VTL Devices** tab, select the medium changer you
   want to change, and then choose **Change Media
   Changer**.
7. In the Change Media Changer Type dialog box that appears, select the media
   changer you want from the drop-down list box and then choose
   **Save**.

## Updating the Device Driver for Your Medium

Changer

1. Open Device Manager on your Windows server, and expand the **Medium
   Changer devices** tree.
2. Open the context (right-click) menu for **Unknown Medium
   Changer**, and choose **Update Driver Software**
   to open the **Update Driver Software-unknown Medium Changer**
   window.
3. In the **How do you want to search for driver software?**
   section, choose **Browse my computer for driver
   software**.
4. Choose **Let me pick from a list of device drivers on my
   computer**.

###### Note

We recommend using the Sony TSL-A500C Autoloader driver with the Veeam
Backup & Replication 11A and Microsoft System Center Data Protection
Manager backup software. This Sony driver has been tested with these types
of backup software up to and including Windows Server 2019. 5. In the **Select the device driver you want to install for this
hardware** section, clear the **Show compatible
hardware** check box, choose **Sony** in the
**Manufacturer** list, choose **Sony - TSL-A500C
Autoloader** in the **Model** list, and then
choose **Next**. 6. In the warning box that appears, choose **Yes**. If the
driver is successfully installed, close the **Update drive
software** window.

## Displaying Barcodes for Tapes in Microsoft System

Center DPM

If you use the media changer driver for Sony TSL-A500C Autoloader, Microsoft System
Center Data Protection Manager doesn't automatically display barcodes for virtual
tapes created in Storage Gateway. To display barcodes correctly for your tapes, change the
media changer driver to Sun/StorageTek Library.

###### To display barcodes

1. Ensure that all backup jobs have completed and that there are no tasks pending
   or in progress.
2. Eject and move the tapes to offline storage (S3 Glacier Flexible Retrieval or
   S3 Glacier Deep Archive) and exit the DPM Administrator console. For
   information about how to eject a tape in DPM, see [Archiving a Tape by Using DPM](backup-DPM.md#dpm-archive-tape "backup-DPM.md#dpm-archive-tape").
3. In **Administrative Tools**, choose
   **Services** and open the context (right-click) menu for
   **DPM Service** in the **Detail** pane,
   and then choose **Properties**.
4. On the **General** tab, ensure that the **Startup
   type** is set to **Automatic** and choose
   **Stop** to stop the DPM service.
5. Get the StorageTek drivers from [Microsoft Update Catalog](http://www.catalog.update.microsoft.com/Search.aspx?q=storagetek%20-%20sun%2Fstoragetek%20library "http://www.catalog.update.microsoft.com/Search.aspx?q=storagetek%20-%20sun%2Fstoragetek%20library") on the Microsoft website.

###### Note

Take note of the different drivers for the different sizes.

For **Size** 18K, choose **x86
drivers**.

For **Size** 19K, choose **x64
drivers**. 6. On your Windows server, open Device Manager, and expand the **Medium
Changer Devices** tree. 7. Open the context (right-click) menu for **Unknown Medium
Changer**, and choose **Update Driver Software**
to open the **Update Driver Software-unknown Medium Changer**
window. 8. Browse to the path of the new driver location and install. The driver appears
as **Sun/StorageTek Library**. The tape drives remain as an IBM
ULT3580-TD5 SCSI sequential device. 9. Reboot the DPM server. 10. In the Storage Gateway console, create new tapes. 11. Open the DPM Administrator console, choose **Management**,
then choose **Rescan for new tape libraries** . You should see
the **Sun/StorageTek library**. 12. Choose the library and choose **Inventory**. 13. Choose **Add Tapes** to add the new tapes into DPM. The new
tapes should now display their barcodes.
