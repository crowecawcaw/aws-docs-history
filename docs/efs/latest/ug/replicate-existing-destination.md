

# Configuring replication to an existing EFS file system
<a name="replicate-existing-destination"></a>

Amazon EFS replicates the data and metadata on the source file system to the destination file system and AWS Region that you choose. During replication, Amazon EFS identifies data differences between the file systems and applies the differences to the destination file system. 



To replicate to an existing file system, perform the following steps. 

**Topics**
+ [Step 1: Disable the file system's replication overwrite protection](#replication-overwrite)
+ [Step 2: Create the replication configuration](#replicate-existing-step)

**Note**  
A file system can be part of only one replication configuration. You cannot use a destination file system as the source file system in another replication configuration.

## Step 1: Disable the file system's replication overwrite protection
<a name="replication-overwrite"></a>

When you create an Amazon EFS file system, its replication overwrite protection is enabled by default. Replication overwrite protection prevents the file system from being used as the destination in a replication configuration. Before you can use the file system as the destination in a replication configuration, you must disable the protection. If you delete the replication configuration, the file system's replication overwrite protection is re-enabled and the file system becomes writeable. 

The status of the replication overwrite protection for an Amazon EFS file system can have one of the values described in the following table.


| File system state  | Description | 
| --- | --- | 
| ENABLED | The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is ENABLED by default. | 
| DISABLED | The file system can be used as the destination file system in a replication configuration.  | 
| REPLICATING | The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by Amazon EFS during replication. | 

### Required permission
<a name="disable-protection-permission"></a>

Disabling replication overwrite protection requires permissions for the `elasticfilesystem:UpdateFileSystemProtection` action. For more information, see [AWS managed policy: AmazonElasticFileSystemFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonElasticFileSystemFullAccess). 

### Using the console
<a name="replication-overwrite-disable"></a>

1. Sign in to the AWS Management Console and open the Amazon EFS console at [ https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. In the left navigation pane, choose **File systems**.

1. In the **File systems** list, choose the Amazon EFS file system that you want to use as the destination file system in a replication configuration.

1. In the **File system protection** section, turn off **Replication Overwrite Protection**.

### To disable replication overwrite protection (AWS CLI)
<a name="replication-overwrite-disable-cli"></a>

In the following example, the `update-file-system-protection` CLI command disables the replication overwrite protection for the specified file system. The equivalent API command is [ UpdateFileSystemProtection](https://docs.aws.amazon.com/efs/latest/ug/limits.html#API_UpdateFileSystemProtection). 

```
aws efs update-file-system-protection
 --file-system-id {{fs-0a8b2be428114d97c}}
 --replication-overwrite-protection DISABLED
```

The AWS CLI responds as follows.

```
{
    "ReplicationOverwriteProtection": "DISABLED"
}
```

## Step 2: Create the replication configuration
<a name="replicate-existing-step"></a>

After you disable replication overwrite protection on the destination file system, you can create the replication configuration. When replicating to an existing file system, the destination file system can be in the same account or in a different account than the source file system.

Before creating a replication configuration for Amazon EFS, review the following important requirements and considerations:
+ If the source file system is encrypted, then the destination file system must also be encrypted. Additionally, if the source file is unencrypted and the destination file system is encrypted, then you cannot fail back to the source destination after performing failover. For more information about encryption, see [Data encryption in Amazon EFS](encryption.md).
+ When you initially configure replication to an existing file system, Amazon EFS writes data to or removes existing data from the destination file system to match data in the source file system. If you don't want to change data in the destination file system, then you should replicate to a new file system instead. For more information, see [Configuring replication to new EFS file system](create-replication.md).
+ Data replicated to the destination file system is accessible only after the initial sync completes. The sync duration depends on factors such as the size of the source file system and the number of files in it. For more information about replication performance, see [Replication performance](efs-replication.md#efs-replication-performance).

### Prerequisites
<a name="replication-existing-fs-reqs"></a>

Have a copy of the destination file system ID (for same-account replication) or the destination file system ARN (for cross-account replication) that you want to use. 

If the destination file system is in a different AWS account than the source file system, create an IAM role that allows Amazon EFS to perform replication and assign resource policies to the file systems. For more information, see [Replicating EFS file systems across AWS accounts](cross-account-replication.md).

### Using the console
<a name="create-replication-console"></a>

1. Sign in to the AWS Management Console and open the Amazon EFS console at [ https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Open the file system that you want to replicate:

   1. In the left navigation pane, choose **File systems**.

   1. In the **File systems** list, choose the Amazon EFS file system that you want to replicate. The file system that you choose cannot be a source or destination file system in an existing replication configuration.

1. Choose the **Replication** tab. 

1. In the **Replication** section, choose **Create replication**.

1. For **Replication configuration**, choose existing file system. 

1. Choose the destination file system.
   + To replicate to a file system that's in the same AWS account as the source file system:

     1. Select **Choose a file system in this account** and, for **Destination AWS Region**, select the AWS Region to which to replicate the file system.

     1. Choose **Browse EFS**, and then select the file system. The path to your destination file system appears in the **Destination** box.
   + To replicate to a file system that’s in a different AWS account than the source file system:

     1. Choose **Specify a file system in another account**.

     1. For **Destination file system ARN**, enter the Amazon Resource Name (ARN) of the destination file system. 
**Note**  
If replication overwrite protection is enabled on the file system, then a warning displays. Choose **Disable protection** to open the file system in a new tab and turn off its **Replication overwrite protection**. After disabling the protection, return to the **Create replication** tab and click the **Refresh** button to clear the message.

1. For **IAM role**, enter the ARN of the IAM role that allows Amazon EFS to replicate to the destination file system. This is optional for same-account replication, but required for cross-account replication. For more information, see [Replicating EFS file systems across AWS accounts](cross-account-replication.md).

1. Choose **Create replication**, type **confirm** in the confirmation message input box, and then choose **Create replication**. The **Replication** section shows the replication details.

### To create the replication configuration (AWS CLI)
<a name="create-replication-cli"></a>

This section provides examples for creating a replication configuration in the AWS CLI using the `create-replication-configuration` command. The equivalent API command is [CreateReplicationConfiguration](https://docs.aws.amazon.com/efs/latest/APIReference/API_CreateReplicationConfiguration.html). 

**Example : Create a replication configuration to an existing destination file system in another Region**  
The following example creates a replication configuration where the file system ID `{{fs-0123456789abcdef1}}` is replicated to file system ID {{{{fs-0a8b2be428114d97c}}}} in the `{{eu-west-2}}` AWS Region.   

```
aws efs create-replication-configuration \
--source-file-system-id {{fs-0123456789abcdef1}} \
--destinations "[{\"Region\":\"eu-west-2\",\"FileSystemId\":\"fs-0a8b2be428114d97c\"}]"
```
The AWS CLI responds as follows:  

```
{
    "SourceFileSystemId": "fs-0123456789abcdef1",
    "SourceFileSystemRegion": "us-east-1",
    "SourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/fs-0123456789abcdef1",
    "OriginalSourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:111122223333:file-system/fs-0123456789abcdef1",
    "CreationTime": "2024-10-20T20:40:13+00:00",
    "Destinations": [
        {
            "Status": "ENABLING",
            "FileSystemId": "fs-0a8b2be428114d97c",
            "Region": "eu-west-2",
            "OwnerId": "123456789012,
         }
    ],
    "SourceFileSystemOwnerId": "123456789012"
}
```

**Example : Create a cross-account replication configuration**  
The following example creates a replication configuration where the source and destination file systems are in different AWS accounts. The source file system ID {{`fs-0123456789abcdef1`}} in account {{555666777888}} is replicated to file system ID {{`fs-0a8b2be428114d97c`}} in account {{123456789012}}. The example specifies the Amazon Resource Name (ARN) of the destination file system and the ARN of the IAM role in the source account that allows Amazon EFS to perform replication on its behalf. Because no KMS key is specified, the destination file system is encrypted using the account's default AWS KMS service key (`aws/elasticfilesystem`).  

```
aws efs
--region $REGION 
--endpoint $ENDPOINT create-replication-configuration 
--source-file-system-id {{fs-0123456789abcdef1}} 
--destinations Region={{eu-west-2}},FileSystemId={{{{arn:aws:elasticfilesystem:eu-west-2:123456789012:file-system/fs-0a8b2be428114d97c}}}},RoleArn={{arn:aws:iam::555666777888:role/cross-account-replication}}
```
The AWS CLI responds as follows:  

```
{
    "SourceFileSystemId": "fs-0123456789abcdef1",
    "SourceFileSystemRegion": "us-east-1",
    "SourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:555666777888:file-system/fs-0123456789abcdef1",
    "OriginalSourceFileSystemArn": "arn:aws:elasticfilesystem:us-east-1:555666777888:file-system/fs-0123456789abcdef1",
    "CreationTime": "2024-10-20T20:40:13+00:00",
    "Destinations": [
        {
            "Status": "ENABLING",
            "FileSystemId": "fs-0a8b2be428114d97c",
            "Region": "eu-west-2",
            "OwnerId": "123456789012,
            "RoleArn": "arn:aws:iam::555666777888:role/cross-account-replication"
        }
    ],
    "SourceFileSystemOwnerId": "555666777888"
}
```