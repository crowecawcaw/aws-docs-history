# How application settings

persistence works

Persistent application settings are saved to a Virtual Hard Disk (VHD) file. This file
is created the first time a user streams an application from a directory on which
application settings persistence is enabled. If the WorkSpace Pool associated with the
directory is based on an image that contains default application and Windows settings,
the default settings are used for the user's first streaming
session.

When the streaming session ends, the VHD is unmounted and uploaded to an Amazon S3 bucket
within your account. The bucket is created when you enable persistent application
settings for the first time for a directory in an AWS Region. The bucket is unique to
your AWS account and the Region. The VHD is encrypted in transit using Amazon S3 SSL
endpoints, and at rest using [AWS
Managed CMKs](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk").

The VHD is mounted to the WorkSpace in both `C:\Users\%username%` and
`D:\%username%`. If your WorkSpace is not joined to an Active Directory
domain, the Windows user name is PhotonUser. If your WorkSpace is joined to an Active
Directory domain, the Windows user name is that of the logged in user.

Application settings persistence does not work across different operating system
versions. For example, if you enable application settings persistence for a WorkSpace Pool that
uses a Windows Server 2019 image, if you update the WorkSpace Pool to use an image that runs a different operating
system (such as Windows Server 2022), settings from previous streaming sessions are not
saved for users of the directory. Instead, after you update the WorkSpace Pool to use
the new image, when users launch a streaming session from a WorkSpace, a new Windows
user profile is created. However, if you apply an update to the same operating system on
the image, users' customizations and settings from previous streaming sessions are
saved. When updates to the same operating system are applied to an image, the same
Windows user profile is used when users launch a streaming session from the WorkSpace.

###### Important

WorkSpaces Pools supports applications that rely on the [Microsoft Data Protection API](https://docs.microsoft.com/en-us/windows/desktop/seccng/cng-dpapi "https://docs.microsoft.com/en-us/windows/desktop/seccng/cng-dpapi") only when the WorkSpace is joined to a
Microsoft Active Directory domain. In cases where a WorkSpace is not joined to an
Active Directory domain, the Windows user, PhotonUser, is different on each
WorkSpace. Due to the way in which the DPAPI security model works, users' passwords
don’t persist for applications that use DPAPI in this scenario. In cases where WorkSpaces
are joined to an Active Directory domain and the user is a domain user, the Windows
user name is that of the logged in user, and users’ passwords persist for
applications that use DPAPI.

WorkSpaces Pools automatically saves all files and folders in this path, except for the
following folders:

- Contacts
- Desktop
- Documents
- Downloads
- Links
- Pictures
- Saved Games
- Searches
- Videos
  Files and folders created outside of these folders are saved within the VHD and synced
  to Amazon S3. The default VHD maximum size is 5 GB for Pools. The size of the saved VHD is
  the total size of the files and folders that it contains. WorkSpaces Pools automatically saves
  the `HKEY_CURRENT_USER` registry hive for the user. For new users (users
  whose profiles don't exist in Amazon S3), WorkSpaces Pools creates the initial profile by using the
  default profile. This profile is created in the following location on the image builder:
  `C:\users\default`.

###### Note

The entire VHD must be downloaded to the WorkSpace before a streaming session can
begin. For this reason, a VHD that contains a large amount of data can delay the
start of the streaming session. For more information, see [Best practices for
enabling application settings persistence](enabling-app-settings-persistence.md#best-practices-app-settings-persistence "enabling-app-settings-persistence.md#best-practices-app-settings-persistence").

When you enable application settings persistence, you must specify a settings group.
The settings group determines which saved application settings are used for a streaming
session from this directory. WorkSpaces Pools creates a new VHD file for the settings group
that is stored separately within the S3 bucket in your AWS account. If the settings
group is shared between directories, the same application settings are used in each
directory. If a directory requires its own application settings, specify a unique
settings group for the directory.
