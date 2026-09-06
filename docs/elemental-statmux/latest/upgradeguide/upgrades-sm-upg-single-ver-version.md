

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step A: Get Ready
<a name="upgrades-sm-upg-single-ver-version"></a>

The following steps prepare you for upgrading. Perform these steps to ensure that you don't lose any data. 

## Check Essential Notes
<a name="ver-ess-notes"></a>

Refer to the essential notes in the [AWS Elemental Statmux Release Notes](https://docs.aws.amazon.com/elemental-live/) to identify changes in behavior with the upgrade. 

## Verify the Worker Type
<a name="ver-version-node"></a>

The software installer that you use for the nodes varies depending on if you have GPU-accelerated software type, or CPU-only. To determine the type of software, look at any web interface screen of the worker node. The top shows icons as follows:
+ CPU and GPU icons: the software is *GPU-accelerated*.
+ CPU icon only: the software is *CPU-only*.

![](http://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/images/upg-type-shared-png.png)


## Save the Latest Backup
<a name="ver-version-bup"></a>

When you install the upgraded operating system, your previous database backups are deleted. Locate and save the most recent backup off the system. You can use this backup later if you need to downgrade from 2.20.

**To save the latest backup**

1. From a Linux prompt, log in to the hardware unit with the *elemental* user credentials.

1. Navigate to the directory where AWS Elemental Statmux saves its backups.

   ```
   [elemental@host ~]$ cd /home/elemental/database_backups
   ```

1. Locate the most recent backup and save it to a location off of the AWS Elemental system. The backup name includes the date and time that the backup was taken, in a format similar to this: `elemental-db-backup_live_2.14.8_2018-02-08_21-01-36.tar`

## Create Bootable Kickstart
<a name="ver-version-ks"></a>

You must install the host operating system from an `.iso` file onto each physical machine that will be running AWS Elemental software. Doing so is referred to as “kickstarting the system”.

Make sure that you install the right version of the operating system with each piece of software. The correct `.iso` file is available at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations).

**Create a Boot USB Drive**  
Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a bootable USB drive from your `.iso` file. For help, see the knowledge base article [Creating Bootable Recovery (kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-CentOS-Elemental-v2-0-Windows-and-Apple-OS-X).