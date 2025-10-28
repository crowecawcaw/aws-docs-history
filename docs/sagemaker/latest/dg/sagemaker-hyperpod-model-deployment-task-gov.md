# Task governance for model

deployment on HyperPod

This section covers how to optimize your shared Amazon SageMaker HyperPod EKS clusters for
real-time inference workloads. You'll learn to configure Kueue's task governance
features—including quota management, priority scheduling, and resource sharing
policies—to ensure your inference workloads get the GPU resources they need during
traffic spikes while maintaining fair allocation across your teams' training,
evaluation, and testing activities. For more general information on task governance, see
[SageMaker HyperPod task
governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md") .

## How inference

workload management works

To effectively manage real-time inference traffic spikes in shared
HyperPod EKS clusters, implement the following task governance strategies
using Kueue's existing capabilities.

**Priority class configuration**

Define dedicated priority classes for inference workloads with high weights (such
as 100) to ensure inference pods are admitted and scheduled before other task types.
This configuration enables inference workloads to preempt lower-priority jobs during
cluster load, which is critical for maintaining low-latency requirements during
traffic surges.

**Quota sizing and allocation**

Reserve sufficient GPU resources in your team's `ClusterQueue` to
handle expected inference spikes. During periods of low inference traffic, unused
quota resources can be temporarily allocated to other teams' tasks. When inference
demand increases, these borrowed resources can be reclaimed to prioritize pending
inference pods. For more information, see [Cluster
Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/ "https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/").

**Resource Sharing Strategies**

Choose between two quota sharing approaches based on your requirements:

1. **Strict Resource Control:** Disable quota
   lending and borrowing to guarantee reserved GPU capacity is always available
   for your workloads. This approach requires sizing quotas large enough to
   independently handle peak demand and may result in idle nodes during
   low-traffic periods.
2. **Flexible Resource Sharing:** Enable quota
   borrowing to utilize idle resources from other teams when needed. Borrowed
   pods are marked as preemptible and may be evicted if the lending team
   reclaims capacity.

**Intra-Team Preemption**

Enable intra-team preemption when running mixed workloads (evaluation, training,
and inference) under the same quota. This allows Kueue to preempt lower-priority
jobs within your team to accommodate high-priority inference pods, ensuring
real-time inference can run without depending on external quota borrowing. For more
information, see [Preemption](https://kueue.sigs.k8s.io/docs/concepts/preemption/ "https://kueue.sigs.k8s.io/docs/concepts/preemption/").

## Sample

inference workload setup

The following example shows how Kueue manages GPU resources in a shared
Amazon SageMaker HyperPod cluster.

###### Cluster configuration and policy setup

Your cluster has the following configuration:

- **Team A**: 10 P4 GPU quota
- **Team B**: 20 P4 GPU quota
- **Static provisioning**: No
  autoscaling
- **Total capacity**: 30 P4 GPUs

The shared GPU pool uses this priority policy:

1. **Real-time inference**: Priority 100
2. **Training**: Priority 75
3. **Evaluation**: Priority 50

Kueue enforces team quotas and priority classes, with preemption and quota
borrowing enabled.

###### Initial state: Normal cluster utilization

In normal operations:

- Team A runs training and evaluation jobs on all 10 P4 GPUs
- Team B runs real-time inference (10 P4s) and evaluation (10 P4s) within
  its 20 GPU quota
- The cluster is fully utilized with all jobs admitted and running

###### Inference spike: Team B requires additional GPUs

When Team B experiences a traffic spike, additional inference pods require 5
more P4 GPUs. Kueue detects that the new pods are:

- Within Team B's namespace
- Priority 100 (real-time inference)
- Pending admission due to quota constraints

###### Kueue's response process chooses between two options:

**Option 1: Quota borrowing** - If Team A uses
only 6 of its 10 P4s, Kueue can admit Team B's pods using the idle 4 P4s.
However, these borrowed resources are preemptible—if Team A submits jobs to
reach its full quota, Kueue evicts Team B's borrowed inference pods.

**Option 2: Self-preemption (Recommended)** - Team B
runs low-priority evaluation jobs (priority 50). When high-priority inference pods
are waiting, Kueue preempts the evaluation jobs within Team B's quota and admits the
inference pods. This approach provides safe resource allocation with no external
eviction risk.

Kueue follows a three-step process to allocate resources:

1. **Quota check**

Question: Does Team B have unused quota?

    * Yes → Admit the pods
    * No → Proceed to Step 2

2. **Self-preemption within Team B**

Question: Can lower-priority Team B jobs be preempted?

    * Yes → Preempt evaluation jobs (priority 50), free 5 P4s, and admit
     inference pods
    * No → Proceed to Step 3

This approach keeps workloads within Team B's guaranteed quota, avoiding
external eviction risks. 3. **Borrowing from other teams**

Question: Is there idle, borrowable quota from other teams?

    * Yes → Admit using borrowed quota (marked as preemptible)
    * No → Pod remains in `NotAdmitted` state
