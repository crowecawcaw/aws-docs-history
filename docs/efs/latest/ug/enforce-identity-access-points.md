# Enforcing a user identity using an access point

You can use an access point to enforce user and group information for all file system requests
made through the access point. To enable this feature, you need to specify the operating system identity to enforce when you create the access point.

As part of this, you provide the following:

- User ID – The numeric POSIX user ID for the user.
- Group ID – The numeric POSIX group ID for the user.
- Secondary group IDs – An optional list of secondary group IDs.
  When user enforcement is enabled, Amazon EFS replaces the NFS client's user and group IDs with
  the identity configured on the access point for all file system operations. User
  enforcement also does the following:

- The owner and group for new files and directories are set to the user ID and group ID of the access point.
- EFS considers the user ID, group ID, and secondary group IDs of the access point when
  evaluating file system permissions. EFS ignores the NFS client's IDs.

###### Important

Enforcing a user identity is subject to the `ClientRootAccess` IAM permission.

For example, in some cases you might configure the access point user ID, group ID,
or both to be root (that is, setting the UID, GID, or both to 0). In such cases, you
must grant the `ClientRootAccess` IAM permission to the NFS
client.
