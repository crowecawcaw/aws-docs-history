# Using the Amazon EBS CSI driver on SageMaker HyperPod EKS

clusters

SageMaker HyperPod supports the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver,
which manages the lifecycle of Amazon EBS volumes as storage for the Kubernetes volumes that you
create. With the Amazon EBS CSI driver, you can create, attach, and manage your Amazon EBS volumes for
your machine learning workloads running on SageMaker HyperPod clusters with Amazon EKS
orchestration.

###### In this topic:

- [Key storage capabilities](#sagemaker-hyperpod-eks-ebs-features "#sagemaker-hyperpod-eks-ebs-features")
- [Use cases](#sagemaker-hyperpod-eks-ebs-use "#sagemaker-hyperpod-eks-ebs-use")
- [Setting up the Amazon EBS CSI driver on
  SageMaker HyperPod EKS clusters](#sagemaker-hyperpod-eks-ebs-setup "#sagemaker-hyperpod-eks-ebs-setup")
- [Using the APIs](#sagemaker-hyperpod-eks-ebs-setup-apis "#sagemaker-hyperpod-eks-ebs-setup-apis")

## Key storage capabilities

The Amazon EBS CSI driver on SageMaker HyperPod supports the following storage
capabilities.

- Static provisioning: Associates pre-created Amazon EBS volumes with Kubernetes
  [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/ "https://kubernetes.io/docs/concepts/storage/persistent-volumes/") for use in your pods.
- Dynamic provisioning: Automatically creates Amazon EBS volumes and associated
  persistent volumes from [`PersistentVolumeClaims`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims"). Parameters can be passed
  via [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/ "https://kubernetes.io/docs/concepts/storage/storage-classes/") for fine-grained control over volume
  creation.
- Volume resizing: Expands existing volumes by updating the [`PersistentVolumeClaims`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims") size specification without disrupting
  running workloads. This can be essential for handling growing model repositories
  or adapting to larger nodes without service disruption.
- Volume snapshots: Creates point-in-time snapshots of volumes for backup,
  recovery, and data versioning.
- Block volumes: Provides raw block device access for high-performance
  applications requiring direct storage access.
- Volume modification: Changes volume properties such as type, input or output
  operations per second (IOPS), or throughput using [volume attributes classes](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ "https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/").

For more information about the Amazon EBS CSI driver, see [Use Kubernetes volume storage with
Amazon EBS](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md") from the _Amazon EKS User Guide_.

For more information about storage to pods in your cluster, see [Storage](https://kubernetes.io/docs/concepts/storage/ "https://kubernetes.io/docs/concepts/storage/") from the
_Kubernetes Documentation_.

## Use cases

The Amazon EBS CSI driver integration enables several key use cases for both training and
inference workloads on SageMaker HyperPod EKS clusters.

**Training workloads**

- Dataset storage: Provision volumes for training datasets that persist across
  pod restarts

- Checkpoint storage: Save model checkpoints and intermediate training
  results

- Shared artifacts: Access common datasets and model artifacts across multiple
  training jobs

**Inference workloads**

- Model storage: Dynamically provision appropriately sized volumes based on
  model requirements

- Container caching: Create ephemeral storage for improved inference
  performance

- Event logging: Store inference results and logs with persistent storage

## Setting up the Amazon EBS CSI driver on

SageMaker HyperPod EKS clusters

The Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver allows you to dynamically
provision and manage Amazon EBS volumes for your containerized workloads running on SageMaker HyperPod clusters
with EKS orchestration. This section walks you through installing and
configuring the Amazon EBS CSI driver to enable persistent storage for your machine learning
workloads.

### Prerequisites

Before you begin, do the following:

- [Install and configure the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")
- [Create a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md")
- Install the Amazon EBS CSI driver with the version of [v1.47.0](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/CHANGELOG.md#v1470 "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/CHANGELOG.md#v1470")

### Additional permissions

To set up the Amazon EBS CSI driver add-on, follow the instructions in [Use Kubernetes
volume storage with Amazon EBS](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md") from the _Amazon EKS User
Guide_. You should also add the following additional permissions to
the IAM role used to run the driver add-on. Note that this is the IAM role
specified in your service account configuration for the driver add-on, not the
HyperPod cluster execution role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "sagemaker:AttachClusterNodeVolume",
 "sagemaker:DetachClusterNodeVolume"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/*"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "eks:DescribeCluster"
 ],
 "Resource": "arn:aws:eks:`us-east-1`:`111122223333`:cluster/my-cluster-name"
 }
 ]
}`

```

## Using the APIs

As an alternative, you can use the [AttachClusterNodeVolume](../APIReference/API_AttachClusterNodeVolume.md "../APIReference/API_AttachClusterNodeVolume.md") and [DetachClusterNodeVolume](../APIReference/API_DetachClusterNodeVolume.md "../APIReference/API_DetachClusterNodeVolume.md") API operations to attach and detach your Amazon EBS
volumes to SageMaker HyperPod EKS cluster instances.

**Key requirements for using these APIs include the
following.**

- Both the Amazon EBS volume and SageMaker HyperPod EKS cluster must be owned by the same AWS account.
- The calling principal needs specific minimum permissions to successfully
  perform the attach or detach operation. For more information about the
  minimum permissions, see the following sections.
- After attaching a volume to your HyperPod node, follow the
  instructions in [Accessing SageMaker HyperPod cluster nodes](sagemaker-hyperpod-eks-operate-access-through-terminal.md "sagemaker-hyperpod-eks-operate-access-through-terminal.md") to access the cluster
  node, and [Make a volume available for use](../../../ebs/latest/userguide/ebs-using-volumes.md "../../../ebs/latest/userguide/ebs-using-volumes.md") to mount the attached
  volume.

### Required permissions for `sagemaker:AttachClusterNodeVolume`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "sagemaker:AttachClusterNodeVolume"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/*"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "eks:DescribeCluster"
 ],
 "Resource": "arn:aws:eks:`us-east-1`:`111122223333`:cluster/my-cluster-name"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "ec2:AttachVolume",
 "ec2:DescribeVolumes"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*"
 }
 ]
}`

```

### Required

permissions for `sagemaker:DetachClusterNodeVolume`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "sagemaker:DetachClusterNodeVolume"
 ],
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:cluster/*"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "eks:DescribeCluster"
 ],
 "Resource": "arn:aws:eks:`us-east-1`:`111122223333`:cluster/my-cluster-name"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "ec2:DetachVolume",
 "ec2:DescribeVolumes"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:volume/*"
 }
 ]
}`

```

### Required permissions

for AWS KMS keys

Add the following AWS KMS permissions only if you're using customer managed
KMS keys to encrypt your Amazon EBS volumes attached to HyperPod
cluster nodes. These permissions are not required if you're using
AWS-managed KMS keys (the default encryption option).

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::`111122223333`:role/caller-role"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::`111122223333`:role/caller-role"
 },
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition":
 {
 "StringEquals":
 {
 "kms:CallerAccount": "`111122223333`",
 "kms:ViaService": "ec2.`us-east-1`.amazonaws.com"
 },
 "ForAnyValue:StringEquals":
 {
 "kms:EncryptionContextKeys": "aws:ebs:id"
 },
 "Bool":
 {
 "kms:GrantIsForAWSResource": true
 },
 "ForAllValues:StringEquals":
 {
 "kms:GrantOperations":
 [
 "Decrypt"
 ]
 }
 }
 }
 ]
}`

```

###### Note

These AWS KMS permissions are not required for
`sagemaker:DetachClusterNodeVolume` when detaching a Cluster
Auto Volume Attachment (CAVA) volume encrypted with customer managed
KMS keys.
