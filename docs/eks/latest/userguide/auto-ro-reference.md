

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# EKS Auto Mode resource optimization resource reference

EKS Auto Mode resource optimization uses two Kubernetes resources in the `eks.amazonaws.com/v1beta1` API group and two annotations that you set on workloads. Every EKS Auto Mode cluster that runs Kubernetes 1.36 or later includes the custom resource definitions. There’s no Amazon EKS API field for resource optimization.


| Kind | Short name | Scope | Who creates it | 
| --- | --- | --- | --- | 
|  `ClusterResourceOptimizationPolicy`  |  `crop`  | Cluster | You. A policy turns on resource optimization and selects workloads. | 
|  `ResourceOptimization`  |  `ro`  | Namespace | Resource optimization, one for each workload that a policy selects. You read it, but you don’t create it. | 

## ClusterResourceOptimizationPolicy
<a name="auto-ro-reference-crop"></a>

A `ClusterResourceOptimizationPolicy` selects workloads and sets the mode and profile they get. Policies are the only switch for resource optimization: creating the first policy turns it on, and deleting the last one turns it off. For how several policies combine, see [How resource optimization policies select and combine](auto-ro-policies.md).

### Example – ClusterResourceOptimizationPolicy
<a name="auto-ro-reference-crop-example"></a>

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ClusterResourceOptimizationPolicy
metadata:
  name: search-web
spec:
  mode: Apply
  profile: Balanced
  namespaceSelector:
    matchLabels:
      team: search
  workloadSelector:
    matchExpressions:
      - key: tier
        operator: In
        values:
          - web
          - api
```

The smallest valid policy is `spec: {}`. It selects every Deployment and StatefulSet in every non-system namespace, in `Recommend` mode with the `Balanced` profile.

### Spec fields
<a name="auto-ro-reference-crop-spec"></a>

The following table describes the fields that you can set in a policy’s `spec`.


| Field | Values | Default | Description | 
| --- | --- | --- | --- | 
|  `mode`  |  `Recommend`, `Apply`  |  `Recommend`  |  `Recommend` publishes recommendations and doesn’t change Pods. `Apply` also resizes running Pods in place and sizes new Pods at admission. | 
|  `profile`  |  `Balanced`  |  `Balanced`  | The sizing targets for recommendations. `Balanced` is the only profile in this preview. For its values, see [Balanced profile](#auto-ro-reference-balanced). | 
|  `namespaceSelector`  | A Kubernetes label selector | Not set. Selects every non-system namespace. | Selects namespaces by their labels. To select namespaces by name, use the `kubernetes.io/metadata.name` label. The `kube-system`, `kube-public`, and `kube-node-lease` namespaces are always excluded. | 
|  `workloadSelector`  | A Kubernetes label selector | Not set. Selects every Deployment and StatefulSet in the selected namespaces. | Selects workloads by the labels on the Deployment or StatefulSet object, not the labels in its Pod template. | 

### Status fields
<a name="auto-ro-reference-crop-status"></a>

 `kubectl get crop` shows the `MODE`, `PROFILE`, `READY`, and `SELECTED` columns. The full status has the following fields.


| Field | Description | 
| --- | --- | 
|  `selectedWorkloads`  | The number of workloads this policy selects that don’t opt out, including any that failed to sync. A workload that more than one policy selects counts on each of them. | 
|  `optedOutWorkloads`  | The number of workloads this policy selects that opt out with the `optimization.eks.amazonaws.com/enabled: "false"` annotation. A workload that more than one policy selects counts on each of them. | 
|  `conditions`  | The conditions in the following table. | 

The following table describes the conditions of a policy.


| Condition | Reason when `False`  | Description | 
| --- | --- | --- | 
|  `Ready`  |  `UnhealthyDependents`  |  `True` when the policy’s selectors are valid and resource optimization uses the policy. When `False`, the message names the condition that failed, for example `SelectorsValid=False`. | 
|  `SelectorsValid`  |  `InvalidSelector`  |  `False` when `namespaceSelector` or `workloadSelector` can’t be parsed. The Kubernetes API server accepts invalid selectors, so this condition is where you see the error. Resource optimization skips the policy until you fix it. | 
|  `WorkloadsSynced`  |  `SyncFailed`  |  `False` when resource optimization couldn’t create or update the `ResourceOptimization` object for one or more selected workloads. The message gives the count and names the workloads. This condition doesn’t affect `Ready`. | 

## ResourceOptimization
<a name="auto-ro-reference-ro"></a>

Resource optimization creates a `ResourceOptimization` object in the workload’s namespace for each Deployment or StatefulSet that a policy selects. The object records the workload’s settings, its recommendations, and conditions that explain what resource optimization is doing. Don’t edit these objects, because resource optimization overwrites their spec from the winning policy. Creating your own `ResourceOptimization` objects isn’t supported in this preview. To control which workloads resource optimization manages, use a policy’s `workloadSelector` or the opt-out annotation.

Name  
The workload’s name followed by `-deploy` for a Deployment or `-sts` for a StatefulSet. For example, the object for Deployment `checkout` is `checkout-deploy`. If the result would be longer than 253 characters, resource optimization shortens the workload’s name and adds an 8-character hash before the suffix.

Owners  
Every policy that selects the workload is an owner reference. The winning policy’s owner reference has `controller: true`. It’s the same policy named in `status.policySource`.

Deletion  
Resource optimization deletes the object when no valid policy selects the workload, or when the workload opts out. For example, deleting the last policy that selects a workload, changing the workload’s labels, or making a selector invalid deletes the object. This also deletes the workload’s usage history. If the workload is managed again, the wait of about 12 hours for a first recommendation starts over.

### Example – ResourceOptimization
<a name="auto-ro-reference-ro-example"></a>

The following object is for a Deployment named `checkout` with one container that declares requests of `cpu: 250m` and `memory: 256Mi` and limits of `cpu: 500m` and `memory: 512Mi`.

```yaml
apiVersion: eks.amazonaws.com/v1beta1
kind: ResourceOptimization
metadata:
  name: checkout-deploy
  namespace: shop
  ownerReferences:
    - apiVersion: eks.amazonaws.com/v1beta1
      kind: ClusterResourceOptimizationPolicy
      name: team-shop
      controller: true
      uid: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
