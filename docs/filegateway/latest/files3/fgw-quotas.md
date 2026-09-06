

# Limits and quotas for Amazon S3 File Gateway
<a name="fgw-quotas"></a>

## Quotas for file shares
<a name="resource-file-limits"></a>

The following table lists quotas for file shares.


| Description | Limit | 
| --- | --- | 
| Maximum number of file shares per gateway Each file share can only connect to one S3 bucket, but multiple file shares can connect to the same bucket. If you connect more than one file share to the same bucket, you must configure each file share to use a unique, non-overlapping prefix name to prevent read/write conflicts. <br />The number of file shares managed by a gateway can impact the gateway's performance. For more information, see [Performance guidance for gateways with multiple file shares](https://docs.aws.amazon.com/filegateway/latest/files3/Performance.html#performance-multiple-file-shares).   | 50 | 
| The maximum number of files for which a gateway can simultaneously cache metadata Because S3 File Gateway is backed by Amazon S3, there is no maximum folder size or limit to the number of files that you can store or access using a gateway. <br />Each gateway has a configurable limit that determines the number of files for which it can simultaneously cache metadata. You can use the [UpdateGatewayInformation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateGatewayInformation.html) API action to set [GatewayCapacity](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateGatewayInformation.html#StorageGateway-UpdateGatewayInformation-request-GatewayCapacity) to `Small`, `Medium`, or `Large`. This setting impacts gateway performance and hardware recommendations. For more information, see [Performance guidance for gateways with multiple file shares](https://docs.aws.amazon.com/filegateway/latest/files3/performance-multiple-file-shares.html).   | **Gateway Capacity:**<br />Small — 5M files<br />Medium — 10M files<br />Large — 20M files | 
| The maximum size of an individual file  If you try to write files larger than the size limit piece by piece, only the first 5 TiB will be uploaded. If you try to write the files larger than the size limit all at once, on Windows clients no file is created and on Linux clients a file of size zero is created.   | 5 TiB | 
| Maximum path length Clients are not allowed to create a path exceeding this length, and doing so results in an error. This limit applies to both protocols supported by File Gateways, NFS and SMB. <br />Path length in bytes is calculated from character bit values in UTF-8 encoding.  | 1024 bytes | 
| Maximum file name length File Gateway does not support file names that exceed this length. <br />File name length in bytes is calculated from character bit values in UTF-8 encoding.  | 255 bytes | 

## Recommended local disk sizes for your gateway
<a name="disk-sizes"></a>

The following table recommends sizes for local disk storage for your deployed gateway. 


| Gateway Type | Cache (Minimum) | Cache (Maximum) | 
| --- | --- | --- | 
| S3 File Gateway | 150 GiB | 64 TiB | 

**Note**  
You can configure one or more local drives for your cache up to the maximum capacity.  
When adding cache to an existing gateway, it's important to create new disks in your host (hypervisor or Amazon EC2 instance). Don't change the size of existing disks if the disks have been previously allocated as a cache.