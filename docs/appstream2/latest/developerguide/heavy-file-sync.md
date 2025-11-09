# Enabling and Disabling Heavy File Sync Mode for Home

Folders

You can enable Amazon Simple Storage Service Home Folders options for your organization. When you
enable Amazon S3 Home Folders for an WorkSpaces Applications stack, users of the stack can access
a persistent storage folder during their application streaming sessions. No further
conﬁguration is required for your users to access their home folder. Data stored by
users in their home folder is automatically backed up to an Amazon S3 bucket in
your AWS account, and is made available to those users in subsequent sessions. For
more information, see [Enable and Administer Home Folders for Your WorkSpaces Applications
Users](home-folders.md "home-folders.md").

To ensure a smooth experience and address some existing limitations, where an
inconsistent file sync might be observed when users save large text files from their
streaming instances to their Home Folders, WorkSpaces Applications administrators can turn on the
**heavy_sync** configuration option if large file uploads to
Amazon S3 is a common user scenario while using WorkSpaces Applications. Turning on this option
means that it might add some latency to the home folder file sync process, but
completeness of all syncs to Amazon S3 is guaranteed.

This feature is available on all Red Hat Enterprise Linux images, and Linux WorkSpaces Applications
images that use a Linux WorkSpaces Applications agent released on or after September 12, 2024.

The heavy sync feature is disabled by default for Red Hat Enterprise Linux and Amazon
Linux streaming sessions. To configure heavy sync permission for your users on a Red Hat
Enterprise Linux or Amazon Linux image builder, create
`/etc/appstream/appstream.conf` and add the following
contents:

###### Note

Specify `1` to enable heavy sync, or `0`
to disable heavy sync.

```
[storage]
heavy_sync = 1
```