spec:
  scaleTargetRef:
    kind: Deployment
    name: checkout
  mode: Apply
  profile: Balanced
  objectives:
    - dimension: Vertical
      resource:
        metric: cpu
        utilization: 87
    - dimension: Vertical
      resource:
        metric: memory
        utilization: 70
  constraints:
    - operator: Minimum
      resources:
        cpu: 125m
        memory: 128Mi
    - operator: Maximum
      resources:
        cpu: "1"
        memory: 1Gi
status:
  policySource:
    mode: team-shop
    profile: team-shop
  recommendations:
    - type: Vertical
      verticalRecommendations:
        - containerName: checkout
          request:
            cpu: 140m
            memory: 300Mi
          limit:
            cpu: 280m
            memory: 600Mi
          phase: Applied
          reason: "Vertical scaling recommendation: CPU request: 140m, CPU limit: 280m, Memory request: 300Mi, Memory limit: 600Mi"
          createTime: "2026-11-18T10:00:00Z"
          lastUpdateTime: "2026-11-18T10:02:00Z"
  conditions:
    - type: Ready
      status: "True"
      reason: Ready
      message: ""
      lastTransitionTime: "2026-11-17T22:00:00Z"
    - type: AdmissionSizing
      status: "True"
      reason: Sized
      message: new pods are created at the recommended size
      lastTransitionTime: "2026-11-18T10:00:00Z"
