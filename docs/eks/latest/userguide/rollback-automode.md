**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Rollback EKS Auto Mode clusters

When you initiate a version rollback on a cluster running EKS Auto Mode, Amazon EKS automatically manages the rollback of Auto Mode worker nodes before reverting the control plane. This page explains how Auto Mode node rollback works, how to speed it up, and how to cancel it if needed.

For general information about version rollback, including prerequisites, insight checks, and the overall rollback process, see [Roll back a cluster to a previous Kubernetes version](rollback-cluster.md "rollback-cluster.md").

## How Auto Mode rollback works

EKS Auto Mode uses a Karpenter-based system to manage worker node infrastructure, including Kubernetes version upgrades and rollbacks. When you call `UpdateClusterVersion` with the previous (N-1) version on a cluster with Auto Mode enabled, EKS performs the following sequence:

1. Validates prerequisites and refreshes rollback readiness insights.
2. Drifts nodes towards the desired rollback version using a Karpenter-based system, honoring configured disruption controls.
3. After all nodes are within the Kubernetes version skew policy for the desired rollback version, EKS re-checks insights and proceeds with the control plane rollback.

The control plane remains on the current (newer) version and continues serving traffic normally while nodes are rolling back. The Kubernetes version skew policy allows nodes to run up to three minor versions older than the kube-apiserver, so this intermediate state is valid.

###### Note

You trigger the rollback using the same API and process described in [Roll back a cluster to a previous Kubernetes version](rollback-cluster.md "rollback-cluster.md"). There is no separate API for Auto Mode node rollback.

###### Note

The node rollback phase (step 2) can take anywhere from minutes to 7 days depending on your disruption controls. If the node rollback does not complete within the configured timeout, the update is marked as failed.

###### Note

While a rollback is in progress, other customer-triggered control plane updates are blocked. To perform a different update, cancel the rollback first using the CancelUpdate API.

## Cluster status during rollback

| Phase                     | Cluster status | What is happening                                                                                                                |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Node rollback in progress | **ACTIVE**     | Karpenter is replacing nodes with the previous version AMI. Control plane is healthy and serving traffic at the current version. |
| Control plane rollback    | **UPDATING**   | API server and control plane components are being reverted to the previous version.                                              |
| Rollback complete         | **ACTIVE**     | Cluster is fully on the previous version.                                                                                        |

The cluster status remains `ACTIVE` during the node rollback phase. Use `ListUpdates` or `DescribeUpdate` to determine if a rollback is in progress. In the Amazon EKS console, navigate to your cluster and open the **Update history** tab to view the status of the update ID associated with the rollback.

To track individual node progress during rollback, check the Kubernetes version of your Auto Mode nodes:

```
kubectl get nodes -l karpenter.sh/nodepool=<nodepool-name> -o wide
```

## Disruption controls

Auto Mode rollback honors all existing disruption controls. These controls determine how quickly nodes can be replaced and might significantly affect rollback duration.

### NodePool Disruption Budgets

NodePool disruption budgets control how many nodes can be disrupted simultaneously. During rollback, Karpenter respects these budgets when drifting nodes to the previous version.

- A budget of `nodes: 0` for drift blocks rollback indefinitely. This triggers an ERROR insight.
- A restrictive budget (for example, `nodes: 1`) slows rollback but allows forward progress.

Example NodePool with a disruption budget that allows 10% of nodes to be replaced at a time:

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  disruption:
    budgets:
      - nodes: "10%"
        reasons:
          - Drifted
