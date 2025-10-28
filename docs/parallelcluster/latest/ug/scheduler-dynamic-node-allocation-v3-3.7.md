# Slurm dynamic node allocation

strategies in version 3.7.x

ParallelCluster uses 2 types of dynamic node allocation strategies to scale the
cluster:

- ###### Allocation based on available requested node information:
  - **All-nodes resume** or **node-list** scaling:

  ParallelCluster scales up the cluster based only on Slurm's requested node list names
  when Slurm's `ResumeProgram` runs. It allocates compute resources to
  nodes only by node name. The list of node names can span multiple jobs.
  - **Job-level resume** or **job-level** scaling:

  ParallelCluster scales up the cluster based on the requirements of each job, the
  current number of nodes that are allocated to the job, and which nodes need to be
  resumed. ParallelCluster gets this information from the
  `SLURM_RESUME_FILE` environment variable.

- ###### Allocation with an Amazon EC2 launch strategy:

      + **Best-effort** scaling:


      ParallelCluster scales up the cluster by using an Amazon EC2 launch instance API call with the
       minimum target capacity equal to 1, to launch some, but not necessarily all of
       instances needed to support the requested nodes.
      + **All-or-nothing** scaling:


      ParallelCluster scales up the cluster by using an Amazon EC2 launch instance API call that
       only succeeds if all of the instances needed to support the requested nodes are
       launched. In this case, it calls the Amazon EC2 launch instance API with the minimum target
       capacity equal to the total requested capacity.

  By default, ParallelCluster uses **node-list** scaling with a
  **best-effort** Amazon EC2 launch strategy to launch some, but not
  necessarily all of instances needed to support the requested nodes. It tries to provision as
  much capacity as possible to serve the submitted workload.

Starting with ParallelCluster version 3.7.0, ParallelCluster uses **job-level** scaling with an **all-or-nothing** EC2
launch strategy for jobs submitted in **exclusive mode**. When
you submit a job in exclusive mode, the job has exclusive access to its allocated nodes. For
more information, see [EXCLUSIVE](https://slurm.schedmd.com/slurm.conf.html#OPT_EXCLUSIVE "https://slurm.schedmd.com/slurm.conf.html#OPT_EXCLUSIVE") in the Slurm documentation.

To submit a job in exclusive mode:

- Pass the exclusive flag when submitting a Slurm job to the cluster. For example,
  `sbatch ... --exclusive`.

OR

- Submit a job to a cluster queue that has been configured with [JobExclusiveAllocation](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-JobExclusiveAllocation "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-JobExclusiveAllocation") set to `true`.
  When submitting a job in exclusive mode:

- ParallelCluster currently batches launch requests to include up to 500 nodes. If a job
  requests more than 500 nodes, ParallelCluster makes an **all-or-nothing** launch request for each set of 500 nodes and an additional
  launch request for the remainder of nodes.
- If node allocation is in a single compute resource, ParallelCluster makes an **all-or-nothing** launch request for each set of 500 nodes and an
  additional launch request for the remainder of nodes. If a launch request fails,
  ParallelCluster terminates the unused capacity created by all of the launch
  requests.
- If node allocation spans multiple compute resources, ParallelCluster needs to make an
  **all-or-nothing** launch request for each compute
  resource. These requests are also batched. If a launch request fails for one of the
  compute resources, ParallelCluster terminates the unused capacity created by all of the
  compute resource launch requests.
  **job-level** scaling with **all-or-nothing** launch strategy known limitations:

- When you submit a job in a compute resource with a single instance type, in a queue that
  spans multiple Availability Zones, the **all-or-nothing** EC2
  launch API call only succeeds if all of the capacity can be provided in a single Availability
  Zone.
- When you submit a job in a compute resource with multiple instance types, in a queue with
  a single Availability Zone, the **all-or-nothing** Amazon EC2 launch API
  call only succeeds if all of the capacity can be provided by a single instance type.
- When you submit a job in a compute resource with multiple instance types, in a queue
  spanning multiple Availability Zones, the **all-or-nothing** Amazon EC2 launch API call isn't supported and ParallelCluster
  performs **best-effort** scaling instead.
