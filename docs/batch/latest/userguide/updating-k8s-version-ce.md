# Update the Kubernetes version of the compute environment

With AWS Batch, you can update the Kubernetes version of a compute environment to support Amazon EKS cluster upgrades. The
Kubernetes version of a compute environment is the Amazon EKS AMI version for the Kubernetes nodes that AWS Batch launches to run jobs.
You can perform a Kubernetes version upgrade on their Amazon EKS nodes before or after you update the version of Amazon EKS cluster's
control-plane. We recommend that you update the nodes after upgrading the control plane. For more information, see
[Updating an Amazon EKS cluster Kubernetes
version](../../../eks/latest/userguide/update-cluster.md "../../../eks/latest/userguide/update-cluster.md") in the _Amazon EKS User Guide_.

To upgrade the Kubernetes version of a compute environment, use the [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") API
operation.

```
`$` `aws batch update-compute-environment \
 --compute-environment `<compute-environment-name>` \
 --compute-resources \
 'ec2Configuration=[{imageType=EKS_AL2,imageKubernetesVersion=`1.32`}]'`
```
