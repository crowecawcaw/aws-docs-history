

# Removing Runtime Monitoring from an Amazon ECS cluster
<a name="ecs-guard-duty-remove-manual"></a>

You can remove Runtime Monitoring from a cluster. This causes GuardDuty to stop monitoring all resources in the cluster.

**To remove Runtime Monitoring from a cluster**

1. Use the Amazon ECS console or AWS CLI to set the `GuardDutyManaged` tag key on the cluster to `false`. For more information, see [Updating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-cluster-v2.html) or [Working with tags using the CLI or API](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html#tag-resources-api-sdk).
**Note**  
The Key and Value are case sensitive and must exactly match the strings.

   Key = `GuardDutyManaged`, Value = `false`

1. Uninstall the GuardDuty security agent on you EC2 container instances in the cluster.

   For more information, see [Uninstalling the security agent manually](https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html#gdu-update-security-agent-ec2) in the *GuardDuty User Guide*.

1. Delete the GuardDuty VPC endpoint for each cluster VPC. For more information about how to delete VPC endpoints, see [Delete an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-interface-endpoint.html) in the *AWS PrivateLink User Guide*.