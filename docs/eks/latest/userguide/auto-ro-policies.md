

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# How resource optimization policies select and combine

EKS Auto Mode resource optimization manages a Deployment or StatefulSet only when a `ClusterResourceOptimizationPolicy` selects it. A policy selects workloads with two optional label selectors and sets the `mode` and `profile` that those workloads get. More than one policy can select the same workload. This topic explains which workloads a policy selects, which policy’s settings a workload gets, and where you can see the result.

## What the selectors match
<a name="auto-ro-policies-selectors"></a>

A policy has two selectors. Both are standard Kubernetes label selectors, so you can use `matchLabels`, `matchExpressions`, or both.

 `namespaceSelector`   
Matches labels on the namespace. If you don’t set it, the policy selects every namespace except the system namespaces.  
The Kubernetes API server sets the `kubernetes.io/metadata.name` label on every namespace to the namespace’s name. Use this label to select or exclude namespaces by name without adding your own labels.

 `workloadSelector`   
Matches labels on the Deployment or StatefulSet object itself, in its `metadata.labels`. If you don’t set it, the policy selects every Deployment and StatefulSet in the namespaces it selects. You can set `workloadSelector` without `namespaceSelector`. The policy then applies to matching workloads in every non-system namespace.

**Note**  
 `workloadSelector` doesn’t match the labels in the Pod template (`spec.template.metadata.labels`). Many workloads use the same labels in both places, but not all of them do. If a policy doesn’t select a workload you expect it to, compare the selector with the workload’s own labels, which `kubectl get deployment` {{my-app}} `--show-labels` shows.

A policy selects a workload when the workload’s namespace matches `namespaceSelector` and the workload matches `workloadSelector`. An empty selector (`{}`) matches everything, like an unset one.

The following YAML policy selects every Deployment and StatefulSet labeled `tier: web`, in every namespace except `payments`:

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: web-except-payments
spec:
  namespaceSelector:
    matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: NotIn
        values:
          - payments
  workloadSelector:
    matchLabels:
      tier: web
```

**Note**  
The Kubernetes API server doesn’t validate the selectors in a policy. If a selector is invalid, for example because it uses an unknown `operator`, the API server still accepts the policy. Resource optimization doesn’t use it. The policy’s `SelectorsValid` condition is `False` with reason `InvalidSelector`, and its `Ready` condition is `False`. Other policies keep working. If you edit a policy and make its selector invalid, workloads that only that policy selected stop being managed. Resource optimization deletes their `ResourceOptimization` objects and usage history. Workloads that the policy was winning for switch to the settings of the next policy that selects them. For more information, see [Troubleshoot EKS Auto Mode resource optimization](auto-ro-troubleshoot.md).

## How resource optimization decides whether and how to manage a workload
<a name="auto-ro-policies-resolve"></a>

Resource optimization evaluates every Deployment and StatefulSet in the following order:

1.  **At least one policy exists.** If there are no policies in the cluster, resource optimization manages no workloads.

1.  **The workload isn’t in a system namespace.** Resource optimization never manages workloads in `kube-system`, `kube-public`, or `kube-node-lease`. No policy can select these namespaces.

1.  **The workload doesn’t opt out.** A workload with the annotation `optimization.eks.amazonaws.com/enabled: "false"` isn’t managed, even if a policy selects it. For more information, see [Opt a workload out](#auto-ro-policies-opt-out).

1.  **At least one policy selects the workload.** The policy’s `namespaceSelector` matches the workload’s namespace, and its `workloadSelector` matches the workload.

1.  **The most specific selecting policy supplies the settings.** If more than one policy selects the workload, resource optimization uses the `mode` and `profile` of the most specific one. For more information, see [When more than one policy selects a workload](#auto-ro-policies-specificity).

For each workload it manages, resource optimization creates a `ResourceOptimization` object in the workload’s namespace. The object holds the workload’s settings and recommendations. For more information, see [EKS Auto Mode resource optimization resource reference](auto-ro-reference.md).

### When more than one policy selects a workload
<a name="auto-ro-policies-specificity"></a>

When several policies select the same workload, the most specific policy wins. Specificity depends on which selectors a policy sets, from most to least specific:

1. Both `namespaceSelector` and `workloadSelector` 

1.  `workloadSelector` only

1.  `namespaceSelector` only

1. Neither selector, for example `spec: {}` 

A `workloadSelector` names specific workloads, so it ranks above a `namespaceSelector`, which takes everything in a namespace. An empty selector (`{}`) counts as not set. The most specific policy wins even when its settings are less conservative. For example, a namespace-only policy in `Apply` mode wins over a `spec: {}` policy in `Recommend` mode.

If two or more policies are equally specific, resource optimization breaks the tie as follows:

1. A policy with `mode: Recommend` wins over a policy with `mode: Apply`.

1. If the policies still tie, the policy whose name comes first alphabetically wins.

A policy that doesn’t set `mode` is in `Recommend` mode, so it wins a tie against an equally specific policy in `Apply` mode.

The order in which you create policies doesn’t matter, and there’s no priority field. `Balanced` is the only profile in this preview, so only `mode` differs between policies.

### Example – Three overlapping policies
<a name="auto-ro-policies-example"></a>

Suppose a cluster has the following three policies.

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: default
spec: {}
---
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: search-namespace
spec:
  mode: Apply
  namespaceSelector:
    matchLabels:
      team: search
---
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: batch
spec:
  mode: Recommend
  workloadSelector:
    matchLabels:
      tier: batch
```

