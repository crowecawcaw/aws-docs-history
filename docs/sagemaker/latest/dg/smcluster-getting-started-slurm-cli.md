

# Getting started with SageMaker HyperPod using the AWS CLI
<a name="smcluster-getting-started-slurm-cli"></a>

The following tutorial demonstrates how to create a new SageMaker HyperPod cluster with Slurm through the [AWS CLI commands for SageMaker HyperPod](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-cli). By the end of this tutorial, you will have a working Slurm cluster with a controller node, a login node, and a compute worker group, ready to schedule and run ML workloads. The tutorial covers Slurm topology setup, node lifecycle configuration options, optional FSx shared storage, and how to connect to your cluster.

Before starting, ensure you have completed the [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md) (VPC, quotas, FSx) and [AWS Identity and Access Management for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md) (IAM roles, execution role with `AmazonSageMakerClusterInstanceRolePolicy`).

## Key concepts
<a name="smcluster-getting-started-slurm-cli-key-concepts"></a>

This section covers the core configuration concepts for creating a SageMaker HyperPod Slurm cluster. Understanding these concepts will help you make informed choices when configuring your cluster, but if you want to get started immediately you can jump directly to [Create your cluster](#smcluster-getting-started-slurm-cli-create-cluster) and refer back here as needed.

When creating a Slurm-orchestrated cluster, you make two independent configuration choices:

1. **Slurm topology configuration** – How is the Slurm cluster topology (node roles, partitions) defined?

1. **Node lifecycle configuration** – How are nodes provisioned and customized?

For Slurm topology, this tutorial uses the API-driven configuration approach, where you define node roles and partitions directly in the `CreateCluster` request using `SlurmConfig` on each instance group and `Orchestrator.Slurm` at the cluster level. This is the recommended approach for new clusters. It provides a single source of truth, built-in validation, and partition configuration drift detection with no additional files to manage. Alternatively, you can use a legacy `provisioning_parameters.json` file stored in Amazon S3 for backward compatibility with existing clusters. For details on the legacy approach, see [SageMaker HyperPod Slurm configuration](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration).

For node lifecycle configuration, SageMaker HyperPod supports three options. In the simplest case you omit `LifeCycleConfig` entirely and HyperPod automatically configures nodes using AMI-based configuration, setting up Slurm and essential packages such as Docker, Enroot, and Pyxis for running ML workloads, with no scripts or Amazon S3 bucket required. If you need customizations on top of the AMI-based configuration, you can provide an extension script via `OnInitComplete` that runs after the configuration completes. For full control over the entire provisioning sequence, the `OnCreate` path lets your scripts own everything, including when Slurm starts.

For ML workloads you will typically also need a shared high-performance filesystem for training data, checkpoints, and shared libraries. SageMaker HyperPod supports Amazon FSx for Lustre and FSx for OpenZFS, configured per instance group via `InstanceStorageConfigs`. FSx configuration is optional for cluster creation but recommended for production workloads.

### Configuring Slurm topology via the API
<a name="smcluster-getting-started-slurm-cli-slurm-topology"></a>

All examples in this tutorial use API-driven Slurm topology configuration, where you define the Slurm cluster structure directly in the `CreateCluster` API request rather than through a separate configuration file.

A Slurm cluster requires at least a controller node (which runs the `slurmctld` daemon and coordinates job scheduling) and one or more compute nodes (which execute jobs). Optionally, you can add a login node to provide users with a dedicated access point for submitting and managing jobs without logging into the controller directly. In the API request, you assign each instance group its Slurm role using `SlurmConfig`, specifying whether the group serves as the controller, login, or compute node. Compute groups are also mapped to one or more Slurm partitions, which act as logical queues that organize how jobs are scheduled across different sets of nodes.

At the cluster level, `Orchestrator.Slurm` controls how HyperPod manages the partition configuration in `slurm.conf`. You choose a strategy that determines whether HyperPod is the single source of truth for partition topology, whether it overwrites manual changes, or whether it merges API-defined configuration with any manual edits you've made. Here is a reference for the fields used.

**SlurmConfig** (per instance group):

```
"SlurmConfig": {
    "NodeType": "Controller | Login | Compute",
    "PartitionNames": ["partition-name"]
}
```


| Field | Description | 
| --- | --- | 
| NodeType | Required. The Slurm role for this instance group. Valid values: Controller, Login, Compute. Exactly one instance group must be Controller. | 
| PartitionNames | Conditional. Slurm partition names. Required for Compute node type; not allowed for Controller or Login. | 

**Orchestrator.Slurm** (cluster level):

```
"Orchestrator": {
    "Slurm": {
        "SlurmConfigStrategy": "Managed | Overwrite | Merge"
    }
}
```

`SlurmConfigStrategy` determines how HyperPod manages the partition-to-node mappings in `slurm.conf` on the controller node. When you create or update a cluster, HyperPod writes the partition configuration to `slurm.conf` based on the `SlurmConfig` you defined on each instance group, mapping compute instance groups to their assigned partitions and registering controller and login nodes with the appropriate Slurm roles.

The strategy you choose controls what happens when the partition configuration in `slurm.conf` has been modified outside of the API, for example, by an administrator editing the file directly on the controller node. With `Managed`, HyperPod treats the API as the single source of truth and will detect and block updates if `slurm.conf` on disk has drifted. With `Overwrite`, HyperPod forces the API-defined configuration onto the controller, discarding any manual edits to `slurm.conf`. This is useful for recovering from an unintended change. With `Merge`, HyperPod preserves manual edits to `slurm.conf` and merges them with the API configuration, giving advanced users the flexibility to maintain custom `slurm.conf` settings alongside API-managed partitions.


| Strategy | Partition drift detection | Manual changes | Use case | 
| --- | --- | --- | --- | 
| Managed (default) | Enabled; blocks updates if drift found | Not supported | Single source of truth | 
| Overwrite | Disabled | Overwritten on update | Recovery from drift | 
| Merge | Disabled | Preserved and merged | Custom slurm.conf needs | 

**Important**  
Drift detection applies only to Slurm partition configuration in `slurm.conf` (partition-to-node mappings defined through the API). Changes to other `slurm.conf` settings, such as scheduling parameters, resource limits, or accounting configuration, are not monitored and will not be detected or reported by HyperPod.

**Note**  
If you prefer to define Slurm topology using a `provisioning_parameters.json` file instead of the API, omit `SlurmConfig` from instance groups and `Orchestrator.Slurm` from the cluster request, and upload the file to Amazon S3 alongside your node lifecycle scripts. For details, see [SageMaker HyperPod Slurm configuration](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration).

### Node lifecycle configuration options
<a name="smcluster-getting-started-slurm-cli-lifecycle-options"></a>

When creating a SageMaker HyperPod Slurm cluster, you choose how each instance group's nodes are provisioned by configuring the `LifeCycleConfig` block in the `CreateCluster` request. SageMaker HyperPod supports three node lifecycle configuration options, each offering a different level of control over the provisioning process.

With **AMI-based configuration** only, you omit `LifeCycleConfig` entirely. HyperPod automatically configures nodes using AMI-based configuration, setting up Slurm, installing essential packages, and starting all required services. This is the simplest path and requires no Amazon S3 bucket or scripts.

With the **Extension** option, you specify `OnInitComplete` in `LifeCycleConfig` along with a `SourceS3Uri` pointing to your extension script in Amazon S3. HyperPod runs the full AMI-based configuration first, then executes your script. This lets you add customizations, such as monitoring agents, LDAP integration, or additional storage mounts, without managing the baseline provisioning.

With the **Custom** option, you specify `OnCreate` in `LifeCycleConfig` along with a `SourceS3Uri` pointing to your full lifecycle script set in Amazon S3. HyperPod does not run AMI-based configuration and does not start Slurm. Your scripts own the entire provisioning sequence. This gives you complete control over what software is installed, how it is configured, and when Slurm starts.


| Node lifecycle option | Amazon S3 bucket needed? | Scripts to upload? | LifeCycleConfig in API? | 
| --- | --- | --- | --- | 
| AMI-based configuration only (simplest) | No | No | Omit entirely | 
| Extension (OnInitComplete) | Yes | Only your extension script | OnInitComplete \+ SourceS3Uri | 
| Custom (OnCreate) | Yes | Full lifecycle script set | OnCreate \+ SourceS3Uri | 

**Note**  
Optional node lifecycle configuration is supported only for Slurm-orchestrated clusters. Amazon EKS-orchestrated clusters continue to require `LifeCycleConfig` with `OnCreate` and `SourceS3Uri` on every instance group.

**Note**  
`OnCreate` and `OnInitComplete` are mutually exclusive. Specifying both on the same instance group results in a validation error.

### FSx and VPC configuration
<a name="smcluster-getting-started-slurm-cli-fsx-vpc"></a>

For ML workloads, a shared high-performance filesystem is essential for storing training data, model checkpoints, and shared libraries across cluster nodes. SageMaker HyperPod supports Amazon FSx for Lustre and FSx for OpenZFS, configured per instance group via `InstanceStorageConfigs`. FSx filesystems reside in your VPC, so a custom VPC configuration (`VpcConfig`) is required when using FSx.

FSx configuration works with all three node lifecycle configuration options. When using AMI-based configuration or `OnInitComplete`, HyperPod handles FSx mounting automatically. When using `OnCreate`, your lifecycle scripts are responsible for mounting.

**FSx for Lustre:**

```
"InstanceStorageConfigs": [
    {
        "FsxLustreConfig": {
            "DnsName": "fs-0abc123def456789.fsx.us-west-2.amazonaws.com",
            "MountPath": "/fsx",
            "MountName": "abcdefgh"
        }
    }
]
```


| Field | Description | 
| --- | --- | 
| DnsName | Required. The DNS name of the FSx for Lustre filesystem. | 
| MountPath | Optional. The local mount path on the instance. Default: /fsx | 
| MountName | Required. The mount name of the FSx for Lustre filesystem. Find this in the FSx for Lustre console or via aws fsx describe-file-systems. | 

**FSx for OpenZFS:**

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


| Field | Description | 
| --- | --- | 
| DnsName | Required. The DNS name of the FSx for OpenZFS filesystem. | 
| MountPath | Optional. The local mount path on the instance. Default: /home | 

**Note**  
Each instance group can have at most one FSx for Lustre and one FSx for OpenZFS configuration. Different instance groups can mount different filesystems.

**VPC configuration** (required for FSx):

Add `VpcConfig` at the cluster level in your `CreateCluster` request:

```
"VpcConfig": {
    "SecurityGroupIds": ["sg-0abc123def456789a"],
    "Subnets": ["subnet-0abc123def456789a"]
}
```

For more information on setting up a VPC, see [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md). For more information on FSx setup, see [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md).

## Create your cluster
<a name="smcluster-getting-started-slurm-cli-create-cluster"></a>

This section walks you through creating a cluster using each of the three node lifecycle configuration options described in [Node lifecycle configuration options](#smcluster-getting-started-slurm-cli-lifecycle-options). For most users, we recommend starting with **Option A**, AMI-based configuration only. It requires no scripts or Amazon S3 bucket and delivers a fully functional cluster out of the box. Choose Option B if you need to add customizations on top of the AMI-based configuration, or Option C if you need full control over the provisioning process.

For `ExecutionRole` in all examples, provide the ARN of the IAM role you created with the managed `AmazonSageMakerClusterInstanceRolePolicy` in [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md).

### Option A: AMI-based configuration only (without lifecycle configuration)
<a name="smcluster-getting-started-slurm-cli-option-a"></a>

This is the simplest path. No Amazon S3 bucket, scripts, or configuration files are needed. SageMaker HyperPod configures nodes automatically using AMI-based configuration, installing essential software and applying configurations so the cluster is ready to run ML workloads out of the box. All software packages are embedded in the AMI, so no internet access is required during provisioning.

The following table lists the capabilities included in AMI-based configuration:


| Capability | Description | 
| --- | --- | 
| Slurm daemons | Controller and compute daemons started automatically | 
| Docker | Container runtime for building and running ML containers | 
| Enroot | Rootless container execution for Slurm workloads | 
| Pyxis | Slurm plugin for container integration | 
| Slurm accounting | Configures Slurm job accounting for tracking job history and resource consumption | 
| MariaDB | Deploys MariaDB on the controller node as the backing database for Slurm accounting | 
| SSH key generation | Key pair generated for default ubuntu user | 
| SSH propagation | User credentials propagated across compute nodes for multi-node jobs | 
| Slurm log rotation | Prevents log bloat and disk-full issues | 
| Home directory setup | Ubuntu user home directory mounted to shared filesystem | 

1. Save the following as `create_cluster.json`:

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
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole",
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
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole"
           },
           {
               "InstanceGroupName": "worker-group-1",
               "InstanceType": "ml.trn1.32xlarge",
               "InstanceCount": 1,
               "SlurmConfig": {
                   "NodeType": "Compute",
                   "PartitionNames": ["partition-1"]
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole",
               "InstanceStorageConfigs": [
                   {
                       "FsxLustreConfig": {
                           "DnsName": "{{fs-0abc123def456789.fsx.us-west-2.amazonaws.com}}",
                           "MountPath": "/fsx",
                           "MountName": "{{abcdefgh}}"
                       }
                   }
               ]
           }
       ],
       "Orchestrator": {
           "Slurm": {
               "SlurmConfigStrategy": "Managed"
           }
       },
       "VpcConfig": {
           "SecurityGroupIds": ["{{sg-0abc123def456789a}}"],
           "Subnets": ["{{subnet-0abc123def456789a}}"]
       }
   }
   ```

   Notice that no `LifeCycleConfig` is specified on any instance group.

   The Slurm topology is defined through `SlurmConfig` on each instance group: `my-controller-group` is assigned the `Controller` role (runs `slurmctld`), `my-login-group` serves as the `Login` node for user access, and `worker-group-1` is a `Compute` node assigned to `partition-1` for job scheduling. At the cluster level, `SlurmConfigStrategy: "Managed"` ensures HyperPod is the single source of truth for partition configuration. The worker group includes an FSx for Lustre filesystem mounted at `/fsx` for shared storage, and `VpcConfig` is specified at the cluster level as required for FSx.
**Tip**  
If you are testing without FSx, you can omit `FsxLustreConfig` from `InstanceStorageConfigs` and remove `VpcConfig` from the request. FSx is not required for cluster creation, but is recommended for production ML workloads.

1. Create the cluster:

   ```
   aws sagemaker create-cluster \
       --cli-input-json {{file://create_cluster.json}}
   ```

1. Check the status:

   ```
   aws sagemaker describe-cluster --cluster-name {{my-hyperpod-cluster}}
   ```

   With AMI-based configuration only, instance groups in the response do not include a `LifeCycleConfig` block. The following is a truncated example showing the controller instance group:

   ```
   {
       "ClusterName": "my-hyperpod-cluster",
       "ClusterStatus": "InService",
       "InstanceGroups": [
           {
               "InstanceGroupName": "my-controller-group",
               "SlurmConfig": { "NodeType": "Controller" }
           }
       ]
   }
   ```

   After the status turns to **InService**, proceed to [Connect to your cluster](#smcluster-getting-started-slurm-cli-connect).

### Option B: Extend AMI-based configuration with OnInitComplete
<a name="smcluster-getting-started-slurm-cli-option-b"></a>

Use this option when you need customizations on top of the AMI-based configuration, such as monitoring agents, LDAP/SSSD integration, or additional storage mounts. SageMaker HyperPod runs AMI-based configuration first, then executes your extension script.

1. Write your extension script. For example, `extend-defaults.sh`:

   ```
   #!/bin/bash
   set -e
   
   echo "Running post-initialization customizations..."
   
   # Example: Install a monitoring agent
   # apt-get install -y my-monitoring-agent
   
   # Example: Configure LDAP integration
   # /opt/custom/setup-ldap.sh
   
   # Example: Mount an additional S3 bucket
   # mount-s3 my-data-bucket /mnt/s3-data
   
   echo "Custom extensions complete."
   ```
**Using extension scripts from the Awsome Distributed Training repository**  
The [Extensions folder](https://github.com/awslabs/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/Extensions) in the Awsome Distributed Training repository provides ready-to-use extension scripts for common tasks such as adding users and enabling observability. Each capability is self-contained in its own directory with its own entry point script that can be provided directly as the `OnInitComplete` script.  
For clusters that need multiple capabilities, we recommend using the `run_extensions.sh` script available at the top level of the Extensions folder. This script orchestrates all available extension scripts and provides simple boolean toggles to enable or disable each capability. To use it, upload the entire Extensions folder to your Amazon S3 bucket and specify `run_extensions.sh` as the `OnInitComplete` script:  

   ```
   s3://<bucket>/<prefix>/
   |-- run_extensions.sh          (OnInitComplete target)
   |-- detect-node/               (node type detection utility)
   |-- add-users/                 (user management scripts + config)
   |-- observability/             (observability scripts + config)
   ```
Inside `run_extensions.sh`, enable or disable each capability by setting the corresponding flag:  

   ```
   ENABLE_ADD_USERS="true"
   ENABLE_OBSERVABILITY="true"
   ```
Each enabled capability's configuration file must be populated before uploading to Amazon S3. Refer to the README in each capability's directory for configuration details.

1. Upload to Amazon S3 (bucket path must start with `s3://sagemaker-`):

   ```
   aws s3 cp extend-defaults.sh \
       s3://sagemaker-{{amzn-s3-demo-bucket}}/scripts/
   ```

1. Save the following as `create_cluster.json`:

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
                   "OnInitComplete": "extend-defaults.sh",
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/scripts/"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole",
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
                   "OnInitComplete": "extend-defaults.sh",
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/scripts/"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole"
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
                   "OnInitComplete": "extend-defaults.sh",
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/scripts/"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole"
           }
       ],
       "Orchestrator": {
           "Slurm": {
               "SlurmConfigStrategy": "Managed"
           }
       }
   }
   ```
**Important**  
When `OnInitComplete` is specified, `SourceS3Uri` is required. `OnCreate` and `OnInitComplete` cannot be used together on the same instance group.
**Tip**  
You can mix options within a cluster. For example, use AMI-based configuration only on the controller and `OnInitComplete` on the workers.

   The Slurm topology is the same as in Option A. Each instance group has a `SlurmConfig` defining its node role and partition assignment, and `SlurmConfigStrategy: "Managed"` is set at the cluster level. The only difference is the addition of `LifeCycleConfig` with `OnInitComplete`, which tells HyperPod to run your extension script after AMI-based configuration completes on each node. To add FSx, include `FsxLustreConfig` or `FsxOpenZfsConfig` in `InstanceStorageConfigs` on the relevant instance groups and add `VpcConfig` at the cluster level, as described in [FSx and VPC configuration](#smcluster-getting-started-slurm-cli-fsx-vpc).

1. Create the cluster:

   ```
   aws sagemaker create-cluster \
       --cli-input-json {{file://create_cluster.json}}
   ```

1. Check the status:

   ```
   aws sagemaker describe-cluster --cluster-name {{my-hyperpod-cluster}}
   ```

   With `OnInitComplete`, the response shows `OnInitComplete` in the `LifeCycleConfig`. The following is a truncated example showing the controller instance group:

   ```
   {
       "ClusterName": "my-hyperpod-cluster",
       "ClusterStatus": "InService",
       "InstanceGroups": [
           {
               "InstanceGroupName": "my-controller-group",
               "SlurmConfig": { "NodeType": "Controller" },
               "LifeCycleConfig": {
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/scripts/",
                   "OnInitComplete": "extend-defaults.sh"
               }
           }
       ]
   }
   ```

   After the status turns to **InService**, proceed to [Connect to your cluster](#smcluster-getting-started-slurm-cli-connect).

### Option C: Full custom control with OnCreate (advanced)
<a name="smcluster-getting-started-slurm-cli-option-c"></a>

Use this option when you need complete control over provisioning, including installing software, making infrastructure changes, and deciding when to start Slurm. With `OnCreate`, SageMaker HyperPod does **not** run AMI-based configuration and does **not** start Slurm automatically.

**Note**  
If you are new to SageMaker HyperPod and do not have specific customization requirements, we recommend starting with Option A or Option B. You can always migrate to custom mode later.

1. Prepare and upload lifecycle scripts to Amazon S3. If starting from scratch, use the sample scripts from the [Awsome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/):

   ```
   git clone https://github.com/aws-samples/awsome-distributed-training/
   cd awsome-distributed-training/1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config
   ```

   Upload to Amazon S3 (bucket path must start with `s3://sagemaker-`):

   ```
   aws s3 sync . \
       s3://sagemaker-{{amzn-s3-demo-bucket}}/lifecycle/src
   ```

   To learn more about the lifecycle scripts, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

1. Save the following as `create_cluster.json`:

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
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/lifecycle/src",
                   "OnCreate": "on_create.sh"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole",
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
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/lifecycle/src",
                   "OnCreate": "on_create.sh"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole"
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
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/lifecycle/src",
                   "OnCreate": "on_create.sh"
               },
               "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/HyperPodExecutionRole"
           }
       ],
       "Orchestrator": {
           "Slurm": {
               "SlurmConfigStrategy": "Managed"
           }
       }
   }
   ```

   The Slurm topology follows the same `SlurmConfig` pattern as the other options. The key difference is `LifeCycleConfig` with `OnCreate`. This tells HyperPod to skip AMI-based configuration entirely and run your `on_create.sh` script instead. Your scripts are responsible for the full provisioning sequence, including installing software, configuring Slurm, and starting the Slurm daemons. To add FSx, include `FsxLustreConfig` or `FsxOpenZfsConfig` in `InstanceStorageConfigs` on the relevant instance groups and add `VpcConfig` at the cluster level, as described in [FSx and VPC configuration](#smcluster-getting-started-slurm-cli-fsx-vpc).

1. Create the cluster:

   ```
   aws sagemaker create-cluster \
       --cli-input-json {{file://create_cluster.json}}
   ```

1. Check the status:

   ```
   aws sagemaker describe-cluster --cluster-name {{my-hyperpod-cluster}}
   ```

   With `OnCreate`, the response shows `OnCreate` in the `LifeCycleConfig`. The following is a truncated example showing the controller instance group:

   ```
   {
       "ClusterName": "my-hyperpod-cluster",
       "ClusterStatus": "InService",
       "InstanceGroups": [
           {
               "InstanceGroupName": "my-controller-group",
               "SlurmConfig": { "NodeType": "Controller" },
               "LifeCycleConfig": {
                   "SourceS3Uri": "s3://sagemaker-{{amzn-s3-demo-bucket}}/lifecycle/src",
                   "OnCreate": "on_create.sh"
               }
           }
       ]
   }
   ```

   After the status turns to **InService**, proceed to [Connect to your cluster](#smcluster-getting-started-slurm-cli-connect).

### Common validation errors
<a name="smcluster-getting-started-slurm-cli-validation-errors"></a>


| Error | Resolution | 
| --- | --- | 
| "Cluster must have exactly one InstanceGroup with Controller node type" | Ensure exactly one instance group has SlurmConfig.NodeType: "Controller" | 
| "Partitions can only be assigned to Compute node types" | Remove PartitionNames from Controller or Login instance groups | 
| "FSx configurations are only supported for Custom VPC" | Add VpcConfig to your request when using FSx | 
| "LifeCycleConfig is required for instance group..." | EKS clusters. Optional node lifecycle configuration is not supported. | 
| "OnCreate and OnInitComplete in LifeCycleConfig are mutually exclusive..." | Remove either OnCreate or OnInitComplete. You cannot specify both. | 
| "LifeCycleConfig for instance group is incomplete..." | When OnCreate or OnInitComplete is specified, SourceS3Uri must also be provided. | 
| "LifeCycleConfig is optional but requires a compatible AMI..." | Run UpdateClusterSoftware to update to an AMI that supports optional node lifecycle configuration. | 
| "LifeCycleConfig for instance group is provided but contains no configuration..." | Specify SourceS3Uri with OnCreate or OnInitComplete, or omit LifeCycleConfig entirely. | 

## Connect to your cluster
<a name="smcluster-getting-started-slurm-cli-connect"></a>

After the cluster status turns to **InService** (typically 10 to 15 minutes), connect and verify.

1. List cluster nodes to get instance IDs:

   ```
   aws sagemaker list-cluster-nodes --cluster-name {{my-hyperpod-cluster}}
   ```

1. Connect using AWS Systems Manager Session Manager:

   ```
   aws ssm start-session \
       --target sagemaker-cluster:{{my-hyperpod-cluster}}_{{my-login-group}}-{{i-0abc123def456789b}} \
       --region {{us-west-2}}
   ```

1. Verify Slurm is configured correctly:

   ```
   # Check Slurm nodes
   sinfo
   
   # Check Slurm partitions
   sinfo -p partition-1
   
   # Submit a test job
   srun -p partition-1 --nodes=1 hostname
   ```

For more information about running ML workloads, see [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md).

## Delete the cluster and clean resources
<a name="smcluster-getting-started-slurm-cli-delete-cluster-and-clean"></a>

After testing, delete the cluster to avoid continued charges:

```
aws sagemaker delete-cluster --cluster-name {{my-hyperpod-cluster}}
```

If you used node lifecycle scripts (Option B or Option C), clean up the Amazon S3 bucket:

```
aws s3 rm s3://sagemaker-{{amzn-s3-demo-bucket}}/{{lifecycle/src}} --recursive
```

If you used AMI-based configuration only (Option A), no Amazon S3 cleanup is needed for node lifecycle scripts.

If you ran training workloads, also check for data or artifacts in Amazon S3, Amazon FSx for Lustre, or Amazon Elastic File System and delete them to prevent charges.

## Related topics
<a name="smcluster-getting-started-slurm-cli-related-topics"></a>
+ [SageMaker HyperPod Slurm configuration](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-configuration)
+ [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md)
+ [FSx configuration via InstanceStorageConfigs](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-slurm-fsx-config)
+ [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md)
+ [Extension scripts for SageMaker HyperPod](https://github.com/awslabs/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/Extensions)
+ [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md)