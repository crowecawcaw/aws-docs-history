# Resilience-related

Kubernetes labels by SageMaker HyperPod

_Labels_ are key-value pairs that are attached to
[Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects"). SageMaker HyperPod introduces the following labels for the
health checks it provides.

## Node

health status labels

The `node-health-status` labels represent the status of the node health
and to be used as part of node selector filter in healthy nodes.

| Label                                                                            | Description                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sagemaker.amazonaws.com/node-health-status:<br>Schedulable`                     | The node has passed basic health checks and is available for<br>running workloads. This health check is the same as the [currently available SageMaker HyperPod resiliency features for Slurm<br>clusters](sagemaker-hyperpod-resiliency-slurm.md "sagemaker-hyperpod-resiliency-slurm.md"). |
| `sagemaker.amazonaws.com/node-health-status:<br>Unschedulable`                   | The node is running deep health checks and is not available for<br>running workloads.                                                                                                                                                                                                        |
| `sagemaker.amazonaws.com/node-health-status:<br>UnschedulablePendingReplacement` | The node has failed deep health checks or health-monitoring agent<br>checks and requires a replacement. If automatic node recovery is<br>enabled, the node will be automatically replaced by<br>SageMaker HyperPod.                                                                          |
| `sagemaker.amazonaws.com/node-health-status:<br>UnschedulablePendingReboot`      | The node has failed deep health checks or health-monitoring agent<br>checks and requires a reboot. If automatic node recovery is enabled,<br>the node will be automatically rebooted by SageMaker HyperPod.                                                                                  |

## Deep health check labels

The `deep-health-check-status` labels represent the progress of deep
health check on a specific node. Helpful for Kubernetes users to quickly filter for
progress of overall deep health checks.

| Label                                                             | Description                                                                                                                                                                                                                               |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sagemaker.amazonaws.com/deep-health-check-status:<br>InProgress` | The node is running deep health checks and is not available for<br>running workloads.                                                                                                                                                     |
| `sagemaker.amazonaws.com/deep-health-check-status:<br>Passed`     | The node has successfully completed deep health checks and<br>health-monitoring agent checks, and is available for running<br>workloads.                                                                                                  |
| `sagemaker.amazonaws.com/deep-health-check-status:<br>Failed`     | The node has failed deep health checks or health-monitoring agent<br>checks and requires a reboot or replacement. If automatic node<br>recovery is enabled, the node will be automatically rebooted or<br>replaced by SageMaker HyperPod. |

## Fault type and reason labels

The following describes the `fault-type` and `fault-reason`
labels.

- `fault-type` labels represent high-level fault categories when
  health checks fail. These are populated for failures identified during both
  deep health and health-monitoring agent checks.
- `fault-reason` labels represent the detailed fault reason
  associated with a `fault-type`.

## How

SageMaker HyperPod labels

The following topics cover how labeling is done depending on various cases.

###### Topics

- [When a node is added to a SageMaker HyperPod cluster with deep health check
  config disabled](#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-dhc-is-off "#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-dhc-is-off")
- [When a node is added to a SageMaker HyperPod cluster with deep health check
  config enabled](#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-dhc-is-on "#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-dhc-is-on")
- [When there are any compute failures on nodes](#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-node-fails "#sagemaker-hyperpod-eks-resiliency-node-how-it-labels-when-node-fails")

### When a node is added to a SageMaker HyperPod cluster with deep health check

config disabled

When a new node is added into a cluster, and if deep health check is not enabled
for the instance group, SageMaker HyperPod runs the same health checks as the [currently
available SageMaker HyperPod health checks for Slurm clusters](sagemaker-hyperpod-resiliency-slurm.md "sagemaker-hyperpod-resiliency-slurm.md").

If the health check passes, the nodes will be marked with the following
label.

```
sagemaker.amazonaws.com/node-health-status: Schedulable
```

If the health check doesn't pass, the nodes will be terminated and replaced.
This behavior is the same as the way SageMaker HyperPod health check works for Slurm
clusters.

### When a node is added to a SageMaker HyperPod cluster with deep health check

config enabled

When a new node is added into a SageMaker HyperPod cluster, and if the deep health
check test is enabled for the instance group, HyperPod first taints the
node and starts the ~2-hour deep health check/stress test on the node. There are
3 possible outputs of the node labels after the deep health check.

1. When the deep health check test passes

```
sagemaker.amazonaws.com/node-health-status: Schedulable
```

2. When the deep health check test fails, and the instance needs to be
   replaced

```
sagemaker.amazonaws.com/node-health-status: UnschedulablePendingReplacement
```

3. When the deep health check test fails, and the instance needs to be
   rebooted to rerun the deep health check

```
sagemaker.amazonaws.com/node-health-status: UnschedulablePendingReboot
```

If an instance fails the deep health check test, the instance will always be
replaced. If the deep health check tests succeeds, the taint on the node will be
removed.

### When there are any compute failures on nodes

The SageMaker HyperPod health monitor agent also continuously monitors the health
status of each node. When it detects any failures (such as GPU failure and
driver crash), the agent marks the node with one of the following labels.

1. When the node is unhealthy and needs to be replaced

```
sagemaker.amazonaws.com/node-health-status: UnschedulablePendingReplacement
```

2. When the node is unhealthy and needs to be rebooted

```
sagemaker.amazonaws.com/node-health-status: UnschedulablePendingReboot
```

The health monitor agent also taints the node when it detects any node health
issues.