```

 `kubectl get ro` shows the `KIND`, `TARGET`, `POLICY`, and `MODE` columns. `POLICY` is the policy that supplied the mode.

### Spec fields
<a name="auto-ro-reference-ro-spec"></a>

Resource optimization sets every spec field from the winning policy and the workload’s Pod template. Treat them as read-only. The following table describes each field.


| Field | Description | 
| --- | --- | 
|  `scaleTargetRef.kind`  |  `Deployment` or `StatefulSet`. | 
|  `scaleTargetRef.name`  | The name of the workload. | 
|  `mode`  |  `Recommend` or `Apply`, from the winning policy. | 
|  `profile`  |  `Balanced`, from the winning policy. | 
|  `objectives`  | The utilization targets that the profile sets. With `Balanced`, CPU is `87` and memory is `70`. Each entry has `dimension: Vertical` and a `resource` with `metric` (`cpu` or `memory`) and `utilization` (a percentage). | 
|  `constraints`  | The lowest and highest values that a recommendation can have, calculated from the profile and the requests and limits in the Pod template. Each entry has an `operator` (`Minimum` or `Maximum`) and `resources`. A resource missing from `Maximum` has no upper bound. For how resource optimization calculates the values, see [Balanced profile](#auto-ro-reference-balanced). | 

### Status fields
<a name="auto-ro-reference-ro-status"></a>

The following table describes the `status` fields of a `ResourceOptimization` object.


| Field | Description | 
| --- | --- | 
|  `policySource`  | The policy that supplied each spec field, for example `mode: team-shop`. | 
|  `recommendations[].type`  |  `Vertical`. | 
|  `recommendations[].verticalRecommendations[].containerName`  | The container that the recommendation is for. Not set for a recommendation for the whole Pod, when the Pod template uses Pod-level resources. | 
|  `recommendations[].verticalRecommendations[].request`  | The recommended CPU and memory requests. | 
|  `recommendations[].verticalRecommendations[].limit`  | The recommended CPU and memory limits. Resource optimization keeps each container’s ratio of request to limit from the Pod template, so a Pod’s quality of service class doesn’t change. A resource with no limit in the template gets no limit. | 
|  `recommendations[].verticalRecommendations[].reason`  | A description of the recommendation. If a HorizontalPodAutoscaler holds part of the recommendation, the reason ends with the resources that weren’t applied. If the container declares no request for a resource, the reason says that the value is a recommendation only. | 
|  `recommendations[].verticalRecommendations[].phase`  | See [Recommendation phases](#auto-ro-reference-phases). | 
|  `recommendations[].verticalRecommendations[].createTime`, `lastUpdateTime`  | When the recommendation was created and last changed. | 
|  `resourceOwnership.vertical[]`  | Resources that a HorizontalPodAutoscaler scales on, so resource optimization publishes recommendations for them but doesn’t apply them. Each entry has `resource`, `container`, `owner` (the HorizontalPodAutoscaler), and `reason` (`ResourceMetric` or `ContainerResourceMetric`). | 
|  `oomMemoryCaps[]`  | Containers whose memory resource optimization couldn’t raise after an out-of-memory kill because memory is already at its cap. Each entry has `container`, `memory`, `limit`, `source` (`Maximum` or `NodeCapacity`), and `lastOOMTime`. | 
|  `startupShrink`  | Present only for a workload with the `startup-boost` annotation. Counts of the workload’s Ready Pods: `eligiblePods`, `matchingPods`, `pendingPods`, and `blockedPods`. `eligiblePods` equals the sum of the other three. | 
|  `newPodSize`  | Present only for a workload with the `startup-boost` annotation. For each container whose CPU resource optimization lowers below the template’s CPU after startup, the CPU request a new Pod starts with, under `<container>.requests.cpu`. Not set when the recommendation is at or above the template’s CPU, when a HorizontalPodAutoscaler holds CPU, or when the Pod template uses Pod-level resources. | 
|  `conditions`  | See [Conditions](#auto-ro-reference-ro-conditions). | 

### Recommendation phases
<a name="auto-ro-reference-phases"></a>


| Phase | Meaning | 
| --- | --- | 
|  `Recommended`  | Resource optimization produced the recommendation and isn’t applying it. Either the mode is `Recommend`, or resource optimization can’t apply any value in it, for example because a HorizontalPodAutoscaler holds the resource or the container declares no request for it. | 
|  `Pending`  | The mode is `Apply` and the recommendation is queued. This phase usually lasts only a moment. | 
|  `InProgress`  | Resource optimization is applying the recommendation, or waiting until it can. For example, it waits while a VerticalPodAutoscaler targets the workload, while it can’t read the workload’s autoscalers, or while the Pods run in a sandbox. | 
|  `Applied`  | The kubelet applied the resize. | 

### Conditions
<a name="auto-ro-reference-ro-conditions"></a>

Most conditions appear only in `Apply` mode, and only when they apply to the workload. For what to do about each one, see [Troubleshoot EKS Auto Mode resource optimization](auto-ro-troubleshoot.md).


| Condition | Reasons | Meaning | 
| --- | --- | --- | 
|  `Ready`  |  `VPAConflict`, `InvalidScaleTargetRef`, `NoPolicy`, `SystemNamespace`, `OptedOut`  |  `False` when resource optimization can’t manage the workload. `VPAConflict` means a VerticalPodAutoscaler that isn’t in `Off` mode targets the workload. Resource optimization keeps publishing recommendations but doesn’t apply them. `InvalidScaleTargetRef` means the workload can’t be found. `NoPolicy`, `SystemNamespace`, and `OptedOut` appear only on a `ResourceOptimization` object that you created yourself, which isn’t supported in this preview. | 
|  `HPAResourceConflict`  |  `PartialOwnership`, `NoEligibleObjectives`  |  `True` when a HorizontalPodAutoscaler scales on the CPU or memory utilization of the workload, so resource optimization leaves that resource alone. `NoEligibleObjectives` means the HorizontalPodAutoscalers hold every resource that resource optimization sizes, for every container. `Ready` stays `True`. | 
|  `AdmissionSizing`  |  `True`: `Sized`, `SizedExceptStartupCPU`. `False`: `RecommendMode`, `RecommendOnly`, `NoRecommendationYet`, `StartupBoost`, `NotReady`, `SandboxRuntime`, `SelectorOverlap`, `WorkloadSelectorUnavailable`, `UnsupportedWorkloadKind`, `AdmissionSizingUnavailable`, `AdmissionSizingNotPermitted`, `AdmissionPolicyMissing`, `ReconcileFailed`, and on objects you created yourself, `NoPolicy`, `SystemNamespace`, `OptedOut`  | Whether new Pods start at the recommended size. | 
|  `InPlaceInfeasible`  |  `True`: `NodeCannotHoldResize`. `False`: `ResizesFit`. |  `True` when some Pods can’t be resized because their node doesn’t have room. The message gives the number of Pods. | 
|  `InPlaceResizeUnsupported`  |  `SandboxRuntime`  |  `True` when the Pod template uses the `isolated-sandbox` or `confidential-sandbox` RuntimeClass. Pods in a Nitro sandbox can’t be resized in place, so resource optimization publishes recommendations but doesn’t change the Pods, including at admission. | 
|  `EvictionRefused`  |  `True`: `DisruptionBudget`. `False`: `EvictionsAllowed`. |  `True` when a PodDisruptionBudget prevents resource optimization from evicting a Pod it needs to replace after an out-of-memory kill. | 
|  `MemoryDecreaseHeld`  |  `True`: `MemoryInUse`, `MemoryDecreaseRefused`. `False`: `MemoryDecreasesApplied`. |  `Apply` mode only. `True` when some Pods keep their current memory. `MemoryInUse` means the recommended limit would be less than 10% above the Pod’s recent memory usage. `MemoryDecreaseRefused` means the kubelet refused the decrease. Resource optimization lowers memory once usage allows. | 
|  `OOMRaiseRejected`  |  `True`: `RejectedByPolicy`. `False`: `RaisesAllowed`. |  `True` when something in your cluster rejects a memory increase after an out-of-memory kill. It can be a ResourceQuota, a LimitRange, a validating webhook, or a ValidatingAdmissionPolicy. The message names what rejected it. | 
|  `OOMAtMaximum`  |  `MemoryCapReached`  |  `True` when a container was killed for running out of memory and its memory is already at the `Maximum` constraint or at the largest node that can run the Pod. | 
|  `ScaleLimited`  |  `InsufficientNodeCapacity`, `NodeCapacityBelowFloor`  |  `True` when a recommendation was capped, for example at the capacity of the nodes your NodePools can launch. | 
|  `StartupShrinkPending`  |  `True`: `PodResizePending`. `False`: `NoPendingPods`. | Startup boost only. `True` while resource optimization is returning startup CPU on some Pods. | 
|  `StartupShrinkBlocked`  |  `True`: `RecommendMode`, `PodLevelResources`, `CPUScaledByHPA`, `SteadyRecommendationUnavailable`, `VPAConflict`, `SandboxRuntime`, `PodResizeBlocked`. `False`: `NotBlocked`. | Startup boost only. `True` when resource optimization can’t return startup CPU. | 
|  `CPUFloorWaived`  |  `True`: `StartupBoost`. `False`: `OwnBounds`. | Startup boost only. `True` when the workload has no CPU `Minimum` because its declared CPU is the raised startup value. | 
|  `HeapUndetected`  |  `NoUnambiguousMaximumHeap`  |  `True` when a Java container’s maximum heap size can’t be determined, so resource optimization can’t keep memory above it. | 
|  `HeapFloorInfeasible`  |  `MaximumBelowFloor`, `MemoryLimitBelowFloor`, `NodeCapacityBelowFloor`, `MemoryLimitAboveMaximum`  |  `True` when memory can’t be kept above a Java container’s heap, because the `Maximum` constraint, the container’s memory limit, or the node size is below it. `MemoryLimitAboveMaximum` means a Guaranteed Pod’s memory limit, which resource optimization keeps unchanged for a `-XX:MaxRAMPercentage` heap, is above the `Maximum`. | 

## Balanced profile
<a name="auto-ro-reference-balanced"></a>

 `Balanced` is the only profile in this preview. The following table shows the values that resource optimization calculates from the workload’s Pod template, as you wrote it.


| Setting | Value | 
| --- | --- | 
| CPU request | 1.15 times the 95th percentile of per-minute average CPU usage. The objective is written as `utilization: 87`. | 
| Memory request | 1.43 times the 95th percentile of per-minute peak memory usage. The objective is written as `utilization: 70`. | 
|  `Minimum`  | Half of the smallest request that any container in the Pod declares for the resource. | 
|  `Maximum`  | Twice the largest limit that any container in the Pod declares for the resource. If any container declares a request for the resource without a limit, there’s no `Maximum` for that resource. Recommendations can then grow up to the size of the largest node the Pod can run on. | 
| Limits | Each container keeps the ratio of request to limit from its Pod template. Resource optimization doesn’t add a limit to a container that doesn’t have one. | 

Every container in the Pod, including sidecars, shares one `Minimum` and one `Maximum` for each resource. A container that declares only a limit counts its limit as its request.

A container that declares neither a request nor a limit for a resource still gets a recommendation. Resource optimization never applies that value, because adding a request would change the Pod’s quality of service class.

A workload with the `startup-boost` annotation has no CPU `Minimum`, because its declared CPU is the raised startup value. Its `CPUFloorWaived` condition is `True`.

## Workload annotations
<a name="auto-ro-reference-annotations"></a>

Set these annotations in the `metadata.annotations` of the Deployment or StatefulSet, not in its Pod template. Annotation values are strings, so quote them in YAML.


| Annotation | Value | Effect | 
| --- | --- | --- | 
|  `optimization.eks.amazonaws.com/enabled`  |  `"false"`  | Opts the workload out of resource optimization, whatever the policies select. Resource optimization deletes the workload’s `ResourceOptimization` object. Values already applied to running Pods stay in place. | 
|  `optimization.eks.amazonaws.com/startup-boost`  |  `"true"`  | Turns on startup boost. Set a raised CPU request in the Pod template for startup. In `Apply` mode, resource optimization returns the extra CPU in place after each Pod is Ready. | 