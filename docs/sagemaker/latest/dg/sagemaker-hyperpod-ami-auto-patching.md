

# Amazon SageMaker HyperPod AMI automatic patching
<a name="sagemaker-hyperpod-ami-auto-patching"></a>

Amazon SageMaker HyperPod can automatically apply security-only AMI patches to your clusters without disrupting running workloads. Auto-patching is an opt-in capability that you configure for each instance group, allowing HyperPod to keep your nodes on a secure, up-to-date AMI version on a predictable cadence while respecting active training jobs.

## Overview
<a name="sagemaker-hyperpod-ami-auto-patching-overview"></a>

Keeping clusters patched is operationally expensive, even with full AMI visibility and manual update tools. Workloads that run for days or weeks cannot easily be interrupted to apply a security patch, and manual patching requires coordination, maintenance windows, and careful sequencing. This friction commonly causes updates to be deferred.

Auto-patching on HyperPod addresses this by applying patch-level AMI updates automatically and in a workload-aware manner:
+ **Opt-in, per instance group** – You enable auto-patching by adding an `AutoPatchConfig` to an instance group on [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) or [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html). Different instance groups in the same cluster can use different patching strategies.
+ **Workload-aware** – HyperPod applies patches only as nodes become idle, so it does not interrupt running workloads.
+ **Patch-only** – Auto-patching applies only patch-level updates within your currently selected AMI line (for example, 1.2.3 → 1.2.4), following semantic versioning. It never crosses a minor or major version boundary, which preserves backward compatibility between critical AI/ML software components such as NVIDIA drivers, CUDA, and EFA with your existing training and inference containers.
+ **Predictable schedule** – When a new patch AMI is released, HyperPod sets a fixed patch date 21 days out. You can move it earlier or defer it up to 60 days.
+ **Built-in visibility** – You receive AWS Health (PHD) notifications when a patch AMI is available, and on completion or failure. Live patch progress is shown on the cluster details page in the console.

The result is that security patches land on a predictable cadence without workload disruption.

## Prerequisites
<a name="sagemaker-hyperpod-ami-auto-patching-prerequisites"></a>
+ **AMI versioning** – Auto-patching requires that your cluster has a tracked AMI version. Clusters created on or after January 1, 2026 have AMI versioning; clusters created before that date are not eligible for auto-patching.
+ **HyperPod EKS clusters** – Auto-patching is available only for HyperPod Amazon EKS clusters.

## Enabling auto-patching
<a name="sagemaker-hyperpod-ami-auto-patching-enable"></a>

You enable auto-patching for each instance group through an `AutoPatchConfig`. You can set it when you create a cluster ([CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html)) or update an existing one ([UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html)). You configure auto-patching through the API.

Create an `update_cluster.json` file for your cluster.

```
{
    "ClusterName": "name-of-cluster-to-update",
    "InstanceGroups": [{
        "AutoPatchConfig": {
            "PatchingStrategy": "WhenIdle"
        },
        "InstanceGroupName": "string",
        "InstanceType": "string",
        "InstanceCount": number,
        "ExecutionRole": "string",
        "ThreadsPerCore": number,
        "InstanceStorageConfigs": [{
            "EbsVolumeConfig": {
                "VolumeSizeInGB": number
            }
        }],
        "OverrideVpcConfig": {
            "SecurityGroupIds": ["string"],
            "Subnets": ["string"]
        }
    }]
}
```

Run the following `update-cluster` command to submit the request.

```
aws sagemaker update-cluster \
    --cli-input-json file://complete/path/to/update_cluster.json
```

Set `PatchingStrategy` to one of:
+ `"WhenIdle"` – ideal for training workloads; patches each node as it goes idle.
+ `"WhenAllIdle"` – ideal for training workloads; patches the whole instance group atomically once it is fully idle.

## Disabling auto-patching
<a name="sagemaker-hyperpod-ami-auto-patching-disable"></a>

To disable auto-patching, run the `update-cluster` command without the `AutoPatchConfig` object. This stops all future automated AMI patch upgrades for the instance group.

## Viewing and updating the auto-patching schedule
<a name="sagemaker-hyperpod-ami-auto-patching-schedule-view"></a>

You can view and adjust the auto-patching schedule for an instance group at any time through the API.

You can view the current `PatchingStrategy` by calling the `describe-cluster` API.