```

For more information about configuring NodePool disruption budgets, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md") and [Karpenter disruption budgets](https://karpenter.sh/docs/concepts/disruption/#disruption-budgets "https://karpenter.sh/docs/concepts/disruption/#disruption-budgets").

### PodDisruptionBudgets

Kubernetes PodDisruptionBudgets are honored during node replacement. If a PDB prevents pod eviction, the node disruption is delayed up to the TerminationGracePeriod.

- PDBs with `maxUnavailable: 0` delay node disruption. This triggers a WARNING insight.
- PDBs do not permanently block rollback but can significantly slow it down.

For more information, see [Protect critical workloads with a PDB](../../../prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/pdb.md "../../../prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/pdb.md") and the [Kubernetes PDB documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/ "https://kubernetes.io/docs/tasks/run-application/configure-pdb/").

### Do-not-disrupt annotations

The `karpenter.sh/do-not-disrupt` annotation can be set on nodes or pods:

**On nodes:** Blocks node disruption indefinitely. This triggers an ERROR insight and must be removed before rollback can proceed on that node.

**On pods:** Delays node disruption up to the TerminationGracePeriod. This triggers a WARNING insight but does not permanently block rollback.

For more information about Karpenter disruption behavior, see the [Karpenter disruption documentation](https://karpenter.sh/docs/concepts/disruption/ "https://karpenter.sh/docs/concepts/disruption/").

## Speeding up rollback

If rollback is taking longer than expected, you can adjust disruption controls while rollback is in progress.

### Increase NodePool disruption budgets

Edit the NodePool resource to allow more concurrent node replacements:

```
kubectl edit nodepool default
```

Change the budget to a higher value:

```
spec:
  disruption:
    budgets:
      - nodes: "50%"
        reasons:
          - Drifted
```

### Remove do-not-disrupt annotations from nodes

List nodes with the annotation and remove it:

```
# List nodes with the annotation
kubectl get nodes -o json | jq '.items[] | select(.metadata.annotations["karpenter.sh/do-not-disrupt"] == "true") | .metadata.name'

# Remove from a specific node
kubectl annotate node <node-name> karpenter.sh/do-not-disrupt-
```

### Adjust PodDisruptionBudgets

If PDBs are slowing down pod eviction, temporarily adjust them:

```
kubectl edit pdb <pdb-name> -n <namespace>
```

###### Warning

Adjusting disruption controls affects your application availability guarantees. Ensure you understand the impact before making changes in production.

For more information about managing disruption controls, see [Preventing pod and node disruption in Amazon EKS Auto Mode](https://repost.aws/articles/ARONpaMO8rQAqXM_BLmhyqWA/preventing-pod-and-node-disruption-in-amazon-eks-auto-mode "https://repost.aws/articles/ARONpaMO8rQAqXM_BLmhyqWA/preventing-pod-and-node-disruption-in-amazon-eks-auto-mode").

## Canceling a rollback

A rollback is in a cancellable state only while nodes are rolling back. You can use CancelUpdate during this phase to stop the operation.

```
aws eks cancel-update \
  --name my-cluster \
  --update-id <update-id> \
  --region us-west-2
```

### Cancel behavior

| Aspect                   | Behavior                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------- |
| When cancellable         | Only while Auto Mode nodes are being rolled back (before control plane rollback starts) |
| Semantics                | Best-effort stop. Stops the node rollback operation.                                    |
| Mid-disruption nodes     | If a node is mid-disruption at cancel time, it completes its current operation.         |
| Post-cancellation status | Update transitions from `Cancelling` to `Cancelled`.                                    |
| Cluster status           | Remains `ACTIVE` throughout.                                                            |

### After cancellation

Upon successful cancellation, nodes drift towards the current cluster version as usual. The update transitions from `Cancelling` to `Cancelled`.

After cancellation, you can immediately:

- Retry the rollback (as long as you are still within the 7-day eligibility window).
- Perform a different cluster update.
- Leave the cluster as-is on the current version.

### When cancel is not possible

Cancel fails if node rollback is already complete and the control plane rollback has started, or if the update has already completed with `Successful` or `Failed` status.

###### Note

CloudFormation and Terraform do not directly support the CancelUpdate API. If you need to cancel a rollback initiated through IaC, you must call the API directly.

## Rollback timeout

Auto Mode node rollback has a configurable timeout controlled by the `timeoutMinutes` parameter in `rollbackConfig`. The default timeout is 720 minutes (12 hours). You can set a value between 120 minutes (2 hours) and 10080 minutes (7 days). The timeout is a minimum-bound property, meaning it occurs no sooner than the time you specify, but can occur shortly thereafter.

```
aws eks update-cluster-version \
  --name my-cluster \
  --kubernetes-version 1.30 \
  --rollback-config timeoutMinutes=1440 \
  --region us-west-2
