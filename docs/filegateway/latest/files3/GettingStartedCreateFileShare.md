# Creating a file share

In this section, you can find instructions on how to create a file share that can be
accessed using the Network File System (NFS) or the Server Message Block (SMB)
protocol.

When you create an NFS share, anyone who has access to the NFS server can access the NFS
file share by default. You can limit access to clients by IP address.

When you create an SMB file share, you can use one of three modes of
authentication:

- A file share with Microsoft Active Directory (AD) access. Any authenticated
  Microsoft AD user gets access to this file share type.
- An SMB file share with limited access. Only certain domain users and groups that
  you specify are allowed access (through an allow list). Users and groups can also be
  denied access (through a deny list).
- An SMB file share with guest access. Any user who can provide the guest password
  has access to this file share.

###### Note

File shares that are exported through the gateway for NFS file shares support
POSIX permissions. For SMB file shares, you can use access control lists (ACLs)
to manage permissions on files and folders in your file share. For more
information, see [Using Windows ACLs to limit SMB file share access](smb-acl.md "smb-acl.md").
A File Gateway can host one or more file shares of different types. You can have multiple
NFS and SMB file shares on a File Gateway.

###### Important

To create a file share, a File Gateway requires you to activate AWS Security Token Service (AWS STS). If
AWS STS isn't activated in the AWS Region where you create your File Gateway, activate
it. For information about how to activate AWS STS, see
[Activating and deactivating AWS Security Token Service in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the
_AWS Identity and Access Management User Guide_.

###### Topics

- [Avoiding unanticipated costs when uploading
  gateway data](avoid-unanticipated-costs.md "avoid-unanticipated-costs.md")
- [Encrypt objects stored
  by File Gateway in Amazon S3](encrypt-objects-stored-by-file-gateway-in-amazon-s3.md "encrypt-objects-stored-by-file-gateway-in-amazon-s3.md")
- [Create an NFS file share](create-nfs-file-share.md "create-nfs-file-share.md")
- [Create an SMB file share](create-smb-file-share.md "create-smb-file-share.md")
