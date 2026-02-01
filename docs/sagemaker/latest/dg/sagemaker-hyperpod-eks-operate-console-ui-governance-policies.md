# Policies

Amazon SageMaker HyperPod task governance simplifies how your Amazon EKS cluster resources are
allocated and how tasks are prioritized. The following provides information on
HyperPod EKS cluster policies. For information on how to set up task
governance, see [Task governance setup](sagemaker-hyperpod-eks-operate-console-ui-governance-setup-task-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance-setup-task-governance.md").

The policies are divided up into **Compute prioritization** and
**Compute allocation**. The policy concepts below will be organized
in the context of these policies.

**Compute prioritization**, or cluster policy, determines how idle
compute is borrowed and how tasks are prioritized by teams.

- **Idle compute allocation** defines how idle compute is
  allocated across teams. That is, how unused compute can be borrowed from teams.
  When choosing an **Idle compute allocation**, you can choose
  between:
  - **First-come first-serve**: When applied, teams are
    not prioritized against each other and each incoming task is equally
    likely to obtain over-quota resources. Tasks are prioritized based on
    order of submission. This means a user may be able to use 100% of the
    idle compute if they request it first.
  - **Fair-share**: When applied, teams borrow idle
    compute based on their assigned **Fair-share weight**.
    These weights are defined in **Compute allocation**.
    For more information on how this can be used, see [Sharing idle compute
    resources examples](#hp-eks-task-governance-policies-examples "#hp-eks-task-governance-policies-examples").

- **Task prioritization** defines how tasks are queued as
  compute becomes available. When choosing a **Task
  prioritization**, you can choose between:
  - **First-come first-serve**: When applied, tasks are
    queued in the order they are requested.
  - **Task ranking**: When applied, tasks are queued in
    the order defined by their prioritization. If this option is chosen, you
    must add priority classes along with the weights at which they should be
    prioritized. Tasks of the same priority class will be executed on a
    first-come first-serve basis. When enabled in Compute allocation, tasks
    are preempted from lower priority tasks by higher priority tasks within
    the team.

  When data scientists submit jobs to the cluster, they use the priority
  class name in the YAML file. The priority class is in the format
  ``priority-class-name`-priority`.
  For an example, see [Submit a job to SageMaker AI-managed queue and
  namespace](sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md#hp-eks-cli-start-job "sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md#hp-eks-cli-start-job").
  - **Priority classes**: These classes establish a
    relative priority for tasks when borrowing capacity. When a task is
    running using borrowed quota, it may be preempted by another task of
    higher priority than it, if no more capacity is available for the
    incoming task. If **Preemption** is enabled in the
    **Compute allocation**, a higher priority task may
    also preempt tasks within its own team.

- **Unallocated resource sharing** enables teams to borrow
  compute resources that are not allocated to any team through compute quota. When
  enabled, unallocated cluster capacity becomes available for teams to borrow
  automatically. For more information, see [How unallocated resource sharing works](#sagemaker-hyperpod-eks-operate-console-ui-governance-policies-idle-resource-sharing-how-it-works "#sagemaker-hyperpod-eks-operate-console-ui-governance-policies-idle-resource-sharing-how-it-works").
  **Compute allocation**, or compute quota, defines a team’s compute
  allocation and what weight (or priority level) a team is given for fair-share idle
  compute allocation.

- **Team name**: The team name. A corresponding
  **Namespace** will be created, of type
  `hyperpod-ns-`team-name``.
- **Members**: Members of the team namespace. You will need to
  set up a Kubernetes role-based access control (RBAC) for data scientist users
  that you want to be part of this team, to run tasks on HyperPod
  clusters orchestrated with Amazon EKS. To set up a Kubernetes RBAC, use the
  instructions in [create team role](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#5-create-team-role").
- **Fair-share weight**: This is the level of prioritization
  assigned to the team when **Fair-share** is applied for
  **Idle compute allocation**. The highest priority has a
  weight of 100 and the lowest priority has a weight of 0. Higher weight enables a
  team to access unutilized resources within shared capacity sooner. A zero weight
  signifies the lowest priority, implying this team will always be at a
  disadvantage compared to other teams.

The fair-share weight provides a comparative edge to this team when vying for
available resources against others. Admission prioritizes scheduling tasks from
teams with the highest weights and the lowest borrowing. For example, if Team A
has a weight of 10 and Team B has a weight of 5, Team A would have priority in
accessing unutilized resources as in would have jobs that are scheduled earlier
than Team B.

- **Task preemption**: Compute is taken over from a task based
  on priority. By default, the team loaning idle compute will preempt tasks from
  other teams.
- **Lending and borrowing**: How idle compute is being lent by the team and if the team can borrow from other teams.

      + **Percentage-based borrow limit**: The limit of idle compute that a team is allowed to borrow, expressed as a percentage of their guaranteed quota. A team can borrow up to 10,000% of allocated compute. The value you provide here is interpreted as a percentage. For example, a value of 500 will be interpreted as 500%. This percentage applies uniformly across all resource types (CPU, GPU, Memory) and instance types in the team's quota.
      + **Absolute borrow limit**: The limit of idle compute that a team is allowed to borrow, defined as absolute resource values per instance type. This provides granular control over borrowing behavior for specific instance types. You need to specify absolute limits using the same schema as **Compute quota**, including instance count, accelerators, vCPU, memory, or accelerator partitions. You can specify absolute limits for one or more instance types in your team's quota.

  For information on how these concepts are used, such as priority classes and name
  spaces, see [Example
  HyperPod task governance AWS CLI commands](sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md "sagemaker-hyperpod-eks-operate-console-ui-governance-cli.md").

## Sharing idle compute

resources examples

The total reserved quota should not surpass the cluster's available capacity for
that resource, to ensure proper quota management. For example, if a cluster
comprises 20 `ml.c5.2xlarge` instances, the cumulative quota assigned to
teams should remain under 20.

If the **Compute allocation** policies for teams allow for
**Lend and Borrow** or **Lend**, the idle
capacity is shared between these teams. For example, Team A and Team B have
**Lend and Borrow** enabled. Team A has a quota of 6 but is
using only 2 for its jobs, and Team B has a quota of 5 and is using 4 for its jobs.
A job that is submitted to Team B requiring 4 resources. 3 will be borrowed from
Team A.

If any team's **Compute allocation** policy is set to
**Don't Lend**, the team would not be able to borrow any
additional capacity beyond its own allocations.

## How unallocated resource sharing works

Unallocated resource sharing automatically manages the pool of resources that are not allocated to any compute quota in your cluster. This means HyperPod continuously monitors your cluster state and automatically updates to the correct configuration over time.

**Initial Setup**

- When you set `IdleResourceSharing` to `Enabled` in your ClusterSchedulerConfig (by default it is `Disabled`), HyperPod task governance begins monitoring your cluster and calculates available idle resources by subtracting team quotas from total node capacity.
- Unallocated resource sharing ClusterQueues are created to represent the
  borrowable resource pool.
- When you first enable unallocated resource sharing, infrastructure setup
  takes several mins. You can monitor the progress through policy
  `Status` and `DetailedStatus` in
  ClusterSchedulerConfig.

**Ongoing Reconciliation**

- HyperPod task governance continuously monitors for changes such as node
  additions or removals and cluster queue quota updates.
- When changes occur, unallocated resource sharing recalculates quota and
  updates ClusterQueues. Reconciliation typically completes within seconds.

**Monitoring**

You can verify that unallocated resource sharing is fully configured by
checking for unallocated resource sharing ClusterQueues:

```
kubectl get clusterqueue | grep hyperpod-ns-idle-resource-sharing
```

When you see ClusterQueues with names like
`hyperpod-ns-idle-resource-sharing-cq-1`, unallocated resource
sharing is active. Note that multiple unallocated resource sharing ClusterQueues
may exist depending on the number of resource flavors in your cluster.

## Node eligibility for unallocated resource sharing

Unllocated Resource Sharing only includes nodes that meet the following
requirements:

1. **Node Ready Status**
   - Nodes must be in `Ready` status to contribute to the
     unallocated resource pool.
   - Nodes in `NotReady` or other non-ready states are
     excluded from capacity calculations.
   - When a node becomes `Ready`, it is automatically
     included in the next reconciliation cycle.

2. **Node Schedulable Status**
   - Nodes with `spec.unschedulable: true` are excluded
     from unallocated resource sharing.
   - When a node becomes schedulable again, it is automatically
     included in the next reconciliation cycle.

3. **MIG Configuration (GPU nodes only)**
   - For GPU nodes with MIG (Multi-Instance GPU) partitioning, the
     `nvidia.com/mig.config.state` label must show
     `success` for the node to contribute MIG profiles to
     unallocated resource sharing.
   - These nodes will be retried automatically once MIG configuration
     completes successfully.

4. **Supported Instance Types**
   - The instance must be a supported SageMaker HyperPod instance type.
   - See the list of supported instance types in the SageMaker HyperPod cluster.

###### Topics

- [Create policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-create.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-create.md")
- [Edit policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-edit.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-edit.md")
- [Delete policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-delete.md")
- [Allocating compute quota
  in Amazon SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-compute-allocation.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-compute-allocation.md")
