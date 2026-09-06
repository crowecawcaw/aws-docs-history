

# Create a replicator using the AWS console
<a name="msk-replicator-create-console"></a>

**Note**  
The following steps focus on creating a replicator between two MSK clusters. MSK Replicator also supports replication between self-managed Apache Kafka clusters and Amazon MSK Provisioned clusters. If you are migrating from a self-managed Kafka deployment, see [Migrate from non-MSK Apache Kafka clusters to Amazon MSK Provisioned](msk-replicator-migrate-external.md) and [Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters](msk-replicator-external-prereqs.md) for the prerequisites specific to self-managed clusters.

## Replicator details
<a name="msk-replicator-console-details"></a>

1. In the AWS Region where your target MSK cluster is located, open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose **Replicators** to display the list of replicators in the account.

1. Choose **Create replicator**.

1. In the **Replicator details** pane, give the new replicator a unique name.

## Choose your source cluster
<a name="msk-replicator-console-source"></a>

The source cluster contains the data you want to copy to a target MSK cluster.

1. In the **Source cluster** pane, choose the AWS Region where the source cluster is located.

   You can look up a cluster's Region by going to **MSK Clusters** and looking at the **Cluster** details ARN. The Region name is embedded in the ARN string. In the following example ARN, `ap-southeast-2` is the cluster Region.

   ```
   arn:aws:kafka:ap-southeast-2:123456789012:cluster/cluster-11/eec93c7f-4e8b-4baf-89fb-95de01ee639c-s1
   ```

1. Select **MSK cluster** as the cluster type, then enter the ARN of your source cluster or choose **Browse** to select it.

1. Choose subnet(s) for your source cluster. The subnets will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually. You must select a minimum of two subnets. For a same-region MSK Replicator, the subnets you select to access the source cluster and the subnets to access the target cluster must be in the same Availability Zone.

1. Choose security group(s) for the MSK Replicator to access your source cluster. The security groups will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually.
   + For cross-region replication (CRR), you do not need to provide security group(s) for your source cluster.
   + For same-region replication (SRR), go to the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/) and ensure that the security groups you will provide for the Replicator have outbound rules to allow traffic to your source cluster's security groups. Also, ensure that your source cluster's security groups have inbound rules that allow traffic from the Replicator security groups provided for the source.

