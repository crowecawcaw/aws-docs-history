# Launch instances with Capacity Blocks (CB)

AWS ParallelCluster supports [On-Demand Capacity Reservations (ODCR)](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") and [Capacity Blocks (CB) for Machine Learning](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md"). Unlike ODCR, CB can have a future start time and is time-bound.
For more information about launching with ODCR, see [Launch
instances with On-Demand Capacity Reservations (ODCR)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md").

## Using CB with AWS ParallelCluster

To configure your new or existing clusters to use a CB, you first need to have a valid CB
in your AWS account. You can use the AWS Management Console, AWS Command Line Interface, or SDK to find and purchase an
available CB by following the official documentation. Once you have a valid CB, you can set
the CB Amazon Resource Name (ARN) and related parameters in your AWS ParallelCluster configuration file. For more
information, see [Find and purchase
Capacity Blocks (CB)](../../../AWSEC2/latest/UserGuide/capacity-blocks-using.md#capacity-blocks-purchase "../../../AWSEC2/latest/UserGuide/capacity-blocks-using.md#capacity-blocks-purchase")

### CB in the cluster configuration

To use a CB for a specific queue you must use the `CapacityReservationId`
parameter. Configure it to an existing CB ID. You can obtain the CB ARN from the AWS Management Console,
AWS CLI, or SDK that you used to create the CB.

You must set `CapacityType = CAPACITY_BLOCK` for the queue where you want
to use the CB. Set it to the `InstanceType` of the compute resource (the same
as the Amazon Elastic Compute Cloud instance type of the CB).

When you specify the `CapacityReservationId` at the compute resource level,
the `InstanceType` is optional because it will be automatically retrieved from
the reservation.

When you use `CapacityType = CAPACITY_BLOCK`, `MaxCount` must be
equal to `MinCount` and greater than 0, because all the instances that are part
of the CB reservation are managed as static nodes.

At the cluster creation time, the head node waits for all the static nodes to be ready
before it signals the success of the cluster creation. However, when you use
`CapacityType = CAPACITY_BLOCK`, the nodes that are part of the compute resources
associated with won't be considered for this check. The cluster will be created even
if all the configured are not active.

The following configuration file snippet shows the parameters required to enable
in the AWS ParallelCluster configuration file.

```
SlurmQueues:
 - Name: string
   CapacityType: CAPACITY_BLOCK
   ComputeResources:
   - Name: string
     InstanceType: String (EC2 Instance type of the CB)
     MinCount: integer (<= total capacity of the CB)
     MaxCount: integer (equal to MinCount)
     CapacityReservationTarget:
        CapacityReservationId: String (CB id)
```

### How AWS ParallelCluster uses Capacity Blocks (CB)

AWS ParallelCluster manages static nodes associated with in a peculiar way. AWS ParallelCluster
creates a cluster even if the CB is not yet active, and instances are launched automatically
once the CB is active.

The Slurm nodes that correspond to compute resources, are associated with , and
are not yet active, are kept in maintenance until they reach the CB start time. Slurm
nodes remain in a reservation/maintenance state and are associated with the slurm admin
user. This means they can accept jobs, but the jobs remain `pending` until the
reservation is removed.

AWS ParallelCluster automatically updates Slurm reservations and puts the related CB
nodes in maintenance state (corresponding to the CB state). When the CB is active, the
Slurm reservation is removed, and the nodes start and become available for pending jobs
or for new job submissions.

When the CB end time is reached, the nodes will be moved back to a reservation/maintenance
state. It's up to users to resubmit/requeue the jobs to a new queue/compute-resource when
the CB is no longer active and the instances are terminated.
