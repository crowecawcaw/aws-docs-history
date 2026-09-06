

# Step A: Get ready
<a name="upgrades-cl3-upg-red-single-ver-version"></a>

The following steps prepare you for upgrading. Perform these steps to ensure that you don't lose any data.

## Enabling HTTPS
<a name="red-upgr-enabling-ssl"></a>

Do not follow the reduced downtime upgrade process if you're enabling HTTPS at the same time that you're upgrading the cluster. HTTPS must be enabled on all nodes at the same time, so you have to use the [standard upgrade process](upgrades-cl3-upg-std.md).

## Check essential notes
<a name="ver-ess-notes-red"></a>

Refer to the essential notes in the [ current Release Notes](https://docs.aws.amazon.com/elemental-live/) to identify changes in behavior with the upgrade. 

## Verify the worker node type
<a name="ver-version-node-red"></a>

The software installer that you use for the nodes varies depending on if you have GPU-accelerated software type, or CPU-only. To determine the type of software, look at any web interface screen of the worker node. The top shows icons as follows:
+ CPU and GPU icons: the software is *GPU-accelerated*.
+ CPU icon only: the software is *CPU-only*.

![Dashboard showing status indicator, CPU usage, GPUs usage, and memory usage meters.](http://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/images/upg-type-shared-png.png)


## Save the latest database backup
<a name="ver-version-bup-red"></a>

Perform these steps on the primary Conductor Live node and all worker nodes in the cluster.

When you install the upgraded operating system, your previous database backups are deleted. Locate and save the most recent backup off the system. You can use this backup later if you need to downgrade.

**To save the latest backup**

1. From a Linux prompt, log in to the appliance with the *elemental* user credentials.

1. Navigate to the directory where Conductor Live saves its backups.

   ```
   [elemental@host ~]$ cd /home/elemental/database_backups
   ```

1. Locate the most recent backup and save it to a location off the AWS Elemental system. The backup name includes the date and time that the backup was taken, in a format similar to this: `elemental-db-backup_live_2.23.5_2018-02-08_21-01-36.tar`

## Move custom files
<a name="upg-red-move"></a>

If the primary Conductor Live or any worker nodes have custom AWS Elemental assets, such as scripts, saved to `/opt/elemental_se/scripts`, then move them to a safe location so they're not deleted during the upgrade.

## Create bootable kickstart
<a name="ver-version-ks-red"></a>

You must install the host operating system from an `.iso` file onto each physical machine that will be running AWS Elemental software. Doing so is referred to as “kickstarting the system”.

Make sure that you install the right version of the operating system with each piece of software. The correct `.iso` file is available at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations).

**Create a Boot USB Drive**  
Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a bootable USB drive from your `.iso` file. For help, see the knowledge base article [Creating Bootable Recovery (kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X).