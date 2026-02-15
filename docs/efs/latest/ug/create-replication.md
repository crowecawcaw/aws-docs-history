# Configuring replication to new EFS file

system

Amazon EFS automatically creates a new file system and copies the data and metadata on the source
file system to a new read-only destination file system in the AWS Region that you choose. When
you replicate to a new file system, you choose the file system type and the AWS Key Management Service (AWS KMS) key
to use for encryption. Additionally, Amazon EFS does not create any mount targets when it creates the
destination file system. After you create the replication configuration, you must [create one or more mount targets](accessing-fs.md "accessing-fs.md") to [mount a destination file system](efs-mount-helper.md "efs-mount-helper.md").

###### Note

A file system can be part of only one replication configuration. You cannot use a
destination file system as the source file system in another replication configuration.

- **File system type** – The file system type
  determines the availability and durability with which the Amazon EFS file system stores data within
  an AWS Region.

      + Choose **Regional** to create a file system that stores
       data and metadata redundantly across all Availability Zones within the AWS Region.
      + Choose **One Zone** to create a file system that stores
       data and metadata redundantly within a single Availability Zone.

  For more information about file system types, see [EFS file system types](features.md#file-system-type "features.md#file-system-type").

- **Encryption** – All destination file systems are
  created with encryption at rest enabled. You can specify the AWS KMS key that is used to encrypt
  the destination file system. If you don't specify a KMS key, your service-managed KMS key
  for Amazon EFS is used.

###### Important

After the destination file system is created, you cannot change the KMS key.
The destination file system is created with default settings based on your source file
system. Additional settings can be changed after creation.

- **Automatic backups** – For destination file systems
  using One Zone storage, automatic backups are enabled by default. After the file
  system is created, you can change the automatic backup setting. For more information, see [Managing automatic backups of EFS file
  systems](automatic-backups.md "automatic-backups.md").
- **Performance mode** – The destination file
  system's **Performance mode** matches that of the source file system,
  unless the destination file system uses One Zone storage. In that case, the
  **General Purpose** mode is used. The performance mode cannot be
  changed.
- **Throughput mode** – The destination file
  system's **Throughput mode** matches that of the source file system. After
  the file system is created, you can change the mode.

If the source file system's throughput mode is
**Provisioned**, then the destination file system's provisioned
throughput amount matches that of the source file system, unless the source file's provisioned
amount exceeds the limit for the destination file system's Region. If the
source file system's provisioned amount exceeds the Region limit for the
destination file system, then the destination file system's provisioned throughput amount is
the Region limit. For more information, see [Amazon EFS quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits").

- **Lifecycle management** –
  Lifecycle management is not enabled on the destination file system. After the destination
  file system is created, you can enable it. For more information, see [Managing storage lifecycle](lifecycle-management-efs.md "lifecycle-management-efs.md").

## Step 1: Create the replication configuration

The first step in replicating to a new file system is to create the replication
configuration.Data replicated to the destination file system is accessible only after the initial sync
completes. The initial sync duration depends on factors such as the size of the source file
system and the number of files in it. For more information about replication performance, see
[Replication performance](efs-replication.md#efs-replication-performance "efs-replication.md#efs-replication-performance").

1. Sign in to the AWS Management Console and open the Amazon EFS console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Open the file system that you want to replicate:
   1. In the left navigation pane, choose **File systems**.
   2. In the **File systems** list, choose the file system that you want
      to replicate. The file system that you choose cannot be a source or destination file
      system in an existing replication configuration.

3. Choose the **Replication** tab.
4. In the **Replication** section, choose **Create
   replication**.
5. In the **Replication settings** section, define the replication
   settings:
   1. For **Replication configuration**, choose whether to replicate to a
      new or existing file system.
   2. For **Destination AWS Region**, choose the AWS Region in which
      to replicate the file system.

6. In the **Destination file system settings** section, define the
   destination file system settings.
   1. For **File system type**, choose a storage option for the file
      system:
      - To create a file system that stores data redundantly across multiple geographically
        separated Availability Zones within an AWS Region, choose **Regional**.
      - To create a file system that stores data redundantly within a single Availability Zone in
        an AWS Region, choose **One Zone**, and then select the
        Availability Zone.

      For more information, see [EFS file system types](features.md#file-system-type "features.md#file-system-type").

      ###### Note

      One Zone file systems are not available in all Availability Zones in the
      AWS Regions where Amazon EFS is available.

   2. For **Encryption**, encryption of data at rest is automatically
      enabled on the destination file system. By default, Amazon EFS uses your AWS Key Management Service (AWS KMS)
      service key (`aws/elasticfilesystem`). To use a different KMS key,
      choose the KMS key or enter the key's Amazon Resource Name (ARN).

   ###### Important

   After the file system is created, you cannot change the KMS key.

This section provides examples for creating a replication configuration in the AWS CLI
using the `create-replication-configuration` command. The equivalent API command is
[CreateReplicationConfiguration](API_CreateReplicationConfiguration.md "API_CreateReplicationConfiguration.md").

###### Example: Create a replication configuration for a Regional destination file

system

The following example creates a replication configuration for the file system
`fs-0123456789abcdef1`. The example uses the
`Region` parameter to create a destination file system in the
`eu-west-2` AWS Region. The `KmsKeyId`
parameter specifies the KMS key ID to use when encrypting the destination file
system:

```
`aws efs create-replication-configuration \
--source-file-system-id `fs-0123456789abcdef1` \
--destinations "[{\"Region\":\"`eu-west-2`\", \"KmsKeyId\":\"`arn:aws:kms:us-east-2:111122223333:key\/abcd1234-ef56-ab78-cd90-1111abcd2222`\"}]"`
```

The AWS CLI responds as follows:

```

         `{
 "SourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/fs-0123456789abcdef1",
 "SourceFileSystemRegion": "us-east-1",
 "Destinations": [
 {
 "Status": "ENABLING",
 "FileSystemId": "fs-0123456789abcde22",
 "Region": "eu-west-2"
 }
 ],
 "SourceFileSystemId": "fs-0123456789abcdef1",
 "CreationTime": 1641491892.0,
 "OriginalSourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/fs-0123456789abcdef1"
}`

```

###### Example: Create a replication configuration for a One Zone destination file

system

The following example creates a replication configuration for the file system
`fs-0123456789abcdef1`. The example uses the
`AvailabilityZoneName` parameter to create a One Zone destination
file system in the `us-west-2a` Availability Zone. Because no
KMS key is specified, the destination file system is encrypted using the account's default
AWS KMS service key (`aws/elasticfilesystem`).

```
aws efs create-replication-configuration \
--source-file-system-id `fs-0123456789abcdef1` \
--destinations AvailabilityZoneName=`us-west-2a`
```

## Step 2: Mount the destination file

system

Amazon EFS does not create any mount targets when it creates the destination file system. To
mount the destination file system, you must create one or more mount targets. For more
information, see [Mounting EFS file systems](mounting-fs.md "mounting-fs.md").
