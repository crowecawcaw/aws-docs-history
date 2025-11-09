# SageMaker HyperPod cluster management

The following topics discuss logging and managing SageMaker HyperPod clusters.

## Logging SageMaker HyperPod events

All events and logs from SageMaker HyperPod are saved to Amazon CloudWatch under the log group name
`/aws/sagemaker/Clusters/[ClusterName]/[ClusterID]`. Every call to the
`CreateCluster` API creates a new log group. The following list contains
all of the available log streams collected in each log group.

|                                                     |                                                       |
| --------------------------------------------------- | ----------------------------------------------------- |
| **Log Group Name**                                  | **Log Stream Name**                                   |
| `/aws/sagemaker/Clusters/[ClusterName]/[ClusterID]` | `LifecycleConfig/[instance-group-name]/[instance-id]` |

## Logging SageMaker HyperPod at instance level

You can access the LifecycleScript logs published to CloudWatch during cluster
instance configuration. Every instance within the created cluster generates a separate
log stream, distinguishable by the
`LifecycleConfig/[instance-group-name]/[instance-id]` format.

All logs that are written to `/var/log/provision/provisioning.log` are
uploaded to the preceding CloudWatch stream. Sample LifecycleScripts at [`1.architectures/5.sagemaker_hyperpods/LifecycleScripts/base-config`](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config")
redirect their `stdout` and `stderr` to this location. If you are
using your custom scripts, write your logs to the
`/var/log/provision/provisioning.log` location for them to be available
in CloudWatch.

## Tagging resources

AWS Tagging system helps manage, identify, organize, search for, and filter
resources. SageMaker HyperPod supports tagging, so you can manage the clusters as an AWS
resource. During cluster creation or editing an existing cluster, you can add or edit
tags for the cluster. To learn more about tagging in general, see [Tagging your
AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

### Using the SageMaker HyperPod console UI

When you are [creating a new cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-create-cluster "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-create-cluster") and [editing a
cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters"), you can add, remove, or edit tags.

### Using the SageMaker HyperPod APIs

When you write a [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
or [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")
API request file in JSON format, edit the `Tags` section.

### Using the

AWS CLI tagging commands for SageMaker AI

**To tag a cluster**

Use [`aws sagemaker add-tags`](../../../cli/latest/reference/sagemaker/add-tags.md "../../../cli/latest/reference/sagemaker/add-tags.md") as follows.

```
aws sagemaker add-tags --resource-arn `cluster_ARN` --tags Key=`string`,Value=`string`
```

**To untag a cluster**

Use [`aws sagemaker delete-tags`](../../../cli/latest/reference/sagemaker/delete-tags.md "../../../cli/latest/reference/sagemaker/delete-tags.md") as follows.

```
aws sagemaker delete-tags --resource-arn `cluster_ARN` --tag-keys `"tag_key"`
```

**To list tags for a resource**

Use [`aws sagemaker list-tags`](../../../cli/latest/reference/sagemaker/list-tags.md "../../../cli/latest/reference/sagemaker/list-tags.md") as follows.

```
aws sagemaker list-tags --resource-arn `cluster_ARN`
```
