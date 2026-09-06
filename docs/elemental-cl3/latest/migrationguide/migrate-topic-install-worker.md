

# Installing Elemental Live on a worker node
<a name="migrate-topic-install-worker"></a>

This install procedure isn't the same as the install procedure on a newly obtained appliance (as described in [AWS Elemental Live Installation Guide](https://docs.aws.amazon.com/elemental-live/latest/installguide/)). You don't have to configure the node. 

This install procedure is very similar to the upgrade procedure (as described in [AWS Elemental Live Upgrade Guide](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/)), but there are significant differences in the options you include.

1. From the Linux command line, log in to the worker node. Use the **elemental** user credentials.

1. Run the installer. Use the appropriate command:
   + For GPU and CPU versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_live_2.26.x.12345.run --cleandb --skip-mellanox --skip-all --start -xeula 
     ```
   + For CPU-only versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_live_cpu_2.26.x.12345.run --cleandb --skip-mellanox --skip-all --start -xeula
     ```

   Where:

   `--cleandb` deletes the application database. This option is required on the worker nodes. You don't need the application database because when you add a worker node back into the cluster, the worker node will synchronize with the database of the primary Conductor node.

   `--skip-mellanox`. Optional. Skips installation of the Mellanox driver, even if the script detects that a Mellanox NIC is installed in the appliance. For more information, see the [ current Release Notes](https://docs.aws.amazon.com/elemental-live/).

   `--skip-all` skips all the prompts. There is no need to view prompts about configuration because when you restore the database to the node, all the configuration data is copied over and overwrites any configuration data already on the node. 

   `--start` restarts the software after installation.

   `--xeula` skips the display of the license agreement. There is no need to view this prompt because you have previously accepted the agreement.

1. When the installation is complete, restart the node:

   ```
   [elemental@hostname ~] sudo reboot
   ```