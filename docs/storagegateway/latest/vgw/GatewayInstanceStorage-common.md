# Managing Amazon EBS volumes on Amazon EC2

gateways

When you initially configured your gateway to run as an Amazon EC2 instance, you allocated
Amazon EBS volumes for use as an upload buffer and cache storage. Over time, as your applications
needs change, you can allocate additional Amazon EBS volumes for this use. You can also reduce
the storage you allocated by removing previously allocated Amazon EBS volumes. For more
information about Amazon EBS, see [Amazon Elastic Block Store
(Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") in the _Amazon EC2 User Guide_.

Before you add more storage to the gateway, you should review how to size your upload
buffer and cache storage based on your application needs for a gateway. To do so, see [Determining the size of
upload buffer to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common "decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common") and [Determining the size of cache
storage to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskCacheSizing-common "decide-local-disks-and-sizes.md#CachedLocalDiskCacheSizing-common").

There are quotas on the maximum storage you can allocate as an upload buffer and cache
storage. You can attach as many Amazon EBS volumes to your instance as you want, but you can only
configure these volumes as upload buffer and cache storage space up to these storage quotas.
For more information, see [AWS Storage Gateway quotas](resource-gateway-limits.md "resource-gateway-limits.md").

###### To add an Amazon EBS volume and configure it

for your gateway

1. Create an Amazon EBS volume. For instructions, see [Creating or Restoring an Amazon EBS
   Volume](../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md "../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md") in the _Amazon EC2 User Guide_.
2. Attach the Amazon EBS volume to your Amazon EC2 instance. For instructions, see [Attaching an Amazon EBS Volume to
   an Instance](../../../AWSEC2/latest/UserGuide/ebs-attaching-volume.md "../../../AWSEC2/latest/UserGuide/ebs-attaching-volume.md") in the _Amazon EC2 User Guide_.
3. Configure the Amazon EBS volume you added as either an upload buffer or cache storage.
   For instructions, see [Managing local disks for your Storage Gateway](ManagingLocalStorage-common.md "ManagingLocalStorage-common.md").
   There are times you might find you don’t need the amount of storage you allocated for the
   upload buffer.

###### To remove an Amazon EBS volume

###### Warning

These steps apply only for Amazon EBS volumes allocated as upload buffer space, not for
volumes allocated to cache.

1. Shut down the gateway by following the approach described in the [Shutting Down Your Gateway VM](MaintenanceShutDown-common.md "MaintenanceShutDown-common.md") section.
2. Detach the Amazon EBS volume from your Amazon EC2 instance. For instructions, see [Detaching an Amazon EBS Volume
   from an Instance](../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md "../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md") in the _Amazon EC2 User Guide_.
3. Delete the Amazon EBS volume. For instructions, see [Deleting an Amazon EBS
   Volume](../../../AWSEC2/latest/UserGuide/ebs-deleting-volume.md "../../../AWSEC2/latest/UserGuide/ebs-deleting-volume.md") in the _Amazon EC2 User Guide_.
4. Start the gateway by following the approach described in the [Shutting Down Your Gateway VM](MaintenanceShutDown-common.md "MaintenanceShutDown-common.md") section.
