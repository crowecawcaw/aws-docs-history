This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step A: Get Ready

The following steps prepare you for downgrading. Perform these steps to ensure that you
don't lose any data.

## Save the Database Backup

Locate the database backup for the version that you're downgrading to. Copy the backup to a
location off of the system. Performing a downgrade removes your entire file
structure.

Every time that you downgrade, a backup of the database is automatically made and saved in the following location.

```
/home/elemental/database_backups/elemental-db-backup_statmux_n.n.n.n_yyyy-mm-dd_hh-mm-ss.tar
```

###### Example

`elemental-db-backup_statmux_2.17.8_2018-02-08_21-01-36.tar`

When you perform a downgrade, you must specify a database to restore. You should
restore the backup that corresponds to the version you are downgrading to. For example, when
downgrading to 2.17.8, restore the 2.17.8 database.

## Create Bootable Kickstart

You must install the host operating system from an `.iso` file onto each physical machine
that will be running AWS Elemental software. Doing so is referred to as “kickstarting
the system”.

Make sure that you install the right version of the operating system with each piece of software. The correct `.iso` file
is available at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").

###### Create a Boot USB Drive

Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a bootable USB drive
from your `.iso` file. For help, see the knowledge base article [Creating Bootable Recovery
(kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-CentOS-Elemental-v2-0-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-CentOS-Elemental-v2-0-Windows-and-Apple-OS-X").
