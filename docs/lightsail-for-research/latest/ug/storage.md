# Secure and store data with Lightsail for Research volumes

Amazon Lightsail for Research provides block-level storage volumes (disks) that you can attach to a running
Lightsail for Research virtual computer. You can use a disk as a primary storage device for data that
requires frequent and granular updates. For example, disks are the recommended storage
option when you run a database on a Lightsail for Research virtual computer.

A disk behaves like an unformatted external block device that you can attach to a single
virtual computer. The volume persists independently from the running life of a computer.
After you attach a disk to a computer, you can use it like any other physical hard drive.

You can attach multiple disks to a computer. You can also detach a disk from one computer
and attach it to another
computer.

To keep a backup copy of your data, create a snapshot of the disk. You can create a new
disk from a snapshot and attach it to another computer.

###### Topics

- [Create a storage disk in the Lightsail for Research console](create-disk.md "create-disk.md")
- [View storage disk details in the Lightsail for Research console](view-disk.md "view-disk.md")
- [Add storage to a virtual computer in Lightsail for Research](attach-disk.md "attach-disk.md")
- [Detach a disk from a virtual computer in Lightsail for Research](detach-disk.md "detach-disk.md")
- [Delete unused storage disks in Lightsail for Research](delete-disk.md "delete-disk.md")
