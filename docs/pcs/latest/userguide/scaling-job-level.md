

# Job-level scaling
<a name="scaling-job-level"></a>

AWS PCS uses *job-level scaling* to manage the dynamic capacity of your cluster (the instances between the minimum and maximum counts you set on a compute node group). At regular intervals, AWS PCS reviews waiting jobs, launches Amazon EC2 instances to satisfy them, and scales dynamic capacity back down as jobs finish and instances become idle. You don't manage this process. AWS PCS evaluates your workload and adjusts capacity for you.

Static capacity (the minimum you keep always-on) is not affected by job-level scaling. For more information, see [Creating a compute node group in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_create.html).

## How scheduling and scaling work together
<a name="scaling-how-scheduling-works"></a>

When you submit a job, Slurm selects and allocates cluster nodes that satisfy the job's requirements. For allocated nodes backed by dynamic capacity, AWS PCS launches the Amazon EC2 instances needed to back those nodes and assigns each instance to its node. You don't manage these Amazon EC2 instances directly. AWS PCS handles launching and releasing dynamic capacity on your behalf.

## How AWS PCS provides capacity for a job
<a name="scaling-how-pcs-provides-capacity"></a>

A job runs only after all required nodes are available. It does not start on a partial allocation. How AWS PCS provides capacity depends on the job's requirements and your compute node group's configuration. For example, it depends on how many nodes the job needs, whether it spans multiple compute node groups, whether it requests more capacity than a single Amazon EC2 request can provide, and whether the target node group is backed by a capacity reservation.

AWS PCS evaluates each job and picks the appropriate approach. In practice, this takes one of two forms:
+ **All at once.** AWS PCS provides all the nodes the job needs together, or none. The job starts only once its full capacity is available.
+ **Incrementally.** For some jobs, such as those that need more capacity than a single Amazon EC2 request can provide, AWS PCS provides capacity as it becomes available, holding what it has acquired while it works toward the full set.

When a job's full capacity isn't available, it doesn't start. AWS PCS might not launch any instances for the job, or it might release instances it had launched. The job remains pending, and AWS PCS re-evaluates it on later intervals until its capacity can be provided.

**Example Large job with incremental capacity provisioning**  
Suppose you submit a job that requires a large number of nodes, more than can be provided at once. AWS PCS launches instances for a portion of the job's nodes, assigns them, and retains that capacity while it continues to acquire the remaining nodes on later intervals. The job starts once all of its required nodes are available. If you need to ensure the full capacity is available when the job starts, back the compute node group with a capacity reservation, as described in the next section.

## Guaranteeing capacity for large or time-sensitive jobs
<a name="scaling-guaranteeing-capacity"></a>

If a job needs a large amount of capacity, or must start at a specific time, on-demand capacity might not be available when you submit it. To reserve capacity in advance so it's available when your job runs, you can use On-Demand Capacity Reservations (ODCRs) or Amazon EC2 Capacity Blocks for ML.

Configure your compute node group to use the reservation, then submit jobs to a queue associated with that node group. Reserved capacity is billed according to your ODCR or Capacity Block whether or not a job is running against it. For more information, see [Using ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html) and [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html).