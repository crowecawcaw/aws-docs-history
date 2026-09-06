

# Adding Runtime Monitoring an Amazon ECS cluster
<a name="ecs-guard-duty-configure-manual-customize"></a>

Configure Runtime Monitoring for the cluster, and then install the GuardDuty security agent on your EC2 container instances.

## Prerequisites
<a name="ecs-guard-duty-configure-manual-customize-prereq"></a>

1. Turn on Runtime Monitoring. For more information, see [Turning on Runtime Monitoring for Amazon ECS](ecs-guard-duty-configure-manual-guard-duty.md).

1. You control Runtime Monitoring for a cluster with a pre-defined tag. If your access policies restrict access based on tags, you must grant explicit permissions to your IAM users to tag clusters. For more information, see [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Procedure
<a name="ecs-guard-duty-configure-manual-customize-procedure"></a>

Perform the following operations to add Runtime Monitoring to a cluster.

1. Create a VPC endpoint for GuardDuty for each cluster VPC. For more information, see [Creating Amazon VPC endpoint manually ](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html#creating-vpc-endpoint-ec2-agent-manually) in the *GuardDuty User Guide*.

1. Configure the EC2 container instances.

   1. Update the Amazon ECS agent to version `1.77` or later on the EC2 container instances in the cluster. For more information see [Updating the Amazon ECS container agent](ecs-agent-update.md).

   1. Install the GuardDuty security agent on the EC2 container instances in the cluster. For more information, see [Managing the security agent on an Amazon EC2 instance manually](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html) in the *GuardDuty User Guide*.

      All new and existing tasks, and deployments are immediately protected because the GuardDuty security agent runs as a process on the EC2 container instance.

1. Use the Amazon ECS console or AWS CLI to set the `GuardDutyManaged` tag key on the cluster to `true`. For more information, see [Updating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-cluster-v2.html) or [Working with tags using the CLI or API](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html#tag-resources-api-sdk). Use the following values for the tag.
**Note**  
The Key and Value are case sensitive and must exactly match the strings.

   Key = `GuardDutyManaged`, Value = `true`