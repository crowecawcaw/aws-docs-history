

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Automatically repair nodes in EKS clusters
<a name="node-repair"></a>

This topic details the EKS automatic node repair behavior and how to configure it to meet your requirements. EKS automatic node repair is enabled by default in EKS Auto Mode, and can be used with EKS managed node groups and Karpenter.

The default EKS automatic node repair actions are summarized in the table below. They apply to EKS Auto Mode, EKS managed node groups, and self-managed Karpenter, with two exceptions on self-managed Karpenter `v1.15.0` and later that are described in [Repair behavior on Karpenter v1.15.0 and later](#node-repair-karpenter-115).

For a detailed list of node health issues detected by the EKS node monitoring agent, their corresponding repair actions, and the per-code actions behind the `AcceleratedHardwareReady` condition, see [Detect node health issues with the EKS node monitoring agent](node-health-nma.md).


| Node Condition | Description | Repair after | Repair action(s) | 
| --- | --- | --- | --- | 
| AcceleratedHardwareReady | AcceleratedHardwareReady indicates whether accelerated hardware (GPU, Neuron) on the node is functioning correctly. | 10m | Replace or Reboot, depending on the condition reason. `Reboot` requires EKS managed node groups, or self-managed Karpenter `v1.15.0` and later with the `RebootForRepair` feature gate enabled. See [NVIDIA XID error codes](node-health-nma.md#nvidia-xid-codes). | 
| ContainerRuntimeReady | ContainerRuntimeReady indicates whether the container runtime (containerd, etc.) is functioning correctly and able to run containers. | 30m | Replace | 
| DiskPressure | DiskPressure is a standard Kubernetes condition indicating the node is experiencing disk pressure (low disk space or high I/O). | N/A | None | 
| KernelReady | KernelReady indicates whether the kernel is functioning correctly without critical errors, panics, or resource exhaustion. | 30m | Replace | 
| MemoryPressure | MemoryPressure is a standard Kubernetes condition indicating the node is experiencing memory pressure (low available memory). | N/A | None | 
| NetworkingReady | NetworkingReady indicates whether the node’s networking stack is functioning correctly (interfaces, routing, connectivity). | 30m | Replace | 
| StorageReady | StorageReady indicates whether the node’s storage subsystem is functioning correctly (disks, filesystems, I/O). | 30m | Replace | 
| Ready | Ready is the standard Kubernetes condition indicating the node is healthy and ready to accept pods. | 30m | Replace | 

By default, EKS automatic node repair stops taking new repair actions when more than 20 percent of the nodes in a group are unhealthy, which limits the impact of a widespread problem on cluster capacity. In-progress repair actions continue. The definition of the group, and the additional scenarios that stop repair, depend on the compute type.


| Compute type | Repair stops when | 
| --- | --- | 
| EKS managed node groups | The node group has more than five nodes and more than 20% of the nodes in the node group are unhealthy, or a zonal shift for your cluster triggers through the Application Recovery Controller (ARC). | 
| EKS Auto Mode and Karpenter | More than 20% of the nodes in the NodePool are unhealthy. For standalone NodeClaims, 20% of the nodes in the cluster are unhealthy. Karpenter records a `NodeRepairBlocked` event on the affected nodes with a message such as `more than 20% nodes are unhealthy in the nodepool`. | 

See [Configure automatic node repair](#configure-node-repair) for how to override these default settings.

**Important**  
Automatic node repair is a forceful action. On EKS Auto Mode, and on self-managed Karpenter earlier than `v1.15.0`, repair deletes the Pods on the unhealthy node with a minimal grace period rather than performing a standard drain, and it bypasses Pod disruption budgets. For more information, see [Node Auto Repair](https://karpenter.sh/docs/concepts/disruption/#node-auto-repair) in the Karpenter documentation. Design workloads that can’t be interrupted safely, such as long-running training jobs, to checkpoint and resume.  
Self-managed Karpenter `v1.15.0` and later applies a termination grace period and respects Pod disruption budgets within it, and honors the `karpenter.sh/do-not-repair` annotation. For more information, see [Repair behavior on Karpenter v1.15.0 and later](#node-repair-karpenter-115).  
On every compute type, the `karpenter.sh/do-not-disrupt` annotation doesn’t exclude a node from repair.

## How the repair action is chosen
<a name="node-repair-reason-vs-status"></a>

For most node conditions, the repair action depends only on the condition status: a node whose condition holds the unhealthy status for the wait period is repaired. For `AcceleratedHardwareReady`, the action also depends on the condition reason, because the EKS node monitoring agent reports the specific GPU or Neuron fault as the reason. For the per-code actions, see [NVIDIA XID error codes](node-health-nma.md#nvidia-xid-codes).

The condition reason can change while a fault persists, because a single fault can be detected through more than one path. For an example, see [AcceleratedHardware node health issues](node-health-nma.md#node-health-AcceleratedHardware). The effect of a change of reason depends on the compute type.

 **EKS managed node groups** 

A change of reason can change the outcome, because the repair action follows the reason. Reasons whose default action is `None`, such as `DCGMError` and `DCGMHealthCode[Code]`, aren’t repaired. For example, the reason might change from `NvidiaXID79Error` to `DCGMHealthCode120`. The default action changes from `Replace` to `None`, and the node is no longer repaired. To repair nodes for a reason that isn’t repaired by default, add a `nodeRepairConfigOverrides` entry for it, as described in [Managed node groups](#configure-node-repair-mng).

 **EKS Auto Mode** 

A change of reason has no effect. Repair acts on the condition status alone, so the node is replaced after the wait period whatever the reason, including reasons that managed node groups don’t repair.

 **Self-managed Karpenter `v1.15.0` and later** 

A change of reason can change the wait period, because each repair policy matches on the reason. A reason that no policy matches falls through to a longer wait. For more information, see [Repair behavior on Karpenter v1.15.0 and later](#node-repair-karpenter-115).

## Replacement sequence on EKS Auto Mode and Karpenter
<a name="node-repair-replace-sequence"></a>

When the repair action is `Replace` on EKS Auto Mode or Karpenter, the repair follows this sequence:

1. The node reports an unhealthy node condition.

1. The wait period for that condition passes.

1. Karpenter marks the node for deletion and taints it with `karpenter.sh/disrupted:NoSchedule`. On self-managed Karpenter, the controller logs the repair decision. On EKS Auto Mode, Karpenter runs in the AWS managed control plane, so there are no controller logs to view.

1. Karpenter launches a replacement NodeClaim. The replacement launches before the unhealthy node is terminated, so both nodes exist for a few minutes.

1. The unhealthy node is terminated, and Pods reschedule onto the replacement node.

The replacement node is created from the same NodePool, so it can land in any Availability Zone and on any instance type that the NodePool allows.

## Repair behavior on Karpenter v1.15.0 and later
<a name="node-repair-karpenter-115"></a>

Karpenter `v1.15.0` runs node repair as a disruption method rather than through the legacy node repair controller, and this is the default in that version and later. The repair actions are the same as the defaults described in this topic, with the exceptions noted in [NVIDIA XID error codes](node-health-nma.md#nvidia-xid-codes), but the following behavior differs. EKS Auto Mode and earlier Karpenter versions don’t include these changes.

 **Reboot support** 

Karpenter can reboot a node instead of replacing it when you enable the AWS-specific `RebootForRepair` feature gate, which is disabled by default. Set it through the `AWS_FEATURE_GATES` environment variable or the `--aws-feature-gates` CLI option in the Karpenter deployment. A reboot retains the instance, which avoids reprovisioning accelerated capacity that might have limited availability.

 **Termination grace period** 

Repair doesn’t terminate the node immediately. Karpenter applies a termination grace period and respects Pod disruption budgets within it. The following table shows the grace period that each matched repair policy applies.


| Matched repair policy | Grace period | 
| --- | --- | 
| An `AcceleratedHardwareReady` reason matched by one of the XID repair policies | 5m | 
| Any other condition or reason, including an `AcceleratedHardwareReady` reason that fell through to the 30-minute wait | 10m | 

The `selected repair policy` log entry reports the period that was applied as `termination-grace-period`.

 **The do-not-repair annotation** 

Setting the `karpenter.sh/do-not-repair: "true"` annotation on a node excludes it from automatic node repair. The `karpenter.sh/do-not-disrupt` annotation still doesn’t exclude a node from repair.

To run the legacy node repair controller on these versions instead, set the `--legacy-node-repair` CLI option or the `LEGACY_NODE_REPAIR` environment variable to `true`. The legacy controller only replaces nodes and doesn’t support reboot, termination grace periods, or the `karpenter.sh/do-not-repair` annotation. The Karpenter project plans to deprecate it.

## Configure automatic node repair
<a name="configure-node-repair"></a>

Automatic node repair cannot be configured when using EKS Auto Mode. It is always enabled there, with the default settings described in this topic.

### Karpenter
<a name="configure-node-repair-karpenter"></a>

To use automatic node repair with Karpenter, enable the feature gate `NodeRepair=true`. You can enable the feature gates through the `--feature-gates` CLI option or the `FEATURE_GATES` environment variable in the Karpenter deployment. For more information, see the [Karpenter documentation](https://karpenter.sh/docs/concepts/disruption/#node-auto-repair).

On Karpenter `v1.15.0` and later, you can also enable the `RebootForRepair` feature gate to allow reboots, and annotate nodes with `karpenter.sh/do-not-repair` to exclude them from repair. For more information, see [Repair behavior on Karpenter v1.15.0 and later](#node-repair-karpenter-115).

### Managed node groups
<a name="configure-node-repair-mng"></a>

You can enable automatic node repair when creating new EKS managed node groups or by updating existing EKS managed node groups.
+  **Amazon EKS console** – Select the **Enable node auto repair** checkbox for the managed node group. For more information, see [Create a managed node group for your cluster](create-managed-node-group.md).
+  ** AWS CLI** – Add `--node-repair-config enabled=true` to the [`eks create-nodegroup`](https://docs.aws.amazon.com/cli/latest/reference/eks/create-nodegroup.html) or [`eks update-nodegroup-config`](https://docs.aws.amazon.com/cli/latest/reference/eks/update-nodegroup-config.html) command.
+  **eksctl** – Configure `managedNodeGroups.nodeRepairConfig.enabled: true`, see the example in the [eksctl GitHub](https://github.com/eksctl-io/eksctl/blob/main/examples/44-node-repair.yaml).

When using EKS managed node groups, you can control node auto repair behavior with the following settings.

To control when node auto repair stops taking action, set a threshold based on the number of unhealthy nodes in the node group. Set either the absolute count or percentage, but not both.


| Setting | Description | 
| --- | --- | 
|  `maxUnhealthyNodeThresholdCount`  | The absolute number of unhealthy nodes above which node auto repair stops. Use this to limit the scope of repairs. | 
|  `maxUnhealthyNodeThresholdPercentage`  | The percentage of unhealthy nodes above which node auto repair stops (0-100). | 

To control how many nodes repair at the same time, you can configure repair parallelism. As with the unhealthy node threshold, set either the absolute count or percentage, but not both.


| Setting | Description | 
| --- | --- | 
|  `maxParallelNodesRepairedCount`  | The maximum number of nodes to repair concurrently. | 
|  `maxParallelNodesRepairedPercentage`  | The maximum percentage of unhealthy nodes to repair concurrently (0-100). | 

With `nodeRepairConfigOverrides`, you can customize repair behavior for specific conditions. Use this setting when different issue types require different repair actions or wait times.

Each override requires all of the following fields:


| Field | Description | 
| --- | --- | 
|  `nodeMonitoringCondition`  | The node condition type reported by the EKS node monitoring agent. For example: `AcceleratedHardwareReady`, `NetworkingReady`, `StorageReady`, `KernelReady`. | 
|  `nodeUnhealthyReason`  | The specific reason code for the unhealthy condition. For example: `NvidiaXID79Error`, `IPAMDNotRunning`. | 
|  `minRepairWaitTimeMins`  | The minimum time in minutes that the condition must persist before the node becomes eligible for repair. Use this to avoid repairing nodes for temporary issues. The value must be from 10 through 120 and a multiple of 10. | 
|  `repairAction`  | The action to take when conditions are met. Valid values: `Replace` (terminate and replace the node), `Reboot` (reboot the node), or `NoAction` (no repair actions). | 

The following AWS CLI example creates a node group with custom repair settings.

```
aws eks create-nodegroup \
  --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --node-role arn:aws:iam::111122223333:role/NodeRole \
  --subnets subnet-0123456789abcdef0 \
  --node-repair-config '{
    "enabled": true,
    "maxUnhealthyNodeThresholdPercentage": 10,
    "maxParallelNodesRepairedCount": 3,
    "nodeRepairConfigOverrides": [
      {
        "nodeMonitoringCondition": "AcceleratedHardwareReady",
        "nodeUnhealthyReason": "NvidiaXID46Error",
        "minRepairWaitTimeMins": 10,
        "repairAction": "Replace"
      },
      {
        "nodeMonitoringCondition": "AcceleratedHardwareReady",
        "nodeUnhealthyReason": "NvidiaXID63Error",
        "minRepairWaitTimeMins": 20,
        "repairAction": "NoAction"
      },
      {
        "nodeMonitoringCondition": "AcceleratedHardwareReady",
        "nodeUnhealthyReason": "DCGMHealthCode120",
        "minRepairWaitTimeMins": 10,
        "repairAction": "Replace"
      }
    ]
  }'
```

This configuration does the following:
+ Enables node auto repair
+ Stops repair actions when more than 10% of nodes are unhealthy
+ Repairs up to 3 nodes at a time
+ Overrides XID 46 errors (GPU stopped processing) to replace the node after 10 minutes. The default is reboot.
+ Overrides XID 63 errors (GPU memory remapping event, which is often recoverable) to take no action. The default is reboot.
+ Repairs nodes whose condition reason is `DCGMHealthCode120` (`DCGM_FR_FALLEN_OFF_BUS`) by replacing them after 10 minutes. The default action for `DCGMHealthCode[Code]` reasons is none.