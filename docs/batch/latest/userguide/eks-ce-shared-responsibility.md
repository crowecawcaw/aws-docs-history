# Shared responsibility of the Kubernetes nodes

Maintenance of the compute environments is a shared responsibility.

- Don't change or remove AWS Batch nodes, labels, taints, namespaces, launch templates, or auto scaling groups.
  Don't add taints to AWS Batch managed nodes. If you make any of these changes, your compute environment cannot be
  supported and failures including idle instances occur.
- Don't target your pods to AWS Batch managed nodes. If you target your pods to the managed nodes, broken
  scaling and stuck job queues occur. Run workloads that don't use AWS Batch on self-managed nodes or managed node
  groups. For more information, see [Managed node groups](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md") in the _Amazon EKS User Guide_.
- You can target a DaemonSet to run on AWS Batch managed nodes. For more information, see [Run a DaemonSet on AWS Batch managed nodes](daemonset-on-batch-eks-nodes.md "daemonset-on-batch-eks-nodes.md").
  AWS Batch doesn't automatically update compute environment AMIs. It's your responsibility to update them. Run the
  following command to update your AMIs to the latest AMI version.

```
`$` `aws batch update-compute-environment \
 --compute-environment `<compute-environment-name>` \
 --compute-resources 'updateToLatestImageVersion=true'`
```

AWS Batch doesn't automatically upgrade the Kubernetes version. Run the following command to update
the Kubernetes version of your computer environment to `1.32`.

```
`$` `aws batch update-compute-environment \
 --compute-environment `<compute-environment-name>` \
 --compute-resources \
 'ec2Configuration=[{imageType=EKS_AL2,imageKubernetesVersion=`1.32`}]'`
```

When updating to a more recent AMI or the Kubernetes version, you can specify whether to terminate jobs when they're
updated (`terminateJobsOnUpdate`) and how long to wait for before an instance is replaced if running jobs
don't finish (`jobExecutionTimeoutMinutes`.) For more information, see [Update a compute environment in
AWS Batch](updating-compute-environments.md "updating-compute-environments.md") and the infrastructure update
policy ([UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")) set in the [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") API
operation.
