# Configuring Amazon EFS file system

permissions

By default, only the root user (UID `0`) has read, write, and execute
permissions for a newly created EFS file system. For other users to modify the file system,
the root user must explicitly grant them access. The user for the RDS for Oracle DB instance is in
the `others` category. For more information, see [Working with users, groups, and
permissions at the Network File System (NFS) Level](../../../efs/latest/ug/accessing-fs-nfs-permissions.md "../../../efs/latest/ug/accessing-fs-nfs-permissions.md") in the _Amazon Elastic File System
User Guide_.

To allow your RDS for Oracle DB instance to read and write files on an EFS file system, do the
following:

- Mount an EFS file system locally on your Amazon EC2 or on-premises instance.
- Configure fine grain permissions.
  For example, to grant `other` users permissions to write to the EFS file system
  root, run `chmod 777` on this directory. For more information, see [Example Amazon EFS file system use cases and permissions](../../../efs/latest/ug/accessing-fs-nfs-permissions.md#accessing-fs-nfs-permissions-ex-scenarios "../../../efs/latest/ug/accessing-fs-nfs-permissions.md#accessing-fs-nfs-permissions-ex-scenarios") in the _Amazon Elastic File System
  User Guide_.
