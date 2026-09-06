

# Task governance for model deployment on HyperPod
<a name="sagemaker-hyperpod-model-deployment-task-gov"></a>

This section covers how to optimize your shared Amazon SageMaker HyperPod EKS clusters for real-time inference workloads. You'll learn to configure Kueue's task governance features—including quota management, priority scheduling, and resource sharing policies—to ensure your inference workloads get the GPU resources they need during traffic spikes while maintaining fair allocation across your teams' training, evaluation, and testing activities. For more general information on task governance, see [SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md) .

## How inference workload management works
<a name="sagemaker-hyperpod-model-deployment-task-gov-how"></a>

To effectively manage real-time inference traffic spikes in shared HyperPod EKS clusters, implement the following task governance strategies using Kueue's existing capabilities.

**Priority class configuration**

Define dedicated priority classes for inference workloads with high weights (such as 100) to ensure inference pods are admitted and scheduled before other task types. This configuration enables inference workloads to preempt lower-priority jobs during cluster load, which is critical for maintaining low-latency requirements during traffic surges.

**Quota sizing and allocation**

Reserve sufficient GPU resources in your team's `ClusterQueue` to handle expected inference spikes. During periods of low inference traffic, unused quota resources can be temporarily allocated to other teams' tasks. When inference demand increases, these borrowed resources can be reclaimed to prioritize pending inference pods. For more information, see [Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/).

**Resource Sharing Strategies**

Choose between two quota sharing approaches based on your requirements:

1. **Strict Resource Control:** Disable quota lending and borrowing to guarantee reserved GPU capacity is always available for your workloads. This approach requires sizing quotas large enough to independently handle peak demand and may result in idle nodes during low-traffic periods.

1. **Flexible Resource Sharing:** Enable quota borrowing to use idle resources from other teams when needed. Borrowed pods are marked as preemptible and may be evicted if the lending team reclaims capacity.

**Intra-Team Preemption**