```
# View
aws sagemaker describe-cluster --cluster-name $HP_CLUSTER_NAME --query 'InstanceGroups[0].AutoPatchConfig'

# Expected Output: { "PatchingStrategy": "WhenIdle" }
```

By default, HyperPod sets the patch date to be 21 days after a security patch AMI is released. You can use [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) to change this schedule. `NextPatchDate` is a UTC timestamp in ISO 8601 format and must fall within 60 days of the patch AMI release. To patch sooner, set an earlier timestamp; to defer, set a later one (up to the maximum).

Add the `PatchSchedule` to the `AutoPatchConfig` object in the `update_cluster.json` file above, then call the `update-cluster` CLI command.

```
"AutoPatchConfig": {
    "PatchingStrategy": "WhenIdle",
    "PatchSchedule": {
        "NextPatchDate": "2026-07-15T00:00:00Z"
    }
}
```

## Patching strategies
<a name="sagemaker-hyperpod-ami-auto-patching-strategies"></a>

When you enable auto-patching on an instance group, you choose a patching strategy. HyperPod currently supports two strategies, both designed for training workloads.


| Strategy | How it works | Best for | Caveat | 
| --- | --- | --- | --- | 
| WhenIdle | HyperPod cordons all nodes in the instance group, then patches each node individually as it becomes idle. | Training workloads where you want opportunistic, disruption-less patching node by node. | Long-running workloads can leave some nodes unpatched and cordoned for an extended period. The instance group might temporarily run a mix of AMI versions. | 
| WhenAllIdle | HyperPod cordons all nodes, then patches the entire instance group atomically once every node is idle. | Training workloads where you want all nodes on a consistent AMI version after a single, atomic patch. | If the instance group does not fully drain, the patch fails and is retried on the next cycle. | 

In both strategies, HyperPod cordons nodes first so that no new workload is scheduled onto a node that is waiting to be patched. HyperPod patches a node only after it is idle, so it never forcibly interrupts active workloads. No new pods are assigned to already cordoned nodes for 24 hours until the node is successfully patched. Nodes stay cordoned for up to 24 hours, and then HyperPod uncordons them whether or not patching succeeded. During auto-patching, HyperPod modifies the following node attributes when cordoning and uncordoning nodes.
+ Label `sagemaker.amazonaws.com/cordoned-by: AutoPatching` – added when the node is cordoned, removed when it is uncordoned.
+ Node spec `spec.unschedulable: true` – set when the node is cordoned, cleared when it is uncordoned.

Separately, HyperPod adds the following label when it detects that a node is idle.
+ Label `sagemaker.amazonaws.com/idle: true`

### Choosing a strategy
<a name="sagemaker-hyperpod-ami-auto-patching-choosing-strategy"></a>
+ Use `WhenIdle` when you want patches to make progress as soon as individual nodes free up and you can tolerate temporary AMI version skew across the instance group. If some nodes stay busy for a long time, you can manually upgrade the remaining nodes to converge faster, or uncordon them.
+ Use `WhenAllIdle` when AMI version consistency across the instance group matters more than patch speed, and you expect the group to drain fully within a few hours. If the group does not drain, you can trigger a manual patch later or wait for the next auto-patch cycle.

## Patch schedule
<a name="sagemaker-hyperpod-ami-auto-patching-patch-schedule"></a>

HyperPod manages the patch schedule for you through the `NextPatchDate` field:
+ When a new patch AMI becomes available for your selected AMI line, HyperPod automatically sets `NextPatchDate` to a fixed 21 days from the release.
+ You can pull the date in to patch sooner, or push it back up to a maximum of 60 days from the patch AMI release, using [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html).
+ If you do not want the upcoming patch, you can opt out of auto-patching for that instance group.

## AWS Health notifications
<a name="sagemaker-hyperpod-ami-auto-patching-notifications"></a>

Throughout the auto-patching process, HyperPod sends AWS Health (Personal Health Dashboard) notifications so you always know what is happening:
+ When a new AMI is available for patching.
+ On patch start, partial-completion, full-completion, and failures.

## AMI support policy
<a name="sagemaker-hyperpod-ami-auto-patching-support-policy"></a>

Auto-patching applies security patches within the support window defined for your AMI version. For the full HyperPod AMI support policy, see [Amazon SageMaker HyperPod AMI support policy](sagemaker-hyperpod-ami-support-policy.md).

## Frequently asked questions
<a name="sagemaker-hyperpod-ami-auto-patching-faq"></a>

