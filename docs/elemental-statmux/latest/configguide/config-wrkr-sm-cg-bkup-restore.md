This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Restore a Backup

Follow this procedure if you ever need to restore a backed-up version of the database.

###### To restore the database

1. At your workstation, start a remote terminal session to the AWS Elemental Conductor File hardware unit. Log in with the elemental user credentials.
2. Type the following command to identify the version of AWS Elemental Conductor File that is currently installed.

```
[elemental@hostname ~]$ cat /opt/elemental_se/versions.txt
```

Several lines of information appear, including the version number. For example: `AWS Elemental Conductor File (2.15.1.12345)`. 3. Run the install script with the restore option.

```
[elemental@hostname ~]$ sudo sh product
--restore-db-backup path backup-file --https
```

where:

    * `product` is the product installer, including the version number that you obtained in the previous step: `elemental_production_conductor_file_2.15.1.12345.run`.
    * `path` is the path to the backup file. This path could simply be the remote folder where backups were originally stored.
    * `backup-file` is the file that you want to restore. The file is unzipped and copied to the appropriate folder. Do not unzip the file manually before restoring it!
    * `--https` keeps SSL enabled. If you omit this flag, SSL is disabled when you run the install script. If you don't have or don't want SSL, omit this flag.
