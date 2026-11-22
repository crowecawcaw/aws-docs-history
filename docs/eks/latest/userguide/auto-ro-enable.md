

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Turn on and configure EKS Auto Mode resource optimization

You turn on, configure, and turn off EKS Auto Mode resource optimization with `ClusterResourceOptimizationPolicy` objects. A policy is a cluster-scoped Kubernetes object that you manage with `kubectl` or your GitOps tooling, like any other manifest. There is no EKS API setting for resource optimization.

## Prerequisites
<a name="auto-ro-enable-prereqs"></a>
+ An EKS Auto Mode cluster running Kubernetes version 1.36 or later. For more information, see [Create a cluster with Amazon EKS Auto Mode](create-auto.md).
+  `kubectl` configured to communicate with your cluster, with permission to create cluster-scoped resources.

## Turn on resource optimization with default settings
<a name="auto-ro-enable-default"></a>

Complete the following steps to turn on resource optimization with default settings:

1. Save the following manifest as `ro-default-policy.yaml`.

   ```yaml
   apiVersion: eks.amazonaws.com/v1beta1
   kind: ClusterResourceOptimizationPolicy
   metadata:
     name: default
   spec: {}
   ```

   With an empty `spec`, the policy selects every Deployment and StatefulSet in every namespace except the system namespaces, in `Recommend` mode with the `Balanced` profile. The policy doesn’t change any Pod.

1. Apply the manifest.

   ```bash
   kubectl apply -f ro-default-policy.yaml
   ```

1. Confirm that the policy is ready.

   ```bash
   kubectl get crop
   ```

   An example output is as follows.

   ```bash
   NAME      MODE        PROFILE    READY   SELECTED   AGE
   default   Recommend   Balanced   True    42         5m
   ```

    `READY` is `True` when the policy’s selectors are valid. `SELECTED` is the number of workloads that the policy currently selects. If `READY` is `False`, run `kubectl describe crop default` and review the conditions. For more information, see [Troubleshoot EKS Auto Mode resource optimization](auto-ro-troubleshoot.md).

1. View the per-workload objects that resource optimization creates.

   ```bash
   kubectl get ro --all-namespaces
   ```

   An example output is as follows.

   ```bash
   NAMESPACE   NAME              KIND          TARGET     POLICY    MODE        AGE
   checkout    checkout-deploy   Deployment    checkout   default   Recommend   5m
   data        redis-sts         StatefulSet   redis      default   Recommend   5m
   ```

   The `POLICY` column shows which policy supplied the workload’s mode. Recommendations appear on each object after resource optimization collects about 12 hours of usage history for the workload’s containers. For the fields on these objects, see [EKS Auto Mode resource optimization resource reference](auto-ro-reference.md).

## Example policies
<a name="auto-ro-enable-examples"></a>

Use `namespaceSelector` and `workloadSelector` to limit which workloads a policy manages. Both are standard Kubernetes label selectors. `namespaceSelector` matches labels on namespaces. `workloadSelector` matches labels on the Deployment or StatefulSet object, not on its Pod template.

When more than one policy selects a workload, resource optimization combines them field by field, and the more specific policy takes precedence. For the full rules, see [How resource optimization policies select and combine](auto-ro-policies.md).

To use an example, save it to a file and run `kubectl apply -f` with the file name.

### Produce recommendations in every namespace except one
<a name="auto-ro-enable-example-exclude"></a>

Kubernetes sets the `kubernetes.io/metadata.name` label on every namespace, so you can select or exclude a namespace by name without adding labels. The following policy produces recommendations for every namespace except `payments-prod`:

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: all-but-payments
spec:
  namespaceSelector:
    matchExpressions:
      - key: kubernetes.io/metadata.name
        operator: NotIn
        values: [payments-prod]
```

Resource optimization doesn’t manage workloads in `payments-prod` unless another policy selects that namespace. If you also have the `default` policy from the previous procedure, `default` still selects `payments-prod`. Use this policy in place of `default`, not alongside it.

### Apply recommendations for one team’s stateless workloads
<a name="auto-ro-enable-example-apply"></a>

The following policy selects namespaces labeled `team: search`, narrows to workloads labeled `tier: stateless`, and sets `mode: Apply`:

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: team-search
spec:
  namespaceSelector:
    matchLabels:
      team: search
  workloadSelector:
    matchLabels:
      tier: stateless
  mode: Apply
```

If you also have the `default` policy from the previous procedure, both policies select these workloads. `team-search` sets both selectors, so it’s more specific, and its `mode: Apply` takes effect. The search team’s other workloads stay in `Recommend` mode under `default`.

## Start applying recommendations
<a name="auto-ro-enable-switch-apply"></a>

To have resource optimization resize the Pods that a policy selects, set `mode: Apply` on the policy. You can set the mode in your policy manifest and apply it, or patch the policy directly. Before you do, review the recommendations on the workloads' `ResourceOptimization` objects and [Preview considerations](auto-resource-optimization.md#auto-ro-considerations).

