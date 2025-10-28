Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Using ephemeral storage with EC2 gateways

We do not recommend the use of ephemeral disks for cache storage
on FSx File Gateways.

Ephemeral disks provide temporary block-level storage for your Amazon EC2 instance. When
you launch your gateway with an Amazon EC2 Amazon Machine Image and the instance type you
select supports ephemeral storage, the ephemeral disks are listed automatically. You can
select one of the disks to store your gateway's cache data. For more information,
see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md") in the
_Amazon EC2 User Guide_.

Data that applications write to the gateway is stored synchronously in cache on the
ephemeral disks, and then asynchronously uploaded to durable storage in FSx for Windows File Server.
If the Amazon EC2 instance is stopped after data is written to ephemeral storage, but before
an asynchronous upload occurs, any data that has not yet been uploaded to FSx for Windows File Server
can be lost.

###### Important

If you stop and start an Amazon EC2 gateway that uses ephemeral storage, the gateway
will be permanently offline. This happens because the physical storage disk is
replaced. There is no work-around for this issue. The only resolution is to delete
the gateway and activate a new one on a new EC2 instance.
