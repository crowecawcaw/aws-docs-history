# Restoring a backup

To restore a backup version of the database on a Conductor Live, Elemental Live, or Elemental Statmux node, follow
this procedure.

If you're restoring the Conductor Live database, restore to the primary
Conductor Live node.

###### To restore the database

1. At your workstation, [start a remote
   terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to the Conductor Live node.
2. Enter the following command to identify the version of Conductor Live that is currently
   installed.

```
[elemental@hostname ~]$ cat /opt/elemental_se/versions.txt
```

Several lines of information appear, including the version
number. For example: `Conductor Live (2.20.1.12345)`. 3. Run the install script with the restore option.

```
[elemental@hostname ~]$ sudo sh <product> --restore-db-backup <path> <backup-file> --https
```

Where:

    * `product` is the product installer, including the
     version number that you obtained in the previous step. For
     example, if you are restoring on Conductor Live, the product installed
     might be:


    `elemental_production_conductor_live_2.20.1.12345.run`.
    * `path` is the path to the backup file.
    * `backup-file` is the file that you want to restore.
     This is a zipped file. Don't unzip the file; the restore command
     automatically unzips the file for you.
    * `--https` keeps HTTPS enabled. If you currently
     have HTTP enabled, include this option. If you don't currently
     have HTTPS enabled, omit this option.

4. The file is unzipped and copied to the
   appropriate
   folder.
