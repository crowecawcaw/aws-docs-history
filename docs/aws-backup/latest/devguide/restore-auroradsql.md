

# Amazon Aurora DSQL restore
<a name="restore-auroradsql"></a>

**Topics**
+ [Overview](#restore-auroradsql-overview)
+ [Restore Aurora DSQL single Region cluster](#restore-auroradsql-singleregion)
+ [Restore an Aurora DSQL multi-Region cluster](#restore-auroradsql-multiregion)
+ [Troubleshoot Aurora DSQL restore issues](#restore-auroradsql-troubleshoot)
+ [Aurora DSQL restore frequently asked questions](#restore-auroradsql-faq)

## Overview
<a name="restore-auroradsql-overview"></a>

To restore a Amazon Aurora DSQL single-Region cluster, use the AWS Backup console or CLI to select the recovery point (backup) you wish to restore. To restore a Aurora DSQL multi-Region cluster, you can now use either the AWS Backup console or CLI.

For single-Region restore, include the name, cluster encryption, and deletion protection, then initiate the restore to a newly created cluster.

For multi-Region restore, you'll need to specify additional parameters including a witness Region, peer Region(s), and regional configuration settings. Multi-Region restore creates a cluster that spans multiple AWS Regions, providing enhanced availability and disaster recovery capabilities.

## Restore Aurora DSQL single Region cluster
<a name="restore-auroradsql-singleregion"></a>

You can restore an Aurora DSQL cluster to a single Region by using the AWS Backup console or AWS CLI.

------
#### [ Console ]

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Select the "Restore" button next to the recovery point you wish to restore.

1. Configure the settings for the new cluster to which your recovery point will be restored.

   1. By default, the AMK (AWS managed key) will be used to encrypt the restored data. You may alternatively specify a different key.

   1. [Deletion protection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.html#USER_DeletionProtection) for your Aurora clusters is enabled by default, but unselect the box to turn off the option.

1. Review the settings; when they are satisfactory, select the **Restore backup** button.

AWS Backup will create a new Aurora DSQL cluster.

------
#### [ AWS CLI ]

**Single Region restore**

1. Use the CLI command `aws backup start-restore-job` to restore an Aurora cluster from the specified recovery point.

1. Include the necessary metadata for the restore job. Example:  
**Example**  

   ```
   aws backup start-restore-job \
       --recovery-point-arn "arn:aws:dsql:us-east-1:123456789012:cluster/example-cluster/backup/example-backup" \
       --iam-role-arn "arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole" \
       --metadata '{"regionalConfig":"[{\"region\":\"us-east-1\",\"isDeletionProtectionEnabled\":true,\"kmsKeyId\":\"my_key\"}]"}' \
       --copy-source-tags-to-restored-resource
   ```

------

## Restore an Aurora DSQL multi-Region cluster
<a name="restore-auroradsql-multiregion"></a>

Aurora DSQL multi-Region cluster restore occurs within a continent group, which is a set of AWS Regions peers. Multi-Region restore requires that the Regions you specify in the operation are contained in one continent group. For more information about multi-Region clusters, see [Configuring multi-Region clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuring-multi-region-clusters.html).

The following continent groups are supported:
+ **Americas**: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada West (Calgary), Canada (Central)
+ **Europe**: Europe (Frankfurt), Europe (Stockholm), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris)
+ **Asia-Pacific**: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Singapore)

To complete multi-Region restore, ensure you have the following permissions:
+ `backup:StartRestoreJob`
+ `dsql:UpdateCluster`
+ `dsql:AddPeerCluster`
+ `dsql:RemovePeerCluster`

You can restore a backup of an Aurora DSQL cluster to multiple Regions using either the AWS Backup console or CLI commands.

**Tip**  
If you have a backup plan with a rule that automatically creates a cross-Region copy to one of the indicated Regions, the created copy can be used for this multi-Region restore.

Multi-Region restore starts with your current Region. You will also need a:
+ Peer Region with an identical cross-Region copy of the recovery point in your current Region
+ Witness Region, a designated AWS Region that participates in multi-Region cluster configurations by supporting transaction log-only writes without consuming storage for the actual data. For more information about witness Regions, see [Creating a multi-Region cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#getting-started-multi-region).

The individual steps are shown below:

------
#### [ Console ]

The AWS Backup console now supports multi-Region restore for Aurora DSQL clusters, providing a streamlined process for creating clusters that span multiple Regions. For more information about multi-Region clusters, see [Configuring multi-Region clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuring-multi-region-clusters.html).

1. Sign in to the AWS Management Console and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the navigation pane, choose **Backup vaults**.

1. Choose the backup vault that contains the Aurora DSQL recovery point you want to restore.

1. Select the recovery point you want to restore, then choose **Restore**.

1. On the restore page, under **Restore options**, select **Add peer Regions** to enable multi-Region restore.

1. Select a **Peer cluster Region** from the dropdown menu. This Region must be within the same continent group as your current Region and also must contain a cross-Region copy from the recovery point in the current (first) Region.

1. Select a **Witness Region** from the dropdown menu. This Region must also be within the same continent group.

1. Configure the **Cluster settings** for both the primary and peer Region clusters:

   1. For the primary cluster, configure:
      + **Cluster encryption** (optional): Select a KMS key for encryption.
      + **Deletion protection**: Enable or disable deletion protection.

   1. For the peer Region cluster, configure:
      + **Peer Region cluster encryption** (optional): Select a KMS key for encryption.
      + **Peer Region cluster deletion protection**: Enable or disable deletion protection.

1. Review your settings and choose **Restore backup**.

1. The console will initiate the multi-Region restore process, which creates clusters in both Regions and automatically links them together.

------
#### [ AWS CLI ]

Multi-Region restore can now be achieved using the new orchestrated restore metadata with AWS Backup CLI commands. This approach simplifies the process by handling the cluster linking automatically. For more information about creating multi-Region clusters programmatically, see [Configuring multi-Region clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/configuring-multi-region-clusters.html) in the Aurora DSQL User Guide.

**Important**  
Both the primary cluster and peer cluster must be in Regions within the same continent group. The operation will fail if the clusters are in Regions outside the continent group. Supported continent groups include:  
**Americas**: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada West (Calgary), Canada (Central)
**Europe**: Europe (Frankfurt), Europe (Stockholm), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris)
**Asia-Pacific**: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Singapore)

**Multi-Region restore through AWS CLI using orchestrated restore metadata**

1. Create a restore job using the CLI command `aws backup start-restore-job` with the new multi-Region orchestration metadata:  
**Example**  

   ```
   aws backup start-restore-job \
   --recovery-point-arn "arn:aws:backup:us-east-1:123456789012:recovery-point:abcd1234" \
   --iam-role-arn "arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole" \
   --metadata '{
       "witnessRegion":"us-west-2",
       "useMultiRegionOrchestration":"true",
       "peerRegion":"[\"us-east-2\"]",
       "regionalConfig":"[{\"region\":\"us-east-1\",\"isDeletionProtectionEnabled\":true,\"kmsKeyId\":\"arn:aws:kms:us-east-1:123456789012:key/ba4b3773-4bb8-4a7a-994c-46ede70202f5\"},{\"region\":\"us-west-2\",\"isDeletionProtectionEnabled\":true,\"kmsKeyId\":\"arn:aws:kms:us-west-2:123456789012:key/ba4b3773-4bb8-4a7a-994c-46ede70202f5\"}]"
   }' \
   --copy-source-tags-to-restored-resource
   ```

   The metadata structure includes:
   + `witnessRegion`: The Region that will serve as the witness for the multi-Region cluster. For more information, see [Resilience in Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/disaster-recovery-resiliency.html).
   + `useMultiRegionOrchestration`: Set to `true` to enable multi-Region orchestration.
   + `peerRegion`: An array containing the Region(s) with peer clusters in the multi-Region cluster. For more information, see [MultiRegionProperties](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_MultiRegionProperties.html) in the Aurora DSQL API Reference.
   + `regionalConfig`: An array containing configuration for each Region:
     + `region`: The AWS Region identifier.
     + `isDeletionProtectionEnabled`: Boolean flag to enable/disable deletion protection. For more information, see [CreateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html#API_CreateCluster_RequestSyntax) in the Aurora DSQL API Reference.
     + `kmsKeyId`: The KMS key ARN for encryption (optional).

     If `regionalConfig` properties are not specified, then default values will be applied: default encryption and `isDeletionProtectionEnabled` = `TRUE`.

1. Monitor the restore job status using the `aws backup describe-restore-job` command:

   ```
   aws backup describe-restore-job --restore-job-id job-12345678
   ```

1. Once the restore job completes, you can verify the multi-Region cluster configuration using the Aurora DSQL CLI:

   ```
   aws dsql describe-cluster --cluster-identifier your-cluster-id
   ```

   For more information about multi-Region cluster operations, see [UpdateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html) in the Aurora DSQL API Reference.

------

## Troubleshoot Aurora DSQL restore issues
<a name="restore-auroradsql-troubleshoot"></a>

**Error:** Insufficient permissions

**Possible cause:** If you try to copy an Aurora DSQL recovery point into an account (cross-account copy) that has never interacted with DSQL API, you may get a permission issue error since the DSQL service-linked role isn't set up in the destination account.

**Remedy:** Attach the [DSQL managed policy](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html) that includes the DSQL service-linked role, [AuroraDsqlServiceLinkedRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/             AuroraDsqlServiceLinkedRolePolicy.html), to a role in the destination account.

If you encounter any other issues with the backup or restore process, you can check the status of your backup and restore jobs in the AWS Backup console or using the AWS CLI. Additionally, you can review the AWS CloudTrail logs for any relevant error messages or events related to your AWS Backup operations.

## Aurora DSQL restore frequently asked questions
<a name="restore-auroradsql-faq"></a>

1. *"Can I use AWS Backup for Aurora DSQL from the Aurora DSQL console?"*

   No, you can only perform backups and restores, as well as managing backups, from AWS Backup console, SDK, or CLI.

   

1. *"What backup granularity is available for Aurora DSQL? Can I backup specific tables or databases in my cluster"*

   You can only back up and restore a whole Aurora DSQL cluster. 

   

1. *"Are backups of Aurora DSQL full backups or incremental backups?"*

   Recovery points of Aurora DSQL clusters (backups) are full backups of your clusters.

   

1. *"Can I create backups for my Aurora DSQL multi-Region clusters?"*

   Yes, you can create backups for each cluster in multi-Region clusters in the using the same steps as when you create a backup of a single cluster in a single Region.

    AWS Backup recommends as a best practice to create a cross-Region copy of your backup in the other Region from which you plan to restore the Multi-Region cluster, as multi-Region restore requires an identical copy of the same recovery point [*identical* in this operation means the recovery points have the same resource name and creation time].

   

1. *"Will my restored cluster overwrite my existing cluster?"*

   No. When you restore your Aurora DSQL data, AWS Backup creates a new cluster from your snapshots; the restored cluster won’t overwrite the source cluster.

   