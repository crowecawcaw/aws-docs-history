# Step H: Restore the database on a Elemental Live

node

You restore data using the same lifeboat script that you used to create the
backup.

###### Topics

- [Step H1: Perform the
  restore](#migrate-worker-restore-command "#migrate-worker-restore-command")
- [Step H2: Perform manual restore
  tasks](#migrate-worker-restore-manual "#migrate-worker-restore-manual")

## Step H1: Perform the

restore

1. Download the lifeboat script, following the procedure that you followed
   when you [created the
   backup](migrate-worker-backup.md#migrate-worker-topic-lifeboat "migrate-worker-backup.md#migrate-worker-topic-lifeboat").

###### Important

Make sure that you have latest version of the script. AWS Elemental is
continually making improvements to the script. 2. Enter the restore command.

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
to continue. 3. After the restore has succeeded, reboot the node:

```
[elemental@hostname ~]$ sudo reboot
```

**Recovery steps**

Read this information if there was a problem with the file, as mentioned in step
two earlier on this page.

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

## Step H2: Perform manual restore

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

1. Determine where the custom certifcates are located on the node. If you
   originally followed the recommendation from AWS Elemental, then the
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
For more information, see [current Release Notes](../../../elemental-live.md "../../../elemental-live.md").

You must open port 443 on every node to allow access to the web interfaces for
the AWS Elemental software. See the section about opening ports in the [AWS Elemental Live Configuration Guide](../configguide.md "../configguide.md"). When
you save, the port is added and the firewall is started.
