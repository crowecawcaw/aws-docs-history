# Accessing data using file shares

A Microsoft Windows _file share_ is a specific folder or directory on
your file system. It includes any sub folders that might exist. Clients access the file shares on your file system
using the Server Message Block (SMB) protocol. Your FSx for Windows File Server file system comes with a
default Windows file share, named `share`. You can create and manage as many other
file shares as you want by using the Windows _Shared Folders_
graphical user interface (GUI) tool.

Microsoft Windows continuously available (CA) shares provide the primary benefit of maintaining uninterrupted access to
shared files even when a server node within a cluster fails. Using CA file shares can minimize interruptions
to the server applications that are storing their data files on these file shares during file system maintenance windows.

For more information about creating and managing file shares on your FSx for Windows File Server file system, including CA shares, see
[Creating, updating, removing file shares](managing-file-shares.md "managing-file-shares.md").

## Mapping file shares

To access your file shares, use the Windows Map Network Drive functionality to map a
drive letter on your compute instance to your Amazon FSx file share. The process of mapping a file
share to a drive on your compute instance is known as _mounting_ a file share in Linux. This process differs depending on the type of
compute instance and the operating system. After your file share is mapped, your applications
and users can access files and folders on your file share as if they are local files and
folders.

For more information about mapping and mounting file shares to access data on your file system, see the following procedures:

- [Mapping a file share on an Amazon EC2 Windows instance](map-share-windows.md "map-share-windows.md").
- [Mounting a file share on an Amazon EC2 Mac instance](map-share-mac.md "map-share-mac.md")
- [Mounting a file share on an Amazon EC2 Linux instance](map-shares-linux.md "map-shares-linux.md")
