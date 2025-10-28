# Testing Your Setup by Using Dell EMC NetWorker

You can back up your data to virtual tapes, archive the tapes and manage your virtual tape
library (VTL) devices by using Dell EMC NetWorker. In this topic, you can find basic
documentation on how to configure the Dell EMC NetWorker software to work with a
Tape Gateway and perform a backup, including how to configure storage devices, write data
to a tape, archive a tape and restore data from a tape.

For detailed information about how to install and use the Dell EMC NetWorker software, see
the NetWorker documentation.

For more information about compatible backup applications, see [Supported third-party backup
applications for a Tape Gateway](Requirements.md#requirements-backup-sw-for-vtl "Requirements.md#requirements-backup-sw-for-vtl").

###### Topics

- [Configuring to Work with VTL Devices](#emc-configure-software "#emc-configure-software")
- [Allowing Import of WORM Tapes into Dell EMC
  NetWorker](#emc-import-tapes "#emc-import-tapes")
- [Backing Up Data to a Tape in Dell EMC
  NetWorker](#emc-write-data-to-tape "#emc-write-data-to-tape")
- [Archiving a Tape in Dell EMC NetWorker](#emc-archive-tape "#emc-archive-tape")
- [Restoring Data from an Archived Tape in Dell EMC
  NetWorker](#emc-restore-tape "#emc-restore-tape")

## Configuring to Work with VTL Devices

After you have connected your virtual tape library (VTL) devices to your Microsoft
Windows client, you configure to recognize your devices. For information about how to
connect VTL devices to the Windows client, see [Connecting your VTL devices](GettingStartedAccessTapesVTL.md "GettingStartedAccessTapesVTL.md").

doesn't automatically recognize Tape Gateway devices. To expose your VTL devices to
the NetWorker software and get the software to discover them, you manually configure the
software. Following, we assume that you have correctly installed the software and that
you are familiar with the Management Console. For more information about the Management
Console, see the NetWorker Management Console interface section of the _[Dell EMC NetWorker Administration Guide](https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf "https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf")_.

###### To configure the Dell EMC NetWorker software for VTL devices

1. Start the Dell EMC NetWorker Management Console application, choose
   **Enterprise** from the menu, and then choose
   **localhost** from the left pane.
2. Open the context (right-click) menu for **localhost**, and
   then choose **Launch Application**.
3. Choose the **Devices** tab, open the context (right-click)
   menu for **Libraries**, and then choose **Scan for
   Devices**.
4. In the Scan for Devices wizard, choose **Start Scan**, and
   then choose **OK** from the dialog box that appears.
5. Expand the **Libraries** folder tree to see all your
   libraries and hit F5 to refresh. This process might take a few seconds to load
   the devices into the library.
6. Open a command window (cmd.exe) with admin privileges and run the
   `jbconfig` utility that is installed with Dell EMC NetWorker
   19.5.
   1. At the menu prompt, enter the corresponding numeral to select
      **Configure an Autodetected SCSI Jukebox**.
   2. When prompted to provide a name for the jukebox device, enter a name
      such as `AWSVTL`.
   3. When prompted to turn NetWorker auto-cleaning on, enter
      `no`.
   4. When prompted to bypass auto-configure, enter `no`.
   5. When prompted to configure another jukebox, enter
      `no`.

7. When "jbconfig" completes, return to the Networker GUI and press F5 to
   refresh.
8. Choose your library to see your tapes in the left pane and the corresponding
   empty volume slots list in the right pane.
9. In the volume list, select the volumes you want to activate (selected volumes
   are highlighted), open the context (right-click) menu for the selected volumes,
   and then choose **Deposit**. This action moves the tape from
   the I/E slot into the volume slot.
10. In the dialog box that appears, choose **Yes**, and then in
    the **Load the Cartridges into** dialog box, choose
    **Yes**.
11. If you don't have any more tapes to deposit, choose **No** or
    **Ignore**. Otherwise, choose **Yes** to
    deposit additional tapes.

## Allowing Import of WORM Tapes into Dell EMC

NetWorker

You are now ready to import tapes from your Tape Gateway into the Dell EMC NetWorker
library.

The virtual tapes are write once read many (WORM) tapes, but Dell EMC NetWorker
expects non-WORM tapes. For Dell EMC NetWorker to work with your virtual tapes, you must
activate import of tapes into non-WORM media pools.

###### To allow import of WORM tapes into non-WORM media pools

1. On NetWorker Console, choose **Media**, open the context
   (right-click) menu for **localhost**, and then choose
   **Properties**.
2. In the **NetWorker Sever Properties** window, choose the
   **Configuration** tab.
3. In the **Worm tape handling** section, clear the
   **WORM tapes only in WORM pools** box, and then choose
   **OK**.

## Backing Up Data to a Tape in Dell EMC

NetWorker

Backing up data to a tape is a two-step process.

1. Label the tapes you want to back up your data to, create the target media
   pool, and add the tapes to the pool.

You create a media pool and write data to a virtual tape by using the same
procedures you do with physical tapes. For detailed information, see the Backing
Up Data section of the _[Dell EMC NetWorker Administration Guide](https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf "https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf")_. 2. Write data to the tape. You back up data by using the Dell EMC NetWorker User
application instead of the Dell EMC NetWorker Management Console. The Dell EMC
NetWorker User application installs as part of the NetWorker
installation.

###### Note

You use the Dell EMC NetWorker User application to perform backups, but you view
the status of your backup and restore jobs in the EMC Management Console. To view
status, choose the **Devices** menu and view the status in the
**Log** window.

###### Note

If your Tape Gateway restarts for any reason during an ongoing backup job, the
backup job will be suspended, and the tape status in Dell EMC Networker will change
to **Write Protected**. You can archive the tape or continue to
read data from it. You can resume the suspended backup job on a different
tape.

## Archiving a Tape in Dell EMC NetWorker

When you archive a tape, Tape Gateway moves the tape from the Dell EMC NetWorker tape
library to the offline storage. You begin tape archival by ejecting a tape from the tape
drive to the storage slot. You then withdraw the tape from the slot to the archive by
using your backup application—that is, the Dell EMC NetWorker software.

###### To archive a tape by using Dell EMC NetWorker

1. On the **Devices** tab in the NetWorker Administration
   window, choose **localhost** or your EMC server, and then
   choose **Libraries**.
2. Choose the library you imported from your virtual tape library.
3. From the list of tapes that you have written data to, open the context
   (right-click) menu for the tape you want to archive, and then choose
   **Eject/Withdraw**.
4. In the confirmation box that appears, choose **OK**.

The archiving process can take some time to complete. The initial status of the tape
appears as **IN TRANSIT TO VTS**. When archiving starts, the status
changes to **ARCHIVING**. When archiving is completed, the tape is no
longer listed in the VTL.

In the Dell EMC NetWorker software, verify that the tape is no longer in the storage
slot.

In the navigation pane of the Storage Gateway console, choose **Tapes**.
Verify that your archived tape's status is **ARCHIVED**.

## Restoring Data from an Archived Tape in Dell EMC

NetWorker

Restoring your archived data is a two-step process:

1. Retrieve the archived tape a Tape Gateway. For instructions, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").
2. Use the Dell EMC NetWorker software to restore the data. You do this by
   creating a restoring a folder file, as you do when restoring data from physical
   tapes. For instructions, see the Using the NetWorker User program section of the
   _[Dell EMC NetWorker Administration Guide](https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf "https://www.dellemc.com/en-us/collaterals/unauth/technical-guides-support-information/products/data-protection/docu91933.pdf")_.

**Next Step**

[Cleaning up unecessary resources](best-practices.md#cleanup-vtl "best-practices.md#cleanup-vtl")
