# Create an NFS file share

The Network File System (NFS) protocol is a stateful file sharing protocol for Unix-based
systems. When an NFS-enabled client and NFS server communicate, the client requests a file
or directory from the server using remote procedure calls (RPC). The server verifies that
the file or directory is available and that the client has the required access permissions.
The server then mounts the file or directory remotely on the client and shares access via a
virtual connection. For client operations, NFS makes using the remote server file similar to
accessing a local file.

###### Note

The NFS protocol supports a maximum of 16 groups per user. Users might have issues mounting NFS file
shares if they belong to more than 16 groups. To avoid mounting issues, make sure that users are members
of 16 or fewer groups when accessing NFS file shares.

The following topics explain various methods for creating an NFS file share for your
File Gateway:

###### Contents

- [Create an NFS file share using the
  default configuration](nfs-fileshare-quickstart-settings.md "nfs-fileshare-quickstart-settings.md")
  - [Default configuration settings for NFS file
    shares](nfs-fileshare-quickstart-settings.md#quickstart-default-settings "nfs-fileshare-quickstart-settings.md#quickstart-default-settings")

- [Create an NFS file share with a custom
  configuration](CreatingAnNFSFileShare.md "CreatingAnNFSFileShare.md")
