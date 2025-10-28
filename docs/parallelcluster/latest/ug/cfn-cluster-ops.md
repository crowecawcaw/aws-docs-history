# Cluster operations

When a cluster custom resource is added to a CloudFormation stack, CloudFormation can perform the following cluster operations:

- CloudFormation creates a cluster in a new separate stack when it deploys a stack that includes the AWS ParallelCluster custom resource.
- If you update the cluster configuration defined in the stack, according to configuration update policies, CloudFormation updates the
  cluster. The AWS ParallelCluster custom resource provider doesn't stop the compute fleet before updating the cluster. We recommend that you use the
  [QueueUpdateStrategy](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy") setting for cluster updates. This way,
  you can avoid making explicit `pcluster update-compute-fleet` calls before and after updates when using the AWS ParallelCluster custom
  resource.
- If you delete the stack, the cluster is deleted.
