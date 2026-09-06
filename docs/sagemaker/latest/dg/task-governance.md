

# Task governance for Interactive Spaces on HyperPod
<a name="task-governance"></a>

This section covers how to optimize your shared Amazon SageMaker HyperPod EKS clusters for Interactive Spaces workloads. You'll learn to configure Kueue's task governance features—including quota management, priority scheduling, and resource sharing policies—to ensure your development workloads run without interruption while maintaining fair allocation across your teams' training, evaluation, and batch processing activities.

## How Interactive Space management works
<a name="task-governance-how"></a>

To effectively manage Interactive Spaces in shared HyperPod EKS clusters, implement the following task governance strategies using Kueue's existing capabilities.

**Priority class configuration**

Define dedicated priority classes for Interactive Spaces with high weights (such as 100) to ensure development pods are admitted and scheduled before other task types. This configuration enables Interactive Spaces to preempt lower-priority jobs during cluster load, which is critical for maintaining uninterrupted development workflows.

**Quota sizing and allocation**

Reserve sufficient compute resources in your team's ClusterQueue to handle expected development workloads. During periods when development resources are idle, unused quota resources can be temporarily allocated to other teams' tasks. When development demand increases, these borrowed resources can be reclaimed to prioritize pending Interactive Space pods.

**Resource Sharing Strategies**

Choose between two quota sharing approaches based on your requirements:

*Strict Resource Control*: Disable quota lending and borrowing to guarantee reserved compute capacity is always available for your Interactive Spaces. This approach requires sizing quotas large enough to independently handle peak development demand and may result in idle nodes during low-usage periods.

*Flexible Resource Sharing*: Enable quota lending to allow other teams to utilize idle development resources when needed. However, disable borrowing to ensure Interactive Spaces never run on borrowed, reclaimable resources that could lead to unexpected evictions.

**Intra-Team Preemption**

Enable intra-team preemption when running mixed workloads (training, evaluation, and Interactive Spaces) under the same quota. This allows Kueue to preempt lower-priority jobs within your team to accommodate high-priority Interactive Space pods, ensuring development work can proceed without depending on external quota borrowing.

## Sample Interactive Space setup
<a name="task-governance-space-setup"></a>

The following example shows how Kueue manages compute resources for Interactive Spaces in a shared Amazon SageMaker HyperPod cluster.

**Cluster configuration and policy setup**

Your cluster has the following configuration:
+ *Team Alpha (Dev Team)*: 8 CPU quota for Interactive Spaces
+ *Team Beta (ML Team)*: 16 CPU quota for training and evaluation
+ *Team Gamma (Research)*: 6 CPU quota for experimentation
+ *Static provisioning*: No autoscaling
+ *Total capacity*: 30 CPUs

The shared CPU pool uses this priority policy:
+ *Interactive Spaces*: Priority 100
+ *Training*: Priority 75
+ *Evaluation*: Priority 50
+ *Batch Processing*: Priority 25

Kueue enforces team quotas and priority classes, with preemption enabled and borrowing disabled for the dev team.

**Initial state: Normal cluster utilization**

In normal operations:
+ *Team Alpha*: Runs 6 Interactive Spaces using 6 CPUs, 2 CPUs idle
+ *Team Beta*: Runs training jobs (12 CPUs) and evaluation (4 CPUs) within its 16 CPU quota
+ *Team Gamma*: Runs research workloads on all 6 CPUs
+ *Resource sharing*: Team Beta borrows Team Alpha's 2 idle CPUs for additional training

**Development spike: Team Alpha requires additional resources**

When Team Alpha's developers need to scale up development work, additional Interactive Space pods require 4 more CPUs. Kueue detects that the new pods are:
+ Within Team Alpha's namespace
+ Priority 100 (Interactive Spaces)
+ Pending admission due to quota constraints

**Kueue's response process**

Kueue follows a three-step process to allocate resources:

1. **Quota check**

   Question: Does Team Alpha have unused quota?
   + *Current usage*: 6 CPUs used, 2 CPUs available
   + *New requirement*: 4 CPUs needed
   + *Result*: Insufficient quota → Proceed to Step 2

1. **Self-preemption within Team Alpha**

   Question: Can lower-priority Team Alpha jobs be preempted?
   + *Available targets*: No lower-priority jobs in Team Alpha
   + *Result*: No preemption possible → Proceed to Step 3

1. **Reclaim borrowed resources**

   Question: Are Team Alpha resources being borrowed by other teams?
   + *Borrowed resources*: Team Beta using 2 CPUs from Team Alpha
   + *Action*: Kueue evicts Team Beta's borrowed training pods, freeing 2 CPUs
   + *Remaining need*: Still need 2 more CPUs → Interactive Spaces remain in NotAdmitted state until resources become available

This approach prioritizes Interactive Spaces while maintaining team quota boundaries and preventing development work from running on unstable borrowed resources.