**Will auto-patching trigger an Amazon EKS version upgrade, or a major/minor AMI upgrade at end of life?**

No. Auto-patching only applies patch-level updates within your currently selected AMI line (for example, 1.2.1 → 1.2.2). Amazon EKS control-plane upgrades and major/minor AMI version bumps remain explicit, customer-initiated operations – even when an AMI version approaches end of support. HyperPod surfaces end-of-support signals through `ImageVersionStatus` and AWS Health notifications well ahead of the support window closing. However, it never crosses a minor or major boundary on your behalf.

**What does a node being idle mean?**

On HyperPod Amazon EKS, a node is considered idle when it has no active workload pods running on it. Because HyperPod cordons nodes before patching, no new workloads are scheduled onto a node after it is queued for a patch, so after your workload pods complete and drain, the node becomes idle and HyperPod patches it. `WhenIdle` evaluates idleness per node; `WhenAllIdle` waits until every node in the instance group is idle at the same time.

The following namespaces are excluded when evaluating node idleness – pods running in them are not counted when determining whether a node is idle:
+ `kube-system`
+ `kube-public`
+ `kube-node-lease`
+ `aws-hyperpod`
+ `hyperpod-inference-system`
+ `kueue-system`
+ `amazon-cloudwatch`
+ `amazon-network-flow-monitor`
+ `aws-secrets-manager`
+ `cert-manager`
+ `external-dns`
+ `fluent-bit`
+ `hyperpod-observability`
+ `keda`
+ `kube-state-metrics`
+ `kubeflow`
+ `prometheus-node-exporter`
+ `jupyter-k8s-system`

In addition, the following pods are excluded when evaluating node idleness – they are not counted when determining whether a node is idle:
+ **DaemonSet pods** – infrastructure pods managed by a DaemonSet that run on every node.
+ **Static pods** – pods owned by the node itself.
+ **Completed pods** – pods that have finished execution (in the `Succeeded` or `Failed` phase).
+ **Terminating pods** – pods that are in the process of being deleted.

**What happens if my nodes never go idle?**

With the `WhenIdle` patching strategy, nodes that remain busy stay cordoned and unpatched until they become idle, up to a maximum of 24 hours. If some nodes can't be patched because of running workloads, the instance group can end up with a mix of AMI versions across its nodes. To converge faster, you can manually upgrade the remaining nodes by calling the `UpdateClusterSoftware` API. With the `WhenAllIdle` strategy, if all nodes in an instance group don't fully drain within 24 hours, the patch fails and is retried on the next auto-patch cycle. This ensures that all nodes end up on a consistent AMI version. However, if you have workloads that run longer than 24 hours, the patch fails under this strategy.

**What should I do if my instance group is partially patched?**

If your cluster's instance group is only partially patched – that is, not all nodes are using the same AMI version – you receive an AWS Personal Health Dashboard (PHD) notification. To bring the instance group to a consistent AMI version, call the [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) API with the `ImageReleaseVersion` you want to apply. Only the nodes that are not already on the desired AMI version are upgraded.

**How do I know a patch is happening?**

You receive AWS Health (PHD) notifications when a patch AMI becomes available, and on patch start, completion, and failure. Live progress is also shown on the cluster details page in the console. Notifications are delivered via AWS Health / Personal Health Dashboard (PHD). They go to the AWS account that owns the cluster. Routing is per-account and whoever has access to the Health Dashboard in that account sees them. To route to a specific channel, you can use EventBridge rules on AWS Health events to forward to Amazon SNS, Lambda, or PagerDuty.

**Can I select a particular AMI version for patching?**

No, you cannot select a target AMI version for patching. The system automatically patches to the next available patch-level version in the same major.minor line. For example, if a node is on 1.1.1, it auto-patches only to 1.1.2 (a patch release), never to 1.2.0 (a minor release). However, you can specify the major.minor branch using the `ImageReleaseVersion` field in the [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) API or during cluster creation/updates. After you select a major.minor line, auto-patching keeps your nodes on patch releases within that same major.minor line for as long as it remains supported. For more information about the AMI version support policy, see [Amazon SageMaker HyperPod AMI support policy](sagemaker-hyperpod-ami-support-policy.md).

**Can I roll back a patch?**

Automatic rollback is not supported. If you need to revert to a previous AMI version, you must roll back manually by calling the [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) API with the `ImageReleaseVersion` of the AMI version you want to restore.