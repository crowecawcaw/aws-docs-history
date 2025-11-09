# Service quotas on Amazon FSx for OpenZFS resources

FSx for OpenZFS has default AWS account and file system resource quotas. The following sections contain information on these quotas as well as how to request an increase from the default limit.

###### Topics

- [Resource quotas for each file
  system](#limits-openzfs-resources-file-system "#limits-openzfs-resources-file-system")
- [Resource quotas for each AWS account](#soft-limits "#soft-limits")
- [Requesting a quota increase](#request-quota-increase "#request-quota-increase")

## Resource quotas for each file

system

Following are the default quotas on FSx for OpenZFS resources for each file system in an AWS Region. For information on how to request an increase on a quota, see [Requesting a quota increase](#request-quota-increase "#request-quota-increase").

| Resource                                                                              | Limit per file system |
| ------------------------------------------------------------------------------------- | --------------------- |
| Minimum storage capacity                                                              | 64 GiB                |
| Maximum storage capacity                                                              | 512 TiB 1             |
| Minimum throughput capacity                                                           | 64 MBps               |
| Maximum throughput capacity                                                           | 10,240 MBps           |
| Maximum number of volumes                                                             | 100                   |
| Maximum number of user and group quotas per volume                                    | 100                   |
| Maximum number of snapshots                                                           | 700                   |
| Maximum number of tags                                                                | 50                    |
| Maximum retention period for automated backups                                        | 90 days               |
| Maximum retention period for user-initiated backups                                   | no retention limit    |
| Maximum storage capacity for file systems using the Intelligent-Tiering storage class | 512 TiB               |
| Maximum number of client connections per file server                                  | 32,7682               |

###### Note

1 The maximum storage capacity for Single-AZ 2 (non-HA and HA) file systems is 512 TiB. The maximum storage capacity for Single-AZ 1 (non-HA and HA) and Multi-AZ (HA) file systems depends on the file system's provisioned throughput capacity, deployment type, and AWS Region. For more information, see the following tables.

2 For more information, see [Data access from cache](performance-ssd.md#data-access-memory-cache "performance-ssd.md#data-access-memory-cache").

| Provisioned throughput capacity (MBps) | Maximum Storage Capacity (TiB)2 | Maximum Storage Capacity (TiB)3 | Maximum Storage Capacity (TiB)4 |
| -------------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| 160                                    | 32                              | 24                              | 96                              |
| 320                                    | 64                              | 48                              | 128                             |
| 640                                    | 128                             | 96                              | 128                             |
| 1,280                                  | 256                             | 128                             | 128                             |
| 2,560                                  | 512                             | 128                             | 128                             |
| 3,840                                  | 512                             | 128                             | 128                             |
| 5,120                                  | 512                             | 128                             | 128                             |
| 7,680                                  | 512                             | –                               | –                               |
| 10,240                                 | 512                             | –                               | –                               |

###### Note

2 These storage capacity limits apply to the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Europe (Frankfurt),
Asia Pacific (Tokyo), Asia Pacific (Sydney), Asia Pacific (Singapore).

3 These storage capacity limits apply to the following AWS Regions: Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Mumbai), Asia Pacific (Hong Kong),
Canada (Central),Europe (Milan), Europe (Paris), Europe (London), Europe (Stockholm) Israel (Tel Aviv), Middle East (Bahrain), South America (São Paulo), Europe (Zurich), Europe (Spain).

4 These storage capacity limits apply to the following AWS Regions: US West (N. California), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Jakarta),
Middle East (UAE), AWS GovCloud (US-East), AWS GovCloud (US-West).

| Provisioned throughput capacity (MBps) | Maximum Storage Capacity (TiB) 5 | Maximum Storage Capacity (TiB) 6 |
| -------------------------------------- | -------------------------------- | -------------------------------- |
| 64                                     | 512                              | 128                              |
| 128                                    | 512                              | 128                              |
| 256                                    | 512                              | 128                              |
| 512                                    | 512                              | 128                              |
| 1,024                                  | 512                              | 128                              |
| 2,048                                  | 512                              | 128                              |
| 3,072                                  | 512                              | 128                              |
| 4,096                                  | 512                              | 128                              |

###### Note

5 These storage capacity limits apply to the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon),
Europe (Stockholm), Europe (London), Europe (Ireland), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Mumbai),
Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Hong Kong), Canada (Central).

