# Updating the SageMaker HyperPod platform software

When you create your SageMaker HyperPod cluster, SageMaker HyperPod selects an Amazon Machine
Image (AMI) corresponding to the Kubernetes version of your Amazon EKS cluster.

Run [update-cluster-software](../../../cli/latest/reference/sagemaker/update-cluster-software.md "../../../cli/latest/reference/sagemaker/update-cluster-software.md") to update existing clusters with software and
security patches provided by the SageMaker HyperPod service. For
`--cluster-name`, specify either the name or the ARN of the cluster
to update.

###### Important

- When this API is called, SageMaker HyperPod doesn’t drain or redistribute
  the jobs (Pods) running on the nodes. Make sure to check if there are
  any jobs running on the nodes before calling this API.
- The patching process replaces the root volume with the updated AMI,
  which means that your previous data stored in the instance root volume
  will be lost. Make sure that you back up your data from the instance
  root volume to Amazon S3 or Amazon FSx for Lustre.
- All cluster nodes experience downtime (nodes appear as
  `<NotReady>` in the output of `kubectl get
node`) while the patching is in progress. We recommend that
  you terminate all workloads before patching and resume them after the
  patch completes.

If the security patch fails, you can retrieve failure messages by
running the [`DescribeCluster`](../APIReference/API_DescribeCluster.md "../APIReference/API_DescribeCluster.md") API as instructed at [Describe a cluster](sagemaker-hyperpod-eks-operate-cli-command-cluster-details.md#sagemaker-hyperpod-eks-operate-cli-command-describe-cluster "sagemaker-hyperpod-eks-operate-cli-command-cluster-details.md#sagemaker-hyperpod-eks-operate-cli-command-describe-cluster").

```
aws sagemaker update-cluster-software --cluster-name `your-hyperpod-cluster`
```

When calling the `UpdateClusterSoftware` API, SageMaker HyperPod updates the
Kubernetes version of the nodes by selecting the latest [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami") based on the Kubernetes version
of your Amazon EKS cluster. It then runs the lifecycle scripts in the Amazon S3 bucket that
you specified during the cluster creation or update.

You can verify the kubelet version of a node by running the `kubectl describe
 node` command.

The Kubernetes version of SageMaker HyperPod cluster nodes does not automatically update
when you update your Amazon EKS cluster version. After updating the Kubernetes version
for your Amazon EKS cluster, you must use the `UpdateClusterSoftware` API to
update your SageMaker HyperPod cluster nodes to the same Kubernetes version.

It is recommended to update your SageMaker HyperPod cluster after updating your Amazon EKS
nodes, and avoid having more than one version difference between the Amazon EKS cluster
version and the SageMaker HyperPod cluster nodes version.

The SageMaker HyperPod service team regularly rolls out new [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami")s for enhancing security and
improving user experiences. We recommend that you always keep updating to the latest
SageMaker HyperPod DLAMI. For future SageMaker HyperPod DLAMI updates for security patching,
follow up with [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

###### Note

You can only run this API programmatically. The patching functionality is not
implemented in the SageMaker HyperPod console UI.
