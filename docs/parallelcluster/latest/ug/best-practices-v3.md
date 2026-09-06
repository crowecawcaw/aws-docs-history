

# Best practices
<a name="best-practices-v3"></a>

The following sections provide best practices for using AWS ParallelCluster, which includes network performance and budget alerts. If you encounter problems even though you follow these best practices, see [AWS ParallelCluster troubleshooting](troubleshooting-v3.md) for possible solutions.

## Best practices: head node instance type selection
<a name="best-practices-head-node-instance-type"></a>

Even though the head node doesn't run a job, its functions and its sizing are crucial to the overall performance of the cluster. When you choose the instance type to use for your head node, consider the following characteristics:

**Cluster size:** The head node orchestrates the scaling logic of the cluster and is responsible for attaching new nodes to the scheduler. To scale up and down a cluster that has a large number of nodes, provide the head node some extra compute capacity.

**Shared file systems:** When you use shared file systems, choose an instance type with enough network bandwidth, and enough Amazon EBS bandwidth, to handle your workflows. Ensure that the head node is able to both expose sufficient NFS server directories for the cluster and handle the artifacts that need to be shared between the compute nodes and head node. 

## Best practices: network performance
<a name="best-practices-network-performance-v3"></a>

Network performance is critical for high performance computing (HPC) applications. Without reliable network performance, these applications can't perform as expected. To optimize network performance, consider the following best practices.
+ **Placement group:** If you're using Slurm, consider configuring each Slurm queue to use a cluster placement group . A cluster's *placement group* is a logical grouping of instances within a single Availability Zone. For more information, see [placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*. You can specify a [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup) in the queue's [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) section, each compute resource is assigned to the queue's placement group. When specifying a [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Networking-PlacementGroup) in the compute resource's [`Networking`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Networking) section, that specific compute resource is assigned to that placement group. The compute resource placement group specification overrides the queue specification for the compute resource. For more information, see [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup) and [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`ComputeResources`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources) / [`Networking`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Networking) / [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Networking-PlacementGroup).

  ```
  Networking:
    PlacementGroup:
      Enabled: true
      Id: {{your-placement-group-name}}
  ```

  Alternatively, have AWS ParallelCluster create a placement group for you.

  ```
  Networking:
    PlacementGroup:
      Enabled: true
  ```

  Starting with AWS ParallelCluster version 3.3.0, placement group creation and management is modified. When you specify the placement group to be enabled, without a `name` or `Id`, in the queue, each compute resource is assigned its own managed placement group, instead of one managed group for the entire queue. This helps to reduce insufficient capacity errors. If you need to have one placement group for the entire queue, you can use a named placement group.

  [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup) / [`Name`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name) was added as a preferred alternative to [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup) / [`Id`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id).

  For more information, see [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking).
+ **Enhanced networking:** Consider choosing an instance type that supports enhanced networking. This recommendation applies to all [current generation instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances). For more information, see [enhanced networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) in the *Amazon EC2 User Guide*.
+ **Elastic Fabric Adapter:** To support high levels of scalable instance to instance communication, consider choosing EFA network interfaces for your network. The EFA's custom-built operating system (OS) bypass hardware enhances instance to instance communications with the on-demand elasticity and flexibility of the AWS Cloud. You can configure each Slurm queue [`ComputeResource`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources) to use [`Efa`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa). For more information about using EFA with AWS ParallelCluster, see [Elastic Fabric Adapter](efa-v3.md).

  ```
  ComputeResources:
    - Name: {{your-compute-resource-name}}
      Efa:
        Enabled: true
  ```

  For more information about EFA, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide for Linux Instances*.
+ **Instance bandwidth:** The bandwidth scales with instance size. For information about the different instance types, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) and [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the *Amazon EC2 User Guide*.

## Best practices: budget alerts
<a name="best-practices-budget-alerts-v3"></a>

To manage resource costs in AWS ParallelCluster, we recommend that you use AWS Budgets actions to create a budget. You can also create defined budget threshold alerts for selected AWS resources. For more information, see [Configuring a budget action](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) in the *AWS Budgets User Guide*. Similarly, you can also use Amazon CloudWatch to create a billing alarm. For more information, see [Creating a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html).

## Best practices: moving a cluster to a new AWS ParallelCluster minor or patch version
<a name="best-practices-cluster-upgrades-v3"></a>

Currently each AWS ParallelCluster minor version is self-contained along with its `pcluster` CLI. To move a cluster to a new minor or patch version, you must re-create the cluster using the new version's CLI.

To optimize the process of moving a cluster to a new minor or patch version, we recommend that you do the following:
+ Save personal data in external volumes that are created outside the cluster, such as Amazon EFS and FSx for Lustre. By doing this, you can easily move the data from one cluster to another in the future.
+ Create shared storage systems using the following types. You can create these systems using the AWS CLI or AWS Management Console.
  + [`SharedStorage`](SharedStorage-v3.md) / [`EbsSettings`](SharedStorage-v3.md#SharedStorage-v3-EbsSettings) / [`VolumeId`](SharedStorage-v3.md#yaml-SharedStorage-EbsSettings-VolumeId)
  + [`SharedStorage`](SharedStorage-v3.md) / [`EfsSettings`](SharedStorage-v3.md#SharedStorage-v3-EfsSettings) / [`FileSystemId`](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-FileSystemId)
  + [`SharedStorage`](SharedStorage-v3.md) / [`FsxLustreSettings`](SharedStorage-v3.md#SharedStorage-v3-FsxLustreSettings) / [`FileSystemId`](SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-FileSystemId)

  Define a file system or volume in a cluster configuration as existing file system or volume. This way, they're preserved when you delete the cluster and can be attached to a new cluster.

  We recommend that you use Amazon EFS or FSx for Lustre file systems. Both of these systems can be attached to multiple clusters at the same time. Moreover, you can attach either of these systems to a new cluster before you delete your existing cluster.
+ Use [custom bootstrap actions](custom-bootstrap-actions-v3.md) to customize your instances rather than using a custom AMI. If instead, you use a custom AMI, then you need to delete and recreate that AMI for each new version release.
+ We recommend that you apply the preceding recommendations in the following sequence:

  1. Update the existing cluster configuration to use existing file system definitions.

  1. Verify the `pcluster` version and update it if needed.

  1. Create and test the new cluster. When you test the new cluster, check the following:
     + Make sure that your data is available in the new cluster.
     + Make sure that your application works in the new cluster.

  1. After your new cluster is fully tested and operational and you no longer need the existing cluster, delete it.

## Best practices: GPU health checks
<a name="best-practices-gpu-health-checks-v3"></a>

### The built-in GPU health check
<a name="best-practices-gpu-health-checks-builtin-v3"></a>

The built-in GPU health check ([`HealthChecks/Gpu/Enabled`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-HealthChecks-Gpu-Enabled)) is off unless you enable it. When enabled, it runs an NVIDIA DCGM level-2 diagnostic on the node's GPUs as part of the Slurm prolog. Because the diagnostic runs in the prolog and a job can't start until the prolog completes, this design suits instance types where the diagnostic finishes quickly.

The built-in check is reliable only with job-exclusive allocation (one job per node). On nodes shared by more than one job, it can interfere with running jobs and drain healthy nodes, so enable it only on queues with [`JobExclusiveAllocation: true`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-JobExclusiveAllocation).

In addition, on the P6 and P6e GPU instance families (for example, `p6-b200` and `p6-b300`) and later P-family GPU instance generations, the diagnostic takes long enough that it should not be run in the prolog: it typically exceeds the Slurm prolog's time limits and causes healthy nodes to be drained and jobs to be requeued. On these instance types, keep the GPU health check disabled (`HealthChecks/Gpu/Enabled: false`).

### Options for running your own GPU health checks
<a name="best-practices-gpu-health-checks-options-v3"></a>

To run GPU health checks on these instances, choose from the following approaches, matching each check to when it runs — at node startup, before a job, or after a job. This follows NVIDIA's model for GPU health and diagnostics (see [NVIDIA DCGM health and diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#health-and-diagnostics)); the `dcgmi diag` diagnostic grows in depth and duration by level (see [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html#run-levels-and-tests)).

**Important**  
On a node shared by more than one job, run any `dcgmi diag` diagnostic (from level-1 to level-4) only when no other job is using the node. Otherwise, it can fail and drain the node.
+ **Check at node startup.** Use this to validate a node once, when it joins the cluster, before it accepts work. Because no job is running yet, it can run a deep `dcgmi diag`; note that it catches only faults present at startup, not degradation that appears later. Install and invoke your check with an `OnNodeConfigured` custom action. See [Custom bootstrap actions](custom-bootstrap-actions-v3.md).
+ **Check in the prolog.** Use this for a fast readiness gate before each job. Because the prolog runs on every job and blocks the job from starting until it completes, keep the check to a few seconds. For example, `nvidia-smi` (optionally with a kernel-log scan for [NVIDIA Xid errors](https://docs.nvidia.com/deploy/xid-errors/index.html)), or a level-1 `dcgmi diag`. See [Slurm `prolog` and `epilog`](slurm-prolog-epilog-v3.md).
+ **Check in the epilog.** Use this to validate a node after a job completes. For example, to run a deeper check when a job fails, or to catch a GPU that degraded during a run before the next job is scheduled. It can run a deeper `dcgmi diag`. To avoid checking after every job, you might want to run a level-2 diagnostic only when the job fails. See [Slurm `prolog` and `epilog`](slurm-prolog-epilog-v3.md).

**Note**  
AWS ParallelCluster replaces drained or failed static nodes (and terminates dynamic ones), so draining a node with a confirmed fault results in it being replaced.