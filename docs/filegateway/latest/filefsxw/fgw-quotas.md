Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Limits and quotas for Amazon FSx File Gateway

## Quotas for Amazon FSx file systems

The following table lists minimum and maximum limits and quotas for Amazon FSx file
systems.

| Resource                                                                                       | Limit per Amazon FSx file system |
| ---------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum number of tags                                                                         | 50 tags                          |
| Maximum retention period for automated backups                                                 | 90 days                          |
| Maximum number of backup copy requests in progress to a single destination Region per account. | 5 requests                       |
| Minimum storage capacity for SSD file systems                                                  | 32 GiB                           |
| Minimum storage capacity for HDD file systems                                                  | 2,000 GiB                        |
| Maximum storage capacity for SSD and HDD file systems                                          | 64 TiB                           |
| Minimum throughput capacity                                                                    | 8 MBps                           |
| Maximum throughput capacity                                                                    | 2,048 MBps                       |
| Maximum number of Amazon FSx file shares                                                       | 100,000                          | ## Recommended local disk sizes for your gateway The following table recommends sizes for local disk storage for each AWS Storage Gateway in your deployment. |
| Gateway Type                                                                                   | Cache (Minimum)                  | Cache (Maximum)                                                                                                                                               |
| ---                                                                                            | ---                              | ---                                                                                                                                                           |
| FSx File Gateway                                                                               | 150 GiB                          | 64 TiB                                                                                                                                                        | ###### Note You can configure one or more local drives for your cache up to the maximum capacity. When adding cache to an existing FSx File Gateway, it is important to create new disks on your virtual host (hypervisor or Amazon EC2 instance). Do not change the size of existing disks if the disks have been previously allocated as a cache. |
