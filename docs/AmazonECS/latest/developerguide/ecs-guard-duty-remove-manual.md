# Removing Runtime Monitoring from an Amazon ECS

cluster

You can remove Runtime Monitoring from a cluster. This causes GuardDuty to stop monitoring
all resources in the cluster.

###### To remove Runtime Monitoring from a cluster

1. Use the Amazon ECS console or AWS CLI to set the `GuardDutyManaged`
   tag key on the cluster to `false`. For more information, see
   [Updating a cluster](update-cluster-v2.md "update-cluster-v2.md") or [Working with tags using the CLI or API](ecs-using-tags.md#tag-resources-api-sdk "ecs-using-tags.md#tag-resources-api-sdk").

###### Note

The Key and Value are case sensitive and must exactly match the
strings.

Key = `GuardDutyManaged`, Value = `false` 2. Uninstall the GuardDuty security agent on you EC2 container instances in the
cluster.

For more information, see [Uninstalling the security agent manually](../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md#gdu-update-security-agent-ec2 "../../../guardduty/latest/ug/managing-gdu-agent-ec2-manually.md#gdu-update-security-agent-ec2") in the _GuardDuty User Guide_. 3. Delete the GuardDuty VPC endpoint for each cluster VPC. For more
information about how to delete VPC endpoints, see [Delete
an interface endpoint](../../../vpc/latest/privatelink/delete-interface-endpoint.md "../../../vpc/latest/privatelink/delete-interface-endpoint.md") in the _AWS PrivateLink User Guide_.
