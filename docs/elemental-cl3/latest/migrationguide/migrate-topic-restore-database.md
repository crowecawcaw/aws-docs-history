# Restoring the database

You restore data using the same lifeboat script that you used to create the
backup.

###### Topics

- [Step A: Perform the restore](#migrate-topic-restore-command "#migrate-topic-restore-command")
- [Step B: Perform manual restore
  tasks](#migrate-topic-restore-manual "#migrate-topic-restore-manual")
- [Result of the
  restore](#migrate-topic-restore-result "#migrate-topic-restore-result")

###### Important

Make sure that you have stopped the node. Don't run the script on an active node.

## Step A: Perform the restore

1. Download the lifeboat script, following the procedure that you followed
   when you [created the
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
this directory:

`/opt/upgrade-backups/system-backup.tar.gz`

This file was created when you created the backup. The script
automatically copied it to this directory. The installation of RHEL 9 should
not have deleted this file. Therefore, it should be in this location.

If this file doesn't exist or if there is a problem with it, the scripts
stops. See the recovery steps below to continue.

The script tries to extract the version of the backup that is stored in
this directory: /opt/upgrade-backups/system-backup.tar.gz This file was
created when you created the backup. The script automatically copied it to
this directory. The installation of RHEL 9 should not have deleted this
file. Therefore, it should be in this location. If this file doesn't exist
or if there is a problem with it, the scripts stops. See the recovery steps
below to continue. 3. After the restore has succeeded, reboot the node:

```
[elemental@hostname ~]$ sudo reboot
```

**Recovery steps**

Read this information if there was a problem with the file, as mentioned in step 2
earlier on this page.

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

## Step B: Perform manual restore

tasks

After you have run the lifeboat script, you might need to perform some manual
steps.

### SSL certificates

Read this section if your organization uses custom SSL certificates.

The lifeboat script backs up and restores the SSL certificates, both the
default certificates and custom certificates you previously set up. However, the
script doesn't update the Apache configuration file to point to the
certificates. You must update the Apache configuration to include these
paths.

Follow these steps on each node.

1. Determine where the custom certificates are located on the node. If
   you originally followed the recommendation from AWS Elemental, then the
   certificates are in `/home/elemental/cert`.
2. Enter this command:

`cd /opt/elemental_se` 3. Enter the `configure` command:

`sudo ./configure -xeula --skip-all `<certificate
 options>``

There are three certificate options:

`--https-crt <path to Apache SSLCertificateFile`

`--https-key <path to Apache
 SSLCertificateKeyFile`

`--https-chain <path to Apache
 SSLCertificateChainFile`

Typically you need to enter either the first two options (to specify
the location of the certificate and the key file) or all three
options.

For example, to specify the location of the certificate and the key:

`sudo ./configure -xeula --skip-all --https --https-cert
 /home/elemental/cert --https-key /home/elemental/cert`

### Firewall configuration

Read this section if the cluster was previously configured to use HTTP.
Starting with versions 2.26.0 (and 3.26.0), HTTPS is always enabled by default.
For more information, see the [current Release Notes](../../../elemental-live.md "../../../elemental-live.md").

You must open port 443 on every node to allow access to the web interfaces for
the AWS Elemental software.

## Result of the

restore

**Restored data**

As a result of the restore command, the following data from the backup is restored
on the nodes:

| Node                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Worker nodes | Secondary Conductor | Primary Conductor |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Licenses                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes          | Yes                 | Yes               |
| Network settings for the node, including Ethernet configurations, DNS information, and host addresses.                                                                                                                                                                                                                                                                                                                                                   | Yes          | Yes                 | Yes               |
| Timecode configuration such as NTP, PTP, and chronyd                                                                                                                                                                                                                                                                                                                                                                                                     | Yes          | Yes                 | Yes               |
| Firewall settings                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes          | Yes                 | Yes               |
| The user credentials used in various components on the cluster (if you included them in the backup)                                                                                                                                                                                                                                                                                                                                                      | Yes          | Yes                 | Yes               |
| Configuration files for features of the AWS Elemental software                                                                                                                                                                                                                                                                                                                                                                                           | Yes          | Yes                 | Yes               |
| Remote storage mounts. The remote storage mounts is only ever stored on the Conductor nodes. The data specific to the node is restored to that node.                                                                                                                                                                                                                                                                                                     |              | Yes                 | Yes               |
| Cluster data. Data relating to the cluster, including data about the channels, MPTSes, channel and MPTS node assignments, users setup, redundancy groups, cluster members. The cluster data is only ever stored on the Conductor nodes. It is restored only to the primary Conductor because when you enable HA later is this migration procedure, the primary Conductor pushes the data to the secondary Conductor and to the appropriate worker nodes. | Yes          |                     |                   | **Directory structure for restored data** On every node, the directory structure after backup-and-restore is identical to the structure before backup-and-restore. **Cluster cleanup** On the primary Conductor node only, the restore command also cleans up the cluster configuration data. It performs the following actions <br>• Removes data about nodes that are assigned to each channel. <br>• Deletes data about nodes in the cluster. <br>• Deletes data about nodes in Conductor and worker redundancy groups. But keep the redundancy groups themselves. <br>• Changes the state of channels and MPTSes to Idle, and delete any data about channel activity. <br>• Clears all active Alerts. This cleanup ensures you can rebuild the cluster without running into configuration conflicts. |
