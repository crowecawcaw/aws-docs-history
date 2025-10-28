# Backing up data

You back up data using the special lifeboat script.

###### Warning

This warning applies if you are migrating to Conductor File version 3.26.1 or 3.26.2 and
if you use the channel schedules feature of Conductor File.

There is an issue with the schedules feature that affects the lifeboat script that
you use to back up and restore the database. If the database includes schedule data,
the backup and restore will fail.

Do not migrate your Conductor File cluster until AWS Elemental releases a version of the software
that fixes this issue.

###### Important

The lifeboat script creates a backup of multiple files that are relevant to the
AWS Elemental software. These files might include credentials and other sensitive
system information. Handle the backup according to your organization's best
practices for handling sensitive data.

## About the backup

process

The script backs up the following data:

- Licenses.
- Network settings for the node, including Ethernet configurations, DNS
  information, and host addresses.
- Timecode configuraton such as NTP, PTP, and chronyd.
- Firewall settings.
- SSL certificates.
- Optionally, the user credentials used in various components on the
  cluster. It is convenient to include these credentials, if your
  organization's policies allow them to be handled in this way.
- Configuration files for features of the AWS Elemental software.
- Remote storage mounts. The data is included only in the database for the
  primary and secondary Conductor nodes.
- Cluster data. Data relating to the cluster, including data about the
  channels, MPTSes, channel and MPTS node assignments, users setup, redundancy
  groups, cluster members. The data is included only in the database for the
  primary Conductor. The primary Conductor pushes data down to the secondary
  Conductor and to the appropriate worker nodes.

## Step 1: Download the lifeboat

script

Perform this procedure on every node in the cluster, to copy the lifeboat script
onto every node.

1. Download the latest version of the lifeboat script from [https://a.co/ElementalRHEL9Lifeboat](https://a.co/ElementalRHEL9Lifeboat "https://a.co/ElementalRHEL9Lifeboat") to your laptop. The lifeboat
   file is called `elemental_lifeboat_el.tar`.

###### Important

Download the script just before you are ready to create the backup.
AWS Elemental is continually making improvements to the script, therefore you
want to make sure that you always have the latest version. 2. Copy the lifeboat file to the `/home/elemental`
directory on every node in the cluster. 3. From the Linux prompt, use the _elemental_ user to
start a remote terminal session with the node. Don’t log in as sudo. 4. Untar the lifeboat file.

```
[elemental@hostname ~]$ cd /home/elemental && tar xvf elemental_lifeboat_el9.tar
```

## Create the backup

###### Important

Make sure that you have stopped the node. We recommend that you don't run the
script on an active node. The script temporarily stops elemental_se and httpd
services.

Enter the backup command as follows:

```
[elemental@hostname ~]$ ./lifeboat.sh --backup --include-creds
```

Where `--include-creds` (optional) includes the following credentials
in the backup: SSH, AWS, SMB/CIFs.

**Results of the backup**

The script creates the following assets:

- Asset 1. One version of the data that is compatible with 2.26.1 or later.
  When you restore the backup after you’ve installed RHEL 9, the lifeboat
  script will automatically select and copy over this version.
- Asset 2. One version of the data that is compatible with 2.25.x and
  earlier. You might later decide to downgrade a node back to a version below
  2.26.0. When you restore the backup after you’ve installed RHEL 7 or CentOS
  7, the lifeboat script will automatically select and copy over this
  version.
- Asset 3. An MD5 checksum of the contents of asset 3.
- Asset 4. A SHA1 checksum of the content of asset 3.

The script also creates the following files:

- File 1. A file that contains assets 1 and 2. The file has this name, where
  `hostname` is the name of the current node:

`<hostname>_lifeboat-archive.zip`

- File 2. A file that contains assets 3 and 4. The file has this name, where
  `hostname` is the name of the current node:

`<hostname>_lifeboat-archive_export-checksum.txt`

- File 3. A file that contains assets 1, 2, 3 and 4. The file is stored on
  the current node at this location:

`/opt/upgrade-backups/system-backup.tar.gz`

**Verify the backup**

Verify the integrity of the backup archive. This step is optional but we strongly
recommend that you follow it because the [restore operation](migrate-topic-restore-database.md "migrate-topic-restore-database.md") that you later
perform might fail if the backup file is corrupted.

You verify the integrity by comparing the checksum that the backup script creates
to the checksum that you perform on the
`<hostname>_lifeboat-archive_export-checksum.txt` file.
You can compare an MD5 or a SHA1 checksum.

1. Enter the `cat` command to view the checksums currently listed
   in the checksum file.:

```
~]$ cat <hostname>_lifeboat-archive_export-checksum.txt
```

The `cat` command simply displays the file contents on your
screen. For example:

```
md5sum
      d41d8cd98f00b204e9800998ecf8427e
sha1sum
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

2. Now run a checksum command on the
   `lifeboat-archive.zip` file. For example:

```
~]$ md5sum /home/elemental/<hostname>_lifeboat-archive.zip
```

Or

```
~]$ sha1sum /home/elemental/<hostname>_lifeboat-archive.zip
```

3. Compare the results from step 1 to the results from step 2. If the
   checksums don’t match, copy the archive file again.

**Store the backup archive**

Copy the `<hostname>_lifeboat-archive.zip` file to storage
off the node, so that you can copy it back to the node when you want to perform the
restore operation.

###### Important

The lifeboat script creates a backup of multiple files that are relevant to
the AWS Elemental software. These files might include credentials and other
sensitive system information. Handle the backup according to your organization's
best practices for handling sensitive data.
