# Restoring the database

You restore data using the same lifeboat script that you used to create the
backup.

###### Important

Make sure that you have stopped the node. Don't run the script on an active node.

## Perform the restore

1. Download the lifeboat script, following the procedure you followed when
   you [created the
   backup](migrate-topic-lifeboat.md#migrate-topic-lifeboat-download "migrate-topic-lifeboat.md#migrate-topic-lifeboat-download").
2. ###### Important

Make sure that you have latest version of the script. AWS Elemental is
continually making improvements to the script.

Enter the restore command.

    * On a worker node or the secondary Conductor node, enter this
     command:



    ```
    [elemental@hostname ~]$ ./lifeboat.sh --restore
    ```

    Don't include any options.
    * On the primary Conductor node, enter this command:



    ```
    [elemental@hostname ~]$ ./lifeboat.sh --restore --import-database
    ```

The script tries to extract the version of the backup that is stored in
this folder:

`/opt/upgrade-backups/system-backup.tar.gz`

This file was created when you created the backup. The script
automatically copied it to this directory. The installation of RHEL 9 should
not have deleted this file. Therefore, it should be in this location.

If this file doesn't exist or if there is a problem with it, the scripts
stops. See the recovery steps below to continue.

The script tries to extract the version of the backup that is stored in
this folder: /opt/upgrade-backups/system-backup.tar.gz This file was created
when you created the backup. The script automatically copied it to this
directory. The installation of RHEL 9 should not have deleted this file.
Therefore, it should be in this location. If this file doesn't exist or if
there is a problem with it, the scripts stops. See the recovery steps below
to continue.

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

## Result of the restore

**Restored data**

As a result of the restore command, the following data from the backup is restored
on the nodes:

| Node                                                                                                                                                                       | Worker nodes | Secondary Conductor | Primary Conductor |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Licenses                                                                                                                                                                   | Yes          | Yes                 | Yes               |
| Network settings for the node, including Ethernet configurations, DNS information, and host addresses                                                                      | Yes          | Yes                 | Yes               |
| Timecode configuraton such as NTP, PTP, and chronyd                                                                                                                        | Yes          | Yes                 | Yes               |
| Firewall settings                                                                                                                                                          | Yes          | Yes                 | Yes               |
| The user credentials used in various components on the cluster (if you included them in the backup)                                                                        | Yes          | Yes                 | Yes               |
| Configuration files for features of the AWS Elemental software                                                                                                             | Yes          | Yes                 | Yes               |
| Remote storage mounts.                                                                                                                                                     |              | Yes                 | Yes               |
| Cluster data. Data relating to the cluster, including data about the channels, MPTSes, channel and MPTS node assignments, users setup, redundancy groups, cluster members. | Yes          |                     |                   | Notes <br>• The cluster data is only ever stored on the Conductor nodes. It is restored only to the primary Conductor because when you enable HA later is this migration procedure, the primary Conductor pushes the data to the secondary Conductor and to the appropriate worker nodes. <br>• The remote storage mounts is only ever stored on the Conductor nodes. The data specific to the node is restored to that node. |
