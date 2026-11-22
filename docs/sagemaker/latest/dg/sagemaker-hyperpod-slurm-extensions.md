

# Cluster extensions for SageMaker HyperPod Slurm clusters

SageMaker HyperPod cluster extensions are software packages, managed by AWS, that HyperPod installs, configures, and maintains on clusters created with Slurm orchestration. Instead of writing and maintaining lifecycle scripts to set up platform capabilities, you install an extension with a single API call. HyperPod then keeps the extension consistent on every node in the cluster, including nodes that you add later and nodes that HyperPod replaces.

On Slurm clusters that use continuous provisioning, you set up observability and user management with cluster extensions. Lifecycle scripts remain the way to install other software.

**Note**  
Cluster extensions aren't lifecycle scripts. AWS builds and maintains extensions, and you manage them through APIs for the life of the cluster. You can use lifecycle scripts for other software on the same cluster, but don't use them to manage software that an extension also manages. Don't set `enable_observability` on a cluster with the observability extension, and don't run `add_users.sh` or set `enable_sssd` on a cluster with the user management extension.

## Available cluster extensions
<a name="sagemaker-hyperpod-slurm-extensions-available-cluster-extensions"></a>

The following table lists the cluster extensions that are available for SageMaker HyperPod Slurm clusters.


| Extension | Name | Description | 
| --- | --- | --- | 
| [Setting up observability with the SageMaker HyperPod observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md) | sagemaker-observability | Collects node, GPU, network, Slurm job, and Slurm cluster metrics, and optionally NVIDIA Collective Communications Library (NCCL) metrics, and sends them to Amazon CloudWatch or Amazon Managed Service for Prometheus. | 
| [User management extension](sagemaker-hyperpod-slurm-user-management-extension.md) | sagemaker-user-management | Creates POSIX users and groups with the same IDs on every node, grants SSH and sudo access by group and node type, registers users with Slurm accounting, and connects the cluster to Active Directory. | 

