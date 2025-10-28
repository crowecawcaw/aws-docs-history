# SageMaker HyperPod references

Find more information and references about using SageMaker HyperPod in the following
topics.

###### Topics

- [SageMaker HyperPod pricing](#sagemaker-hyperpod-ref-pricing "#sagemaker-hyperpod-ref-pricing")
- [SageMaker HyperPod APIs](#sagemaker-hyperpod-ref-api "#sagemaker-hyperpod-ref-api")
- [SageMaker HyperPod forms](#sagemaker-hyperpod-ref-provisioning-forms "#sagemaker-hyperpod-ref-provisioning-forms")
- [SageMaker HyperPod DLAMI](#sagemaker-hyperpod-ref-hyperpod-ami "#sagemaker-hyperpod-ref-hyperpod-ami")
- [SageMaker HyperPod API permissions
  reference](#sagemaker-hyperpod-ref-api-permissions "#sagemaker-hyperpod-ref-api-permissions")
- [SageMaker HyperPod commands in AWS CLI](#sagemaker-hyperpod-ref-cli "#sagemaker-hyperpod-ref-cli")
- [SageMaker HyperPod Python modules in
  AWS SDK for Python (Boto3)](#sagemaker-hyperpod-ref-boto3 "#sagemaker-hyperpod-ref-boto3")

## SageMaker HyperPod pricing

The following topics provide information about SageMaker HyperPod pricing. To find more
details on price per hour for using SageMaker HyperPod instances, see also [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

**Capacity requests**

You can allocate on-demand or reserved compute capacity with SageMaker AI for use on
SageMaker HyperPod. On-demand cluster creation allocates available capacity from the SageMaker AI
on-demand capacity pool. Alternatively, you can request reserved capacity to ensure
access by submitting a ticket for a quota increase. Inbound capacity requests are
prioritized by SageMaker AI and you receive an estimated time for capacity allocation.

**Service billing**

When you provision a compute capacity on SageMaker HyperPod, you are billed for the duration
of the capacity allocation. SageMaker HyperPod billing appears in your anniversary bills with
a line item for the type of capacity allocation (on-demand, reserved), the instance
type, and the time spent on using the instance.

To submit a ticket for a quota increase, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas").

## SageMaker HyperPod APIs

The following list is a full set of SageMaker HyperPod APIs for submitting action requests
in JSON format to SageMaker AI through AWS CLI or AWS SDK for Python (Boto3).

- [BatchDeleteClusterNodes](../APIReference/API_BatchDeleteClusterNodes.md "../APIReference/API_BatchDeleteClusterNodes.md")
- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
- [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md")
- [DescribeCluster](../APIReference/API_DescribeCluster.md "../APIReference/API_DescribeCluster.md")
- [DescribeClusterNode](../APIReference/API_DescribeClusterNode.md "../APIReference/API_DescribeClusterNode.md")
- [ListClusterNodes](../APIReference/API_ListClusterNodes.md "../APIReference/API_ListClusterNodes.md")
- [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md")
- [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")
- [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md")

## SageMaker HyperPod forms

To configure the Slurm workload manager tool on HyperPod, you should create a
Slurm configuration file required by HyperPod using the provided form.

### Configuration form

for provisioning Slurm nodes on HyperPod

The following code is the Slurm configuration form you should prepare to properly
set up Slurm nodes on your HyperPod cluster. You should complete this form
and upload it as part of a set of lifecycle scripts during cluster creation. To
learn how this form should be prepared throughout HyperPod cluster creation
processes, see [Customizing SageMaker HyperPod
clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").

```
// Save as provisioning_parameters.json.
{
    "version": "1.0.0",
    "workload_manager": "slurm",
    "controller_group": "`string`",
    "login_group": "`string`",
    "worker_groups": [
        {
            "instance_group_name": "`string`",
            "partition_name": "`string`"
        }
    ],
    "fsx_dns_name": "`string`",
    "fsx_mountname": "`string`"
}
```

- `version` – Required. This is the version of the
  HyperPod provisioning parameter form. Keep it to
  `1.0.0`.
- `workload_manager` – Required. This is for specifying
  which workload manager to be configured on the HyperPod cluster.
  Keep it to `slurm`.
- `controller_group` – Required. This is for specifying
  the name of the HyperPod cluster instance group you want to assign
  to Slurm controller (head) node.
- `login_group` – Optional. This is for specifying the
  name of the HyperPod cluster instance group you want to assign to
  Slurm login node.
- `worker_groups` – Required. This is for setting up Slurm
  worker (compute) nodes on the HyperPod cluster.
  - `instance_group_name` – Required. This is for
    specifying the name of the HyperPod instance group you want
    to assign to Slurm worker (compute) node.
  - `partition_name` – Required. This is for
    specifying the partition name to the node.

- `fsx_dns_name` – Optional. If you want to set up your
  Slurm nodes on the HyperPod cluster to communicate with Amazon FSx,
  specify the FSx DNS name.
- `fsx_mountname` – Optional. If you want to set up your
  Slurm nodes on the HyperPod cluster to communicate with Amazon FSx,
  specify the FSx mount name.

## SageMaker HyperPod DLAMI

SageMaker HyperPod runs a DLAMI based on:

- [AWS Deep Learning Base GPU AMI (Ubuntu 20.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/") for orchestration
  with Slurm.
- Amazon Linux 2 based AMI for orchestration with Amazon EKS.

The SageMaker HyperPod DLAMI is bundled with additional packages to support open source
tools such as Slurm, Kubernetes, dependencies, and SageMaker HyperPod cluster software
packages to support resiliency features such as cluster health check and auto-resume. To
follow up with HyperPod software updates that the HyperPod service
team distributes through DLAMIs, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

## SageMaker HyperPod API permissions

reference

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

When you are setting up access control for allowing to run SageMaker HyperPod API operations
and writing a permissions policy that you can attach to IAM users for cloud
administrators, use the following table as a reference.

|                                     |                                        |                                                                |
| ----------------------------------- | -------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon SageMaker API Operations** | **Required Permissions (API Actions)** | **Resources**                                                  |
| CreateCluster                       | `sagemaker:CreateCluster`              | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| DeleteCluster                       | `sagemaker:DeleteCluster`              | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| DescribeCluster                     | `sagemaker:DescribeCluster`            | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| DescribeClusterNode                 | `sagemaker:DescribeClusterNode`        | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| ListClusterNodes                    | `sagemaker:ListClusterNodes`           | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| ListClusters                        | `sagemaker:ListClusters`               | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| UpdateCluster                       | `sagemaker:UpdateCluster`              | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` |
| UpdateClusterSoftware               | `sagemaker:UpdateClusterSoftware`      | `arn:aws:sagemaker:`region`:`account-id`:cluster/`cluster-id`` | For a complete list of permissions and resource types for SageMaker APIs, see [Actions, resources, and condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md") in the _AWS Service Authorization Reference_. ## SageMaker HyperPod commands in AWS CLI The following are the AWS CLI commands for SageMaker HyperPod to run the core [HyperPod API operations](#sagemaker-hyperpod-ref-api "#sagemaker-hyperpod-ref-api"). <br>• [batch-delete-cluster-nodes](../../../cli/latest/reference/sagemaker/batch-delete-cluster-nodes.md "../../../cli/latest/reference/sagemaker/batch-delete-cluster-nodes.md") <br>• [create-cluster](../../../cli/latest/reference/sagemaker/create-cluster.md "../../../cli/latest/reference/sagemaker/create-cluster.md") <br>• [delete-cluster](../../../cli/latest/reference/sagemaker/delete-cluster.md "../../../cli/latest/reference/sagemaker/delete-cluster.md") <br>• [describe-cluster](../../../cli/latest/reference/sagemaker/describe-cluster.md "../../../cli/latest/reference/sagemaker/describe-cluster.md") <br>• [describe-cluster-node](../../../cli/latest/reference/sagemaker/describe-cluster-node.md "../../../cli/latest/reference/sagemaker/describe-cluster-node.md") <br>• [list-cluster-nodes](../../../cli/latest/reference/sagemaker/list-cluster-nodes.md "../../../cli/latest/reference/sagemaker/list-cluster-nodes.md") <br>• [list-clusters](../../../cli/latest/reference/sagemaker/list-clusters.md "../../../cli/latest/reference/sagemaker/list-clusters.md") <br>• [update-cluster](../../../cli/latest/reference/sagemaker/update-cluster.md "../../../cli/latest/reference/sagemaker/update-cluster.md") <br>• [update-cluster-software](../../../cli/latest/reference/sagemaker/update-cluster-software.md "../../../cli/latest/reference/sagemaker/update-cluster-software.md") ## SageMaker HyperPod Python modules in AWS SDK for Python (Boto3) The following are the methods of the AWS SDK for Python (Boto3) client for SageMaker AI to run the core [HyperPod API operations](#sagemaker-hyperpod-ref-api "#sagemaker-hyperpod-ref-api"). <br>• [batch_delete_cluster_nodes](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/batch_delete_cluster_nodes.html# "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/batch_delete_cluster_nodes.html#") <br>• [create_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_cluster.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_cluster.html") <br>• [delete_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/delete_cluster.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/delete_cluster.html") <br>• [describe_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster.html") <br>• [describe_cluster_node](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster_node.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster_node.html") <br>• [list_cluster_nodes](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_cluster_nodes.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_cluster_nodes.html") <br>• [list_clusters](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_clusters.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_clusters.html") <br>• [update_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster.html") <br>• [update_cluster_software](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster_software.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster_software.html") |
