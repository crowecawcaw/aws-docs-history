

# SageMaker HyperPod references
<a name="sagemaker-hyperpod-ref"></a>

Find more information and references about using SageMaker HyperPod in the following topics.

**Topics**
+ [SageMaker HyperPod pricing](#sagemaker-hyperpod-ref-pricing)
+ [SageMaker HyperPod APIs](#sagemaker-hyperpod-ref-api)
+ [SageMaker HyperPod Slurm configuration](#sagemaker-hyperpod-ref-slurm-configuration)
+ [SageMaker HyperPod DLAMI](#sagemaker-hyperpod-ref-hyperpod-ami)
+ [SageMaker HyperPod API permissions reference](#sagemaker-hyperpod-ref-api-permissions)
+ [SageMaker HyperPod commands in AWS CLI](#sagemaker-hyperpod-ref-cli)
+ [SageMaker HyperPod Python modules in AWS SDK for Python (Boto3)](#sagemaker-hyperpod-ref-boto3)

## SageMaker HyperPod pricing
<a name="sagemaker-hyperpod-ref-pricing"></a>

The following topics provide information about SageMaker HyperPod pricing. To find more details on price per hour for using SageMaker HyperPod instances, see also [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/). 

**Capacity requests**

You can allocate on-demand or reserved compute capacity with SageMaker AI for use on SageMaker HyperPod. On-demand cluster creation allocates available capacity from the SageMaker AI on-demand capacity pool. Alternatively, you can request reserved capacity to ensure access by submitting a ticket for a quota increase. Inbound capacity requests are prioritized by SageMaker AI and you receive an estimated time for capacity allocation.

**Service billing**

When you provision a compute capacity on SageMaker HyperPod, you are billed for the duration of the capacity allocation. SageMaker HyperPod billing appears in your anniversary bills with a line item for the type of capacity allocation (on-demand, reserved), the instance type, and the time spent on using the instance. 

To submit a ticket for a quota increase, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas).

## SageMaker HyperPod APIs
<a name="sagemaker-hyperpod-ref-api"></a>

The following list is a full set of SageMaker HyperPod APIs for submitting action requests in JSON format to SageMaker AI through AWS CLI or AWS SDK for Python (Boto3).
+ [BatchDeleteClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodes.html)
+ [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html)
+ [DeleteCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteCluster.html)
+ [DescribeCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCluster.html)
+ [DescribeClusterNode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterNode.html)
+ [ListClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterNodes.html)
+ [ListClusters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusters.html)
+ [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html)
+ [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html)

## SageMaker HyperPod Slurm configuration
<a name="sagemaker-hyperpod-ref-slurm-configuration"></a>

HyperPod supports two approaches for configuring Slurm on your cluster. Choose the approach that best fits your needs.


|  |  |  | 
| --- |--- |--- |
| Approach | Description | Recommended For | 
| API-driven configuration | Define Slurm configuration directly in the CreateCluster and UpdateCluster API requests | New clusters; simplified management | 
| Legacy configuration | Use a separate provisioning\_parameters.json file stored in Amazon S3 | Existing clusters; backward compatibility | 

### API-driven Slurm configuration (Recommended)
<a name="sagemaker-hyperpod-ref-slurm-api-driven"></a>

With API-driven configuration, you define Slurm node types, partition assignments, and filesystem mounts directly in the CreateCluster and UpdateCluster API requests. This approach provides:
+ **Single source of truth** – All configuration in the API request
+ **No S3 file management** – No need to create or maintain `provisioning_parameters.json`
+ **Built-in validation** – API validates Slurm topology before cluster creation
+ **Drift detection** – Detects unauthorized changes to `slurm.conf`
+ **Per-instance-group storage** – Configure different FSx filesystems for different instance groups
+ **FSx for OpenZFS support** – Mount OpenZFS filesystems in addition to FSx for Lustre

#### SlurmConfig (per instance group)
<a name="sagemaker-hyperpod-ref-slurm-config"></a>

Add `SlurmConfig` to each instance group to define the Slurm node type and partition assignment.

```
"SlurmConfig": {
    "NodeType": "Controller | Login | Compute",
    "PartitionNames": ["{{string}}"]
}
```

**Parameters:**
+ `NodeType` – Required. The Slurm node type for this instance group. Valid values:
  + `Controller` – Slurm controller (head) node. Runs the `slurmctld` daemon. Exactly one instance group must have this node type.
  + `Login` – Login node for user access. Optional. At most one instance group can have this node type.
  + `Compute` – Worker nodes that execute jobs. Can have multiple instance groups with this node type.
**Important**  
`NodeType` is immutable. Once set during cluster creation, it cannot be changed. To use a different node type, create a new instance group.
+ `PartitionNames` – Conditional. An array of Slurm partition names. Required for `Compute` node types; not allowed for `Controller` or `Login` node types. Currently supports a single partition name per instance group.
**Note**  
All nodes are automatically added to the universal `dev` partition in addition to their specified partition.

**Example:**

```
{
    "InstanceGroupName": "gpu-compute",
    "InstanceType": "ml.p4d.24xlarge",
    "InstanceCount": 8,
    "SlurmConfig": {
        "NodeType": "Compute",
        "PartitionNames": ["gpu-training"]
    },
    "LifeCycleConfig": {
        "SourceS3Uri": "s3://sagemaker-bucket/lifecycle/src/",
        "OnCreate": "on_create.sh"
    },
    "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole"
}
```

#### Orchestrator.Slurm (cluster level)
<a name="sagemaker-hyperpod-ref-slurm-orchestrator"></a>

Add `Orchestrator.Slurm` to the cluster configuration to specify how HyperPod manages the `slurm.conf` file.

```
"Orchestrator": {
    "Slurm": {
        "SlurmConfigStrategy": "Managed | Overwrite | Merge"
    }
}
```

**Parameters:**
+ `SlurmConfigStrategy` – Required when `Orchestrator.Slurm` is provided. Controls how HyperPod manages the `slurm.conf` file on the controller node. Valid values:
  + `Managed` (default) – HyperPod fully controls the partition-node mappings in `slurm.conf`. Drift detection is enabled: if the current `slurm.conf` differs from the expected configuration, UpdateCluster fails with an error. Use this strategy when you want HyperPod to be the single source of truth for Slurm configuration.
  + `Overwrite` – HyperPod forces the API configuration to be applied, overwriting any manual changes to `slurm.conf`. Drift detection is disabled. Use this strategy to recover from drift or reset the cluster to a known state.
  + `Merge` – HyperPod preserves manual `slurm.conf` changes and merges them with the API configuration. Drift detection is disabled. Use this strategy if you need to make manual Slurm configuration changes that should persist across updates.

**Note**  
If `Orchestrator.Slurm` is omitted from the request, the default behavior is `Managed` strategy.

**Tip**  
You can change `SlurmConfigStrategy` at any time using UpdateCluster. There is no lock-in to a specific strategy.

**Example:**

```
{
    "ClusterName": "my-hyperpod-cluster",
    "InstanceGroups": [...],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Managed"
        }
    }
}
```

#### SlurmConfigStrategy comparison
<a name="sagemaker-hyperpod-ref-slurm-strategy-comparison"></a>


|  |  |  |  | 
| --- |--- |--- |--- |
| Strategy | Drift Detection | Manual Changes | Use Case | 
| Managed | Enabled – blocks updates if drift detected | Blocked | HyperPod managed | 
| Overwrite | Disabled | Overwritten | Recovery from drift; reset to known state | 
| Merge | Disabled | Preserved | Advanced users with custom slurm.conf needs | 

#### FSx configuration via InstanceStorageConfigs
<a name="sagemaker-hyperpod-ref-slurm-fsx-config"></a>

With API-driven configuration, you can configure FSx filesystems per instance group using `InstanceStorageConfigs`. This allows different instance groups to mount different filesystems.

**Prerequisites:**
+ Your cluster must use a custom VPC (via `VpcConfig`). FSx filesystems reside in your VPC, and the platform-managed VPC cannot reach them.
+ At least one instance group must have `SlurmConfig` with `NodeType: Controller`.

##### FsxLustreConfig
<a name="sagemaker-hyperpod-ref-slurm-fsx-lustre"></a>

Configure FSx for Lustre filesystem mounting for an instance group.

```
"InstanceStorageConfigs": [
    {
        "FsxLustreConfig": {
            "DnsName": "{{string}}",
            "MountPath": "{{string}}",
            "MountName": "{{string}}"
        }
    }
]
```

**Parameters:**
+ `DnsName` – Required. The DNS name of the FSx for Lustre filesystem. Example: `fs-0abc123def456789.fsx.us-west-2.amazonaws.com`
+ `MountPath` – Optional. The local mount path on the instance. Default: `/fsx`
+ `MountName` – Required. The mount name of the FSx for Lustre filesystem. You can find this in the Amazon FSx console or by running `aws fsx describe-file-systems`.

##### FsxOpenZfsConfig
<a name="sagemaker-hyperpod-ref-slurm-fsx-openzfs"></a>

Configure FSx for OpenZFS filesystem mounting for an instance group.

```
"InstanceStorageConfigs": [
    {
        "FsxOpenZfsConfig": {
            "DnsName": "{{string}}",
            "MountPath": "{{string}}"
        }
    }
]
```

**Parameters:**
+ `DnsName` – Required. The DNS name of the FSx for OpenZFS filesystem. Example: `fs-0xyz987654321.fsx.us-west-2.amazonaws.com`
+ `MountPath` – Optional. The local mount path on the instance. Default: `/home`

**Note**  
Each instance group can have at most one `FsxLustreConfig` and one `FsxOpenZfsConfig`.

**Example with multiple filesystems:**

```
{
    "InstanceGroupName": "gpu-compute",
    "InstanceType": "ml.p4d.24xlarge",
    "InstanceCount": 4,
    "SlurmConfig": {
        "NodeType": "Compute",
        "PartitionNames": ["gpu-training"]
    },
    "InstanceStorageConfigs": [
        {
            "FsxLustreConfig": {
                "DnsName": "fs-0abc123def456789.fsx.us-west-2.amazonaws.com",
                "MountPath": "/fsx",
                "MountName": "abcdefgh"
            }
        },
        {
            "FsxOpenZfsConfig": {
                "DnsName": "fs-0xyz987654321.fsx.us-west-2.amazonaws.com",
                "MountPath": "/shared"
            }
        },
        {
            "EbsVolumeConfig": {
                "VolumeSizeInGB": 500
            }
        }
    ],
    "LifeCycleConfig": {
        "SourceS3Uri": "s3://sagemaker-bucket/lifecycle/src/",
        "OnCreate": "on_create.sh"
    },
    "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole"
}
```

**Important**  
FSx configuration changes only apply during node provisioning. Existing nodes retain their original FSx configuration. To apply new FSx configuration to all nodes, scale down the instance group to 0, then scale back up.

#### Complete API-driven configuration example
<a name="sagemaker-hyperpod-ref-slurm-complete-example"></a>

The following example shows a complete CreateCluster request using API-driven Slurm configuration:

```
{
    "ClusterName": "ml-training-cluster",
    "InstanceGroups": [
        {
            "InstanceGroupName": "controller",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Controller"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-us-west-2-111122223333/lifecycle/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole",
            "ThreadsPerCore": 2
        },
        {
            "InstanceGroupName": "login",
            "InstanceType": "ml.m5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Login"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-us-west-2-111122223333/lifecycle/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole",
            "ThreadsPerCore": 2
        },
        {
            "InstanceGroupName": "gpu-compute",
            "InstanceType": "ml.p4d.24xlarge",
            "InstanceCount": 8,
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["gpu-training"]
            },
            "InstanceStorageConfigs": [
                {
                    "FsxLustreConfig": {
                        "DnsName": "fs-0abc123def456789.fsx.us-west-2.amazonaws.com",
                        "MountPath": "/fsx",
                        "MountName": "abcdefgh"
                    }
                }
            ],
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-us-west-2-111122223333/lifecycle/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole",
            "ThreadsPerCore": 2,
            "OnStartDeepHealthChecks": ["InstanceStress", "InstanceConnectivity"]
        },
        {
            "InstanceGroupName": "cpu-compute",
            "InstanceType": "ml.c5.18xlarge",
            "InstanceCount": 4,
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["cpu-preprocessing"]
            },
            "InstanceStorageConfigs": [
                {
                    "FsxLustreConfig": {
                        "DnsName": "fs-0abc123def456789.fsx.us-west-2.amazonaws.com",
                        "MountPath": "/fsx",
                        "MountName": "abcdefgh"
                    }
                }
            ],
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-us-west-2-111122223333/lifecycle/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodRole",
            "ThreadsPerCore": 2
        }
    ],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Managed"
        }
    },
    "VpcConfig": {
        "SecurityGroupIds": ["sg-0abc123def456789a"],
        "Subnets": ["subnet-0abc123def456789a", "subnet-0abc123def456789b"]
    },
    "Tags": [
        {
            "Key": "Project",
            "Value": "ML-Training"
        }
    ]
}
```

To learn more about using API-driven configuration, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

### Legacy configuration: provisioning\_parameters.json
<a name="sagemaker-hyperpod-ref-provisioning-forms"></a>

**Note**  
The `provisioning_parameters.json` approach is the legacy method for configuring Slurm on HyperPod. For new clusters, we recommend using the API-driven configuration approach described above. The legacy approach remains fully supported for backward compatibility.

With the legacy approach, you create a Slurm configuration file named `provisioning_parameters.json` and upload it to Amazon S3 as part of your lifecycle scripts. HyperPod reads this file during cluster creation to configure Slurm nodes.

#### Configuration form for provisioning\_parameters.json
<a name="sagemaker-hyperpod-ref-provisioning-forms-slurm"></a>

The following code is the Slurm configuration form you should prepare to properly set up Slurm nodes on your HyperPod cluster. You should complete this form and upload it as part of a set of lifecycle scripts during cluster creation. To learn how this form should be prepared throughout HyperPod cluster creation processes, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

```
// Save as provisioning_parameters.json.
{
    "version": "1.0.0",
    "workload_manager": "slurm",
    "controller_group": "{{string}}",
    "login_group": "{{string}}",
    "worker_groups": [
        {
            "instance_group_name": "{{string}}",
            "partition_name": "{{string}}"
        }
    ],
    "fsx_dns_name": "{{string}}",
    "fsx_mountname": "{{string}}"
}
```

**Parameters:**
+ `version` – Required. This is the version of the HyperPod provisioning parameter form. Keep it to `1.0.0`.
+ `workload_manager` – Required. This is for specifying which workload manager to be configured on the HyperPod cluster. Keep it to `slurm`.
+ `controller_group` – Required. This is for specifying the name of the HyperPod cluster instance group you want to assign to Slurm controller (head) node.
+ `login_group` – Optional. This is for specifying the name of the HyperPod cluster instance group you want to assign to Slurm login node.
+ `worker_groups` – Required. This is for setting up Slurm worker (compute) nodes on the HyperPod cluster.
  + `instance_group_name` – Required. This is for specifying the name of the HyperPod instance group you want to assign to Slurm worker (compute) node.
  + `partition_name` – Required. This is for specifying the partition name to the node.
+ `fsx_dns_name` – Optional. If you want to set up your Slurm nodes on the HyperPod cluster to communicate with Amazon FSx, specify the FSx DNS name.
+ `fsx_mountname` – Optional. If you want to set up your Slurm nodes on the HyperPod cluster to communicate with Amazon FSx, specify the FSx mount name.

### Comparison: API-driven vs. legacy configuration
<a name="sagemaker-hyperpod-ref-slurm-comparison"></a>


|  |  |  | 
| --- |--- |--- |
| Feature | API-driven (Recommended) | Legacy (provisioning\_parameters.json) | 
| Configuration location | CreateCluster API request | S3 file | 
| FSx for Lustre | Yes – Per instance group | Yes – Cluster-wide only | 
| FSx for OpenZFS | Yes – Per instance group | No – Not supported | 
| Built-in validation | Yes | No | 
| Drift detection | Yes – (Managed strategy) | No | 
| S3 file management | Not required | Required | 
| Lifecycle script complexity | Simplified | Full SLURM setup required | 

## SageMaker HyperPod DLAMI
<a name="sagemaker-hyperpod-ref-hyperpod-ami"></a>

SageMaker HyperPod runs a DLAMI based on:
+ [AWS Deep Learning Base GPU AMI (Ubuntu 20.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/) for orchestration with Slurm.
+ Amazon Linux 2 based AMI for orchestration with Amazon EKS.

The SageMaker HyperPod DLAMI is bundled with additional packages to support open source tools such as Slurm, Kubernetes, dependencies, and SageMaker HyperPod cluster software packages to support resiliency features such as cluster health check and auto-resume. To follow up with HyperPod software updates that the HyperPod service team distributes through DLAMIs, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md).

## SageMaker HyperPod API permissions reference
<a name="sagemaker-hyperpod-ref-api-permissions"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

When you are setting up access control for allowing to run SageMaker HyperPod API operations and writing a permissions policy that you can attach to IAM users for cloud administrators, use the following table as a reference.


|  |  |  | 
| --- |--- |--- |
| Amazon SageMaker API Operations | Required Permissions (API Actions) | Resources | 
| CreateCluster | sagemaker:CreateCluster | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| DeleteCluster | sagemaker:DeleteCluster | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| DescribeCluster | sagemaker:DescribeCluster | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| DescribeClusterNode | sagemaker:DescribeClusterNode | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| ListClusterNodes | sagemaker:ListClusterNodes | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| ListClusters | sagemaker:ListClusters | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| UpdateCluster | sagemaker:UpdateCluster | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 
| UpdateClusterSoftware | sagemaker:UpdateClusterSoftware | arn:aws:sagemaker:{{region}}:{{account-id}}:cluster/{{cluster-id}} | 

For a complete list of permissions and resource types for SageMaker APIs, see [Actions, resources, and condition keys for Amazon SageMaker AI](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html) in the *AWS Service Authorization Reference*.

## SageMaker HyperPod commands in AWS CLI
<a name="sagemaker-hyperpod-ref-cli"></a>

The following are the AWS CLI commands for SageMaker HyperPod to run the core [HyperPod API operations](#sagemaker-hyperpod-ref-api).
+ [batch-delete-cluster-nodes](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/batch-delete-cluster-nodes.html)
+ [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/create-cluster.html)
+ [delete-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/delete-cluster.html)
+ [describe-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster.html)
+ [describe-cluster-node](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster-node.html)
+ [list-cluster-nodes](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-cluster-nodes.html)
+ [list-clusters](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-clusters.html)
+ [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html)
+ [update-cluster-software](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster-software.html)

## SageMaker HyperPod Python modules in AWS SDK for Python (Boto3)
<a name="sagemaker-hyperpod-ref-boto3"></a>

The following are the methods of the AWS SDK for Python (Boto3) client for SageMaker AI to run the core [HyperPod API operations](#sagemaker-hyperpod-ref-api).
+ [batch\_delete\_cluster\_nodes](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/batch_delete_cluster_nodes.html#)
+ [create\_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_cluster.html)
+ [delete\_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/delete_cluster.html)
+ [describe\_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster.html)
+ [describe\_cluster\_node](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster_node.html)
+ [list\_cluster\_nodes](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_cluster_nodes.html)
+ [list\_clusters](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/list_clusters.html)
+ [update\_cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster.html)
+ [update\_cluster\_software](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_cluster_software.html)