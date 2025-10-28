# Automatic scaling for Amazon MSK clusters

To automatically expand your cluster's storage in response to increased usage, you can
configure an Application Auto-Scaling policy for Amazon MSK. In an auto-scaling policy, you set
the target disk utilization and the maximum scaling capacity.

Before you use automatic scaling for Amazon MSK, you should consider the following:

- ###### Important

A storage scaling action can occur only once every six hours.

We recommend that you start with a right-sized storage volume for your storage
demands. For guidance on right-sizing your cluster, see [Right-size your cluster: Number of Standard
brokers per cluster](bestpractices.md#brokers-per-cluster "bestpractices.md#brokers-per-cluster").

- Amazon MSK does not reduce cluster storage in response to reduced usage. Amazon MSK does not
  support decreasing the size of storage volumes. If you need to reduce the size of
  your cluster storage, you must migrate your existing cluster to a cluster with
  smaller storage. For information about migrating a cluster, see [Migrate to MSK cluster](migration.md "migration.md").
- Amazon MSK doesn't support automatic scaling in the Asia Pacific (Osaka), Africa (Cape Town), and Asia Pacific (Malaysia) Regions.
- When you associate an auto-scaling policy with your cluster, Amazon EC2 Auto Scaling
  automatically creates an Amazon CloudWatch alarm for target tracking. If you delete a cluster
  with an auto-scaling policy, this CloudWatch alarm persists. To delete the CloudWatch alarm, you
  should remove an auto-scaling policy from a cluster before you delete the cluster.
  To learn more about target tracking, see [Target tracking scaling policies for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md "../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md") in the _Amazon EC2 Auto Scaling User Guide_.

###### Topics

- [Auto-scaling policy details for Amazon MSK](msk-autoexpand-details.md "msk-autoexpand-details.md")
- [Set up automatic scaling for your Amazon MSK cluster](msk-autoexpand-setup.md "msk-autoexpand-setup.md")
