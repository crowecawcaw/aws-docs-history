

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step C: Downgrade the Node
<a name="downgrades-sm-upg-dg-node"></a>

The downgrade steps that you take depend on the version that you're downgrading to. The following section describes downgrading from 2.20.x to 2.17.x or 2.16.x .

When you downgrade to 2.17.x, run the installer with the `--downgrade` switch for each node.

**To downgrade the node**

1. From the Linux prompt, log in with the *elemental* user credentials. Once you are logged in, the initial directory is `/home/elemental`.

1. Enter the following command:

   ```
   [elemental@hostname ~]$ chmod 755 elemental_production_statmux_2.17.n.nnnnn.run
   ```

1. Run the prepare for downgrade script:

   ```
   [elemental@hostname ~]$ sudo /opt/elemental_se/web/script/prepare_for_downgrade.sh -i ./elemental_production_statmux_2.17.n.nnnnn.run
   ```

1. Run the installer with the skip-all option. Use the following commands with the actual file name of the `.run` file, rather than the example below:

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_statmux_2.17.n.nnnnn.run -c --skip-all --start -xeula --downgrade
   ```

   Switches are as follows:
   + `2.17.n.nnnnn`: Is the software version that you're downgrading to.
   + `-xeula`: Skips the prompts to read through the EULA. You are prompted once to accept it.
   + `--start`: Specifies to start the services without being prompted.
   + `--downgrade`: Tells the installer that an earlier version is being installed.
   + `--restore-db-backup <path>`: Installs the version old version of the database backup file. Provide the path and file name in the following format: 

     ```
     /home/elemental/elemental-db-backup_{{<date>}}_{{<version>}}.tar
     ```

1. When the installer completes, **do not** reboot or restart\! Run these two commands first:

   ```
   [elemental@hostname ~]$ sudo yum versionlock delete device-mapper*
   ```

   ```
   [elemental@hostname ~]$ sudo yum install lvm2
   ```

   If you don't run these commands before rebooting, the node will boot into emergency mode and you might lose data.

1. Restart the node with the following command:

   ```
   [elemental@hostname ~] sudo reboot
   ```

1. Repeat the downgrade steps on each worker node before moving on to the next step in the downgrade process.