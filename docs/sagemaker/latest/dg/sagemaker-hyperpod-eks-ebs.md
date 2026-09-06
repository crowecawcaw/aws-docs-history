

# Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters
<a name="sagemaker-hyperpod-eks-ebs"></a>

SageMaker HyperPod supports the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver, which manages the lifecycle of Amazon EBS volumes as storage for the Kubernetes volumes that you create. With the Amazon EBS CSI driver, you can create, attach, and manage your Amazon EBS volumes for your machine learning workloads running on SageMaker HyperPod clusters with Amazon EKS orchestration.

**Topics**
+ [Key storage capabilities](#sagemaker-hyperpod-eks-ebs-features)
+ [Considerations](#sagemaker-hyperpod-eks-ebs-considerations)
+ [Use cases](#sagemaker-hyperpod-eks-ebs-use)
+ [Setting up the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](#sagemaker-hyperpod-eks-ebs-setup)
+ [Using the APIs](#sagemaker-hyperpod-eks-ebs-setup-apis)

## Key storage capabilities
<a name="sagemaker-hyperpod-eks-ebs-features"></a>

The Amazon EBS CSI driver on SageMaker HyperPod supports the following storage capabilities.
+ Static provisioning: Associates pre-created Amazon EBS volumes with Kubernetes [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for use in your pods.
+ Dynamic provisioning: Automatically creates Amazon EBS volumes and associated persistent volumes from [`PersistentVolumeClaims`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims). Parameters can be passed via [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/) for fine-grained control over volume creation.
+ Volume resizing: Expands existing volumes by updating the [`PersistentVolumeClaims`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) size specification without disrupting running workloads. This can be essential for handling growing model repositories or adapting to larger nodes without service disruption.
+ Volume snapshots: Creates point-in-time snapshots of volumes for backup, recovery, and data versioning.
+ Block volumes: Provides raw block device access for high-performance applications requiring direct storage access.
+ Volume modification: Changes volume properties such as type, input or output operations per second (IOPS), or throughput using [volume attributes classes](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/).

For more information about the Amazon EBS CSI driver, see [Use Kubernetes volume storage with Amazon EBS](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) from the *Amazon EKS User Guide*.

For more information about storage to pods in your cluster, see [Storage](https://kubernetes.io/docs/concepts/storage/) from the *Kubernetes Documentation*.

## Considerations
<a name="sagemaker-hyperpod-eks-ebs-considerations"></a>

The SageMaker HyperPod AMI already manages local NVMe instance storage on every node. At boot, it combines all of the node's NVMe drives into a single LVM volume group (`vg.01`) and mounts the result at `/opt/sagemaker`. You do not need to install anything else to use local NVMe storage—it is ready to use as soon as the node is up.

**Important**  
Do not install a second CSI driver that targets NVMe instance storage (sometimes called a Local Instance Storage CSI driver). A second storage manager conflicts with `vg.01` and causes NVMe I/O failures, mount failures, and corrupted device state that persists across node reboots and replacements.

This restriction applies only to drivers that manage local NVMe instance storage. Network-backed CSI drivers (Amazon EBS, Amazon FSx, Amazon EFS, and Mountpoint for Amazon S3) are not affected because they do not access the local NVMe disks.

The Amazon EBS CSI driver described on this page manages Amazon EBS volumes only and is not affected by this conflict. The conflict applies only to CSI drivers that manage local NVMe instance storage on the node.

If you have already installed a CSI driver that targets NVMe instance storage and are seeing NVMe I/O errors, follow these steps:

1. Uninstall the local-instance-storage CSI driver add-on.

1. Replace the affected nodes (replacing approximately three at a time is recommended).

1. Verify that NVMe instance storage is restored. The restored state persists through subsequent reboots and replacements.

**Important**  
Do not replace nodes before uninstalling the add-on. The conflict will recur on the new nodes, and the I/O errors will continue.

To use NVMe instance storage on HyperPod, rely on the AMI's built-in LVM configuration through the standard mount path (`/opt/sagemaker`). For dynamically provisioned, pod-level block storage, use the Amazon EBS CSI driver as described in the rest of this page.

## Use cases
<a name="sagemaker-hyperpod-eks-ebs-use"></a>

The Amazon EBS CSI driver integration enables several key use cases for both training and inference workloads on SageMaker HyperPod EKS clusters.

**Training workloads**
+ Dataset storage: Provision volumes for training datasets that persist across pod restarts
+ Checkpoint storage: Save model checkpoints and intermediate training results
+ Shared artifacts: Access common datasets and model artifacts across multiple training jobs

**Inference workloads**
+ Model storage: Dynamically provision appropriately sized volumes based on model requirements
+ Container caching: Create ephemeral storage for improved inference performance
+ Event logging: Store inference results and logs with persistent storage

## Setting up the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters
<a name="sagemaker-hyperpod-eks-ebs-setup"></a>

The Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver allows you to dynamically provision and manage Amazon EBS volumes for your containerized workloads running on SageMaker HyperPod clusters with EKS orchestration. This section walks you through installing and configuring the Amazon EBS CSI driver to enable persistent storage for your machine learning workloads.

### Prerequisites
<a name="sagemaker-hyperpod-eks-ebs-setup-prerequisite"></a>

Before you begin, do the following:
+ [Install and configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
+ [Create a SageMaker HyperPod cluster with Amazon EKS orchestration](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-create-cluster.html)
+ Install the Amazon EBS CSI driver with the version of [v1.47.0](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/CHANGELOG.md#v1470)

### Additional permissions
<a name="sagemaker-hyperpod-eks-ebs-setup-permissions"></a>

To set up the Amazon EBS CSI driver add-on, follow the instructions in [Use Kubernetes volume storage with Amazon EBS](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) from the *Amazon EKS User Guide*. You should also add the following additional permissions to the IAM role used to run the driver add-on. Note that this is the IAM role specified in your service account configuration for the driver add-on, not the HyperPod cluster execution role.

------
#### [ JSON ]

****  

```
{
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
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "eks:DescribeCluster"
            ],
            "Resource": "arn:aws:eks:{{us-east-1}}:{{111122223333}}:cluster/my-cluster-name"
        }
    ]
}
```

------

## Using the APIs
<a name="sagemaker-hyperpod-eks-ebs-setup-apis"></a>

As an alternative, you can use the [AttachClusterNodeVolume](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AttachClusterNodeVolume.html) and [DetachClusterNodeVolume](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DetachClusterNodeVolume.html) API operations to attach and detach your Amazon EBS volumes to SageMaker HyperPod EKS cluster instances.

**Key requirements for using these APIs include the following.**
+ Both the Amazon EBS volume and SageMaker HyperPod EKS cluster must be owned by the same AWS account.
+ The calling principal needs specific minimum permissions to successfully perform the attach or detach operation. For more information about the minimum permissions, see the following sections.
+ After attaching a volume to your HyperPod node, follow the instructions in [Accessing SageMaker HyperPod cluster nodes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-access-through-terminal.html) to access the cluster node, and [Make a volume available for use](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-using-volumes.html) to mount the attached volume.

### Required permissions for `sagemaker:AttachClusterNodeVolume`
<a name="sagemaker-hyperpod-eks-ebs-setup-apis-attach"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "sagemaker:AttachClusterNodeVolume"
            ],
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "eks:DescribeCluster"
            ],
            "Resource": "arn:aws:eks:{{us-east-1}}:{{111122223333}}:cluster/my-cluster-name"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "ec2:AttachVolume",
                "ec2:DescribeVolumes"
            ],
            "Resource": "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:volume/*"
        }
    ]
}
```

------

### Required permissions for `sagemaker:DetachClusterNodeVolume`
<a name="sagemaker-hyperpod-eks-ebs-setup-apis-detach"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Effect": "Allow",
            "Action":
            [
                "sagemaker:DetachClusterNodeVolume"
            ],
            "Resource": "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:cluster/*"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "eks:DescribeCluster"
            ],
            "Resource": "arn:aws:eks:{{us-east-1}}:{{111122223333}}:cluster/my-cluster-name"
        },
        {
            "Effect": "Allow",
            "Action":
            [
                "ec2:DetachVolume",
                "ec2:DescribeVolumes"
            ],
            "Resource": "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:volume/*"
        }
    ]
}
```

------

### Required permissions for AWS KMS keys
<a name="sagemaker-hyperpod-eks-ebs-setup-apis-kms"></a>

Add the following AWS KMS permissions only if you're using customer managed KMS keys to encrypt your Amazon EBS volumes attached to HyperPod cluster nodes. These permissions are not required if you're using AWS-managed KMS keys (the default encryption option).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "key-default-1",
    "Statement":
    [
        {
            "Effect": "Allow",
            "Principal":
            {
                "AWS": "arn:aws:iam::{{111122223333}}:role/caller-role"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Principal":
            {
                "AWS": "arn:aws:iam::{{111122223333}}:role/caller-role"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition":
            {
                "StringEquals":
                {
                    "kms:CallerAccount": "{{111122223333}}",
                    "kms:ViaService": "ec2.{{us-east-1}}.amazonaws.com"
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
}
```

------

**Note**  
These AWS KMS permissions are not required for `sagemaker:DetachClusterNodeVolume` when detaching a Cluster Auto Volume Attachment (CAVA) volume encrypted with customer managed KMS keys.