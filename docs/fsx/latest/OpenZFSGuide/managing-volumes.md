# Managing Amazon FSx for OpenZFS volumes

An FSx for OpenZFS file system can contain one or more
_volumes_, which are isolated data containers for
files and directories. Every FSx for OpenZFS file system has one (and only one)
_root volume_, which is created at file system
creation time. All other volumes created on a file system are children of the root volume.

After the file system is created, you can create volumes as needed. Each
customer-created volume is a child of another volume.
This means that all volumes are children or descendants of the root volume. For
example, you could create 10 volumes with each one being a child of the root
volume (that is, all 10 volumes are siblings) or you could create a hierarchy
of 10 volumes in which each volume is a child of the previous volume.

You use volumes to logically separate an individual file system into
multiple namespaces. This allows you to independently manage the storage capacity,
compression, NFS exports, record size, and user and group quotas at the volume level.

You access volumes from Linux, Windows, or macOS clients over the Network File
System (NFS) protocol (v3, v4.0, v4.1, or v4.2). FSx for OpenZFS presents data to your users
and applications as a local directory or drive.

###### Topics

- [Creating a volume](creating-volumes.md "creating-volumes.md")
- [Viewing a volume](viewing-volumes.md "viewing-volumes.md")
- [Updating a volume](updating-volumes.md "updating-volumes.md")
- [Deleting a volume](deleting-volumes.md "deleting-volumes.md")
