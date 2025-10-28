# Managing Your

Volume Gateway

Managing your gateway includes tasks such as configuring cache storage and upload buffer
space, working with volumes, and doing general maintenance. If you haven't created a gateway, see
[Getting started with AWS Storage Gateway](GettingStarted.md "GettingStarted.md").

Cached volumes are volumes in Amazon Simple Storage Service (Amazon S3) that are exposed as iSCSI
targets on which you can store your application data. You can find information following
about how to add and delete volumes for your cached setup. You can also learn how to add and
remove Amazon Elastic Block Store (Amazon EBS) volumes in Amazon EC2 gateways.

###### Important

If a cached volume keeps your primary data in Amazon S3, you should avoid processes that
read or write all data on the entire volume. For example, we don't recommend using
virus-scanning software that scans the entire cached volume. Such a scan, whether done
on demand or scheduled, causes all data stored in Amazon S3 to be downloaded locally for
scanning, which results in high bandwidth usage. Instead of doing a full disk scan, you
can use real-time virus scanning—that is, scanning data as it is read from or
written to the cached volume.

Resizing a volume is not supported. To change the size of a volume, create
a snapshot of the volume, and then create a new cached volume from the snapshot. The new
volume can be bigger than the volume from which the snapshot was created. For steps
describing how to remove a volume, see [To delete a volume](ApplicationStorageVolumesCached-Removing.md#CachedRemovingAStorageVolume "ApplicationStorageVolumesCached-Removing.md#CachedRemovingAStorageVolume"). For steps describing how to add a volume
and preserve existing data, see [Deleting storage
volumes](ApplicationStorageVolumesCached-Removing.md "ApplicationStorageVolumesCached-Removing.md").

All cached volume data and snapshot data is stored in Amazon S3 and is
encrypted at rest using server-side encryption (SSE). However, you cannot access this data
by using the Amazon S3 API or other tools such as the Amazon S3 Management Console.

Following, you can find information about how to manage your Volume Gateway
resources.

**Topics**

- [Editing Basic Gateway Information](edit-gateway-information.md "edit-gateway-information.md") - Learn how to use the Storage Gateway console to edit basic information for an existing
  gateway, including the gateway name, time zone, and CloudWatch log group.
- [Adding and expanding volumes](volume-size-increase.md "volume-size-increase.md") -
  Learn how to add more volumes to your gateway, or expand the size of existing
  volumes as your application needs grow.
- [Cloning a cached volume from a recovery point](clone-volume.md "clone-volume.md") - Learn how to create
  a new volume from an existing volume's recovery point, which is a saved point in
  time when all of the data on the volume is consistent.
- [Viewing volume usage](volume-usage.md "volume-usage.md") - Learn how to view
  the amount of data stored on a volume by using the Storage Gateway console.
- [Deleting storage
  volumes](ApplicationStorageVolumesCached-Removing.md "ApplicationStorageVolumesCached-Removing.md") - Learn how to delete
  a volume if your application needs change, such as if you migrate an application to
  use a larger storage volume.
- [Moving Your Volumes to a Different
  Gateway](attach-detach-volume.md "attach-detach-volume.md") -
  Learn how to detach and reattach volumes, which is useful if you need to move your
  volumes to a different Volume Gateway as your performance needs change.
- [Creating a recovery snapshot](snapshot.md "snapshot.md") - Learn how to create a
  recovery snapshot from a volume recovery point for a gateway, and where to find that
  snapshot in the Storage Gateway console after you create it.
- [Editing a snapshot schedule](SchedulingSnapshot.md "SchedulingSnapshot.md") - Learn
  how to customize a snapshot schedule by changing either the time the snapshot occurs
  each day or the frequency that snapshots are taken.
- [Deleting snapshots of your storage volumes](DeletingASnapshot.md "DeletingASnapshot.md") - Learn how
  to delete unnecessary snapshots when you no longer need them.
- [Understanding Volume Statuses and
  Transitions](StorageVolumeStatuses.md "StorageVolumeStatuses.md") -
  Learn about the various volume status values that Storage Gateway reports to help determine
  whether a volume is functioning normally, or if there is a problem that might
  require action on your part.
- [Moving your data to a new gateway](migrate-data.md "migrate-data.md") - Learn how to move
  data between gateways as your data and performance needs grow, or if you receive an
  AWS notification to migrate your gateway.
