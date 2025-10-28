# Configuring shared storage encryption with an AWS KMS key

Learn how to set up a customer managed AWS KMS key to encrypt and protect your data in the cluster file storage systems that are configured for
AWS ParallelCluster.

When using the AWS ParallelCluster command line interface (CLI) or API, you only pay for
the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information,
see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

AWS ParallelCluster supports following shared storage configuration options:

- [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") / [EbsSettings](SharedStorage-v3.md#SharedStorage-v3-EbsSettings "SharedStorage-v3.md#SharedStorage-v3-EbsSettings") / [KmsKeyId](SharedStorage-v3.md#yaml-SharedStorage-EbsSettings-KmsKeyId "SharedStorage-v3.md#yaml-SharedStorage-EbsSettings-KmsKeyId")
- [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") / [EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings") / [KmsKeyId](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-KmsKeyId "SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-KmsKeyId")
- [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") / [FsxLustreSettings](SharedStorage-v3.md#SharedStorage-v3-FsxLustreSettings "SharedStorage-v3.md#SharedStorage-v3-FsxLustreSettings") / [KmsKeyId](SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-KmsKeyId "SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-KmsKeyId")
  You can use these options to provide a customer managed AWS KMS key for Amazon EBS, Amazon EFS, and FSx for Lustre shared storage system encryption. To use
  them, you must create and configure an IAM policy for the following:

- [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Iam](HeadNode-v3.md#HeadNode-v3-Iam "HeadNode-v3.md#HeadNode-v3-Iam") / [AdditionalIamPolicies](HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies "HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies") / [Policy](HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies-Policy "HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies-Policy")
- [Scheduler](Scheduling-v3.md#yaml-Scheduling-Scheduler "Scheduling-v3.md#yaml-Scheduling-Scheduler") / [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Iam](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Iam "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Iam") / [AdditionalIamPolicies](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-AdditionalIamPolicies "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-AdditionalIamPolicies") / [Policy](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-AdditionalIamPolicies-Policy "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Iam-AdditionalIamPolicies-Policy")

###### Prerequisites

- AWS ParallelCluster [is installed](install-v3-parallelcluster.md "install-v3-parallelcluster.md").
- The AWS CLI [is installed and configured.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- You have an [Amazon EC2 key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").
- You have an IAM role with the [permissions](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies") that are required to run the [pcluster](pcluster-v3.md "pcluster-v3.md") CLI.

###### Topics

- [Create the policy](creating-the-role-v3.md "creating-the-role-v3.md")
- [Configure and create the cluster](creating-the-cluster-v3.md "creating-the-cluster-v3.md")
