

# Creating an Amazon FSx for OpenZFS file system
<a name="creating-file-systems"></a>

This section contains instructions on how to create a file system using the AWS CLI and the Amazon FSx API, as well as details on the file system properties that you can configure. For information on how to create a file system using the Amazon FSx console, see [Step 1: Create a file system](getting-started.md#getting-started-step1).

**Topics**
+ [Creating a file system (AWS CLI and Amazon FSx API)](#create-file-system-cli)
+ [Configurable file system properties](#fsx-openzfs-file-system-properties)
+ [Creating a FSx for OpenZFS file system using shared subnets](#creating-fs-shared-subnets)

## Creating a file system (AWS CLI and Amazon FSx API)
<a name="create-file-system-cli"></a>

**To create an FSx for OpenZFS file system (CLI and API)**

Use the [create-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/create-file-system.html) CLI command (or the equivalent [CreateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystem.html) API operation). The following example creates an FSx for OpenZFS file system with a `SINGLE_AZ_1` deployment type.

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

After successfully creating the file system, Amazon FSx returns the file system's description in JSON format.

## Configurable file system properties
<a name="fsx-openzfs-file-system-properties"></a>

When you create a file system, you specify the following file system properties:
+ **Deployment type** – The deployment type of your file system—Multi-AZ (HA), Single-AZ (HA), or Single-AZ (non-HA). Multi-AZ (HA) file systems provide additional resiliency by replicating your data and provide high availability by automatically failing over between multiple Availability Zones within the same AWS Region. Single-AZ (HA) file systems deploy primary and standby file servers within the same Availability Zone to ensure continuous availability during failover and failback. Single-AZ (non-HA) file systems replicate your data and provide automatic self-healing within a single Availability Zone. Both Single-AZ (HA) and Single-AZ (non-HA) offer Single-AZ 1 and Single-AZ 2. For more information, see [Availability and durability](availability-durability.md).
+ **Storage class** – The storage class of your file system. Choose either Intelligent-Tiering (elastic) or SSD (provisioned). We recommend Intelligent-Tiering for elastic storage that is suitable for most workloads. Intelligent-Tiering also comes with an optional SSD read cache for frequently accessed data. SSD (provisioned) is best for workloads that are latency sensitve and not cache-friendly. If you select SSD (provisioned), you will also need to specify an SSD storage capacity for your file system, from 64 to 524,288 GiB.
+ **Provisioned SSD IOPS** – The maximum number of read and write operations for your file system. You can use the default setting of 3 IOPS per GB of SSD storage, or you can provision the SSD IOPS to a maximum of 160,000 SSD IOPS per file system for Single-AZ 1 and 400,000 SSD IOPS per file system for Single-AZ 2 and Multi-AZ\*. You pay for additional SSD IOPS that you provision above the default 3 IOPS per GB of SSD storage.
**Note**  
\*The maximum SSD IOPS you can provision for Multi-AZ file systems depends on the AWS Region your file system is located in. For more information, see [Data access from disk](performance-ssd.md#data-access-disk).
+ **Throughput capacity** – The sustained speed at which the file server that hosts your file system can serve data, in megabytes per second (MBps). You can use the default Amazon FSx-provisioned value or you can specify a different value. You pay for additional throughput capacity that you provision above the Amazon FSx default value.

  You can increase the amount of throughput capacity as needed at any time after you create the file system. For more information, see [Modifying throughput capacity](managing-throughput-capacity.md).
+ **Network and security** – The VPC and subnets for the management and data access endpoints that your file system creates. For Multi-AZ file systems, you also define an IP address range and route tables. The maximum number of route tables that you can specify is 15.
+ **Encryption** – Amazon FSx automatically encrypts the data in your file system at rest using the Amazon FSx service AWS Key Management Service key for your AWS account by default. You can choose to use a different KMS key.

## Creating a FSx for OpenZFS file system using shared subnets
<a name="creating-fs-shared-subnets"></a>

VPC sharing enables multiple AWS accounts to create resources into shared, centrally-managed virtual private clouds (VPCs). In this model, the account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong to the same AWS Organization.

Participant accounts can create FSx for OpenZFS Single-AZ and Multi-AZ file systems in a VPC subnet that the owner account has shared with them.

### Prerequisites for VPC owners
<a name="shared-vpc-prereqs"></a>

Before participant accounts can create FSx for OpenZFS file systems in shared subnets, the VPC owner must complete the following:
+ **Share VPC subnets using AWS Resource Access Manager:** Use AWS RAM to share subnets with participant accounts. For more information, see [ Sharing your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS Resource Access Manager User Guide*.
+ **Grant Amazon FSx permission to modify route tables in the shared subnets on behalf of participant accounts (For Multi-AZ file systems only):** Multi-AZ file systems need to update routes during failover events so that clients can seamlessly connect to the host. For instructions, see [Shared VPC settings for Multi-AZ file systems](#maz-shared-vpc-openzfs).

### Shared subnet considerations
<a name="shared-subnet-considerations"></a>

When creating FSx for OpenZFS file systems in shared subnets, note the following:
+ Participant accounts can view, create, modify, and delete file systems and their associated resources in subnets that the owner account has shared with them.
+ The shared VPC owner cannot view, modify, or delete resources that a participant creates in the shared subnet. This is in addition to the VPC resources that each account has different access to. For more information, see [Responsibilities and permissions for owners and participants](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html#vpc-share-limitations) in the *Amazon VPC User Guide*.
+ Participant accounts can't launch resources using the default security group for the VPC because it belongs to the owner. Additionally, participant accounts can't launch resources using security groups that are owned by other participant accounts.
+ In a shared subnet, the participant and the owner separately controls the security groups within each respective account. The owner account can see security groups that are created by participants accounts, but cannot perform any actions on them. If the owner account wants to remove or modify these security groups, the participant that created the security group must take the action.
+ VPC subnets that overlap with a file system's in-VPC CIDR range can interrupt network traffic to the file system. Ensure that subnets in the shared VPC do not conflict with the CIDR ranges used by existing file systems.
+ If a subnet is unshared while participant-created file systems exist, Single-AZ file systems continue to operate but participants can no longer manage them. Multi-AZ file systems enter a `MISCONFIGURED` state and cannot fail over, fail back, or be patched. The same applies if the VPC owner disables route table permissions for Multi-AZ file systems. To restore normal operation, reshare the subnet or re-enable route table permissions.

For more information, see [Share your VPC with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) in the *Amazon VPC User Guide*.

### Shared VPC settings for Multi-AZ file systems
<a name="maz-shared-vpc-openzfs"></a>

Owner accounts can manage whether or not participant accounts can create Multi-AZ FSx for OpenZFS file systems in VPC subnets that the owner has shared with participants using the AWS Management Console, AWS CLI, and API, as described in the following sections.

**Note**  
This setting must be enabled by the AWS account that owns the VPC. If you need to create a Multi-AZ FSx file system in a VPC that was shared with you, contact the VPC owner and ask them to enable this feature under their FSx settings.

#### To manage VPC sharing for Multi-AZ file systems (console)
<a name="maz-shared-vpc-console"></a>

**To manage VPC sharing for Multi-AZ file systems (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the navigation pane, choose **Settings**.

1. Locate the **Multi-AZ shared VPC settings** on the **Settings** page.
   + To enable VPC sharing for Multi-AZ file systems in VPC subnets that you share, choose **Enable**.
   + To disable VPC sharing for Multi-AZ file systems in all VPCs that you own, choose **Disable**.

1. If disabling the feature, you will be prompted to **Confirm**.
**Important**  
We recommend that participant-created Multi-AZ file systems in the shared VPC are deleted before you disable this feature. Once the feature is disabled, these file systems will enter a `MISCONFIGURED` state and will be at risk of becoming unavailable.

#### To manage VPC sharing for Multi-AZ file systems (AWS CLI)
<a name="maz-shared-vpc-cli"></a>

**To manage VPC sharing for Multi-AZ file systems (AWS CLI)**

1. To view the current setting for Multi-AZ VPC sharing, use the [describe-shared-vpc-configuration](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-shared-vpc-configuration.html) CLI command, or the equivalent [DescribeSharedVpcConfiguration](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSharedVpcConfiguration.html) API command, shown as follows:

   ```
   $ aws fsx describe-shared-vpc-configuration
   ```

   The service responds to a successful request as follows:

   ```
   {
       "EnableFsxRouteTableUpdatesFromParticipantAccounts": "false"
   }
   ```

1. To manage the Multi-AZ shared VPC configuration, use the [update-shared-vpc-configuration](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-shared-vpc-configuration.html) CLI command, or the equivalent [UpdateSharedVpcConfiguration](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSharedVpcConfiguration.html) API command. The following example enables VPC sharing for Multi-AZ file systems.

   ```
   $ aws fsx update-shared-vpc-configuration --enable-fsx-route-table-updates-from-participant-accounts true
   ```

   The service responds to a successful request as follows:

   ```
   {
       "EnableFsxRouteTableUpdatesFromParticipantAccounts": "true"
   }
   ```

1. To disable the feature, set `EnableFsxRouteTableUpdatesFromParticipantAccounts` to `false`, as shown in the following example.

   ```
   $ aws fsx update-shared-vpc-configuration --enable-fsx-route-table-updates-from-participant-accounts false
   ```

   The service responds to a successful request as follows:

   ```
   {
       "EnableFsxRouteTableUpdatesFromParticipantAccounts": "false"
   }
   ```