# Step A: Get ready to

downgrade

The following steps prepare you for downgrading AWS Elemental Live. Perform these steps to ensure that you
don't lose any data.

## Save the database

backup

Locate the database backup for the version that you're
downgrading to. Copy the backup to a location off of the system.
Performing a downgrade removes your entire file structure.

Every time that you downgrade, a backup of the database is
automatically made and saved in the following location.

```
/home/elemental/database_backups/elemental-db-backup_live_n.n.n.n_yyyy-mm-dd_hh-mm-ss.tar
```

For example:

`elemental-db-backup_live_2.23.5_2021-02-08_21-01-36.tar`

When you perform a downgrade, you must specify a database to restore. You should restore
the backup that corresponds to the version you are downgrading to. For example, when
downgrading to 2.23.5, restore the 2.23.5 database.

## Create a bootable

kickstart

You must install the host operating system from an
`.iso` file onto each physical machine that will be
running Elemental Live. Doing so is referred to as “kickstarting the
system”.

Make sure that you install the right version of the operating system
with each piece of software. The correct `.iso` file
is available at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").

###### Create a Boot USB Drive

Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a
bootable USB drive from your `.iso` file. For help, see
[this knowledge base article](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").
