# Step D: Create a Elemental Live backup

You must create a backup of the data on the node. You back up data using the special
lifeboat script.

Topic

###### Important

The lifeboat script creates a backup of multiple files that are relevant to the
AWS Elemental software. These files might include credentials and other sensitive system
information. Handle the backup according to your organization's best practices for
handling sensitive data.

## About the backup

process

The script backs up the following data:

- Licenses.
- Network settings for the node, including Ethernet configurations, DNS
  information, and host addresses.
- Timecode configuraton such as NTP, PTP, and chronyd.
- Firewall settings.
- SSL certificates.
- Optionally, the user credentials used in various components on the node.
  It is convenient to include these credentials, if your organization's
  policies allow them to be handled in this way.
- Configuration files for features of the AWS Elemental software.
- Remote storage mounts.
- Node data. Data such as data about the events and MPTSes.

## Step D1: Verify hostnames

RHEL 9 (specifically `systemd`) doesn't support underscores in
hostnames. If the node contain underscores, there are two ways to proceed:

- Continue with this procedure. When you run the lifeboat script, a prompt
  will appear that will force you to change the hostname if it includes an
  underscore.
- Change the hostname before you run the lifeboat script. To change a
  hostname, see the Red Hat documentation.

If your migration process means that you don't run the lifeboat script for
any reason, make sure that you change the hostname before you boot the node
after installing RHEL 9.

## Step D2: Download the lifeboat

script

You must copy the lifeboat script onto every node.

1. Download the latest version of the lifeboat script from [https://a.co/ElementalRHEL9Lifeboat](https://a.co/ElementalRHEL9Lifeboat "https://a.co/ElementalRHEL9Lifeboat") to your laptop. The lifeboat
   file is called `elemental_lifeboat_el.tar`.

###### Important

Download the script just before you are ready to create the backup.
AWS Elemental is continually making improvements to the script, therefore you
want to make sure that you always have the latest version. 2. Copy the lifeboat file to the `/home/elemental`
directory. 3. From the Linux prompt, use the _elemental_ user to
start a remote terminal session with the node. Don’t log in as sudo. 4. Untar the lifeboat file.

```
[elemental@hostname ~]$ cd /home/elemental && tar xvf elemental_lifeboat_el9.tar
```

5. Change to the `elemental_lifeboat_el9` directory.

```
[elemental@hostname ~]$ cd elemental_lifeboat_el9
```

## Step D3: Create the

backup

###### Important

Make sure that you have stopped all running events on the node. The script
temporarily stops `elemental_se` and `httpd` services.

Enter the backup command as follows:

```
[elemental@hostname ~]$ ./lifeboat.sh --backup --include-creds
```

Where `--include-creds` (optional) includes the following credentials
in the backup: SSH, AWS, SMB/CIFs.

**Results of the backup**

The script creates the following assets:

- Asset 1. One version of the data that is compatible with 2.26.0 or later.
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

## Step D4: Store the backup

archive

Copy two files to storage off the node, so that you can copy them back to the node
when you want to perform the restore operation. The files to store off the node are
the following:

- `<hostname>_lifeboat-archive.zip` (File 1)
- `<hostname>_lifeboat-archive_export-checksum.txt`
  (File 2)

###### Important

The lifeboat script creates a backup of multiple files that are relevant to
the AWS Elemental software. These files might include credentials and other
sensitive system information. Handle the backup according to your organization's
best practices for handling sensitive data.

## Step D5: Verify the

backup

Verify the integrity of the backup archive. This step is optional but we strongly
recommend that you follow it because the restore operation that you [later perform](migrate-worker-install-restore.md "migrate-worker-install-restore.md") might fail if the
backup file is corrupted.

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
screen. 2. Now run a checksum command on the
`lifeboat-archive.zip` file.

On a Linux system, enter this command:

```
~]$ md5sum /home/elemental/<hostname>_lifeboat-archive.zip
```

On a macOS system, enter this command:

```
~]$ sha1sum /home/elemental/<hostname>_lifeboat-archive.zip
```

On a Windows system, enter this command:

```
~]$ certutil -hashfile <hostname>_lifeboat-archive.zip MD5
```

3. Compare the results from step 1 to the results from step 2. If the
   checksums don't match, copy the archive file to remote storage again and
   compare the results again.
