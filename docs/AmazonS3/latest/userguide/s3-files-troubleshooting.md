# Troubleshooting S3 Files

This page helps you diagnose and resolve common issues with S3 Files.

- [Mount command fails](#s3-files-troubleshooting-mount-fails "#s3-files-troubleshooting-mount-fails")
- [Permission denied on file operations](#s3-files-troubleshooting-permission-denied "#s3-files-troubleshooting-permission-denied")
- [Intelligent read routing is not working](#s3-files-troubleshooting-read-routing "#s3-files-troubleshooting-read-routing")
- [File system consistently returns NFS server error](#s3-files-troubleshooting-encrypted-fs "#s3-files-troubleshooting-encrypted-fs")
- [Missing object in S3 bucket after file system write](#s3-files-troubleshooting-missing-object "#s3-files-troubleshooting-missing-object")
- [S3 object not visible in the file system](#s3-files-troubleshooting-object-not-visible "#s3-files-troubleshooting-object-not-visible")
- [Files appearing in the lost and found directory](#s3-files-troubleshooting-lost-found "#s3-files-troubleshooting-lost-found")
- [Synchronization falling behind](#s3-files-troubleshooting-sync-behind "#s3-files-troubleshooting-sync-behind")
- [Enabling client debug logs](#s3-files-troubleshooting-debug-logs "#s3-files-troubleshooting-debug-logs")

## Mount command fails

The `mount -t s3files` command fails with an error.

**Common causes and actions:**

- **"mount.s3files: command not found"** –
  The S3 Files client (amazon-efs-utils) is not installed or is below version
  3.0.0. Install or upgrade the client. For more information, see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").
- **"Failed to resolve file system DNS
  name"** – There is no mount target in the Availability Zone where
  your EC2 instance is running. Create a mount target in that Availability Zone, or
  launch your instance in an Availability Zone that has a mount target. For more
  information, see [Creating mount targets](s3-files-mount-targets-creating.md "s3-files-mount-targets-creating.md").
- **Connection timed out** – The security
  group configuration is not allowing NFS traffic. Verify that the mount target's
  security group allows inbound TCP on port 2049 from your instance's security
  group, and that your instance's security group allows outbound TCP on port 2049
  to the mount target's security group. For more information, see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").
- **"Access denied" during mount** – The IAM
  role attached to your compute resource does not have the required S3 Files
  permissions. Verify that the role has the
  `AmazonS3FilesClientFullAccess` or
  `AmazonS3FilesClientReadOnlyAccess` managed policy attached, or
  at minimum the `s3files:ClientMount` permission. For more information,
  see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").
- **botocore not installed** – The mount
  helper requires botocore to interact with AWS services. Install botocore
  following the instructions in the amazon-efs-utils README on
  GitHub.

## Permission denied on file operations

You can mount the file system but receive "Permission denied" or "Operation not
permitted" errors when reading, writing, or accessing files.

**Common causes and actions:**

- **Missing write permission** – If you can
  read but not write, verify that the IAM role attached to your compute resource
  includes the `s3files:ClientWrite` permission, or attach the
  `AmazonS3FilesClientReadWriteAccess` or
  `AmazonS3FilesClientFullAccess` managed policy. For more
  information, see [AWS managed policies for Amazon S3 Files](s3-files-security-iam-awsmanpol.md "s3-files-security-iam-awsmanpol.md").
- **Missing root access** – If you receive
  permission errors when accessing files owned by root (UID 0), your IAM role may
  not have the `s3files:ClientRootAccess` permission. Without this
  permission, all operations are performed as the NFS anonymous user (typically
  nfsnobody), which may not have access to the files. Attach the
  `AmazonS3FilesClientFullAccess` managed policy or add
  `s3files:ClientRootAccess` to your policy.
- **File system policy denying access** – If
  you have attached a file system policy, verify that it does not deny the actions
  your clients need. An "allow" in either the identity-based policy or the file
  system policy is sufficient for access. For more information, see [How S3 Files works with IAM](s3-files-security-iam.md "s3-files-security-iam.md").
- **POSIX permission mismatch** – S3 Files
  enforces standard POSIX permissions (owner, group, others) on files and
  directories. If your application runs as a user that does not match the file's
  owner or group, access may be denied even if IAM permissions are correct. Use an
  access point to enforce a specific UID/GID for all requests. For more
  information, see [Creating access points for an S3 file system](s3-files-access-points-creating.md "s3-files-access-points-creating.md").

## Intelligent read routing is not working

S3 Files performs intelligent read routing as it automatically routes read requests to
the storage layer best suited for them, while maintaining full file system semantics
including consistency, locking, and POSIX permissions. Small, random reads of actively
used files are served from the high-performance storage for low latency. Large sequential
reads and reads of data not on the file system are served directly from your S3 bucket
for high throughput, with no file system data charge.

Intelligent read routing may not be working if one of the client connectivity metrics
(`NFSConnectionAccessible`, `S3BucketAccessible`, and
`S3BucketReachable`) shows 0, or if you are not seeing the expected read
throughput.

**Common causes and actions:**

- **Missing S3 inline policy on compute
  role** – The IAM role attached to your compute resource must include
  an inline policy granting `s3:GetObject` and
  `s3:GetObjectVersion` on the linked S3 bucket. Without this
  policy, the mount helper cannot read directly from S3 and all reads go through
  the file system. For more information, see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").
- **S3 bucket not reachable** – Check the
  `S3BucketReachable` metric. If it shows 0, verify that your
  compute resource has network access to S3 (for example, through a VPC endpoint or
  NAT gateway).
- **File has been modified** – Reads are only
  served directly from S3 when the file has not been modified through the file
  system. If you have written to the file and the changes have not yet been
  synchronized to S3, reads go through the file system until synchronization
  completes.

## File system consistently returns NFS server error

An encrypted file system consistently returns NFS server errors. These errors can occur
when S3 Files cannot retrieve your KMS key from AWS KMS for one of the following
reasons:

- The key was disabled.
- The key was deleted.
- Permission for S3 Files to use the key was revoked.
- AWS KMS is temporarily unavailable.

**Action to take**

First, confirm that the AWS KMS key is enabled. You can view your keys in the AWS
KMS console. For more information, see [Viewing Keys](../../../kms/latest/developerguide/viewing-keys.md "../../../kms/latest/developerguide/viewing-keys.md") in the
_AWS Key Management Service Developer Guide_.

If the key is not enabled, enable it. For more information, see [Enabling and
Disabling Keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") in the _AWS Key Management Service Developer
Guide_.

If the key is pending deletion, cancel the deletion and re-enable the key. For more
information, see [Scheduling and Canceling Key
Deletion](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md") in the _AWS Key Management Service Developer
Guide_.

If the key is enabled and you are still experiencing issues, contact AWS
Support.

## Missing object in S3 bucket after file system write

You wrote a file through the file system and expected it to appear as an object in your
S3 bucket, but the object is not there. S3 Files waits for a period of write inactivity
(60 seconds) before exporting changes back to your S3 bucket. If the object still does
not appear after this period, the export might have failed. In such a case, you see the
`FailedExports` CloudWatch metric increase.

**Action to take**

Check the file's export status using extended attributes:

```
getfattr -n "user.s3files.status;$(date -u +%s)" missing-file.txt --only-values
```

The timestamp in the attribute name ensures you get the latest status. Example
output:

```
S3Key: s3://bucket/prefix/missing-file.txt
ExportError: PathTooLong
```

`ExportError` is not displayed if there is no export failure.
`S3Key` is empty if an S3 object was never linked to the file.

The following table lists all possible `ExportError` values:

| Error                       | Cause                                                                                                                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `S3AccessDenied`            | The IAM role that S3 Files assumes does not have sufficient<br>permissions to write to the S3 bucket. For more information, see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").          |
| `InternalError`             | There was an internal system error.                                                                                                                                                                                               |
| `S3UserMetadataTooLarge`    | S3 user metadata size limit exceeded. See [Unsupported features, limits, and quotas](s3-files-quotas.md "s3-files-quotas.md") for information on these<br>limits.                                                                 |
| `EncryptionKeyInaccessible` | The encryption key used by the S3 bucket is inaccessible to S3<br>Files. Grant S3 Files access to your encryption key. For more<br>information, see [Encryption](s3-files-encryption.md "s3-files-encryption.md").                |
| `RoleAssumptionFailed`      | Could not assume the role. Check your trust policies. For more<br>information, see [Prerequisites for S3 Files](s3-files-prereq-policies.md "s3-files-prereq-policies.md").                                                       |
| `KeyTooLongToBreakCycle`    | S3 Files could not resolve a circular dependency (for example, due to<br>renaming two files to each other's names) because the file path exceeds<br>the S3 key length limit. Shorten the directory path to resolve this<br>error. |
| `PathTooLong`               | Your file path exceeds the S3 key length limit. See [Unsupported features, limits, and quotas](s3-files-quotas.md "s3-files-quotas.md") for information on these<br>limits.                                                       |
| `DependencyExportFailed`    | A parent or a dependency has a non-retryable export failure. Check<br>the status for the parent or any dependencies using<br>`getfattr`.                                                                                          |
| `S3ObjectArchived`          | S3 object is archived (S3 Glacier Flexible Retrieval or S3 Glacier<br>Deep Archive) and cannot be read. Restore the object first using the S3<br>APIs.                                                                            |

S3 Files automatically retries failed exports. `ExportError` is shown only
for non-retryable errors.

## S3 object not visible in the file system

An object exists in your S3 bucket but does not appear in the file system. The object
key name may not map to a valid POSIX file path. S3 Files does not support accessing S3
key names with empty path components (`foo//bar`), relative path components
(`foo/./bar`, `foo/../bar`), key names containing null bytes, or key names where any path
component exceeds 255 bytes. Objects with incompatible key names are not imported into
the file system.

## Files appearing in the lost and found directory

Files have appeared in the
`.s3files-lost+found-`file-system-id`` directory
in your file system's root directory. In this case, you see the
`LostAndFoundFiles` CloudWatch metric increase. This occurs when a
synchronization conflict arises. A conflict occurs when the same file is modified through
the file system and the corresponding S3 object changes before S3 Files synchronizes the
file system changes back to S3. S3 Files treats the S3 bucket as the source of truth,
moves the conflicting file to the lost and found directory, and imports the latest
version from the S3 bucket into the file system.

**Identifying files in the lost and found
directory**

When S3 Files moves a file to the lost and found directory, it prepends the file name
with a hexadecimal identifier to distinguish multiple versions of the same file that may
be moved over time. File names longer than 100 characters are truncated to make room for
this identifier. The file's original directory path is not preserved in the lost and
found directory.

**Action to take**

Get the file's original path and the corresponding S3 object key:

```
getfattr -n "user.s3files.status;$(date -u +%s)" .s3files-lost+found-`fs-12345678`/`abcdef1234_report.csv` --only-values
```

Example output:

```
S3Key: s3://bucket/prefix/report.csv
FilePath: /data/report.csv
```

| Field      | Description                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| `S3Key`    | Full S3 path of the object that caused the conflict, or empty if the<br>object was deleted in the S3 bucket. |
| `FilePath` | Relative path of the file before the conflict.                                                               |

You can then either keep the latest version from your S3 bucket and delete the file
from the lost and found directory, or copy the file from the lost and found directory
back to its original path to overwrite the S3 version.

###### Note

Files in the lost and found directory remain there indefinitely and count toward
your file system storage costs. Delete files from the lost and found directory when
they are no longer needed.

## Synchronization falling behind

The `PendingExports` CloudWatch metric is growing, indicating that your
workload is generating changes faster than S3 Files can synchronize them to S3.

This means that your workload may be exceeding the synchronization rate. S3 Files
exports up to 800 files per second per file system. Consider reducing the rate of file
modifications or distributing work across multiple file systems. Monitor the
`PendingExports` metric over time. If it stabilizes or decreases, S3
Files is catching up. If it continues to grow, contact AWS Support.

## Enabling client debug logs

If you are troubleshooting mount, connectivity, or read bypass issues, you can enable
debug-level logging on the S3 Files client to capture more detail.

**Mount helper and watchdog logs**

Edit `/etc/amazon/efs/s3files-utils.conf` and change the logging level from
INFO to DEBUG:

```
[DEFAULT]
logging_level = DEBUG
```

Unmount and remount the file system for the change to take effect:

```
sudo umount /mnt/s3files
sudo mount -t s3files `file-system-id`:/ /mnt/s3files
```

Logs are written to `/var/log/amazon/efs/`. The mount helper log is
`mount.log`.

**Proxy (efs-proxy) logs**

The proxy handles NFS traffic and S3 read bypass. To enable debug logging for the
proxy, edit `/etc/amazon/efs/s3files-utils.conf`:

```
[proxy]
proxy_logging_level = DEBUG
```

Unmount and remount for the change to take effect. Proxy logs are written to
`/var/log/amazon/efs/`.

**TLS tunnel (stunnel) logs**

TLS tunnel logs are disabled by default. To enable them, edit
`/etc/amazon/efs/s3files-utils.conf` and set the following:

```
[mount]
stunnel_debug_enabled = true
```

To save all stunnel logs for a file system to a single file, also uncomment the
`stunnel_logs_file` line:

```
stunnel_logs_file = /var/log/amazon/efs/{fs_id}.stunnel.log
```

**Log size limits**

Log files are rotated automatically. You can configure the maximum size and number of
rotated files in `s3files-utils.conf`:

```
[DEFAULT]
logging_max_bytes = 1048576
logging_file_count = 10
```

The default is 1 MB per log file with 10 rotated files, for a maximum of 10 MB per log
type.

**Sharing logs with AWS Support**

When contacting AWS Support, collect the client logs and configuration into a single
archive:

```
sudo tar -czf /tmp/s3files-support-logs.tar.gz \
  /var/log/amazon/efs/ \
  /etc/amazon/efs/s3files-utils.conf
```

Include `/tmp/s3files-support-logs.tar.gz` with your support case.
