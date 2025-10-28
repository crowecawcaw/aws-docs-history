# Step H: Restore the database on a AWS Elemental Server

node

You restore data using the same lifeboat script that you used to create the
backup.

###### Important

Make sure that you have stopped the node. Don't run the script on an active node.

1. Download the lifeboat script, following the procedure that you followed when
   you [created the
   backup](migrate-server-218-backup.md#migrate-server-218-topic-lifeboat "migrate-server-218-backup.md#migrate-server-218-topic-lifeboat").

###### Important

Make sure that you have latest version of the script. AWS Elemental is
continually making improvements to the script. 2. Enter the restore command.

```
[elemental@hostname ~]$ ./lifeboat.sh --restore --import-database
```

The script tries to extract the version of the backup that is stored in this
folder: `/opt/upgrade-backups/system-backup.tar.gz`

This file was created when you created the backup. The script automatically
copied it to this directory. The installation of RHEL 9 should not have deleted
this file. Therefore, it should be in this location. If this file doesn't exist
or if there is a problem with it, the scripts stops. See the recovery steps
below to continue.

###### Important

If you updated the routing table in earlier, add the `--exclude
 netscripts-rest` flag when you run the lifeboat.sh script:

```
[elemental@hostname ~]$ ./lifeboat.sh --restore --import-database **--exclude netscripts-rest**
```

3. After the restore has succeeded, reboot the node:

```
[elemental@hostname ~]$ sudo reboot
```

**Recovery steps**

1. Locate the other copies of the backup and of the checksum files that you
   should have copied to storage off the node. The files to locate are:
   - `<hostname>_lifeboat-archive.zip`
   - `<hostname>_lifeboat-archive_export-checksum.txt`

2. Copy the files to `/home/elemental`
3. Enter the restore command again:

```
[elemental@hostname ~]$ ./lifeboat.sh --restore
```

This time the script looks for the files that are in
`/home/elemental`, and restores those files.
