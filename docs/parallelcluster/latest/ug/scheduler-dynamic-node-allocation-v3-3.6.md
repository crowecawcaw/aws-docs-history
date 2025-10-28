# Slurm dynamic node allocation

strategies in version 3.6.x and previous

AWS ParallelCluster uses only one type of dynamic node allocation strategy to scale the
cluster:

- Allocation based on available requested node information:
  - **All-nodes resume** or **node-list** scaling: ParallelCluster scales up the cluster based only on
    Slurm's requested node list names when Slurm's`ResumeProgram` runs.
    It allocates compute resources to nodes only by node name. The list of node names
    can span multiple jobs.

- Allocation with an Amazon EC2 launch strategy:
  - **Best-effort** scaling: ParallelCluster scales up the
    cluster by using an Amazon EC2 launch instance API call with the minimum target capacity
    equal to 1, to launch some, but not necessarily all of instances needed to support
    the requested nodes.
    ParallelCluster uses**node-list** scaling with a **best-effort** Amazon EC2 launch strategy to launch some, but not necessarily
    all of instances needed to support the requested nodes. It tries to provision as much
    capacity as possible to serve the submitted workload.

Limitations

- Possible idle running instances at the end of the scaling process, for the case when it’s not possible to allocate all the nodes requested by the jobs.