**To add inbound rules to your source cluster's security group:**

     1. In the AWS console, go to your source cluster's details by selecting the **Cluster name**.

     1. Select the **Properties** tab, then scroll down to the **Network settings** pane to select the name of the **Security group** applied.

     1. Go to the inbound rules and select **Edit inbound rules**.

     1. Select **Add rule**.

     1. In the **Type** column for the new rule, select **Custom TCP**.

     1. In the **Port range** column, type `9098`. MSK Replicator uses IAM access control to connect to your cluster which uses port 9098.

     1. In the **Source** column, type the name of the security group that you will provide during Replicator creation for the source cluster (this may be the same as the MSK source cluster's security group), and then select **Save rules**.

**To add outbound rules to Replicator's security group provided for the source:**

     1. In the AWS console for Amazon EC2, go to the security group that you will provide during Replicator creation for the source.

     1. Go to the outbound rules and select **Edit outbound rules**.

     1. Select **Add rule**.

     1. In the **Type** column for the new rule, select **Custom TCP**.

     1. In the **Port range** column, type `9098`. MSK Replicator uses IAM access control to connect to your cluster which uses port 9098.

     1. In the **Source** column, type the name of the MSK source cluster's security group, and then select **Save rules**.

**Note**  
Alternately, if you do not want to restrict traffic using your security groups, you can add inbound and outbound rules allowing All Traffic with source `0.0.0.0/0`.

## Choose your target cluster
<a name="msk-replicator-console-target"></a>

The target cluster is the MSK Provisioned or Serverless cluster to which the source data is copied.

**Note**  
By default, MSK Replicator creates new topics in the target cluster with an auto-generated prefix added to the topic name (for example, `<sourceKafkaClusterAlias>.topic`). This distinguishes replicated topics from other topics in the target cluster and avoids circular replication. You can find the prefix under the **sourceKafkaClusterAlias** field using the `DescribeReplicator` API or the **Replicator details** page on the MSK console. Alternatively, you can use Identical topic name replication. See [Topic naming (Prefixed vs Identical)](msk-replicator-topic-naming.md).

1. In the **Target cluster** pane, choose the AWS Region where the target cluster is located.

1. Select **MSK cluster** as the cluster type, then enter the ARN of your target cluster or choose **Browse** to select it.

1. Choose subnet(s) for your target cluster. The subnets will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually. Select a minimum of two subnets.

1. Choose security group(s) for the MSK Replicator to access your target cluster. The security groups will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually. For more information about using security groups, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

   For both CRR and SRR, go to the Amazon EC2 console and ensure that the security groups you will provide to the Replicator have outbound rules to allow traffic to your target cluster's security groups. Also ensure that your target cluster's security groups have inbound rules that accept traffic from the Replicator security groups provided for the target.

**To add inbound rules to your target cluster's security group:**

   1. In the AWS console, go to your target cluster's details by selecting the **Cluster name**.

   1. Select the **Properties** tab, then scroll down to the Network settings pane to select the name of the **Security group** applied.

   1. Go to the inbound rules and select **Edit inbound rules**.

   1. Select **Add rule**.

   1. In the **Type** column for the new rule, select **Custom TCP**.

   1. In the **Port range** column, type `9098`. MSK Replicator uses IAM access control to connect to your cluster which uses port 9098.

   1. In the **Source** column, type the name of the security group that you will provide during Replicator creation for the target cluster, and then select **Save rules**.

**To add outbound rules to Replicator's security group provided for the target:**

   1. In the AWS console, go to the security group that you will provide during Replicator creation for the target.

   1. Select the **Properties** tab, then scroll down to the Network settings pane to select the name of the **Security group** applied.

   1. Go to the outbound rules and select **Edit outbound rules**.

   1. Select **Add rule**.

   1. In the **Type** column for the new rule, select **Custom TCP**.

   1. In the **Port range** column, type `9098`.

   1. In the **Source** column, type the name of the MSK target cluster's security group, and then select **Save rules**.

**Note**  
Alternately, if you do not want to restrict traffic using your security groups, you can add inbound and outbound rules allowing All Traffic with source `0.0.0.0/0`.

## Configure replicator settings and permissions
<a name="msk-replicator-console-settings"></a>

1. In the **Replicator settings** pane, specify the topics you want to replicate using regular expressions in the allow and deny lists. By default, all topics are replicated.
**Note**  
MSK Replicator only replicates up to 750 topics in sorted order. If you need to replicate more topics, create a separate Replicator. Go to the AWS console Support Center and [create a support case](https://console.aws.amazon.com/support/home#/) if you need support for more than 750 topics per Replicator.

1. By default, MSK Replicator starts replication from the *latest* (most recent) offset. Alternatively, you can start replication from the *earliest* (oldest) offset if you want to replicate existing data. Once the Replicator is created, you cannot change this setting. This setting corresponds to the [`startingPosition`](https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators-replicatorarn.html#v1-replicators-replicatorarn-model-replicationstartingposition) field in the [`CreateReplicator`](https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators.html#CreateReplicator) request and [`DescribeReplicator`](https://docs.aws.amazon.com/msk/1.0/apireference-replicator/v1-replicators-replicatorarn.html#DescribeReplicator) response APIs.

1. Choose a topic name configuration:
   + `PREFIXED` topic name replication (**Add prefix to topics name** in console): The default setting.
   + Identical topic name replication (**Keep the same topics name** in console): Topics are replicated with identical names in the target cluster.

   For more information, see [Topic naming (Prefixed vs Identical)](msk-replicator-topic-naming.md).

1. By default, MSK Replicator copies all metadata including topic configurations, ACLs, and consumer group offsets for seamless failover. If you are not creating the Replicator for failover, you can optionally turn off one or more of these settings in the **Additional settings** section.

1. In the **Consumer group replication** pane, specify the consumer groups you want to replicate using regular expressions in the allow and deny lists. By default, all consumer groups are replicated.

   You can also configure the **Consumer group offset sync mode**:
   + **Legacy** (default) — Offsets are synchronized when producers write to the source cluster (unidirectional).
   + **Enhanced** — Consumer offsets are synchronized regardless of producer location (bidirectional). Requires a corresponding Replicator that replicates data from the target cluster back to the source cluster. Use this mode when setting up bidirectional replication for migration or active-active architectures. For more information, see [Consumer group offset synchronization](msk-replicator-bidirectional-offset-sync.md).

1. In the **Compression** pane, you can optionally choose to compress the data written to the target cluster. If you use compression, we recommend using the same compression method as the data in your source cluster.

1. In the **Access permissions** pane, do either of the following:

   1. Select **Create or update IAM role with required policies**. The MSK console will automatically attach the necessary permissions and trust policy to the service execution role.  
![MSK console to create or update replicator IAM role](http://docs.aws.amazon.com/msk/latest/developerguide/images/msk-replicator-ezCRC.png)

   1. Provide your own IAM role by selecting **Choose from IAM roles that Amazon MSK can assume**. We recommend attaching the [`AWSMSKReplicatorExecutionRole`](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.html) managed IAM policy to your service execution role. See [Service execution role (SER)](msk-replicator-ser.md).

1. In the **Log delivery** pane, you can optionally configure log delivery to capture and route replication logs to your chosen destinations. By default, log delivery is not enabled. You can enable one or more of the following destinations:
   + **Deliver to Amazon CloudWatch Logs** — Analyze, query, and set alarms on the logs.
   + **Deliver to Amazon S3** — Store and retrieve raw logs in object storage.
   + **Deliver to Amazon Data Firehose** — Capture, transform, and deliver logs to Amazon OpenSearch Service or other Amazon Data Firehose destinations.

   For more information, see [MSK Replicator logs](msk-replicator-logs.md).

1. In the **Replicator tags** pane, you can optionally assign tags to the MSK Replicator resource. For a cross-region MSK Replicator, tags are synced to the remote Region automatically when the Replicator is created.

1. Select **Create**.

It takes approximately 30 minutes for the MSK Replicator to be successfully created and transition to RUNNING status. If your MSK Replicator transitions to a FAILED status, see [Troubleshoot Amazon MSK Replicator](msk-replicator-troubleshooting.md).