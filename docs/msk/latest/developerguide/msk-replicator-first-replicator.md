

# Create your first replicator
<a name="msk-replicator-first-replicator"></a>

This walkthrough guides you through creating your first MSK Replicator between two MSK clusters using the AWS console. For detailed reference on all creation options, see [Create a replicator using the AWS console](msk-replicator-create-console.md).

Before you begin, make sure you have:
+ A source MSK cluster with IAM access control turned on (see [Prepare the source cluster](msk-replicator-prepare-clusters.md#msk-replicator-prepare-source)).
+ A target MSK cluster with IAM access control turned on (see [Prepare the target cluster](msk-replicator-prepare-clusters.md#msk-replicator-prepare-target)).
+ The required IAM permissions (see [IAM permissions required to create an MSK Replicator](msk-replicator-prerequisites.md#msk-replicator-prereq-iam)).

1. In the AWS Region where your target MSK cluster is located, open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. Choose **Replicators**, then choose **Create replicator**.

1. In the **Replicator details** pane, give the new replicator a unique name.

1. In the **Source cluster** pane, choose the AWS Region where the source cluster is located. Select **MSK cluster** as the cluster type, then enter the ARN of your source cluster or choose **Browse** to select it. The subnets and security groups will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually. You must select at least two subnets.

1. In the **Target cluster** pane, choose the AWS Region where the target cluster is located. Select **MSK cluster** as the cluster type, then enter the ARN of your target cluster or choose **Browse** to select it. The subnets and security groups will auto-populate based on your cluster selection. If they do not populate, or if you want to use different ones, you can select them manually. You must select at least two subnets.

1. In the **Replicator settings** pane, keep the defaults to replicate all topics. Choose a topic name configuration (**Add prefix to topics name** or **Keep the same topics name**). For more information on topic naming, see [Topic naming (Prefixed vs Identical)](msk-replicator-topic-naming.md).

1. In the **Access permissions** pane, select **Create or update IAM role with required policies** to let the MSK console automatically create the service execution role.

1. Choose **Create**.

It takes approximately 30 minutes for the MSK Replicator to be successfully created and transition to RUNNING status. You can monitor the status on the **Replicators** page in the MSK console.

If your MSK Replicator transitions to a FAILED status, see [Troubleshoot Amazon MSK Replicator](msk-replicator-troubleshooting.md).