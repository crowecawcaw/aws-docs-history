

# Mounting S3 file systems on Amazon EKS
<a name="s3-files-mounting-eks"></a>

You can attach an S3 file system to an Amazon EKS cluster by using the Amazon EFS Container Storage Interface (CSI) driver. The driver supports both dynamic and static provisioning. To set this up, install the efs-csi-driver, which is the CSI driver for both Amazon EFS and S3 Files.

![The data flow between an S3 bucket, S3 file system, and Amazon EKS cluster.](http://docs.aws.amazon.com/AmazonS3/latest/userguide/images/S3Files_EKS_dataflow.png)


## Prerequisites
<a name="s3-files-mounting-eks-prereqs"></a>

Before you mount an S3 file system on an EKS cluster, make sure that you have the following:
+ You have an S3 file system that has at least one mount target available.
+ You have configured the required [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups).
+ Your EKS cluster must be in the same VPC as your mount target.
+ The Amazon EFS CSI driver needs AWS Identity and Access Management (IAM) permissions to connect to and interact with S3 file systems. For details, see [IAM role for attaching your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role).
+ AWS suggests using EKS Pod Identities. For more information, see [Overview of setting up EKS Pod Identities](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).
+ For information about IAM roles for service accounts and setting up an IAM OpenID Connect (OIDC) provider for your cluster, see [Create an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).
+ The `kubectl` command line tool is installed on your device or AWS CloudShell. The version must be within one minor version of the Kubernetes version of your cluster. For example, if your cluster version is 1.29, you can use `kubectl` version 1.28, 1.29, or 1.30 with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html).

## How to mount your S3 file system on an EKS cluster
<a name="s3-files-mounting-eks-steps"></a>

The Amazon EFS CSI driver requires IAM permissions to interact with your file system. Create an IAM role and attach the `AmazonS3FilesCSIDriverPolicy` managed policy to it. Then add the EFS CSI driver to your EKS cluster and specify the IAM role. You can use the AWS Management Console or the AWS API. For details, see [Using S3 file system storage with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/s3files-csi.html).

You can also use S3 file systems with AWS Batch on Amazon EKS. To attach an S3 file system volume to your AWS Batch job, use Amazon EKS pods with a persistent volume claim. For more details, see [persistentVolumeClaim](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksVolume.html#Batch-Type-EksVolume-persistentVolumeClaim) section of [Register Job Definitions](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) and [EKS Persistent Volume Claim](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksPersistentVolumeClaim.html) pages of the *AWS Batch API Reference Guide*.

You can monitor your file system storage, performance, client connections, and synchronization errors using [Amazon CloudWatch](s3-files-monitoring-cloudwatch.md).