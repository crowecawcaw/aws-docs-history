# Unsupported features, limits, and quotas

This page describes the limitations and quotas when using S3 Files.

## Unsupported S3 features

- **Archival storage classes** – Objects in
  the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes
  cannot be accessed through the file system. Similarly, objects in the S3
  Intelligent-Tiering Archive Access or Deep Archive Access tiers cannot be
  accessed through the file system. You must first restore these objects using the
  S3 API.
- **S3 Access Control Lists (ACLs)** – S3
  ACLs are not preserved after changes are made through the file system. We
  recommend that you keep ACLs disabled and use policies to control access to all
  objects in your bucket, regardless of who uploaded the objects to your bucket. For
  more information, see [Managing access with
  ACLs](acls.md "acls.md").

## File system limitations

- **Hard links** – S3 Files does not support
  hard links. Each file in the file system corresponds to a single S3 object
  key.
- **Path component size** – S3 Files does not
  support objects where any single directory or file name in the path exceeds 255
  bytes. A path component is a directory or file name derived from an S3 object
  key. For example, the key `dir1/dir2/file.txt` has three path
  components: `dir1`, `dir2`, and
  `file.txt`.
- **Incompatible S3 object key names** –
  S3 Files does not support accessing S3 key names that do not map to valid POSIX
  file paths, including empty path components (`foo//bar`), relative
  path components (`foo/./bar`, `foo/../bar`), and key names containing null
  bytes.
- **S3 key size limit** – Files or
  directories whose full path name exceeds the 1,024-byte S3 object key size limit
  cannot be exported to S3.
- **Symlink targets** – If an S3 object is a
  symlink, its target must be a valid path that is not empty and does not exceed
  4,080 bytes.
- **POSIX permissions metadata size** – Files
  or directories where the POSIX permission metadata exceeds 2 KB cannot be
  exported to S3.

## Quotas

The following quotas can be increased by contacting AWS Support.

| Resource                      | Default quota |
| ----------------------------- | ------------- |
| File systems per AWS account  | 1,000         |
| Access points per file system | 10,000        |

To request an increase, open the [AWS Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home"),
choose **Create Case**, then choose **Service Limit Increase**.

The following quotas cannot be changed.

| Resource                                            | Quota  |
| --------------------------------------------------- | ------ |
| Connections per file system                         | 25,000 |
| Mount targets per file system per Availability Zone | 1      |
| Security groups per mount target                    | 5      |
| Tags per file system                                | 50     |
| VPCs per file system                                | 1      |

There are also quotas specific to individual file systems.

| Resource                                | Quota                                     |
| --------------------------------------- | ----------------------------------------- |
| Maximum file size                       | 52,673,613,135,872 bytes (48 TiB)         |
| Maximum directory depth                 | 1,000 levels                              |
| Maximum file name length                | 255 bytes                                 |
| Maximum symlink target length           | 4,080 bytes                               |
| Maximum S3 object key length            | 1,024 bytes                               |
| Maximum open files per client           | 65,536                                    |
| Maximum active user accounts per client | 65,536                                    |
| Maximum locks per file                  | 512 across all connected instances        |
| Maximum locks per mount                 | 8,192 across up to 256 file-process pairs |
| File system policy size limit           | 20,000 characters                         |

## Unsupported NFS features

S3 Files supports NFSv4.1 and NFSv4.2, with the following exceptions:

- pNFS
- Client delegation or callbacks
- Mandatory locking (all locks are advisory)
- Deny share
- Access control lists (ACLs)
- Kerberos-based security
- NFSv4.1 data retention
- SetUID on directories
- Block devices, character devices, attribute directories, and named
  attributes
- Optional features introduced in NFSv4.2 (such as server-side copy,
  sparse file operations, space reservation, application I/O advise, application
  data blocks, labeled NFS, and custom user-defined extended attributes)
- Persistent reply cache
- The `nconnect` mount option