To see the versions of an extension that you can install, run `list-cluster-extension-versions`. For more information, see [List the available versions of an extension](sagemaker-hyperpod-slurm-extensions-manage.md#sagemaker-hyperpod-slurm-extensions-manage-list-the-available-versions-of-an-extension).

## Versions and configuration
<a name="sagemaker-hyperpod-slurm-extensions-versions-and-configuration"></a>

Each extension has one or more versions, and each version defines the settings that it accepts. If you don't specify a version, HyperPod installs the latest one. Settings that you omit use their defaults, and HyperPod rejects unknown settings and invalid values when you make the request.

A cluster can have one extension of each name. If you delete an extension and create it again, the new extension has a new ARN, so scripts and IAM policies shouldn't depend on the old one.

## Where extensions run
<a name="sagemaker-hyperpod-slurm-extensions-where-extensions-run"></a>

An extension applies to every node in the cluster, including nodes that you add later and nodes that HyperPod replaces. Each extension runs only what is relevant to each node type. For example, the observability extension collects Slurm controller metrics only on the controller node. Each extension's page lists what it runs where.

A new node gets the extension's current version and configuration within a few minutes after it starts. When you remove nodes, no action is needed.

**Note**  
A new node can join Slurm and start running jobs a few minutes before an extension finishes on it. Extensions don't hold back job scheduling. For what this means for the user management extension, see [User management extension](sagemaker-hyperpod-slurm-user-management-extension.md).

## Extension status
<a name="sagemaker-hyperpod-slurm-extensions-extension-status"></a>

The following table describes the extension status values.


| Status | Description | 
| --- | --- | 
| Creating | HyperPod is installing the extension on the cluster's nodes. | 
| Active | The extension is installed with its current version and configuration, and no node reports a problem. | 
| Updating | HyperPod is applying a configuration change or version update to the nodes. | 
| Degraded | The extension has its current version and configuration on some nodes but not all of them, or at least one node reports it as unhealthy. Health in the DescribeClusterExtension response shows the cause. | 
| CreateFailed | HyperPod couldn't install the extension on any node. | 
| UpdateFailed | HyperPod couldn't apply the update on any node. | 
| Deleting | HyperPod is removing the extension from the nodes. When removal is complete, the extension no longer exists. | 
| DeleteFailed | HyperPod couldn't remove the extension from the nodes where it's still installed. | 

Some problems show up only on a node, such as a port or a user ID (UID) that software installed another way already uses. The node reports the failure, and the status becomes `Degraded`, or `CreateFailed` or `UpdateFailed` if every node failed.

`DescribeClusterExtension` also returns a node summary. `ActiveCount` is the number of nodes that run the extension's current version and configuration and don't report it as unhealthy. When `ActiveCount` equals `TotalCount`, the change is on every node. While new or replaced nodes join the cluster, the status stays `Active` and `ActiveCount` can be lower than `TotalCount` for a few minutes.

## Health issues
<a name="sagemaker-hyperpod-slurm-extensions-health-issues"></a>

When the extension has a problem on some nodes, the `DescribeClusterExtension` response also contains `Health`, which groups the problems by cause and gives the number of nodes that each one affects. When no node has a problem, the response doesn't contain `Health`.

Each issue has a `Code`, a `Message`, and a `NodeCount`. The message names the setting or component to check, for example `userSources.localUsers.users[1].uid belongs to another account on this node`. `Health` doesn't list instance IDs. To find the nodes, use the extension health logs. For more information, see [Monitoring cluster extension health](sagemaker-hyperpod-slurm-extensions-health.md).

The following list describes the issue codes and what to do:
+ **`InvalidConfiguration`** – The configuration isn't valid on its own, for example because it refers to a name that it doesn't define. Correct the configuration with `update-cluster-extension`.
+ **`ConfigurationConflict`** – The configuration is valid but conflicts with the node, for example because another account on the node already uses a UID in the configuration, or another process already uses a port that the extension needs.
+ **`AccessDenied`** – The execution role, or a key policy or resource policy, doesn't allow an action that the extension needs, such as reading a secret or sending metrics.
+ **`ResourceNotFound`** – A resource that the configuration names doesn't exist, such as a secret or a workspace.
+ **`DependencyUnreachable`** – The nodes can't reach a service that the extension needs, usually because of VPC routing, a security group, or DNS.
+ **`ExtensionUnhealthy`** – The extension is installed, but one of its components isn't running or fails its health check. The message comes from the extension and names the component or check. Each extension's page lists its checks.
+ **`InternalFailure`** – A server-side error. HyperPod retries automatically with exponential backoff, and no action is needed. If the issue persists, contact AWS Support.
+ **`Other`** – More problems exist than `Health` can show. `Health` lists up to 20 issues. If there are more causes, the 20th issue has this code, and its `NodeCount` is the number of nodes that the other causes affect.

New codes might be added. If you process `Health` in code, handle codes that you don't recognize.

## Retrying failed nodes
<a name="sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes"></a>

To retry the nodes where an install or update failed, fix the cause, then run `update-cluster-extension` without changing the version or configuration. This works when the status is `CreateFailed` or `UpdateFailed`, or `Degraded` because the extension failed to install or update on some nodes. The status stays the same while HyperPod retries those nodes. If the fix is a configuration change, send the corrected configuration instead.

If the status is `DeleteFailed`, fix the cause, then run `delete-cluster-extension` again.

If the extension is `Degraded` only because nodes report `ExtensionUnhealthy`, fix the cause on the node. No API call is needed. HyperPod picks up the next healthy report and returns the status to `Active` within a few minutes. Extensions don't repair a component that someone changed or removed on a node. To apply the extension's software and configuration again, run `update-cluster-extension` with a corrected or changed configuration.

## Updates
<a name="sagemaker-hyperpod-slurm-extensions-updates"></a>

When you update an extension, you send only the settings that you want to change. HyperPod merges them into the current configuration by using JSON merge patch (RFC 7386). The following list describes how the merge works:
+ Settings that you include are changed, and settings that you omit keep their current values.
+ Nested objects are merged setting by setting.
+ A setting with the value `null` is removed and returns to its default value.
+ A list (JSON array) that you include replaces the whole current list. To add one item to a list, send the complete list.

HyperPod validates the merged result against the target version's schema. If the result isn't valid, the update is rejected and nothing changes. When you move to a later version, your current settings are checked against that version. If a setting that you have doesn't exist in the later version, set it to `null` in the same request.

You can update an extension to a later version, but not to an earlier version. To use an earlier version, delete the extension and create it again with that version.

**Topics**
+ [Available cluster extensions](#sagemaker-hyperpod-slurm-extensions-available-cluster-extensions)
+ [Versions and configuration](#sagemaker-hyperpod-slurm-extensions-versions-and-configuration)
+ [Where extensions run](#sagemaker-hyperpod-slurm-extensions-where-extensions-run)
+ [Extension status](#sagemaker-hyperpod-slurm-extensions-extension-status)
+ [Health issues](#sagemaker-hyperpod-slurm-extensions-health-issues)
+ [Retrying failed nodes](#sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes)
+ [Updates](#sagemaker-hyperpod-slurm-extensions-updates)
+ [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md)
+ [Managing cluster extensions](sagemaker-hyperpod-slurm-extensions-manage.md)
+ [Monitoring cluster extension health](sagemaker-hyperpod-slurm-extensions-health.md)