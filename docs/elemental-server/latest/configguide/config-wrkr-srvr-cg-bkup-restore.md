This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Restore a Backup

Follow this procedure if you ever need to restore a backed-up version of the database.

_To restore the database_

1. At your workstation, start a remote terminal session to the AWS Elemental Server hardware unit. Log in with the elemental user credentials.
2. Type the following command to identify the version of AWS Elemental Server that is currently
   installed.

`[elemental@hostname ~]$ cat /opt/elemental_se/versions.txt`

Several lines of information appear, including the version number. For example: `AWS Elemental Server (2.16.1.12345)`. 3. Run the install script with the restore option.

`[elemental@hostname ~]$ sudo sh product`

`--restore-db-backup path backup-file --https`

where:

    1. `product` is the product installer, including the version number that you obtained in the previous step: `elemental_production_server_2.16.1.12345.run`.
    2. `path` is the path to the backup file. This path could simply be the remote folder where backups were originally stored.
    3. `backup-file` is the file that you want to restore. The file is unzipped and copied to the appropriate folder. Do not unzip the file manually before restoring it!
    4. `--https` keeps SSL enabled. If you omit this flag, SSL is disabled when you run the install script. If you don't have or don't want SSL, omit this flag.
