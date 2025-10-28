# Using ephemeral storage with EC2 gateways

This section describes steps you need to take to prevent data loss
when you select an ephemeral disk as storage for your gateway's cache.

Ephemeral disks provide temporary block-level storage for your Amazon EC2 instance. Ephemeral disks are ideal for temporary storage of data that
changes frequently, such as data in a gateway's cache storage. When
you launch your gateway with an Amazon EC2 Amazon Machine Image and the instance type you
select supports ephemeral storage, the ephemeral disks are listed automatically. You can
select one of the disks to store your gateway's cache data. For more information,
see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md") in the
_Amazon EC2 User Guide_.

Data that applications write to the gateway is stored synchronously in cache on the
ephemeral disks, and then asynchronously uploaded to durable storage in Amazon S3.
If the Amazon EC2 instance is stopped after data is written to ephemeral storage, but before
an asynchronous upload occurs, any data that has not yet been uploaded to Amazon S3
can be lost. You can prevent such data loss by following the
steps before you restart or stop the EC2 instance that hosts your
gateway.

###### Important

If you stop and start an Amazon EC2 gateway that uses ephemeral storage, the gateway
will be permanently offline. This happens because the physical storage disk is
replaced. There is no work-around for this issue. The only resolution is to delete
the gateway and activate a new one on a new EC2 instance.

These steps in this following procedure are specific for
File Gateways.

###### To prevent data loss in File Gateways that use ephemeral disks

1. Stop all the processes that are writing to Amazon S3.
2. Subscribe to receive notification from CloudWatch Events. For information, see [Getting notified about file operations](monitoring-file-gateway.md#get-notification "monitoring-file-gateway.md#get-notification").
3. Call the [NotifyWhenUploaded API](../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md "../../../storagegateway/latest/APIReference/API_NotifyWhenUploaded.md") to get notified when data that is written,
   up until the ephemeral storage was lost, has been durably stored in Amazon S3.
4. Wait for the API to complete and you receive a notification id.

You receive a CloudWatch event with the same notification id. 5. Verify that the `CachePercentDirty` metric for your file share is 0. This confirms that all your data has been written to Amazon S3. For information
about file share metrics, see [Understanding
file share metrics](monitoring-file-gateway.md#monitoring-file-gateway-resources "monitoring-file-gateway.md#monitoring-file-gateway-resources"). 6. You can now restart or stop the File Gateway without risk of losing any
data.
