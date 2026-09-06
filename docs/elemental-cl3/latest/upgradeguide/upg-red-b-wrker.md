

# Step D: Upgrade the backup worker nodes
<a name="upg-red-b-wrker"></a>

The role of backup nodes is not to run channels but to take over from an active node that fails. If you have any nodes that are strictly backup nodes, then upgrade these nodes first before performing the upgrade.

Perform these same steps on each node. To limit your downtime, upgrade all of the backup nodes before upgrading the active nodes.

There are two procedures for upgrading. Choose the procedure that applies to your deployment.

**To upgrade backup worker nodes without changing the deployment**

Follow this procedure if you don't need to change anything about the deployment. 

1. From the Linux command line, log in to the worker node. Use the *elemental* user credentials.

1. Run the installer. Make sure to include the `-c` option to clear the database. Use the appropriate command:
   + For GPU and CPU versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_live_2.25.5.12345.run -c --skip-all --start -xeula
     ```
   + For CPU-only versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_live_cpu_2.25.5.12345.run -c --skip-all --start -xeula
     ```

1. If you copied a script to a safe location (as described in [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move)), copy it back to its location in `/opt/elemental_se/scripts`.

1. When the upgrade is complete, restart the node with the following command:

   ```
   [elemental@hostname ~] sudo reboot
   ```

1. Repeat the upgrade steps on each backup worker node before moving on to the next step in the upgrade process.

**To upgrade backup worker nodes and change the deployment**

Follow this procedure if you want to change something in the deployment. Specifically, follow this procedure if you want to enable OCR conversion for the first time. This feature is available in AWS Elemental Live version 2.22.0 and later. (For information about this feature, see [Support for OCR Conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-ocr.html) in the *AWS Elemental Live User Guide*.)

1. Follow the appropriate procedure in the *AWS Elemental Live Installation Guide*:
   + [Install the AWS Elemental Live software](https://docs.aws.amazon.com/elemental-live/latest/installguide/install-lv-ig-install-sw.html): to install on hardware
   + [Install the AWS Elemental Live software](https://docs.aws.amazon.com/elemental-live/latest/installguide/install-vm-lv-ig-install-sw.html): to install on a VM

1. If you copied a script to a safe location (as described in [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move)), copy it back to its location in `/opt/elemental_se/scripts`.

1. When the upgrade is complete, restart the node with the following command:

   ```
   [elemental@hostname ~] sudo reboot
   ```

1. Repeat the upgrade steps on each backup worker node before moving on to the next step in the upgrade process.