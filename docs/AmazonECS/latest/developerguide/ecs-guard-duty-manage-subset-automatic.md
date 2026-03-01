# Removing Runtime Monitoring from an Amazon ECS cluster

You might want to exclude certain clusters from protection, for example clusters
that you use for testing. This causes GuardDuty to perform the following operations on
resources in the cluster:

- No longer deploy the GuardDuty security agent to new standalone Fargate
  tasks, or new service deployments.

In order to preserve the immutability constraint, existing tasks and
deployments with Runtime Monitoring enabled are not affected.

- Stop billing and no longer accepts run time events for tasks.

## Procedure

Perform the following steps to remove Runtime Monitoring from a cluster.

1. Use the Amazon ECS console or AWS CLI to set the `GuardDutyManaged`
   tag key on the cluster to `false`. For more information, see
   [Updating a
   cluster](update-cluster-v2.md "update-cluster-v2.md") or [Working with tags using the CLI or API](ecs-using-tags.md#tag-resources-api-sdk "ecs-using-tags.md#tag-resources-api-sdk"). Use the following
   values for the tag.

###### Note

The Key and Value are case sensitive and must exactly match the
strings.

Key = `GuardDutyManaged`, Value = `false` 2. Delete the GuardDuty VPC endpoint for the cluster. For more information about
how to delete VPC endpoints, see [Delete an
interface endpoint](../../../vpc/latest/privatelink/delete-interface-endpoint.md "../../../vpc/latest/privatelink/delete-interface-endpoint.md") in the _AWS PrivateLink
User Guide_.
