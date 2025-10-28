# Slurm dynamic node allocation strategies

in version 3.8.0

Starting with ParallelCluster version 3.8.0, ParallelCluster uses **Job-level resume** or **job-level scaling** as the
default dynamic node allocation strategy to scale the cluster: ParallelCluster scales up the
cluster based on the requirements of each job, the number of nodes allocated to the job, and
which nodes need to be resumed. ParallelCluster gets this information from the SLURM_RESUME_FILE
environment variable.

The scaling for dynamic nodes is a two steps process, which involves the launch of the EC2
instances and the assignment of the launched Amazon EC2 instances to the Slurm nodes. Each of these two
steps can be done using an **all-or-nothing** or **best-effort** logic.

For launch of the Amazon EC2 instances:

- **all-or-nothing** calls the launch Amazon EC2 API with minimum
  target equals to the total target capacity
- **best-effort** calls the launch Amazon EC2 API with minimum target
  equals to 1 and the total target capacity equals to the requested capacity
  For assignment of the Amazon EC2 instances to Slurm nodes:

- **all-or-nothing** assigns Amazon EC2 instances to Slurm nodes only
  if it's possible to assign an Amazon EC2 instance to every requested node
- **best-effort** assigns Amazon EC2 instances to Slurm nodes even if
  all the requested nodes are not covered by Amazon EC2 instance capacity

