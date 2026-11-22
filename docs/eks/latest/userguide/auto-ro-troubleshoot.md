

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot EKS Auto Mode resource optimization

Use `kubectl` to find out why EKS Auto Mode resource optimization isn’t doing what you expect. This topic covers how to stop changes during an incident. It also covers the common reasons a workload isn’t managed, has no recommendation, or doesn’t get a recommendation applied. If you need to stop changes now, see [Stop changes and revert values during an incident](#auto-ro-troubleshoot-stop).

Resource optimization reports what it’s doing in the status of two kinds of objects:
+ A `ClusterResourceOptimizationPolicy` (`crop`) reports whether the policy works. It also reports how many workloads it selects.
+ A `ResourceOptimization` (`ro`) for each managed workload reports its recommendations and conditions. The object is in the workload’s namespace, and its name is the workload’s name with a `-deploy` or `-sts` suffix.

In the commands in this topic, replace the following placeholders:
+  {{my-app}}: the name of your Deployment or StatefulSet.
+  {{my-namespace}}: the workload’s namespace.
+  {{my-policy}}: the name of your policy.
+  {{my-pod}}: the name of one of the workload’s Pods.

The following `kubectl` commands show most of what you need:

```bash
kubectl get crop
kubectl get ro -n {{my-namespace}}
kubectl describe ro {{my-app-deploy}} -n {{my-namespace}}
kubectl get ro {{my-app-deploy}} -n {{my-namespace}} -o yaml
```

The `Conditions` section of `kubectl describe ro` lists each condition with its status, reason, and message. The message usually says how many Pods are affected and why. For every condition and reason, see [EKS Auto Mode resource optimization resource reference](auto-ro-reference.md).

## Stop changes and revert values during an incident
<a name="auto-ro-troubleshoot-stop"></a>

Resource optimization has no automatic rollback. If you think resource changes are causing a problem, first stop changes, then revert the values.

### Stop changes
<a name="_stop_changes"></a>

Use one of the following options. Each option stops new resizes for the workloads it covers. It also cancels any resize that the kubelet hasn’t applied yet. Values that the kubelet already applied stay in place.
+  **Stop changes for one workload.** Run the following command to add the opt-out annotation to the Deployment. For a StatefulSet, replace `deployment` with `statefulset`.

  ```bash
  kubectl annotate deployment {{my-app}} -n {{my-namespace}} optimization.eks.amazonaws.com/enabled="false"
  ```

  Resource optimization deletes the workload’s `ResourceOptimization` object and its recommendations. New Pods start at the values in the Pod template. This also deletes the workload’s usage history. If you opt the workload back in, the wait of about 12 hours for a first recommendation starts over. For more information, see [Opt out a single workload](auto-ro-enable.md#auto-ro-enable-opt-out).
+  **Stop changes but keep recommendations.** Set `mode: Recommend` on the policy that manages the workload. The `POLICY` column of `kubectl get ro` shows which policy that is. Run the following command:

  ```bash
  kubectl patch crop {{my-policy}} --type merge -p '{"spec":{"mode":"Recommend"}}'
  ```

  Running Pods keep their current values, new Pods start at the values in the Pod template, and recommendations and usage history are kept. For more information, see [Stop resizing but keep recommendations](auto-ro-enable.md#auto-ro-enable-pause).
+  **Turn off resource optimization for the whole cluster.** Run the following command to delete every policy. This stops data collection, recommendations, and resizes. Resource optimization deletes every `ResourceOptimization` object and the usage history of every workload. If you turn resource optimization back on, the wait for first recommendations starts over. For more information, see [Turn off resource optimization](auto-ro-enable.md#auto-ro-enable-turn-off).

  ```bash
  kubectl delete crop --all
  ```

### Revert to the values in the Pod template
<a name="_revert_to_the_values_in_the_pod_template"></a>

Resource optimization never changes your Deployment or StatefulSet. Its Pod template still has the requests and limits you wrote. After you stop changes, run the following command to restart the workload and return its Pods to those values:

```bash
kubectl rollout restart deployment {{my-app}} -n {{my-namespace}}
```

A StatefulSet that uses the `OnDelete` update strategy doesn’t replace its Pods when you restart it. Delete its Pods instead. The StatefulSet controller recreates them from the Pod template.

Outside `Apply` mode, resource optimization doesn’t size new Pods at admission, so they start at the values in the template. To confirm, run the following command to check the resources of a new Pod:

```bash
kubectl get pod {{my-pod}} -n {{my-namespace}} -o jsonpath='{range .spec.containers[*]}{.name}{"\t"}{.resources}{"\n"}{end}'
```

**Important**  
Restart the workload only after you stop changes. If the workload is still in `Apply` mode, new Pods start at the recommended values.

## Workload isn’t managed
<a name="auto-ro-troubleshoot-not-managed"></a>

 **Symptom:** `kubectl get ro -n my-namespace` doesn’t list an object for the workload.

Check the following causes in order:

1.  **No policy exists.** `kubectl get crop` returns `No resources found`. Create a policy. For more information, see [Turn on resource optimization with default settings](auto-ro-enable.md#auto-ro-enable-default).

1.  **The workload is in a system namespace.** Resource optimization never manages workloads in `kube-system`, `kube-public`, or `kube-node-lease`.

1.  **The workload isn’t a Deployment or StatefulSet.** Resource optimization doesn’t manage DaemonSets, Jobs, CronJobs, or bare Pods.

1.  **The workload opts out.** Check for the annotation.

   ```bash
   kubectl get deployment {{my-app}} -n {{my-namespace}} -o jsonpath='{.metadata.annotations.optimization\.eks\.amazonaws\.com/enabled}'
   ```

   If the output is `false`, remove the annotation to opt the workload back in.

1.  **No policy selects the workload.** Compare each policy’s selectors with the labels on the namespace and on the workload object.

   ```bash
   kubectl get namespace {{my-namespace}} --show-labels
   kubectl get deployment {{my-app}} -n {{my-namespace}} --show-labels
   kubectl get crop -o yaml
   ```

    `workloadSelector` matches the labels on the Deployment or StatefulSet object, not the labels in its Pod template. This is a common reason a policy doesn’t select a workload. Add the label to the workload’s `metadata.labels`, or change the selector.

1.  **The policy isn’t Ready, or didn’t sync the workload.** See [Policy isn’t Ready, or some workloads didn’t sync](#auto-ro-troubleshoot-policy).

## Policy isn’t Ready, or some workloads didn’t sync
<a name="auto-ro-troubleshoot-policy"></a>

 **Symptom:** The `READY` column of `kubectl get crop` is `False`, or the policy’s `WorkloadsSynced` condition is `False`.

Run `kubectl describe crop my-policy` and check the conditions. `WorkloadsSynced` doesn’t affect `Ready`, so the policy keeps managing the workloads that did sync. The following table lists the conditions, their causes, and what to do.


| Condition and reason | Cause | Action | 
| --- | --- | --- | 
|  `SelectorsValid` is `False`, reason `InvalidSelector`. `Ready` is `False`. |  `namespaceSelector` or `workloadSelector` can’t be parsed, for example because of an unknown `operator`. The Kubernetes API server accepts the policy, but resource optimization ignores it until you fix it. The message shows the error. | Fix the selector. Valid operators are `In`, `NotIn`, `Exists`, and `DoesNotExist`. `In` and `NotIn` need at least one value. | 
|  `WorkloadsSynced` is `False`, reason `SyncFailed`. The message says that a workload `already has a ResourceOptimization not created by a policy`, or that its `name is held by a ResourceOptimization not created by a policy`. | The workload already has a `ResourceOptimization` object that you or someone else created by hand. Hand-written objects aren’t supported in this preview. Resource optimization leaves that object alone and doesn’t create its own. | Delete the hand-written object. The policy then creates its own object for the workload. To control which workloads resource optimization manages, use a policy’s `workloadSelector` or the opt-out annotation. | 
|  `WorkloadsSynced` is `False`, reason `SyncFailed`, with a message that says resource optimization `could not create` or `could not update` the object. | A temporary error. | Resource optimization retries automatically. If the condition stays, contact AWS Support. | 

## There’s no recommendation yet
<a name="auto-ro-troubleshoot-no-recommendation"></a>

 **Symptom:** The `ResourceOptimization` object exists, but `status.recommendations` is empty. In `Apply` mode, the `AdmissionSizing` condition is `False` with reason `NoRecommendationYet`.

 **Cause:** Resource optimization makes the first recommendation for a container about 12 hours after it collects the container’s first usage sample. Deleting the workload’s `ResourceOptimization` object deletes its usage history, and the wait starts over. That happens when you opt the workload out, when no valid policy selects it any longer, or when you delete the last policy that selects it.

 **Action:** Wait. Changing the policy’s `mode` doesn’t reset the wait or produce a recommendation sooner.

## Recommendation wasn’t applied
<a name="auto-ro-troubleshoot-no-resize"></a>

 **Symptom:** The object has a recommendation, but running Pods still have their old requests.

Run the following commands to check the `phase` of each recommendation and the conditions. Then find what you see in the table that follows.

```bash
kubectl get ro {{my-app-deploy}} -n {{my-namespace}} -o jsonpath='{range .status.recommendations[].verticalRecommendations[]}{.containerName}{"\t"}{.phase}{"\n"}{end}'
kubectl describe ro {{my-app-deploy}} -n {{my-namespace}}
```


| What you see | Cause | Action | 
| --- | --- | --- | 
| The `MODE` column is `Recommend`, and the phase is `Recommended`. | The workload is in `Recommend` mode. Resource optimization publishes recommendations and doesn’t change Pods. | To apply recommendations, set `mode: Apply` on the winning policy, shown in the `POLICY` column. If another, equally specific policy that selects the workload is in `Recommend` mode, it wins the tie, so set that policy to `Apply` too. See [How resource optimization policies select and combine](auto-ro-policies.md). | 
|  `Ready` is `False`, reason `VPAConflict`. | A VerticalPodAutoscaler that isn’t in `Off` mode targets the workload. Resource optimization doesn’t apply recommendations while it does, so the two don’t fight over the same Pods. | Choose one tool for the workload. Set the VerticalPodAutoscaler’s `spec.updatePolicy.updateMode` to `Off` or delete it, or opt the workload out of resource optimization. | 
|  `HPAResourceConflict` is `True`. | A HorizontalPodAutoscaler scales on the utilization of that resource. See [Resource is left alone because of a HorizontalPodAutoscaler](#auto-ro-troubleshoot-hpa). | None. This is expected. | 
|  `InPlaceResizeUnsupported` is `True`, reason `SandboxRuntime`. | The Pods run in a Nitro sandbox, under the `isolated-sandbox` or `confidential-sandbox` RuntimeClass. The sandbox runtime doesn’t support in-place resizes. | None. Resource optimization keeps publishing recommendations. To use them, set the values in the Pod template yourself. | 
| The phase is `Recommended`, and the `reason` says that the container declares no request. | The container declares neither a request nor a limit for the resource. Adding a request in place would change the Pod’s quality of service class, so resource optimization only recommends a value. | To apply the value, add the request to the Pod template yourself. | 
|  `InPlaceInfeasible` is `True`, reason `NodeCannotHoldResize`. The Pod might have a `ResizeInfeasible` Warning event. | The Pod’s node doesn’t have room for the larger request. If the kubelet reports the resize as `Deferred`, there’s no event, and the resize can still apply when the node has room. Otherwise, the Pod keeps its size until it’s replaced. | None. When the Pod is replaced, for example during a rollout, scale-out, or node consolidation, the new Pod starts at the recommended size on a node that fits. To replace the Pods sooner, restart the workload. | 
|  `MemoryDecreaseHeld` is `True`, reason `MemoryInUse` or `MemoryDecreaseRefused`. | The recommended memory limit would be less than 10% above the Pod’s recent memory usage, or the kubelet refused the decrease. Resource optimization applies the rest of the resize and keeps the current memory. | None. Resource optimization lowers memory when usage drops. If usage stays high, the next recommendation accounts for it. | 
|  `ScaleLimited` is `True`, reason `InsufficientNodeCapacity`. | The recommendation is larger than the nodes your NodePools can launch, so resource optimization capped it. | Allow larger instance types in your NodePools, or accept the capped value. | 
| The phase is `InProgress` for a long time, and none of the previous conditions are `True`. | The kubelet hasn’t finished the resize, or resource optimization is waiting before it sends one. For example, resource optimization waits while it can’t read the workload’s HorizontalPodAutoscalers or VerticalPodAutoscalers, because it doesn’t change a workload until it can confirm that no autoscaler holds a resource. No condition reports this wait. | Run `kubectl describe pod my-pod` and check the `PodResizePending` and `PodResizeInProgress` conditions. If the Pod shows no resize, resource optimization retries automatically. If the phase stays `InProgress`, contact AWS Support. | 

## New Pods don’t start at the recommended size
<a name="auto-ro-troubleshoot-new-pods"></a>

 **Symptom:** In `Apply` mode, new Pods start at the values in the Pod template, and resource optimization then resizes them.

 **Cause:** Resource optimization sizes new Pods at admission only when the `AdmissionSizing` condition is `True`. Run the following command to check its reason. Then find the reason in the table that follows.

```bash
kubectl get ro {{my-app-deploy}} -n {{my-namespace}} -o jsonpath='{.status.conditions[?(@.type=="AdmissionSizing")]}'
```


| Reason | Cause and action | 
| --- | --- | 
|  `RecommendMode`  | The workload is in `Recommend` mode. Expected. | 
|  `NoRecommendationYet`  | There’s no recommendation yet. See [There’s no recommendation yet](#auto-ro-troubleshoot-no-recommendation). | 
|  `NotReady`  | The `Ready` condition is `False`, for example because of `VPAConflict`. Resolve the `Ready` condition first. | 
|  `StartupBoost`  | The workload has the `startup-boost` annotation and resource optimization hasn’t recorded its startup status yet. This clears on its own. After that, the reason is `SizedExceptStartupCPU`: new Pods start with the raised startup CPU from the template and the recommended memory. | 
|  `RecommendOnly`  | The workload’s containers declare neither a request nor a limit for CPU or memory, so there’s nothing to set at admission. Add requests to the Pod template if you want resource optimization to size new Pods. | 
|  `SandboxRuntime`  | The Pods run in a Nitro sandbox, which doesn’t support resizing. Resource optimization doesn’t size them. Expected. | 
|  `SelectorOverlap`  | The workload’s Pod label selector overlaps the selector of another workload that resource optimization manages. While they overlap, resource optimization doesn’t size either workload’s new Pods at admission. Give each workload a distinct selector. | 
|  `WorkloadSelectorUnavailable`  | Resource optimization couldn’t find the workload or its Pod label selector. Check that the Deployment or StatefulSet named in the object’s `spec.scaleTargetRef` exists. | 
|  `AdmissionSizingUnavailable`  | The cluster doesn’t serve the `MutatingAdmissionPolicy` API. Upgrade the cluster to Kubernetes 1.36 or later. | 
|  `AdmissionSizingNotPermitted`, `AdmissionPolicyMissing`, `ReconcileFailed`  | A problem on the AWS side. Resource optimization retries automatically. If the condition stays, contact AWS Support. | 

**Important**  
Resource optimization doesn’t take LimitRange objects into account when it sizes new Pods. If a namespace has a LimitRange, the API server can reject new Pods that are sized to a recommendation. For example, the recommendation can exceed the LimitRange maximum, fall below its minimum, or break its `maxLimitRequestRatio`. Change the LimitRange to allow the recommendations, or opt the workload out.

## Workload keeps running out of memory
<a name="auto-ro-troubleshoot-oom"></a>

In `Apply` mode, when the kubelet kills a container for running out of memory, resource optimization raises its memory. It raises memory 1.2 times on the first kill, 1.5 times on the second, and 2 times from the third. If a Pod’s node can’t hold the increase, resource optimization evicts the Pod so that its replacement starts at the new size. It evicts Pods only while new Pods are sized at admission, that is, while the `AdmissionSizing` condition is `True`.

If the container keeps getting killed, run `kubectl describe ro my-app-deploy -n my-namespace` and find the condition in the following table. For Java workloads, also check `HeapUndetected` and `HeapFloorInfeasible`, and see [How resource optimization works with autoscalers and workload types](auto-ro-workloads.md).


| Condition and reason | Cause | Action | 
| --- | --- | --- | 
|  `OOMAtMaximum` is `True`, reason `MemoryCapReached`. `status.oomMemoryCaps` has an entry with `source: Maximum`. | Memory is already at the `Maximum` constraint, which is twice the largest memory limit in the Pod template. | Raise the memory limit in the Pod template. Resource optimization recalculates the `Maximum` from the template. | 
|  `OOMAtMaximum` is `True`, reason `MemoryCapReached`. `status.oomMemoryCaps` has an entry with `source: NodeCapacity`. | Memory is already as large as the largest node the Pod can run on. | Allow larger instance types in your NodePools, or reduce the workload’s memory use. | 
|  `OOMRaiseRejected` is `True`, reason `RejectedByPolicy`. | A ResourceQuota, LimitRange, validating webhook, or ValidatingAdmissionPolicy in your cluster rejected the increase. The message names it and the resources the increase asked for. | Change the quota, limit, or policy to allow the increase. Resource optimization retries automatically. | 
|  `InPlaceInfeasible` is `True`, and `AdmissionSizing` is `False`. | The node can’t hold the increase, and new Pods aren’t sized at admission, so a replacement would start at the template size. Resource optimization doesn’t evict the Pod, and it keeps its size. | Fix the `AdmissionSizing` reason. See [New Pods don’t start at the recommended size](#auto-ro-troubleshoot-new-pods). Or raise the memory in the Pod template. | 
|  `EvictionRefused` is `True`, reason `DisruptionBudget`. | A PodDisruptionBudget doesn’t allow the eviction. Resource optimization never deletes Pods, so the Pod waits. | Allow the eviction. If the budget is already breached because Pods are crashing, set `unhealthyPodEvictionPolicy: AlwaysAllow` on the PodDisruptionBudget so that Pods that aren’t Ready can be evicted. | 
|  `HPAResourceConflict` is `True` and `status.resourceOwnership` lists `memory`. | A HorizontalPodAutoscaler scales on memory utilization. Resource optimization doesn’t raise memory that a HorizontalPodAutoscaler scales on. | Raise the memory request in the Pod template, or scale on a different metric. | 

## Resource is left alone because of a HorizontalPodAutoscaler
<a name="auto-ro-troubleshoot-hpa"></a>

 **Symptom:** Resource optimization recommends a value for CPU or memory but never applies it. The `HPAResourceConflict` condition is `True`, and `status.resourceOwnership.vertical` lists the resource and the HorizontalPodAutoscaler.

 **Cause:** This is expected. A HorizontalPodAutoscaler that scales on the utilization of a resource calculates utilization from its request. If resource optimization changed that request, it would change when the HorizontalPodAutoscaler scales. Resource optimization leaves the resource alone and still sizes the other one. For example, with a HorizontalPodAutoscaler on CPU utilization, resource optimization still sizes memory. KEDA works the same way through the HorizontalPodAutoscaler it creates.

 **Action:** None. `Ready` stays `True`. For more information, see [How resource optimization works with autoscalers and workload types](auto-ro-workloads.md).

## Startup boost doesn’t return CPU
<a name="auto-ro-troubleshoot-startup-boost"></a>

 **Symptom:** A workload has the `optimization.eks.amazonaws.com/startup-boost: "true"` annotation, but its Pods keep the raised startup CPU after they’re Ready.

Run the following command to check the `StartupShrinkBlocked` condition and `status.startupShrink`. Then find the reason in the table that follows.

```bash
kubectl get ro {{my-app-deploy}} -n {{my-namespace}} -o jsonpath='{.status.startupShrink}{"\n"}{.status.conditions[?(@.type=="StartupShrinkBlocked")]}'
```


| Reason | Cause and action | 
| --- | --- | 
|  `RecommendMode`  | Startup boost works only in `Apply` mode. Set `mode: Apply` on the policy. | 
|  `SteadyRecommendationUnavailable`  | Resource optimization doesn’t have a steady-state CPU recommendation for the container yet, which takes about 12 hours of data. Wait. | 
|  `CPUScaledByHPA`  | A HorizontalPodAutoscaler scales the workload on CPU, so resource optimization doesn’t change CPU. You can’t use startup boost with it. | 
|  `PodLevelResources`  | The Pod template uses Pod-level resources, which startup boost doesn’t support. | 
|  `VPAConflict`  | A VerticalPodAutoscaler that isn’t in `Off` mode targets the workload. | 
|  `SandboxRuntime`  | The Pods run in a Nitro sandbox, which doesn’t support in-place resizes. You can’t use startup boost with it. | 
|  `PodResizeBlocked`  | The kubelet reported the resize as `Infeasible` or failed it with an `Error`, or a Pod is still at its startup CPU 2 minutes after its startup ended. Run `kubectl describe pod my-pod` and check the `PodResizePending` and `PodResizeInProgress` conditions. | 

A Pod’s startup ends when it’s Ready. If the Pod has no readiness or startup probe, it’s Ready as soon as its containers start. Resource optimization then waits 10 minutes from Pod creation before it returns the CPU. Add a readiness or startup probe that passes only when startup is done.