```

If all nodes have not completed rollback within the specified timeout:

1. The rollback times out.
2. Nodes begin drifting back to the current cluster version.
3. The control plane remains on the current version (it was never rolled back).
4. The update status transitions to `Failed`.

After a timeout, you can retry the rollback if you are still within the 7-day rollback eligibility window from the original upgrade. In practice, if the node rollback times out at day 7, the rollback eligibility window has likely also expired since both are 7 days.

To avoid timeouts, review rollback readiness insights before initiating the rollback. These insights warn about disruption budgets or annotations that might slow down the node rollback process.

## The --force flag and Auto Mode

The `--force` flag on `UpdateClusterVersion` only bypasses cluster insight checks. It has no effect on Auto Mode node disruption behavior.

Even with `--force`:

- NodePool disruption budgets are still honored.
- PodDisruptionBudgets are still honored.
- Do-not-disrupt annotations are still respected.
- The 7-day node rollback timeout still applies.

The only way to speed up node rollback is to adjust the disruption controls themselves. See [Speeding up rollback](#automode-speed-up-rollback "#automode-speed-up-rollback") for details.

## IaC timeout conflicts

Infrastructure-as-Code tools have timeout limitations that might conflict with Auto Mode rollback duration. CloudFormation allows up to 36 hours per resource. If the operation times out, CloudFormation treats it as a no-op, which can leave the cluster in a drifted state where the template does not reflect the actual cluster version. Version rollback must be explicitly initiated. Terraform Enterprise/Cloud has an approximately 24-hour timeout, though client-side timeouts might vary depending on credential expiration and other factors.

To align rollback duration with your IaC tool, use the `timeoutMinutes` parameter in `rollbackConfig` to set an appropriate timeout. If your IaC tool times out, use the CancelUpdate API directly to regain control. If you have restrictive disruption budgets, consider initiating rollback directly through CLI or API instead of IaC.

## System updates during node rollback

While Auto Mode nodes are rolling back, EKS continues to keep the control plane secure and available.

Customer-triggered updates (such as UpdateClusterVersion or UpdateClusterConfig) are blocked while node rollback is in progress. If you need to perform a high-priority update, cancel the rollback first using `CancelUpdate`, then perform your update, and re-initiate the rollback if still within the eligibility window.

## Related resources

- [Roll back a cluster to a previous Kubernetes version](rollback-cluster.md "rollback-cluster.md")
- [EKS Auto Mode overview](automode.md "automode.md")
- [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md")
- [Update the Kubernetes Version of an EKS Auto Mode cluster](auto-upgrade.md "auto-upgrade.md")
- [Preventing pod and node disruption in Amazon EKS Auto Mode](https://repost.aws/articles/ARONpaMO8rQAqXM_BLmhyqWA/preventing-pod-and-node-disruption-in-amazon-eks-auto-mode "https://repost.aws/articles/ARONpaMO8rQAqXM_BLmhyqWA/preventing-pod-and-node-disruption-in-amazon-eks-auto-mode")
- [Troubleshoot EKS Auto Mode](auto-troubleshoot.md "auto-troubleshoot.md")
- [Karpenter disruption documentation](https://karpenter.sh/docs/concepts/disruption/ "https://karpenter.sh/docs/concepts/disruption/")
- [Kubernetes PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/ "https://kubernetes.io/docs/tasks/run-application/configure-pdb/")