The possible combinations of the above strategies translates into the ParallelCluster
launch strategies.
The available **ParallelCluster\*\***launch strategies** that can be set into the [ScalingStrategy](Scheduling-v3.md#yaml-Scheduling-ScalingStrategy "Scheduling-v3.md#yaml-Scheduling-ScalingStrategy") cluster configuration to be used with **job-level scaling** are:**all-or-nothing\*\* scaling:

This strategy involves AWS ParallelCluster initiating an Amazon EC2 launch instance API call for
each job, that requires all instances necessary for the requested compute nodes to be
successfully launched. This ensures that the cluster scales only when the required capacity per
job is available, avoiding idle instances left at the end of the scaling process.

The strategy uses an **all-or-nothing** logic for the launch of
the Amazon EC2 instances for each job plus and **all-or-nothing** logic
for the assignment of the Amazon EC2 instances to Slurm nodes.

The strategy groups launch requests into batches, one for each compute resource requested
and up to 500 nodes each. For requests spanning multiple compute resources or exceeding 500 nodes,
ParallelCluster sequentially processes multiple batches.

The failure of any single resource's batch results in the termination of all associated
unused capacity, ensuring that no idle instances will be left at the end of the scaling
process.

Limitations

- The time taken for scaling is directly proportional to the number of jobs submitted per
  execution of the Slurm resume program.
- The scaling operation is limited by the RunInstances resource account limit, set at 1000
  instances by default. This limitation is in accordance with AWS's EC2 API throttling policies,
  for more details refer to [Amazon EC2 API throttling documentation](../../../AWSEC2/latest/APIReference/throttling.md "../../../AWSEC2/latest/APIReference/throttling.md")
- When you submit a job in a compute resource with a single instance type, in a queue that
  spans multiple Availability Zones, the **all-or-nothing** EC2
  launch API call only succeeds if all of the capacity can be provided in a single Availability
  Zone.
- When you submit a job in a compute resource with multiple instance types, in a queue with a
  single Availability Zone, the **all-or-nothing** Amazon EC2 launch API
  call only succeeds if all of the capacity can be provided by a single instance type.
- When you submit a job in a compute resource with multiple instance types, in a queue
  spanning multiple Availability Zones, the **all-or-nothing**
  Amazon EC2 launch API call isn't supported and ParallelCluster performs **best-effort** scaling instead.
  **greedy-all-or-nothing** scaling:

This variant of the all-or-nothing strategy still ensures that the cluster scales only when
the required capacity per job is available, avoiding idle instances at the end of the scaling
process, but it involves ParallelCluster initiating an Amazon EC2 launch instance API call that aims
for a minimum target capacity of 1, attempting to maximize the number of nodes launched up to
the requested capacity. The strategy uses a best-effort logic for the launch of the EC2
instances for all the jobs plus the **all-or-nothing** logic for
the assignment of the Amazon EC2 instances to Slurm nodes for each job.

The strategy groups launch requests into batches, one for each compute resource requested and
up to 500 nodes each. For requests spanning multiple compute resources or exceeding 500 nodes,
ParellelCluster sequentially processes multiple batches.

It ensure that no idle instances will be left at the end of the scaling process, by
maximizing the throughput at the cost of temporary over-scaling during the scaling process.

Limitations

- Temporary over-scaling is possible, leading to additional costs for instances that
  transition to a running state before scaling completion.
- The same instance limit as in the all-or-nothing strategy applies, subject to AWS's
  RunInstances resource account limit.
  **best-effort** scaling:

This strategy calls Amazon EC2 launch instance API call by targeting a minimum capacity of 1 and
aiming to achieve the total requested capacity at the cost of leaving idle instances after the
scaling process execution if not all the requested capacity is available. The strategy uses a
best-effort logic for the launch of the Amazon EC2 instances for all the jobs plus the **best-effort** logic for the assignment of the Amazon EC2 instances to Slurm
nodes for each job.

The strategy groups launch requests into batches, one for each compute resource requested and
up to 500 nodes each. For requests spanning multiple compute resources or exceeding 500 nodes,
ParallelCluster sequentially processes multiple batches.

This strategy allows for scaling far beyond the default 1000 instances limit over multiple
scaling process executions, at the cost of having idle instances across the different scaling
processes.

Limitations

- Possible idle running instances at the end of the scaling process, for the case when it’s
  not possible to allocate all the nodes requested by the jobs.
  The following is an example that shows how the scaling of dynamic nodes behave using the
  different **ParallelCluster launch strategies**. Suppose you have
  submitted two jobs requesting 20 nodes each, for a total of 40 nodes of the same type, but there
  are only 30 Amazon EC2 instances available to cover the requested capacity on EC2.

**all-or-nothing** scaling:

- For the first job, an **all-or-nothing** Amazon EC2 launch instance
  API is called, requesting 20 instances. A successful call has results in the launch of 20
  instances
- **all-or-nothing** assignment of the 20 launched instances to
  Slurm nodes for the first job is successful
- Another **all-or-nothing** Amazon EC2 launch instance API is called,
  requesting 20 instances for the second job. The call is not successful, since there is only
  capacity for another 10 instances. No instances are launched at this time
  **greedy-all-or-nothing** scaling:

- A **best-effort** Amazon EC2 launch instance API is called,
  requesting 40 instances, which is the total capacity requested by all the jobs. This results in
  the launch of 30 instances
- An **all-or-nothing** assignment of 20 of the launched
  instances to Slurm nodes for the first job is successful
- Another **all-or-nothing** assignment of the remaining
  launched instances to Slurm nodes for the second job is tried, but since there are only 10
  available instances out of the total 20 requested by the job, the assignment is not
  successful
- The 10 unassigned launched instances are terminated
  **best-effort** scaling:

- A **best-effort** Amazon EC2 launch instance API is called,
  requesting 40 instances, which is the total capacity requested by all the jobs. This results in
  the launch of 30 instances.
- A **best-effort** assignment of 20 of the launched instances
  to Slurm nodes for the first job is successful.
- Another **best-effort** assignment of the remaining 10
  launched instances to Slurm nodes for the second job is successful, even if the total requested
  capacity was 20. But since the job was requesting the 20 nodes, and it was possible to assign
  Amazon EC2 instances to only 10 of them, the job cannot start and the instances are left running idle,
  until enough capacity is found to start the missing 10 instances at a later call of the scaling
  process, or the scheduler schedules the job on other, already running, compute nodes.
