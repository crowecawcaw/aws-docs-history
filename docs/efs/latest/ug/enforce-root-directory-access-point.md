# Enforcing a root directory with an access point

You can use an access point to override the root directory for a file system. When you
enforce a root directory, the NFS client using the access point uses the root directory
configured on the access point instead of the file system's root directory.

You enable this feature by setting the access point `Path` attribute when
creating an access point. The `Path` attribute is the full path of the root
directory of the file system for all file system requests made through this access
point. The full path can't exceed 100 characters in length. It can include up to
four subdirectories.

When you specify a root directory on an access point, it becomes the root directory of the
file system for the NFS client mounting the access point. For example, suppose that the
root directory of your access point is `/data`. In this case,
mounting `fs-12345678:/` using the access point has the same effect
as mounting `fs-12345678:/data` without using the access point.

When specifying a root directory in your access point, ensure that the directory permissions
are configured to allow the user of the access point to successfully mount the file system.
Specifically, make sure that the execute bit is set for the access point user or group, or for everyone.
For example, a directory permission value of 755 allows the directory user owner to list files, create files,
and mount, and all other users to list files and mount.

## Creating the root directory for an access

point

If a root directory path for an access point doesn't exist on the file system, Amazon EFS
automatically creates that root directory with the ownership and
permissions specified. Amazon EFS will not create the root directory if you do not specify the
directory ownership and permissions at creation. This approach makes it possible to provision file system access for a
specific user or application without mounting your file system from a Linux host.
To create a root directory, you have to configure the root directory ownership and permission by using the following
attributes when creating an access point:

- `OwnerUid` – The numeric POSIX user ID to use as the root directory
  owner.
- `OwnerGiD` – The numeric POSIX group ID to use as the root directory owner
  group.
- Permissions – The Unix mode of the directory. A common configuration is 755.
  Ensure that the execute bit is set for the access point user so they are able to mount. This
  configuration gives the directory owner permission to enter, list, and write
  new files in the directory. It gives all other users permission to enter and
  list files. For more information on working with Unix file and directory
  modes, see [Network File System (NFS) level users, groups, and permissions](accessing-fs-nfs-permissions.md "accessing-fs-nfs-permissions.md").

Amazon EFS creates an access point root directory only if the OwnUid, OwnGID, and permissions
are specified for the directory. If you do not provide this information, Amazon EFS does not
create the root directory. If the root directory does not exist, attempts to mount
using the access point will fail.

When you mount a file system with an access point, the root directory for the access point
is created if the directory doesn't already exist, provided that the root directory's
OwnerUid and Permissions were specified when the access point was created. If the
access point's root directory already exists before mount time, the existing permissions
aren't overwritten by the access point. If you delete the root directory, EFS
recreates it the next time that the file system is mounted using the access
point.

###### Note

If you do not specify the ownership and permissions for an access point root
directory, Amazon EFS will not create the root directory. All attempts to mount the access point
will fail.

## Security model for access point root

directories

When a root directory override is in effect, Amazon EFS behaves like a Linux NFS server with the
`no_subtree_check` option enabled.

In the NFS protocol, servers generate file handles that are used by clients as
unique references when accessing files. EFS securely generates file handles that are
unpredictable and specific to an EFS file system. When a root directory override is
in place, Amazon EFS doesn't disclose file handles for files outside the specified
root directory. However, in some cases a user might get a file handle for a file
outside of their access point by using an out-of-band mechanism. For example, they
might do so if they have access to a second access point. If they do this, they can
perform read and write operations on the file.

File ownership and access permissions are always enforced, for access to files
within and outside of a user's access point root directory.
