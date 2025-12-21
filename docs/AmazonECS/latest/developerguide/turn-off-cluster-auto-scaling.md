# Turning off Amazon ECS cluster auto scaling

You turn off cluster auto scaling when you need more granular control of the EC2 instances that are
registered to your cluster,

To turn off cluster auto scaling for a cluster, you can either disassociate the capacity provider
with managed scaling turned on from the cluster or update the capacity provider to turn
off managed scaling.

## Disassociate the capacity

provider

Use the following steps to disassociate a capacity provider with a cluster.

1. Use the `put-cluster-capacity-providers` command to
   disassociate the Auto Scaling group capacity provider with the cluster. The cluster can
   keep the association with the AWS Fargate capacity providers. For more
   information, see `put-cluster-capacity-providers` in the _AWS CLI Command Reference_.

```
`aws ecs put-cluster-capacity-providers \
 --cluster `ClusterName` \
 --capacity-providers FARGATE FARGATE_SPOT \
 --default-capacity-provider-strategy '[]'`
```

Use the `put-cluster-capacity-providers` command to
disassociate the Auto Scaling group capacity provider with the cluster. For more
information, see `put-cluster-capacity-providers` in the _AWS CLI Command Reference_.

```
`aws ecs put-cluster-capacity-providers \
 --cluster `ClusterName` \
 --capacity-providers [] \
 --default-capacity-provider-strategy '[]'`
```

2. Use the `describe-clusters` command to verify that the
   disassociation was successful. For more information, see `describe-clusters` in the _AWS CLI Command Reference_.

```
`aws ecs describe-clusters \
 --cluster `ClusterName` \
 --include ATTACHMENTS`
```

## Turn off managed scaling for the capacity

provider

Use the following steps to turn off managed scaling for the capacity
provider.

- Use the `update-capacity-provider` command to turn off managed
  auto scaling for the capacity provider. For more information, see
  `update-capacity-provider` in the _AWS CLI Command Reference_.

```
`aws ecs update-capacity-provider \
 --name `CapacityProviderName` \
 --auto-scaling-group-provider "managedScaling={status=DISABLED}"`
```
