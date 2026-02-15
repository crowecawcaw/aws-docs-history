# Getting started with SageMaker HyperPod

using the AWS CLI

Create your first SageMaker HyperPod cluster using the AWS CLI commands for
HyperPod.

## Create your

first SageMaker HyperPod cluster with Slurm

The following tutorial demonstrates how to create a new SageMaker HyperPod cluster and
set it up with Slurm through the [AWS CLI
commands for SageMaker HyperPod](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-cli "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-cli"). Following the tutorial, you'll create a
HyperPod cluster with three Slurm nodes: `my-controller-group`,
`my-login-group`, and `worker-group-1`.

With the API-driven configuration approach, you define Slurm node types and
partition assignments directly in the CreateCluster API request using
`SlurmConfig`. This eliminates the need for a separate
`provisioning_parameters.json` file and provides built-in validation,
drift detection, and per-instance-group FSx configuration.

1. First, prepare and upload lifecycle scripts to an Amazon S3 bucket. During
   cluster creation, HyperPod runs them in each instance group. Upload
   lifecycle scripts to Amazon S3 using the following command.

```
aws s3 sync \
    ~/`local-dir-to-lifecycle-scripts`/* \
    s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`
```

###### Note

The S3 bucket path should start with a prefix `sagemaker-`,
because the [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod") with
`AmazonSageMakerClusterInstanceRolePolicy` only allows
access to Amazon S3 buckets that starts with the specific prefix.

If you are starting from scratch, use sample lifecycle scripts provided in
the [Awsome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/"). The following
sub-steps show how to download and upload the sample lifecycle scripts to an
Amazon S3 bucket.

    1. Download a copy of the lifecycle script samples to a directory on
     your local computer.



    ```
    git clone https://github.com/aws-samples/awsome-distributed-training/
    ```
    2. Go into the directory [`1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config`](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config"),
     where you can find a set of lifecycle scripts.



    ```
    cd awsome-distributed-training/1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config
    ```

    To learn more about the lifecycle script samples, see [Customizing SageMaker HyperPod
     clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").
    3. Upload the scripts to
     `s3://sagemaker-`<unique-s3-bucket-name>`/`<lifecycle-script-directory>`/src`.
     You can do so by using the Amazon S3 console, or by running the following
     AWS CLI Amazon S3 command.



    ```
    aws s3 sync \
        ~/`local-dir-to-lifecycle-scripts`/* \
        s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`
    ```###### Note

With API-driven configuration, you do not need to create or upload a
`provisioning_parameters.json` file. The Slurm
configuration is defined directly in the CreateCluster API request in
the next step. 2. Prepare a [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") request file in JSON format and save as
`create_cluster.json`.

With API-driven configuration, you specify the Slurm node type and
partition assignment for each instance group using the
`SlurmConfig` field. You also configure the cluster-level
Slurm settings using `Orchestrator.Slurm`.

For `ExecutionRole`, provide the ARN of the IAM role you
created with the managed
`AmazonSageMakerClusterInstanceRolePolicy` in [Prerequisites for using
SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md").

```
{
    "ClusterName": "my-hyperpod-cluster",
    "InstanceGroups": [
        {
            "InstanceGroupName": "my-controller-group",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Controller"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::`<account-id>`:role/HyperPodExecutionRole",
            "InstanceStorageConfigs": [
                {
                    "EbsVolumeConfig": {
                        "VolumeSizeInGB": 500
                    }
                }
            ]
        },
        {
            "InstanceGroupName": "my-login-group",
            "InstanceType": "ml.m5.4xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Login"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::`<account-id>`:role/HyperPodExecutionRole"
        },
        {
            "InstanceGroupName": "worker-group-1",
            "InstanceType": "ml.trn1.32xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["partition-1"]
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::`<account-id>`:role/HyperPodExecutionRole"
        }
    ],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Managed"
        }
    }
}
```

**SlurmConfig fields:**

| Field            | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| `NodeType`       | The Slurm role for the instance group. Valid values:<br>`Controller`, `Login`,<br>`Compute` |
| `PartitionNames` | The Slurm partition(s) to assign compute nodes to. Only<br>valid for `Compute` node type.   |

**Orchestrator.Slurm fields:**

| Field                 | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| `SlurmConfigStrategy` | Controls how HyperPod manages<br>`slurm.conf`. Valid values:<br>`Managed` (default), `Overwrite`,<br>`Merge` |

**SlurmConfigStrategy options:**

    * `Managed` (recommended): HyperPod fully
     manages `slurm.conf` and detects unauthorized changes
     (drift detection). Updates fail if drift is detected.
    * `Overwrite`: HyperPod overwrites
     `slurm.conf` on updates, ignoring any manual
     changes.
    * `Merge`: HyperPod preserves manual changes and
     merges them with API configuration.

**Adding FSx for Lustre (optional):**

To mount an FSx for Lustre filesystem to your compute nodes, add
`FsxLustreConfig` to the `InstanceStorageConfigs`
for the instance group. This requires a Custom VPC configuration.

```
{
    "InstanceGroupName": "worker-group-1",
    "InstanceType": "ml.trn1.32xlarge",
    "InstanceCount": 1,
    "SlurmConfig": {
        "NodeType": "Compute",
        "PartitionNames": ["partition-1"]
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
        "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
        "OnCreate": "on_create.sh"
    },
    "ExecutionRole": "arn:aws:iam::`<account-id>`:role/HyperPodExecutionRole"
}
```

**Adding FSx for OpenZFS (optional):**

You can also mount FSx for OpenZFS filesystems:

```
"InstanceStorageConfigs": [
    {
        "FsxOpenZfsConfig": {
            "DnsName": "fs-0xyz789abc123456.fsx.us-west-2.amazonaws.com",
            "MountPath": "/shared"
        }
    }
]
```

###### Note

Each instance group can have at most one FSx for Lustre and one FSx for
OpenZFS configuration. Different instance groups can mount different
filesystems.

**Adding VPC configuration (required for FSx):**

If using FSx, you must specify a Custom VPC configuration:

```
{
    "ClusterName": "my-hyperpod-cluster",
    "InstanceGroups": [
        {
            "InstanceGroupName": "my-controller-group",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Controller"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src`",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::`<account-id>`:role/HyperPodExecutionRole"
        },
    ],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Managed"
        }
    },
    "VpcConfig": {
        "SecurityGroupIds": ["sg-0abc123def456789a"],
        "Subnets": ["subnet-0abc123def456789a"]
    }
}
```

3. Run the following command to create the cluster.

```
aws sagemaker create-cluster --cli-input-json `file://complete/path/to/create_cluster.json`
```

This should return the ARN of the created cluster.

```
{
    "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/my-hyperpod-cluster"
}
```

If you receive an error due to resource limits, ensure that you change the
instance type to one with sufficient quotas in your account, or request
additional quotas by following [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas").

**Common validation errors:**

| Error                                                                      | Resolution                                                                         |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| "Cluster must have exactly one InstanceGroup with<br>Controller node type" | Ensure exactly one instance group has<br>`SlurmConfig.NodeType`:<br>`"Controller"` |
| "Partitions can only be assigned to Compute node<br>types"                 | Remove `PartitionNames` from<br>`Controller` or `Login` instance<br>groups         |
| "FSx configurations are only supported for Custom<br>VPC"                  | Add `VpcConfig` to your request when using<br>FSx                                  |

4. Run `describe-cluster` to check the status of the
   cluster.

```
aws sagemaker describe-cluster --cluster-name `my-hyperpod-cluster`
```

Example response:

```
{
    "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/my-hyperpod-cluster",
    "ClusterName": "my-hyperpod-cluster",
    "ClusterStatus": "Creating",
    "InstanceGroups": [
        {
            "InstanceGroupName": "my-controller-group",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 1,
            "CurrentCount": 0,
            "TargetCount": 1,
            "SlurmConfig": {
                "NodeType": "Controller"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-<bucket>/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        },
        {
            "InstanceGroupName": "my-login-group",
            "InstanceType": "ml.m5.4xlarge",
            "InstanceCount": 1,
            "CurrentCount": 0,
            "TargetCount": 1,
            "SlurmConfig": {
                "NodeType": "Login"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-<bucket>/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        },
        {
            "InstanceGroupName": "worker-group-1",
            "InstanceType": "ml.trn1.32xlarge",
            "InstanceCount": 1,
            "CurrentCount": 0,
            "TargetCount": 1,
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["partition-1"]
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://sagemaker-<bucket>/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        }
    ],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Managed"
        }
    },
    "CreationTime": "2024-01-15T10:30:00Z"
}
```

After the status of the cluster turns to `InService`,
proceed to the next step. Cluster creation typically takes 10-15
minutes. 5. Run `list-cluster-nodes` to check the details of the cluster
nodes.

```
aws sagemaker list-cluster-nodes --cluster-name `my-hyperpod-cluster`
```

Example response:

```
{
    "ClusterNodeSummaries": [
        {
            "InstanceGroupName": "my-controller-group",
            "InstanceId": "i-0abc123def456789a",
            "InstanceType": "ml.c5.xlarge",
            "InstanceStatus": {
                "Status": "Running",
                "Message": ""
            },
            "LaunchTime": "2024-01-15T10:35:00Z"
        },
        {
            "InstanceGroupName": "my-login-group",
            "InstanceId": "i-0abc123def456789b",
            "InstanceType": "ml.m5.4xlarge",
            "InstanceStatus": {
                "Status": "Running",
                "Message": ""
            },
            "LaunchTime": "2024-01-15T10:35:00Z"
        },
        {
            "InstanceGroupName": "worker-group-1",
            "InstanceId": "i-0abc123def456789c",
            "InstanceType": "ml.trn1.32xlarge",
            "InstanceStatus": {
                "Status": "Running",
                "Message": ""
            },
            "LaunchTime": "2024-01-15T10:36:00Z"
        }
    ]
}
```

The `InstanceId` is what your cluster users need for logging
(`aws ssm`) into them. For more information about logging
into the cluster nodes and running ML workloads, see [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md "sagemaker-hyperpod-run-jobs-slurm.md"). 6. Connect to your cluster using AWS Systems Manager Session Manager.

```
aws ssm start-session \
    --target sagemaker-cluster:`my-hyperpod-cluster`_`my-login-group`-`i-0abc123def456789b` \
    --region `us-west-2`
```

Once connected, verify Slurm is configured correctly:

```
# Check Slurm nodes
sinfo

# Check Slurm partitions
sinfo -p partition-1

# Submit a test job
srun -p partition-1 --nodes=1 hostname
```

## Delete the cluster and clean resources

After you have successfully tested creating a SageMaker HyperPod cluster, it continues
running in the `InService` state until you delete the cluster. We
recommend that you delete any clusters created using on-demand SageMaker AI capacity when
not in use to avoid incurring continued service charges based on on-demand pricing.
In this tutorial, you have created a cluster that consists of three instance groups.
Make sure you delete the cluster by running the following command.

```
aws sagemaker delete-cluster --cluster-name `my-hyperpod-cluster`
```

To clean up the lifecycle scripts from the Amazon S3 bucket used for this tutorial, go
to the Amazon S3 bucket you used during cluster creation and remove the files
entirely.

```
aws s3 rm s3://sagemaker-`<unique-s3-bucket-name>/<lifecycle-script-directory>/src` --recursive
```

If you have tested running any model training workloads on the cluster, also check
if you have uploaded any data or if your job has saved any artifacts to different
Amazon S3 buckets or file system services such as Amazon FSx for Lustre and Amazon Elastic File System. To
prevent incurring charges, delete all artifacts and data from the storage or file
system.

## Related

topics

- [SageMaker HyperPod Slurm configuration](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration")
- [Customizing SageMaker HyperPod
  clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md")
- [FSx configuration via InstanceStorageConfigs](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-fsx-config "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-fsx-config")
- [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md")
