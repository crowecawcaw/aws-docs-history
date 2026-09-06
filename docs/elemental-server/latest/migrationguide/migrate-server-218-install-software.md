

# Step G: Install worker software on a AWS Elemental Server node
<a name="migrate-server-218-install-software"></a>

This install procedure isn't the same as the install procedure on a newly obtained appliance (as described in [AWS Elemental Server Installation Guide](https://docs.aws.amazon.com/elemental-server/latest/installguide/)). You don't have to configure the node. 

1. From the Linux command line, log in to the worker node. Use the **elemental** user credentials.

1. Check routing table by running the following command:

   ```
   ip r show
   ```

   The system returns something similar to the following:

   ```
   default via 10.x.x.x dev eth0 proto dhcp src 10.x.x.x metric 103
   10.x.x.x/x dev eth1 proto kernel scope link src 10.12.107.43 metric 102
   ...
   ```

   To proceed with the upgrade, your management interface must be listed for the first route. To find which network interface is your system's management interface, see: [Note the network adapter for the management interface](migrate-server-218-prepare-node.md#management-address-note). 

1. If your management interface isn't listed for the first route, you must update the default route.:

1. Run the installer. Use the appropriate command:
   + For GPU versions of the software (for AWS Elemental Server only):

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_server_2.18.n.nnnn.run --skip-all --start --xeula
     ```
   + For CPU-only versions of the software:

     ```
     [elemental@hostname ~]$ sudo sh ./elemental_production_server_cpu_2.18.n.nnnn.run --skip-all --start --xeula
     ```

   Where:

   `--skip-all` skips all the prompts. There is no need to view prompts about configuration because when you restore the database to the node, all the configuration data is copied over and overwrites any configuration data already on the node. 

   `--start` restarts the software after installation.

   `--xeula` skips the display of the license agreement. There is no need to view this prompt because you have previously accepted the agreement.

1. When the installation is complete, restart the node:

   ```
   [elemental@hostname ~] sudo reboot
   ```