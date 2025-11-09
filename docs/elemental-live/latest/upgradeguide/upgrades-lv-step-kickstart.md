# Step B: Kickstart the operating system

software

Your upgrade might require that you re-install (kickstart) the operating system. You might
decide on your own that you want to kickstart, or AWS Elemental Support might recommend that you
kickstart to attempt to solve a problem.

## Create a bootable kickstart

To upgrade the operating system, you need a kickstart file (`.iso`) file. For
example, `centos-20161028T12270-production-usb.iso`. You use this file to put a
preconfigured installation of your operating system on your physical hardware unit.

1. Identify the version of the operating system that corresponds to this version of
   Elemental Live. The correct `.iso` file is available at
   [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").
2. At your workstation, use a third-party utility (such as PowerISO or ISO2USB) to
   create a bootable USB drive from your `.iso` file. For help, see
   [this knowledge base article](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").

## Save the latest backup

When you upgrade the operating system, your previous database backups are deleted.
Locate and save the most recent backup off the system. You can use this backup later if you
need to downgrade back to this version.

###### To save the latest backup

1. From a Linux prompt, log in to the hardware unit with the
   _elemental_ user credentials.
2. Navigate to the directory where Elemental Live saves its backups.

```
[elemental@host ~]$ `cd /home/elemental/database_backups`
```

3. Locate the most recent backup and save it to a location off the AWS Elemental node. The
   backup name includes the date and time that the backup was taken, in this format:

```
/home/elemental/elemental-db-backup_`<version>`_`<date>`.tar
```

For example:

`/home/elemental/elemental-db-backup_live_2.23.5_2021-02-08_21-01-36.tar`

## Upgrade the operating system

Install the operating system on the node.

###### To kickstart the system

1. Insert the USB thumb drive into the hardware unit.
2. Restart the system using the following command.

```
[elemental@hostname ~]$ sudo reboot
```

3. Use the arrow keys to select each option and complete the field, using the
   instructions in the following table as a guide.

| Menu Option                                   | Instructions                                                                                                                                                                        |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Set Hostname`                                | Change the hostname to a useful name such as<br>`live-01` or<br>`live-chicago-01`.<br>Do not use `localhost` as the hostname.<br>Do not use periods or underscores in the hostname. |
| `Disk layout: Auto-detect`                    | Keep this set to `Auto-detect`.                                                                                                                                                     |
| `Set Key`                                     | Arrow down to skip this option.                                                                                                                                                     |
| `Install and configure base operating system` | Press \*_Enter_<br>• to begin the OS installation.                                                                                                                                  |

The operating system is installed. 4. At the `Press return to quit` prompt, press **Enter** to
reboot the system.
