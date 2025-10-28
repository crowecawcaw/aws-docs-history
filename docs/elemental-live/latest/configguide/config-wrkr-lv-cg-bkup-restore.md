# Restore a backup

Follow this procedure if you ever need to restore a backed-up version of the database.

###### To restore the database

1. At your workstation, start a remote terminal session to the AWS Elemental Live hardware unit. Log in with the elemental user credentials.
2. Type the following command to identify the version of Elemental Live that is currently installed.

```
[elemental@hostname ~]$ cat /opt/elemental_se/versions.txt
```

Several lines of information appear, including the version number. For example: `AWS Elemental Live (2.25.1.12345)`. 3. Run the install script with the restore option.

```
[elemental@hostname ~]$ sudo sh product --restore-db-backup path `backup-file` `--https`
```

where:

    * `product` is the product installer, including the version number that
     you obtained in the previous step:
     `elemental_production_conductor_live_2.25.1.12345.run`.
    * `path` is the path to the backup file. This path could simply be the
     remote folder where backups were originally stored.
    * `backup-file` is the file that you want to restore. The file is
     unzipped and copied to the appropriate folder. Do not unzip the file manually before
     restoring it!
    * `--https`



    If you are using Elemental Live 2.25 or earlier, and if you enabled SSL when you configured
     the node\*x\*, enter `HTTPS`. If you omit this flag, the script disables SSL.
     If you don't have or don't want SSL, omit this flag.


    If you are using Elemental Live 2.26 or later, there is no need to enter this option. SSL
     is enabled by default in these versions.