Complete the following steps to switch a policy to `Apply`:

1. Patch the policy to set `mode: Apply`. Replace {{team-search}} with the name of your policy.

   ```bash
   kubectl patch crop {{team-search}} --type merge -p '{"spec":{"mode":"Apply"}}'
   ```

1. Confirm the new mode.

   ```bash
   kubectl get crop {{team-search}}
   ```

   An example output is as follows.

   ```bash
   NAME          MODE    PROFILE    READY   SELECTED   AGE
   team-search   Apply   Balanced   True    12         2d
   ```

Switching modes doesn’t reset the usage history that resource optimization has already collected. Workloads that already have recommendations don’t need to collect 12 hours of usage history again.

Resource optimization resizes running Pods in place, and new Pods start at the recommended size. For more information about how it applies changes and what happens when a resize doesn’t fit on a node, see [How resource optimization applies changes to Pods](auto-ro-resize.md).

## Opt out a single workload
<a name="auto-ro-enable-opt-out"></a>

To remove one workload from resource optimization regardless of which policies select it, add the `optimization.eks.amazonaws.com/enabled: "false"` annotation to the Deployment or StatefulSet. Use this annotation to stop changes to one workload without editing your policies, for example during an incident.

When you opt out a workload, resource optimization deletes its `ResourceOptimization` object. It also cancels any resize that it requested and the kubelet hasn’t applied yet. Resizes that the kubelet already applied stay in place, and new Pods start at the size in the Pod template. Opting out also deletes the workload’s usage history. If you remove the annotation later, resource optimization collects about 12 hours of usage history again before it produces recommendations.

If you manage the workload with a GitOps tool, add the annotation to the workload manifest in your repository instead of running `kubectl annotate`. Otherwise, the tool removes the annotation.

Complete the following steps to opt out a workload with `kubectl`:

1. Annotate the workload. Replace {{my-app}} and {{my-namespace}} with your values. For a StatefulSet, replace `deployment` with `statefulset`.

   ```bash
   kubectl annotate deployment {{my-app}} -n {{my-namespace}} optimization.eks.amazonaws.com/enabled="false"
   ```

1. (Optional) Return the workload’s Pods to the CPU and memory in its Pod template. Resource optimization doesn’t revert values it already applied.

   ```bash
   kubectl rollout restart deployment {{my-app}} -n {{my-namespace}}
   ```

   A StatefulSet that uses the `OnDelete` update strategy doesn’t replace its Pods when you restart it. Delete its Pods instead, and the StatefulSet controller recreates them from the Pod template.

To manage the workload again, remove the annotation.

```bash
kubectl annotate deployment {{my-app}} -n {{my-namespace}} optimization.eks.amazonaws.com/enabled-
```

## Stop resizing but keep recommendations
<a name="auto-ro-enable-pause"></a>

To stop resource optimization from changing Pods while it continues to produce recommendations, set `mode: Recommend` on the policies that set `Apply`. Replace {{team-search}} with the name of your policy.

```bash
kubectl patch crop {{team-search}} --type merge -p '{"spec":{"mode":"Recommend"}}'
```

Running Pods keep the values that resource optimization already applied. New Pods, for example from a scale-out or a rollout, start at the size in the Pod template.

## Turn off resource optimization
<a name="auto-ro-enable-turn-off"></a>

Deleting a policy stops collection, recommendations, and resizes for the workloads that it selects. Workloads that another policy also selects stay managed. Deleting the last policy in the cluster turns off resource optimization for the whole cluster.

Complete the following steps to turn off resource optimization for the whole cluster:

1. List the policies in your cluster.

   ```bash
   kubectl get crop
   ```

1. Delete each policy. Replace {{default}} with the name of each policy.

   ```bash
   kubectl delete crop {{default}}
   ```

1. Confirm that resource optimization removed its per-workload objects.

   ```bash
   kubectl get ro --all-namespaces
   ```

   When no policy selects a workload, resource optimization deletes that workload’s `ResourceOptimization` object. After you delete every policy, the command returns `No resources found`.

1. (Optional) Restart workloads to return their Pods to the CPU and memory in their Pod templates. Running Pods keep the values that resource optimization last applied until they’re replaced. New Pods start at the size in the Pod template. Replace {{my-app}} and {{my-namespace}} with your values. For StatefulSets that use the `OnDelete` update strategy, see [Opt out a single workload](#auto-ro-enable-opt-out).

   ```bash
   kubectl rollout restart deployment {{my-app}} -n {{my-namespace}}
   ```

## View policies on the console
<a name="auto-ro-enable-console"></a>

The Kubernetes resource viewer in the Amazon EKS console shows your policies and per-workload objects as read-only. For more information, see [View Kubernetes resources in the AWS Management Console](view-kubernetes-resources.md).