6 These storage capacity limits apply to the following AWS Regions: US West (N. California), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Jakarta),
Asia Pacific (Osaka), Europe (Milan), Europe (Paris), Israel (Tel Aviv), Middle East (UAE), Middle East (Bahrain), South America (São Paulo), AWS GovCloud (US-East), AWS GovCloud (US-West), Europe (Zurich), Europe (Spain).

| Provisioned throughput capacity (MBps) | Maximum access points per file system |
| -------------------------------------- | ------------------------------------- |
| 128                                    | 3                                     |
| 256                                    | 6                                     |
| 512                                    | 13                                    |
| 1,024                                  | 27                                    |
| 2,048                                  | 55                                    |
| 3,072                                  | 83                                    |
| 4,096                                  | 110                                   |

| Provisioned throughput capacity (MBps) | Maximum access points per file system |
| -------------------------------------- | ------------------------------------- |
| 160                                    | 4                                     |
| 320                                    | 8                                     |
| 640                                    | 17                                    |
| 1,280                                  | 34                                    |
| 2,560                                  | 69                                    |
| 3,840                                  | 103                                   |
| 5,120                                  | 138                                   |
| 7,680                                  | 207                                   |
| 10,240                                 | 276                                   |

## Resource quotas for each AWS account

Following are the default quotas for Amazon FSx for OpenZFS for each AWS account, per AWS Region. For information on how to request an increase on a quota, see [Requesting a quota increase](#request-quota-increase "#request-quota-increase").

| Resource                                                 | Default                                                                         | Description                                                                                                                                |
| -------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| OpenZFS file systems                                     | 100                                                                             | The maximum number of Amazon FSx for OpenZFS file systems that you can create in this account.                                             |
| OpenZFS SSD storage capacity                             | 65,536 (262,144 in US East (N. Virginia), US East (Ohio), and US West (Oregon)) | The maximum amount of SSD storage capacity (in GiB) that you can configure for all<br>Amazon FSx for OpenZFS file systems in this account. |
| OpenZFS throughput capacity                              | 10,240                                                                          | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for OpenZFS file systems in this account.                     |
| OpenZFS disk IOPS                                        | 400,000                                                                         | The total amount of disk IOPS allowed for all Amazon FSx for OpenZFS file systems in this account.                                         |
| OpenZFS backups                                          | 10,000                                                                          | The maximum number of user-initiated backups for all Amazon FSx for OpenZFS file systems that you can have in this account.                |
| OpenZFS Intelligent-Tiering SSD read cache storage (GiB) | 65,536 (262,144 in US East (N. Virginia), US East (Ohio), and US West (Oregon)) | The maximum amount of SSD read cache storage that you configure across all file systems using the Intelligent-Tiering storage class.       |

## Requesting a quota increase

You can request an increase for all AWS account quotas. You can also request an increase on the following file system quotas:

- Maximum number of volumes
- Maximum number of user and group quotas per volume
- Maximum number of snapshots
- Maximum storage capacity for file systems using the Intelligent-Tiering storage class

###### To request a quota increase

1. Open the [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") page, sign
   in if necessary, and then choose **Create case**.
2. For **Create case**, choose **Account and billing support**.
3. In the **Case details** panel make the following entries:
   - For **Type** choose **Account**.
   - For **Category** choose **Other Account Issues**.
   - For **Subject** enter `Amazon FSx for OpenZFS service limit increase request`.
   - Provide a detailed **Description** of your request, including:
     - The FSx quota that you want increased, and the value you want it increased to, if known.
     - The reason why you are seeking the quota increase.
     - The file system ID and region for each file system you are requesting an increase for.

4. Provide your preferred **Contact options** and choose **Submit**.
