

# Step N: Upgrade the secondary Conductor Live node
<a name="upg-red-sec"></a>

If you have only one Conductor Live, skip this step and go to [Step O: Upgrade the primary Conductor node](upg-red-pri.md).

Perform these steps on the secondary Conductor Live node.

**To upgrade the Conductor Live nodes**

Perform these steps on the secondary Conductor Live (if applicable), then on the primary Conductor Live.

1. From the Linux command line, log in to the worker node. Use the *elemental* user credentials.

1. Run the installer. Make sure to include the `-c `option to clear the database. Use this command:

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_conductor_live247_3.25.5.12345.run -c --skip-all --start -xeula
   ```

   The installer automatically stops the software. You will not be prompted to do the following:
   + Change the network setup (eth0 and eth1) or the Ethernet partitioning (setup of eth0 as a management interface).
   + Choose the timezone.
   + Enable or disable user authentication.

1. Make sure that the elemental\_se service restarts. Look for this prompt on the primary Conductor Live command line:

   ```
   Starting elemental_se:            [OK]
   ```

1. If you copied a script to a safe location (as described in [Move custom files](upgrades-cl3-upg-red-single-ver-version.md#upg-red-move)), copy it back to its location in `/opt/elemental_se/scripts`.