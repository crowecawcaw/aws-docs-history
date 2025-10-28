# AWS ParallelCluster processes

This section applies to clusters that are deployed with Slurm. When used with this scheduler,
AWS ParallelCluster interacts with the underlying job scheduler to manage compute node provisioning
and removal.

For HPC clusters that are based on AWS Batch, AWS ParallelCluster relies on the capabilities
provided by AWS Batch to manage compute nodes.

## `clustermgtd`

The cluster management daemon (`clustermgtd`) performs these tasks:

- Clean up inactive partitions
- Manage Slurm reservations and nodes associated with Capacity Blocks (see the
  following section)
- Manage static capacity to make sure it is always up and healthy
- Sync scheduler with Amazon EC2.
- Clean up orphaned instances
- Restore scheduler node status upon an Amazon EC2 termination that happens outside of the
  suspend workflow
- Manage unhealthy Amazon EC2 instances (those that fail Amazon EC2 health checks)
- Manage scheduled maintenance events
- Manage unhealthy scheduler nodes (those that fail scheduler health checks)

### Management of Slurm reservations

and nodes associated with Capacity Blocks

ParallelCluster supports On-Demand Capacity Reservations (ODCR) and Capacity Blocks for
Machine Learning (CB). Unlike ODCR, CB can have a future start time and is time-bound.

`clustermgtd` searches for unhealthy nodes in a loop, terminates any Amazon EC2
instances that are down, and replaces them with new instances if they are static nodes.

AWS ParallelCluster manages static nodes associated with Capacity Blocks differently–
it creates a cluster even if the CB is not yet active, and automatically launches instances
once the CB is active.

The Slurm nodes that correspond to compute resources associated with CBs that are not
yet active are kept in the maintenance state until the CB start time is reached. These Slurm
nodes remain in a reservation/maintenance state associated with the Slurm admin user, which
means they can accept jobs, but the jobs remain pending until the Slurm reservation
is removed.

`clustermgtd` automatically creates or deletes Slurm reservations– it puts
the related CB nodes in a maintenance state based on the CB state. When the CB becomes active,
the Slurm reservation is removed, the nodes start and become available for the pending jobs
or for new job submissions.

When the CB end time is reached, the nodes are moved back to a reservation/maintenance
state. It's up to users to resubmit/requeue the jobs to a new queue/compute resource when
the CB is no longer active and instances are terminated.

## `clusterstatusmgtd`

The cluster status management daemon (`clusterstatusmgtd`) manages the compute fleet
status update. Every minute it fetches the fleet status stored in a DynamoDB table and manages
any STOP/START request.

## `computemgtd`

The compute management daemon (`computemgtd`) processes run on each of the cluster
compute nodes. Every five (5) minutes, the compute management daemon confirms that the head
node can be reached and is healthy. If five (5) minutes pass during which the head node cannot
be reached or is not healthy, the compute node is shut down.
