# Step D: Upgrade the backup worker

nodes

The role of backup nodes is not to run channels but to take over from an active node
that fails. If you have any nodes that are strictly backup nodes, then upgrade these
nodes first before performing the upgrade.

Perform these same steps on each node. To limit your downtime,
upgrade all of the backup nodes before upgrading the active
nodes.

There
are two procedures for
upgrading.
Choose the procedure that applies to your
deployment.

###### To upgrade backup worker

nodes
without changing the deployment

Follow this procedure if you don't need to change anything
about the deployment.

1. From the Linux command line, log in to the worker node.
   Use the _elemental_ user
   credentials.
2. Run the installer. Make sure to include the `-c` option to clear
   the database. Use the appropriate command:
   - For GPU and CPU versions of the software:

   ```
   [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_2.25.5.12345.run -c --skip-all --start -xeula**
   ```

   - For CPU-only versions of the software:

   ```
   [elemental@hostname ~]$ **sudo sh ./elemental\_production\_live\_cpu\_2.25.5.12345.run -c --skip-all --start -xeula**
   ```

3. If you copied a script to a safe location (as described in
   [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move "upgrades-cl3-upg-red-single-ver-version.md#upg-red-move")), copy it back to its location in
   `/opt/elemental_se/scripts`.
4. When the upgrade is complete, restart the node with the
   following command:

```
[elemental@hostname ~] **sudo reboot**
```

5. Repeat the upgrade steps on each backup worker node before
   moving on to the next step in the upgrade process.

###### To upgrade backup worker nodes and change the

deployment

Follow this procedure if you want to change something in the
deployment. Specifically, follow this procedure if you want to
enable OCR conversion for the first time. This feature is available in AWS Elemental Live
version 2.22.0 and later. (For information about this feature,
see [Support
for OCR Conversion](../../../elemental-live/latest/ug/support-for-ocr.md "../../../elemental-live/latest/ug/support-for-ocr.md") in the _AWS Elemental Live User
Guide_.)

1. Follow the appropriate procedure in the
   _AWS Elemental Live Installation
   Guide_:
   - [Install the AWS Elemental Live software](../../../elemental-live/latest/installguide/install-lv-ig-install-sw.md "../../../elemental-live/latest/installguide/install-lv-ig-install-sw.md"): to
     install on hardware
   - [Install the AWS Elemental Live software](../../../elemental-live/latest/installguide/install-vm-lv-ig-install-sw.md "../../../elemental-live/latest/installguide/install-vm-lv-ig-install-sw.md"): to
     install on a VM

2. If you copied a script to a safe location (as described in
   [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move "upgrades-cl3-upg-red-single-ver-version.md#upg-red-move")), copy it back to its location in
   `/opt/elemental_se/scripts`.
3. When the upgrade is complete, restart the node with the
   following command:

```
[elemental@hostname ~] **sudo reboot**
```

4. Repeat the upgrade steps on each backup worker node before
   moving on to the next step in the upgrade process.
