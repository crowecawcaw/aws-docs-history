

# Migrating to API-driven Slurm configuration
<a name="sagemaker-hyperpod-slurm-api-config-migration"></a>

If you have an existing SageMaker HyperPod Slurm cluster that uses the legacy `provisioning_parameters.json` file for Slurm configuration, you can migrate to the API-driven configuration model. With API-driven configuration, you define Slurm node types, partition assignments, and Amazon FSx mounting directly in the [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) and [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) API payloads, removing the need to manage a separate configuration file in Amazon S3.

**Topics**
+ [Before you begin](#sagemaker-hyperpod-slurm-api-config-migration-before-you-begin)
+ [Clusters with multiple controller nodes (multi-head)](#sagemaker-hyperpod-slurm-api-config-migration-multihead)
+ [What changes during migration](#sagemaker-hyperpod-slurm-api-config-migration-what-changes)
+ [Step 1: Back up your current configuration](#sagemaker-hyperpod-slurm-api-config-migration-step1)
+ [Step 2: Upgrade the cluster software](#sagemaker-hyperpod-slurm-api-config-migration-step2)
+ [Step 3: Map your legacy configuration to the API format](#sagemaker-hyperpod-slurm-api-config-migration-step3)
+ [Step 4: Remove provisioning\_parameters.json from Amazon S3](#sagemaker-hyperpod-slurm-api-config-migration-step4)
+ [Step 5: Apply the API-driven configuration](#sagemaker-hyperpod-slurm-api-config-migration-step5)
+ [Step 6: Verify the migration](#sagemaker-hyperpod-slurm-api-config-migration-step6)
+ [Recovering from a failed migration](#sagemaker-hyperpod-slurm-api-config-migration-recovery)
+ [Post-migration considerations](#sagemaker-hyperpod-slurm-api-config-migration-post)
+ [Troubleshooting](#sagemaker-hyperpod-slurm-api-config-migration-troubleshooting)
+ [Migration checklist](#sagemaker-hyperpod-slurm-api-config-migration-checklist)

## Before you begin
<a name="sagemaker-hyperpod-slurm-api-config-migration-before-you-begin"></a>

Before starting the migration, make sure the following prerequisites are met:
+ **Running jobs.** If you choose the default Slurm configuration strategy, `Merge`, running jobs are not affected by the migration. If you choose `Managed` or `Overwrite`, drain all Slurm partitions and wait for active jobs to complete. You can check the job queue by running `squeue` on the controller node. With any strategy, do not submit new jobs while the update is in progress. Keep the default `Merge` strategy for this migration. For more information, see [Choose a Slurm configuration strategy](#sagemaker-hyperpod-slurm-api-config-migration-strategy).
+ **AMI compatibility.** API-driven Slurm configuration requires a SageMaker HyperPod Amazon Machine Image (AMI) released in January 2026 or later. If your cluster already runs a qualifying AMI, you can skip [Step 2: Upgrade the cluster software](#sagemaker-hyperpod-slurm-api-config-migration-step2). Otherwise, upgrade the cluster software before proceeding.
+ **Custom VPC (if using Amazon FSx).** If your cluster mounts Amazon FSx for Lustre or Amazon FSx for OpenZFS filesystems, the cluster must use a custom VPC (specified through `VpcConfig` in the API payload). The platform-managed VPC cannot reach customer Amazon FSx resources.
+ **IAM permissions.** The IAM role used to call the SageMaker AI API must have permissions for `sagemaker:UpdateCluster` and `sagemaker:DescribeCluster`. The cluster execution role must have the managed [AmazonSageMakerClusterInstanceRolePolicy](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html) attached.
+ **Single-controller clusters only.** This migration guide applies to clusters with a single controller (head) node. If your cluster uses multiple controller nodes (multi-head configuration), see [Clusters with multiple controller nodes (multi-head)](#sagemaker-hyperpod-slurm-api-config-migration-multihead) before proceeding.

## Clusters with multiple controller nodes (multi-head)
<a name="sagemaker-hyperpod-slurm-api-config-migration-multihead"></a>

If your cluster is configured with multiple controller (head) nodes using the [SageMaker HyperPod multi-head node support](sagemaker-hyperpod-multihead-slurm.md), you cannot fully migrate to the API-driven configuration model at this time.

The multi-head node architecture relies on the `slurm_configurations` block in `provisioning_parameters.json` to configure several components that have no equivalent in the API-driven approach:

```
"slurm_configurations": {
    "slurm_database_secret_arn": "$SLURM_DB_SECRET_ARN",
    "slurm_database_endpoint": "$SLURM_DB_ENDPOINT_ADDRESS",
    "slurm_shared_directory": "/fsx",
    "slurm_database_user": "$DB_USER_NAME",
    "slurm_sns_arn": "$SLURM_SNS_FAILOVER_TOPIC_ARN"
}
```

The following table lists the fields in `slurm_configurations` and their role in the multi-head node architecture.


| Field | Purpose | API equivalent | 
| --- |--- |--- |
| slurm\_database\_secret\_arn | AWS Secrets Manager secret ARN for the external Slurm accounting database credentials | None | 
| slurm\_database\_endpoint | Amazon RDS for MariaDB endpoint for Slurm accounting data (job records, metering) | None | 
| slurm\_database\_user | Database user name for the Slurm accounting database | None | 
| slurm\_shared\_directory | Shared Amazon FSx for Lustre directory used by multiple controller nodes to replicate Slurm state and configuration | None | 
| slurm\_sns\_arn | Amazon SNS topic ARN for controller failover notifications (Slurm controller ON/OFF status changes) | None | 

These fields configure the external Slurm accounting database (`slurmdbd`), the shared filesystem for controller state replication, and the SNS-based failover notification mechanism. Together, they enable the automatic failover behavior between primary and backup controller nodes.

Because the API-driven `SlurmConfig` and `Orchestrator.Slurm` schema does not include parameters for these components, migrating a multi-head cluster to the API-driven approach would result in the loss of:
+ External Slurm accounting database connectivity (job history, metering data)
+ Automatic controller failover between primary and backup head nodes
+ SNS notifications for controller status changes

### What you can do
<a name="sagemaker-hyperpod-slurm-api-config-migration-multihead-options"></a>

If you have a multi-head node cluster and want to adopt parts of the API-driven approach, you have the following options:
+ **Continue using `provisioning_parameters.json`.** This is the recommended approach for multi-head clusters. The legacy configuration remains fully supported and there is no forced migration. Your cluster continues to operate as expected.
+ **Migrate to a single-controller cluster.** If you no longer require multi-head node high availability and are willing to give up the external accounting database and controller failover, you can restructure your cluster to use a single controller node and then follow the migration steps in this guide. This is a significant architectural change and should be evaluated carefully.

**Important**  
Do not remove `provisioning_parameters.json` from Amazon S3 on a multi-head node cluster. Doing so will break the external database configuration and controller failover mechanism, which can lead to cluster instability.

**Note**  
Support for multi-head node configuration parameters in the API-driven approach may be added in a future release. Check the [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md) for updates.

## What changes during migration
<a name="sagemaker-hyperpod-slurm-api-config-migration-what-changes"></a>

The following table summarizes what changes when you migrate from the legacy approach to API-driven configuration.


| Aspect | Before migration | After migration | 
| --- |--- |--- |
| Slurm node types | Defined in provisioning\_parameters.json | Defined in SlurmConfig within each instance group | 
| Partition mapping | Defined in provisioning\_parameters.json | Defined in SlurmConfig.PartitionNames | 
| Amazon FSx configuration | Defined in provisioning\_parameters.json | Defined in InstanceStorageConfigs per instance group | 
| Configuration storage | Customer-managed Amazon S3 bucket | Managed by HyperPod | 
| Update mechanism | Edit the Amazon S3 file, then call UpdateCluster | Single UpdateCluster API call, no Amazon S3 file | 
| Configuration strategy | Not applicable | Controlled by Orchestrator.Slurm.SlurmConfigStrategy (default Merge) | 

**Note**  
Migration does not change your cluster's instance types, instance counts, lifecycle scripts, or execution roles. Only the source of Slurm topology configuration changes.

**Note**  
If you plan to later migrate the cluster to continuous provisioning (`NodeProvisioningMode` set to `Continuous`), keep the default `Merge` strategy. Clusters using continuous provisioning support only the `Merge` behavior and reject `UpdateCluster` requests that set `SlurmConfigStrategy` explicitly.

## Step 1: Back up your current configuration
<a name="sagemaker-hyperpod-slurm-api-config-migration-step1"></a>

Before making any changes, create backups of your existing configuration.

Download `provisioning_parameters.json` from Amazon S3:

```
aws s3 cp s3://{{DOC-EXAMPLE-BUCKET}}/lifecycle-script-directory/src/provisioning_parameters.json ./backup/
```

**Note**  
If your instance groups use different `SourceS3Uri` locations, back up `provisioning_parameters.json` from each of them. In Step 4, you remove the file from every `SourceS3Uri` location, so make sure you have a backup of each copy before you proceed.

Export the current `slurm.conf` from the controller node:

```
aws ssm start-session --target {{mi-controller-instance-id}}

sudo cp /opt/slurm/etc/slurm.conf ~/slurm.conf.backup
```

Record your current instance groups:

```
aws sagemaker describe-cluster \
    --cluster-name {{my-hyperpod-cluster}} \
    --query "InstanceGroups[*].{Name:InstanceGroupName,Type:InstanceType,Count:CurrentCount}"
```

Keep these backups available throughout the migration process. You need them if you need to recover from a failed migration.

## Step 2: Upgrade the cluster software
<a name="sagemaker-hyperpod-slurm-api-config-migration-step2"></a>

API-driven Slurm configuration requires a SageMaker HyperPod AMI released in January 2026 or later. If your cluster already runs a qualifying AMI, skip this step. Otherwise, upgrade the cluster software first.

**Important**  
Before you upgrade the cluster software, update the lifecycle scripts in your Amazon S3 bucket to the latest version of the [HyperPod sample lifecycle scripts](https://github.com/awslabs/awsome-distributed-ai/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config) on the GitHub website, keeping any custom setup steps you have added. `UpdateClusterSoftware` re-runs your lifecycle scripts on the new AMI, and scripts based on older versions of the samples can fail on newer AMIs, which causes the upgrade to fail. If your scripts are already based on a recent version, no change is needed.

**Important**  
`UpdateClusterSoftware` replaces instance root volumes with the updated AMI. Back up any data stored on root volumes to Amazon S3 or Amazon FSx before running this command. For more information, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software).

```
aws sagemaker update-cluster-software \
    --cluster-name {{my-hyperpod-cluster}}
```

Wait for the update to complete:

```
aws sagemaker describe-cluster \
    --cluster-name {{my-hyperpod-cluster}} \
    --query "ClusterStatus"
```

Proceed to the next step when the cluster status returns to `InService`.

## Step 3: Map your legacy configuration to the API format
<a name="sagemaker-hyperpod-slurm-api-config-migration-step3"></a>

Convert the fields in your `provisioning_parameters.json` file to the corresponding API parameters.

### Field mapping reference
<a name="sagemaker-hyperpod-slurm-api-config-migration-step3-field-mapping"></a>

The following table maps each legacy `provisioning_parameters.json` field to its corresponding API parameter.


| Legacy field (`provisioning_parameters.json`) | API parameter | 
| --- |--- |
| controller\_group | Instance group with SlurmConfig.NodeType set to "Controller" | 
| login\_group | Instance group with SlurmConfig.NodeType set to "Login" | 
| worker\_groups[].instance\_group\_name | Instance group with SlurmConfig.NodeType set to "Compute" | 
| worker\_groups[].partition\_name | SlurmConfig.PartitionNames | 
| fsx\_dns\_name | InstanceStorageConfigs[].FsxLustreConfig.DnsName | 
| fsx\_mountname | InstanceStorageConfigs[].FsxLustreConfig.MountName | 
| No legacy field (mount directory, typically /fsx) | InstanceStorageConfigs[].FsxLustreConfig.MountPath | 

**Note**  
The `slurm_configurations` block used in multi-head node clusters (containing `slurm_database_secret_arn`, `slurm_database_endpoint`, `slurm_database_user`, `slurm_shared_directory`, and `slurm_sns_arn`) has no equivalent in the API-driven approach. If your `provisioning_parameters.json` includes this block, see [Clusters with multiple controller nodes (multi-head)](#sagemaker-hyperpod-slurm-api-config-migration-multihead) before proceeding.

### Example conversion
<a name="sagemaker-hyperpod-slurm-api-config-migration-step3-example"></a>

The following example shows a legacy `provisioning_parameters.json` file and the equivalent API-driven `UpdateCluster` request payload.

Legacy `provisioning_parameters.json`:

```
{
    "version": "1.0.0",
    "workload_manager": "slurm",
    "controller_group": "controller-machine",
    "login_group": "login-group",
    "worker_groups": [
        {
            "instance_group_name": "gpu-compute",
            "partition_name": "gpu-training"
        },
        {
            "instance_group_name": "cpu-compute",
            "partition_name": "cpu-batch"
        }
    ],
    "fsx_dns_name": "fs-0abc123def456789.fsx.us-west-2.amazonaws.com",
    "fsx_mountname": "abcdefgh"
}
```

Equivalent API-driven `UpdateCluster` request (`update_cluster_migration.json`):

```
{
    "ClusterName": "my-hyperpod-cluster",
    "InstanceGroups": [
        {
            "InstanceGroupName": "controller-machine",
            "InstanceType": "ml.c5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Controller"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://DOC-EXAMPLE-BUCKET/lifecycle-script-directory/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole",
            "InstanceStorageConfigs": [
                {
                    "EbsVolumeConfig": {
                        "VolumeSizeInGB": 500
                    }
                }
            ]
        },
        {
            "InstanceGroupName": "login-group",
            "InstanceType": "ml.m5.xlarge",
            "InstanceCount": 1,
            "SlurmConfig": {
                "NodeType": "Login"
            },
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://DOC-EXAMPLE-BUCKET/lifecycle-script-directory/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        },
        {
            "InstanceGroupName": "gpu-compute",
            "InstanceType": "ml.g5.12xlarge",
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
                }
            ],
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://DOC-EXAMPLE-BUCKET/lifecycle-script-directory/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        },
        {
            "InstanceGroupName": "cpu-compute",
            "InstanceType": "ml.c5.4xlarge",
            "InstanceCount": 2,
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["cpu-batch"]
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
                "SourceS3Uri": "s3://DOC-EXAMPLE-BUCKET/lifecycle-script-directory/src",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/HyperPodExecutionRole"
        }
    ],
    "Orchestrator": {
        "Slurm": {
            "SlurmConfigStrategy": "Merge"
        }
    }
}
```

Note the following about this conversion:
+ Each instance group includes a `SlurmConfig` block with the appropriate `NodeType` (`Controller`, `Login`, or `Compute`).
+ Partition names from `worker_groups[].partition_name` move to `SlurmConfig.PartitionNames` on the corresponding compute instance group.
+ Amazon FSx configuration moves from the top-level `fsx_dns_name` and `fsx_mountname` fields to `InstanceStorageConfigs.FsxLustreConfig` on each instance group that needs the filesystem mounted. With the API-driven approach, you can configure Amazon FSx per instance group rather than cluster-wide.
+ `SlurmConfigStrategy` is set to `Merge`, which is the default. This preserves any manual edits you have made to `slurm.conf` on the controller node and is required if you later migrate the cluster to continuous provisioning. For more information about configuration strategies, see [Choose a Slurm configuration strategy](#sagemaker-hyperpod-slurm-api-config-migration-strategy).

**Important**  
Make sure the `InstanceGroupName`, `InstanceType`, and `ExecutionRole` values match your existing cluster configuration. You can retrieve these values by running `aws sagemaker describe-cluster --cluster-name my-hyperpod-cluster`.

## Step 4: Remove provisioning\_parameters.json from Amazon S3
<a name="sagemaker-hyperpod-slurm-api-config-migration-step4"></a>

Removing the `provisioning_parameters.json` file from Amazon S3 signals HyperPod to use the API-driven configuration instead of the legacy file-based approach.

```
aws s3 rm s3://{{DOC-EXAMPLE-BUCKET}}/lifecycle-script-directory/src/provisioning_parameters.json
```

Verify the file has been removed:

```
aws s3 ls s3://{{DOC-EXAMPLE-BUCKET}}/lifecycle-script-directory/src/
```

If your instance groups use different `SourceS3Uri` locations, remove the file from each of them.

**Important**  
HyperPod does not allow a cluster to use both `provisioning_parameters.json` and the API-driven `SlurmConfig`. Remove the file from Amazon S3 before you apply the API-driven configuration in [Step 5: Apply the API-driven configuration](#sagemaker-hyperpod-slurm-api-config-migration-step5). If the file is still present when you call `UpdateCluster`, the update fails and rolls back.

**Important**  
Make sure you have a local backup of `provisioning_parameters.json` before deleting it. You need this file if you need to recover from a failed migration.

## Step 5: Apply the API-driven configuration
<a name="sagemaker-hyperpod-slurm-api-config-migration-step5"></a>

Run the `UpdateCluster` API with the JSON request file you prepared in [Step 3: Map your legacy configuration to the API format](#sagemaker-hyperpod-slurm-api-config-migration-step3):

```
aws sagemaker update-cluster \
    --cli-input-json {{file://update_cluster_migration.json}}
```

Monitor the update progress:

```
aws sagemaker describe-cluster \
    --cluster-name {{my-hyperpod-cluster}} \
    --query "{Status: ClusterStatus, Message: FailureMessage}"
```

Wait for the cluster status to return to `InService` before proceeding. The update typically takes several minutes depending on the number of instance groups and nodes in your cluster.

## Step 6: Verify the migration
<a name="sagemaker-hyperpod-slurm-api-config-migration-step6"></a>

After the cluster status returns to `InService`, verify that the Slurm configuration was applied correctly.

**Check Slurm partitions.** Connect to the controller node using SSM Session Manager and verify the partition layout:

```
aws ssm start-session --target {{mi-controller-instance-id}}
```

```
sinfo
```

Expected output:

```
PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
dev*           up     infinite   6      idle  gpu-compute-[1-4],cpu-compute-[1-2]
gpu-training   up     infinite   4      idle  gpu-compute-[1-4]
cpu-batch      up     infinite   2      idle  cpu-compute-[1-2]
```

**Check node-to-partition assignments.**

```
scontrol show nodes | grep -E "NodeName|Partitions"
```

**Check Amazon FSx mounts (if configured).** On a compute node, verify the filesystem is mounted:

```
df -h | grep fsx
```

Expected output:

```
fs-0abc123def456789.fsx.us-west-2.amazonaws.com@tcp:/abcdefgh  1.2T  12G  1.2T  1% /fsx
```

**Submit a test job.**

```
sbatch --partition=gpu-training --wrap="hostname && nvidia-smi"
```

Check the job output:

```
squeue
cat slurm-*.out
```

## Recovering from a failed migration
<a name="sagemaker-hyperpod-slurm-api-config-migration-recovery"></a>

If the migration does not complete successfully, HyperPod automatically rolls back the cluster to its previous state. The cluster returns to `InService` and continues to use the legacy configuration.

To recover, restore `provisioning_parameters.json` to its original Amazon S3 location so that any new nodes provision with the legacy configuration:

```
aws s3 cp ./backup/provisioning_parameters.json \
    s3://{{DOC-EXAMPLE-BUCKET}}/lifecycle-script-directory/src/provisioning_parameters.json
```

Then review the failure reason, correct your request payload, and retry from [Step 4: Remove provisioning\_parameters.json from Amazon S3](#sagemaker-hyperpod-slurm-api-config-migration-step4):

```
aws sagemaker describe-cluster \
    --cluster-name {{my-hyperpod-cluster}} \
    --query "{Status: ClusterStatus, Message: FailureMessage}"
```

**Important**  
After a migration completes successfully, you cannot revert the cluster to the legacy `provisioning_parameters.json` configuration. Omitting `SlurmConfig` from a later `UpdateCluster` request does not revert the cluster; the existing API-driven Slurm configuration is preserved. Verify the migration ([Step 6: Verify the migration](#sagemaker-hyperpod-slurm-api-config-migration-step6)) before you delete your local backups.

## Post-migration considerations
<a name="sagemaker-hyperpod-slurm-api-config-migration-post"></a>

After a successful migration, consider the following updates to your environment.

### Simplify lifecycle scripts
<a name="sagemaker-hyperpod-slurm-api-config-migration-post-lifecycle"></a>

With API-driven configuration, HyperPod handles Slurm topology setup and Amazon FSx mounting automatically. You can remove the corresponding logic from your lifecycle scripts and keep only custom setup steps such as user creation, package installation, and environment configuration.

The following example shows a minimal `on_create.sh` lifecycle script for clusters using API-driven configuration:

```
#!/bin/bash
set -e

echo "=== HyperPod Lifecycle Script ==="
echo "Timestamp: $(date)"
echo "Hostname: $(hostname)"

# Custom setup only - Slurm configuration and FSx mounting
# are handled by HyperPod based on the API payload.

# Example: Install additional packages
# sudo apt-get update && sudo apt-get install -y htop vim

# Example: Create users
# sudo useradd -m -s /bin/bash researcher

# Example: Set environment variables
# echo 'export NCCL_DEBUG=INFO' >> /etc/profile.d/nccl.sh

echo "=== Lifecycle Script Completed ==="
```

### Update automation workflows
<a name="sagemaker-hyperpod-slurm-api-config-migration-post-automation"></a>

If you have automation scripts or CI/CD pipelines that modify `provisioning_parameters.json` in Amazon S3, update them to use the `UpdateCluster` API instead. Remove any Amazon S3 file management logic related to `provisioning_parameters.json`.

### Choose a Slurm configuration strategy
<a name="sagemaker-hyperpod-slurm-api-config-migration-strategy"></a>

After you migrate, you can choose a `SlurmConfigStrategy` that controls how HyperPod manages the relationship between the API-declared Slurm topology and the actual `slurm.conf` on the controller node. The strategy determines who owns the Slurm topology—you or the API.


| Strategy | Source of truth | Behavior | 
| --- |--- |--- |
| Merge (default) | slurm.conf | HyperPod adds API-declared partitions to slurm.conf without removing manual edits. Use this if you tune slurm.conf directly for advanced parameters the API does not expose. Required if you plan to migrate to continuous provisioning. | 
| Managed | API | HyperPod enforces the API-declared state and detects drift. If someone edits slurm.conf outside the API, the next UpdateCluster fails and rolls back, and DescribeCluster reports the drift in FailureMessage until it is resolved. | 
| Overwrite | API | HyperPod enforces the API-declared state unconditionally, overwriting any manual changes to slurm.conf. Use this for recovery scenarios or strict API governance. | 

You can change the strategy in a later `UpdateCluster` request by including `Orchestrator.Slurm.SlurmConfigStrategy`. Clusters that use continuous provisioning (`NodeProvisioningMode` set to `Continuous`) support only the `Merge` behavior and reject requests that set `SlurmConfigStrategy`. If you plan to migrate to continuous provisioning, keep `Merge`. For more information, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md).

**Tip**  
If you are unsure which strategy to use, start with `Merge`. It matches the behavior of the legacy approach and preserves any manual `slurm.conf` customizations. You can switch to `Managed` or `Overwrite` later as your operational practices evolve, unless you plan to migrate to continuous provisioning, which requires `Merge`.

## Troubleshooting
<a name="sagemaker-hyperpod-slurm-api-config-migration-troubleshooting"></a>

### "Update required to use SlurmConfig in InstanceGroups"
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-update-required"></a>

Your cluster AMI does not include the updated agents required for API-driven configuration. Upgrade the cluster software:

```
aws sagemaker update-cluster-software \
    --cluster-name {{my-hyperpod-cluster}}
```

Wait for the cluster to return to `InService`, then retry the migration.

### "N Controller Groups found: SlurmConfig for InstanceGroups may only have one Controller Group."
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-multiple-controllers"></a>

Your API payload specifies more than one instance group with `SlurmConfig.NodeType` set to `"Controller"`. Make sure exactly one instance group is the controller.

### "Cluster X has no InstanceGroup with Controller node type."
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-no-controller"></a>

Your API payload does not identify a controller instance group. Make sure exactly one instance group has `SlurmConfig.NodeType` set to `"Controller"`.

### "Partitions can only be assigned to Compute node types"
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-partitions-compute"></a>

You specified `PartitionNames` on a controller or login instance group. Remove `PartitionNames` from any instance group that is not a compute node.

### "The LifeCycleConfig cannot include both a SLURM Orchestrator Config and a provisioning\_parameters.json file simultaneously."
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-both-configs"></a>

The update workflow found `provisioning_parameters.json` in the lifecycle script location while your request included `SlurmConfig`. The update fails and rolls back, and `DescribeCluster` reports this message in `FailureMessage`. Complete [Step 4: Remove provisioning\_parameters.json from Amazon S3](#sagemaker-hyperpod-slurm-api-config-migration-step4), verify that no copy of the file remains under the `SourceS3Uri` prefix of any instance group, and retry `UpdateCluster`.

### Slurm partitions not updated after migration
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-partitions-not-updated"></a>

If `sinfo` does not show the expected partitions:

1. Check the Cluster Agent logs on the controller node:

   ```
   sudo journalctl -u cluster-agent
   ```

1. Verify that `SlurmConfig.PartitionNames` is specified for each compute instance group in your API payload.

1. If using the `Managed` strategy, check `DescribeCluster` `FailureMessage` for a drift error. A drift error fails and rolls back the update until the conflict is resolved. You can switch to `Overwrite` temporarily to force the API state, then switch back to `Managed`.

### Amazon FSx not mounted on nodes
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-fsx-not-mounted"></a>

Amazon FSx configuration changes only apply to new nodes. Existing nodes retain their original storage configuration. To apply Amazon FSx changes to all nodes in an instance group:

1. Scale the instance group down to 0 instances.

1. Scale the instance group back up with the new Amazon FSx configuration.

Also verify that your security groups allow the required ports:
+ Amazon FSx for Lustre: TCP ports 988, 1021–1023
+ Amazon FSx for OpenZFS: TCP port 2049

### "Configuration drift detected."
<a name="sagemaker-hyperpod-slurm-api-config-migration-ts-drift"></a>

Drift messages (for example, "Configuration drift detected.", "Partition configuration drift detected.", or "Partition configuration mismatch detected.") appear in the `FailureMessage` field of `DescribeCluster` after an `UpdateCluster` fails and rolls back. They occur when using the `Managed` strategy and HyperPod detects configuration drift—a mismatch between the API-declared configuration and the actual `slurm.conf` on the controller node. Drift occurs in the following cases:
+ A partition exists in `slurm.conf` that no `SlurmConfig` defines.
+ A node belongs to more than one partition.
+ A node is in a different partition than the API expects.

To resolve drift, use one of the following options:
+ **Option 1:** Switch to `Overwrite` strategy temporarily to force the API-declared state, then switch back to `Managed`.
+ **Option 2:** Switch to `Merge` strategy to preserve the manual edits.
+ **Option 3:** Connect to the controller node, manually revert the changes in `slurm.conf` to match the expected state, run `sudo scontrol reconfigure`, and retry the `UpdateCluster` call with `Managed`.

## Migration checklist
<a name="sagemaker-hyperpod-slurm-api-config-migration-checklist"></a>

Use this checklist to track your migration progress:
+ Verify your cluster is not using multi-head node configuration.
+ If your cluster mounts Amazon FSx, confirm it uses a custom VPC.
+ Back up `provisioning_parameters.json` from Amazon S3.
+ Back up `slurm.conf` from the controller node.
+ Document current instance groups and their configuration.
+ If using `Managed` or `Overwrite`, drain partitions and wait for jobs to complete (`squeue`).
+ Do not submit new jobs while the update is in progress.
+ Update lifecycle scripts to the latest sample version before upgrading cluster software.
+ Upgrade cluster software if the AMI predates January 2026 (`UpdateClusterSoftware`).
+ Prepare the API-driven `UpdateCluster` request payload.
+ Remove `provisioning_parameters.json` from every instance group's `SourceS3Uri` location and verify it is gone.
+ Run `UpdateCluster` with the new payload.
+ Verify Slurm partitions (`sinfo`).
+ Verify Amazon FSx mounts (`df -h`).
+ Submit test jobs to each partition.
+ Update lifecycle scripts to remove Slurm and Amazon FSx setup logic.
+ Update automation scripts and CI/CD pipelines.
+ Keep your `provisioning_parameters.json` and `slurm.conf` backups until Step 6 verification passes.