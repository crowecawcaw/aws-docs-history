# File and directory permissions

Files and directories in an EFS file system support standard Unix-style read, write, and
execute permissions based on the user and group ID asserted by the mounting NFSv4.1 client, unless overridden by an EFS access point.
 For more information, see [Network File System (NFS) level users, groups, and permissions](accessing-fs-nfs-permissions.md "accessing-fs-nfs-permissions.md").

###### Note

By default, this layer of access control depends on trusting the NFSv4.1 client in its assertion of
the user and group ID.
You can use AWS Identity and Access Management (IAM) resource-based policies and identity policies
to authorize NFS clients and provide read-only, write, and root access permissions.
You can use EFS access points to override the operating system user and group identity
information provided by the NFS client. For more information, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md")
and [Creating access points](create-access-point.md "create-access-point.md").

As an example of read, write, and execute permissions for files and directories, Alice
might have permissions to read and write to any files that she wants to in her personal
directory on a file system, `/alice`. However, in this example Alice is not allowed
to read or write to any files in Mark's personal directory on the same file
system, `/mark`. Both Alice and Mark are allowed to read but not write files in
the shared directory `/share`.
