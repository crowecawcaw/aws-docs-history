# Creating an Amazon FSx for OpenZFS file system

This section contains instructions on how to create a file system using the AWS CLI and the Amazon FSx API, as well as details on the file system properties that you can configure. For information on how to create a file system using the Amazon FSx console, see [Step 1: Create a file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1").

###### Topics

- [Creating a file system (AWS CLI and Amazon FSx API)](#create-file-system-cli "#create-file-system-cli")
- [Configurable file system properties](#fsx-openzfs-file-system-properties "#fsx-openzfs-file-system-properties")

## Creating a file system (AWS CLI and Amazon FSx API)

**To create an FSx for OpenZFS file system (CLI and API)**

Use the [create-file-system](../../../cli/latest/reference/fsx/create-file-system.md "../../../cli/latest/reference/fsx/create-file-system.md") CLI command (or the equivalent [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md") API operation). The following
example creates an FSx for OpenZFS file system with a
`SINGLE_AZ_1` deployment type.

```
aws fsx create-file-system\
  --region us-east-1 \
   --file-system-type OPENZFS \
   --storage-capacity 10000 \
   --storage-type SSD \
   --security-group-ids sg-0123456789abcdef3,sg-0123abcd4567ef89a \
   --subnet-ids subnet-1234567890abcdef4 \
   --tags Key=creator,Value=allison \
   --open-zfs-configuration '{
      "AutomaticBackupRetentionDays": 30,
      "CopyTagsToBackups": true,
      "DailyAutomaticBackupStartTime": "02:00",
      "DeploymentType": "SINGLE_AZ_1",
      "DiskIopsConfiguration": {
         "Iops": 250,
         "Mode": "USER_PROVISIONED"
      },
      "RootVolumeConfiguration": {
         "CopyTagsToSnapshots": true,
         "DataCompressionType": "LZ4",
         "NfsExports": [
            {
               "ClientConfigurations": [
                  {
                     "Clients": "*",
                     "Options": [ "rw","root_squash","crossmnt" ]
                  }
               ]
            }
         ],
         "ReadOnly": false,
         "RecordSizeKiB": 128,
         "UserAndGroupQuotas": [
            {
               "Id": 1001,
               "StorageCapacityQuotaGiB": 2000,
               "Type": "GROUP"
            }
         ]
      },
      "ThroughputCapacity": 128
   }'
```

After successfully creating the file system, Amazon FSx returns the file
system's description in JSON format.

## Configurable file system properties

When you create a file system, you specify the following file system properties:

- **Deployment type** – The deployment type of your
  file system—Multi-AZ (HA), Single-AZ (HA), or Single-AZ (non-HA). Multi-AZ (HA) file systems provide additional resiliency by replicating your data and provide high availability by automatically failing over between multiple Availability Zones within the same AWS Region.
  Single-AZ (HA) file systems deploy primary and standby file servers within the same Availability Zone to ensure continuous availability during failover and failback. Single-AZ (non-HA) file systems replicate your data and provide automatic self-healing within a single Availability Zone. Both Single-AZ (HA) and Single-AZ (non-HA) offer Single-AZ 1 and Single-AZ 2.
  For more information, see [Availability and durability](availability-durability.md "availability-durability.md").
- **Storage class** – The storage class of
  your file system. Choose either Intelligent-Tiering (elastic) or SSD (provisioned). We recommend Intelligent-Tiering for elastic storage that is suitable for most workloads. Intelligent-Tiering also comes with an optional SSD read cache for frequently accessed data.
  SSD (provisioned) is best for workloads that are latency sensitve and not cache-friendly. If you select SSD (provisioned), you will also need to specify an SSD storage capacity for your file system, from 64 to 524,288 GiB.
- **Provisioned SSD IOPS** – The maximum number of
  read and write operations for your file system. You can use the default
  setting of 3 IOPS per GB of SSD storage, or you can provision the SSD IOPS
  to a maximum of 160,000 SSD IOPS per file system for Single-AZ 1 and 400,000
  SSD IOPS per file system for Single-AZ 2 and Multi-AZ\*. You pay for additional
  SSD IOPS that you provision above the default 3 IOPS per GB of SSD
  storage.

###### Note

\*The maximum SSD IOPS you can provision for Multi-AZ file systems depends on the AWS Region your file system is located in. For more information, see
[Data access from disk](performance-ssd.md#data-access-disk "performance-ssd.md#data-access-disk").

- **Throughput capacity** – The sustained speed at
  which the file server that hosts your file system can serve data, in megabytes per
  second (MBps). You can use the default Amazon FSx-provisioned value or you can
  specify a different value. You pay for additional throughput capacity that
  you provision above the Amazon FSx default value.

You can increase the amount of throughput capacity as needed at any time
after you create the file system. For more information, see [Modifying throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

- **Network and security** – The VPC and subnets for
  the management and data access endpoints that your file system creates. For
  Multi-AZ file systems, you also define an IP address range and route tables.
  The maximum number of route tables that you can specify is 15.
- **Encryption** – Amazon FSx automatically encrypts the
  data in your file system at rest using the Amazon FSx service AWS Key Management Service key for
  your AWS account by default. You can choose to use a different
  KMS key.
