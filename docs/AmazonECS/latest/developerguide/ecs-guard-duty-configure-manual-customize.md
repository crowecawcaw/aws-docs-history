# Adding Runtime Monitoring an Amazon ECS cluster

Configure Runtime Monitoring for the cluster, and then install the GuardDuty security agent
on your EC2 container instances.

## Prerequisites

1. Turn on Runtime Monitoring. For more information, see [Turning on Runtime Monitoring for Amazon ECS](ecs-guard-duty-configure-manual-guard-duty.md "ecs-guard-duty-configure-manual-guard-duty.md").
2. You control Runtime Monitoring for a cluster with a pre-defined tag. If your access policies restrict access based on tags, you must grant explicit permissions to your IAM users to tag clusters. For more information, see [IAM tutorial: Define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Procedure

Perform the following operations to add Runtime Monitoring to a cluster.

1. Create a VPC endpoint for GuardDuty for each cluster VPC. For more information,
   see [Creating Amazon VPC endpoint manually](../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md#creating-vpc-endpoint-ec2-agent-manually "../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md#creating-vpc-endpoint-ec2-agent-manually") in the _GuardDuty User Guide_.
2. Configure the EC2 container instances.
   1. Update the Amazon ECS agent to version `1.77` or later on the EC2 container instances in the cluster.
      For more information see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
   2. Install the GuardDuty security agent on the EC2 container instances in the
      cluster. For more information, see [Managing the security agent on an Amazon EC2 instance manually](../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md "../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md") in the
      _GuardDuty User Guide_.

   All new and existing tasks, and deployments are immediately
   protected because the GuardDuty security agent runs as a process on
   the EC2 container instance.

3. Use the Amazon ECS console or AWS CLI to set the
   `GuardDutyManaged` tag key on the cluster to
   `true`. For more information, see [Updating a cluster](update-cluster-v2.md "update-cluster-v2.md") or [Working with tags using the CLI or API](ecs-using-tags.md#tag-resources-api-sdk "ecs-using-tags.md#tag-resources-api-sdk"). Use the following
   values for the tag.

###### Note

The Key and Value are case sensitive and must exactly match the
strings.

Key = `GuardDutyManaged`, Value =
`true`
