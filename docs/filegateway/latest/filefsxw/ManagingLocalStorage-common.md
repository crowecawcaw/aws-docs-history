Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Managing local disks for your gateway

The gateway virtual machine (VM) uses the local disks that you allocate on-premises for
buffering and storage. A File Gateway that you create on an Amazon EC2 instance will use Amazon EBS
volumes as local disks. The number and size of disks that you want to allocate for your
gateway is up to you. The gateway uses the cache storage that you allocate to provide
low-latency access to your recently accessed data. The cache storage acts as the on-premises
durable store for data that is pending upload to Amazon FSx. File Gateways require at
least one 150 GiB disk to use as a cache. After the initial configuration and deployment of
your gateway, you can add more disks for cache storage as your workload demands increase.
This section contains the following topics, which describe concepts and procedures related
to managing local disks.

**Topics**

- [Deciding the amount of local disk
  storage](decide-local-disks-and-sizes.md "decide-local-disks-and-sizes.md") - Learn how to determine the
  number and size of local cache disks to allocate for your File Gateway.
- [Configuring additional cache
  storage](ConfiguringLocalDiskStorage.md "ConfiguringLocalDiskStorage.md") - Learn how to increase the cache
  storage capacity of your File Gateway as your application needs change.
- [Using ephemeral storage with EC2 gateways](ephemeral-disk-cache.md "ephemeral-disk-cache.md") -
  Learn how to prevent data loss when using ephemeral disk storage with
  File Gateway.