Enable intra-team preemption when running mixed workloads (evaluation, training, and inference) under the same quota. This allows Kueue to preempt lower-priority jobs within your team to accommodate high-priority inference pods, ensuring real-time inference can run without depending on external quota borrowing. For more information, see [Preemption](https://kueue.sigs.k8s.io/docs/concepts/preemption/).

## Sample inference workload setup
<a name="sagemaker-hyperpod-model-deployment-task-gov-example"></a>

The following example shows how Kueue manages GPU resources in a shared Amazon SageMaker HyperPod cluster.

**Cluster configuration and policy setup**  
Your cluster has the following configuration:
+ **Team A**: 10 P4 GPU quota
+ **Team B**: 20 P4 GPU quota
+ **Static provisioning**: No autoscaling
+ **Total capacity**: 30 P4 GPUs

The shared GPU pool uses this priority policy:

1. **Real-time inference**: Priority 100

1. **Training**: Priority 75

1. **Evaluation**: Priority 50

Kueue enforces team quotas and priority classes, with preemption and quota borrowing enabled.

**Initial state: Normal cluster utilization**  
In normal operations:
+ Team A runs training and evaluation jobs on all 10 P4 GPUs
+ Team B runs real-time inference (10 P4s) and evaluation (10 P4s) within its 20 GPU quota
+ The cluster is fully utilized with all jobs admitted and running

**Inference spike: Team B requires additional GPUs**  
When Team B experiences a traffic spike, additional inference pods require 5 more P4 GPUs. Kueue detects that the new pods are:
+ Within Team B's namespace
+ Priority 100 (real-time inference)
+ Pending admission due to quota constraints

**Kueue's response process chooses between two options:**  
**Option 1: Quota borrowing** - If Team A uses only 6 of its 10 P4s, Kueue can admit Team B's pods using the idle 4 P4s. However, these borrowed resources are preemptible—if Team A submits jobs to reach its full quota, Kueue evicts Team B's borrowed inference pods.

**Option 2: Self-preemption (Recommended)** - Team B runs low-priority evaluation jobs (priority 50). When high-priority inference pods are waiting, Kueue preempts the evaluation jobs within Team B's quota and admits the inference pods. This approach provides safe resource allocation with no external eviction risk.

Kueue follows a three-step process to allocate resources:

1. **Quota check**

   Question: Does Team B have unused quota?
   + Yes → Admit the pods
   + No → Proceed to Step 2

1. **Self-preemption within Team B**

   Question: Can lower-priority Team B jobs be preempted?
   + Yes → Preempt evaluation jobs (priority 50), free 5 P4s, and admit inference pods
   + No → Proceed to Step 3

   This approach keeps workloads within Team B's guaranteed quota, avoiding external eviction risks.

1. **Borrowing from other teams**

   Question: Is there idle, borrowable quota from other teams?
   + Yes → Admit using borrowed quota (marked as preemptible)
   + No → Pod remains in `NotAdmitted` state

## Configuring task governance for inference workloads
<a name="sagemaker-hyperpod-model-deployment-task-gov-configure"></a>

To integrate your inference workloads with Kueue, add task governance labels to your `InferenceEndpointConfig` or `JumpStartModel` CRD. These labels determine which LocalQueue receives the workload for quota management and define the scheduling priority used in preemption decisions. The following sections cover prerequisites, resource scoping, label configuration, and verification steps.

### Prerequisites
<a name="sagemaker-hyperpod-model-deployment-task-gov-prereqs"></a>

Before configuring task governance for inference workloads, ensure the following resources exist in your HyperPod cluster:
+ **Kueue** is installed and running on your cluster
+ A **ClusterQueue** exists with GPU quota allocated to your team
+ A **LocalQueue** exists in the namespace where you plan to deploy your inference endpoint
+ One or more **PriorityClass** resources are defined for workload types (such as inference, training, evaluation)

To verify these resources are available, run the following commands:

```
# Verify Kueue is installed
kubectl get crd | grep kueue

# List available PriorityClasses
kubectl get priorityclass

# List ClusterQueues
kubectl get clusterqueue

# List LocalQueues in your namespace
kubectl get localqueue -n <your-namespace>
```

### Understanding resource scoping
<a name="sagemaker-hyperpod-model-deployment-task-gov-scoping"></a>

Task governance resources have different scopes that affect how you configure your inference deployment labels.

The `kueue.x-k8s.io/queue-name` label must reference a LocalQueue that exists in the same namespace as your `InferenceEndpointConfig` or `JumpStartModel`. If no matching LocalQueue is found in that namespace, the workload will not be admitted by Kueue.

ClusterQueue, ResourceFlavor, and PriorityClass are cluster-scoped and accessible from any namespace.

To verify resource scoping on your cluster:

```
kubectl api-resources | grep kueue
```

### Adding task governance labels
<a name="sagemaker-hyperpod-model-deployment-task-gov-labels"></a>

To enable task governance for your inference deployment, add the following labels to the `metadata` section of your `InferenceEndpointConfig` or `JumpStartModel` CRD:

```
metadata:
  name: <your-deployment-name>
  namespace: <your-namespace>
  labels:
    kueue.x-k8s.io/queue-name: <your-localqueue-name>
    kueue.x-k8s.io/priority-class: <your-priority-class>
```

**Label descriptions:**
+ `kueue.x-k8s.io/queue-name` — Routes the workload to your team's LocalQueue for quota tracking. Must match a LocalQueue name in the same namespace as the workload.
+ `kueue.x-k8s.io/priority-class` — Sets the scheduling priority for preemption decisions. References a cluster-scoped PriorityClass by name.

### Verifying task governance configuration
<a name="sagemaker-hyperpod-model-deployment-task-gov-verify"></a>

After applying your `InferenceEndpointConfig` or `JumpStartModel` with task governance labels, verify that Kueue admitted the workload and pods are being scheduled correctly.

**To verify task governance is working**

1. Check workload admission status:

   ```
   kubectl get workloads -n <namespace>
   ```

   A successfully admitted workload shows `True` in the ADMITTED column and lists the ClusterQueue that reserved resources in the RESERVED IN column.

1. Check pod status:

   ```
   kubectl get pods -n <namespace>
   ```

   After admission, pods gradually transition through initialization stages until they reach `Running` state.

1. Check quota consumption:

   ```
   kubectl get clusterqueue <clusterqueue-name> -o yaml
   ```

   Review the `status` section to confirm resource consumption is being tracked.

1. Check LocalQueue pending workloads:

   ```
   kubectl get localqueue -n <namespace>
   ```

   The PENDING WORKLOADS column shows how many workloads are waiting for admission.

1. View Kueue admission events:

   ```
   kubectl describe workload <workload-name> -n <namespace>
   ```

   Review the Events section for admission decisions and any errors.

If pods remain in `Pending` state, determine whether the issue is at the Kueue admission level (workload shows `Admitted: False`) or the Kubernetes scheduler level (workload admitted but pod unschedulable).