The following table shows the result for workloads in different namespaces.


| Workload | Selecting policies | Winning policy | Mode | 
| --- | --- | --- | --- | 
| Deployment `indexer` labeled `tier: batch`, in a namespace labeled `team: search`  |  `default`, `search-namespace`, `batch`  |  `batch` (`workloadSelector` only) |  `Recommend`  | 
| Deployment `frontend` with no `tier` label, in a namespace labeled `team: search`  |  `default`, `search-namespace`  |  `search-namespace` (`namespaceSelector` only) |  `Apply`  | 
| StatefulSet `reports` labeled `tier: batch`, in a namespace with no `team` label |  `default`, `batch`  |  `batch` (`workloadSelector` only) |  `Recommend`  | 
| Deployment `api` with no `tier` label, in a namespace with no `team` label |  `default`  |  `default` (no selectors) |  `Recommend`  | 
| Any workload in `kube-system`  | None | None. System namespaces are never managed. | Not managed | 

 `indexer` gets `Recommend` because `batch` sets a `workloadSelector`, which ranks above the `namespaceSelector` that `search-namespace` sets. If you delete `batch`, `indexer` gets `Apply` from `search-namespace`, because `search-namespace` is more specific than `default`, even though `default` is more conservative.

## Opt a workload out
<a name="auto-ro-policies-opt-out"></a>

To exclude a workload that a policy selects, add the following annotation to the Deployment or StatefulSet metadata, not to its Pod template.

```yaml
metadata:
  annotations:
    optimization.eks.amazonaws.com/enabled: "false"
```

The annotation wins over every policy. Resource optimization deletes the workload’s `ResourceOptimization` object, stops changing its Pods, and cancels any resize that the kubelet hasn’t applied yet. The values it already applied stay in place, and new Pods start at the values in the Pod template. This also deletes the workload’s usage history. If the workload is managed again, the wait of about 12 hours for a first recommendation starts over. The workload counts in the `optedOutWorkloads` status field of each policy that selects it. For the full procedure, including how to return Pods to their template values, see [Opt out a single workload](auto-ro-enable.md#auto-ro-enable-opt-out).

## See which policy manages a workload
<a name="auto-ro-policies-view"></a>

To see how many workloads each policy selects, run the following `kubectl` command. A workload that several policies select counts on each of them.

```bash
kubectl get crop
```

The following example output shows the mode, profile, and number of selected workloads for each policy.

```bash
NAME               MODE        PROFILE    READY   SELECTED   AGE
batch              Recommend   Balanced   True    2          3d
default            Recommend   Balanced   True    4          3d
search-namespace   Apply       Balanced   True    2          3d
```

To see the result for each workload in a namespace, run the following `kubectl` command to list its `ResourceOptimization` objects. The `POLICY` column shows the winning policy, and `MODE` shows the mode the workload gets.

```bash
kubectl get ro -n search
```

The following example output shows the winning policy and mode for each workload.

```bash
NAME              KIND         TARGET     POLICY             MODE        AGE
frontend-deploy   Deployment   frontend   search-namespace   Apply       3d
indexer-deploy    Deployment   indexer    batch              Recommend   3d
```

A workload with no `ResourceOptimization` object isn’t managed. Check that a policy selects it, that it isn’t in a system namespace, and that it doesn’t have the opt-out annotation.

The object’s `status.policySource` field also names the winning policy. Every selecting policy is an owner of the object. The winning policy has `controller: true`. The object exists while at least one valid policy selects the workload. To see the winning policy for one workload, run the following `kubectl` command:

```bash
kubectl get ro indexer-deploy -n search -o jsonpath='{.status.policySource}'
```

The following example output shows the policy that supplied each field.

```bash
{"mode":"batch","profile":"batch"}
```

## Control who can create policies
<a name="auto-ro-policies-rbac"></a>

A policy can switch workloads in any non-system namespace to `Apply` mode, so limit who can create one. Creating a policy requires a `ClusterRole` that allows `create` on `clusterresourceoptimizationpolicies` in the `eks.amazonaws.com` API group. Bind it with a `ClusterRoleBinding`. Grant it only to cluster administrators. Namespace owners can still opt out their own workloads with the annotation.