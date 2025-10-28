# Frequently asked questions about using Capacity Blocks with

AWS PCS

**I just paid for a Capacity Block and immediately attempted to use it with AWS PCS but compute
node group creation failed. What happened?**

Your Capacity Block might not be in a `scheduled` or `active` state.
Try again after the Capacity Block is `scheduled` or `active`.

**I am using a Capacity Block in AWS PCS and I purchased an extension before it expired. How do
I continue using it in AWS PCS?**

You don't have to do anything to continue using the Capacity Block in AWS PCS. The end date
of your Capacity Block updates after your extension payment succeeds. As long as your Capacity
Block doesn't expire, the compute node group continues to operate. If your extension payment
fails, your Capacity Block remains `active` and the compute node group operates
until the Capacity Block expires on its original end date.

**What happens to my queued and running jobs if my Capacity Block expires?**

Queued jobs that didn't start before the Capacity Block expired remain pending until you
attach another compute node group to the queue or you update the compute node group with a new
Capacity Block. You can still submit jobs to the queue. Your Slurm settings affect active jobs.
By default, active jobs are automatically re-queued, but might have errors or fail.

**My Capacity Block expired. Should I do something?**

You don't have to do anything. You can check the Amazon EC2 console for the status of your EC2
capacity reservations. When a Capacity Block expires, the compute node group associated with
that Capacity Block continues to exist and handle the same queues. The compute node group
doesn't have any instances to run jobs. You can delete the compute node group or disassociate
it from the queues to prevent users from submitting jobs that won't run.

**I want to use a new Capacity Block with my AWS PCS compute node group. What should I
do?**

We recommend you create a new compute node group to use the new Capacity Block. For more
information, see [Configure an AWS PCS compute node group to use a Capacity Block](capacity-blocks-configure-cng.md "capacity-blocks-configure-cng.md").

**How can I share 1 Capacity Block across clusters and services?**

You can split a Capacity Block across multiple clusters and services. For example, to
split a Capacity Block with 64 `p5.48xlarge` instances with 20 nodes on
PCS-Cluster-1, 16 nodes on PCS-Cluster-2, and the remaining nodes for other services, set both
`minInstanceCount` and `maxInstanceCount` to 20 for PCS-Cluster-1 and 16
for PCS-Cluster-2.

**Can I use more than 1 Capacity Block or combined capacity with 1 compute node group?**

No. Only 1 Capacity Block can be associated with a single compute node group. AWS PCS
doesn't support capacity reservation groups that combine multiple Capacity Blocks.

**How do I know when my Capacity Blocks start or expire?**

Independent from AWS PCS, Amazon EC2 sends a `Capacity Block Reservation Delivered`
event through EventBridge when a Capacity Block reservation starts and a `Capacity Block
 Reservation Expiration Warning` event 40 minutes before the Capacity Block reservation
expires. For more information, see [Monitor Capacity Blocks using
EventBridge](../../../AWSEC2/latest/UserGuide/capacity-blocks-monitor.md "../../../AWSEC2/latest/UserGuide/capacity-blocks-monitor.md") in the _Amazon Elastic Compute Cloud User Guide_.

**How does Slurm track the state of my Capacity Block?**

You can run `sinfo` to understand how AWS PCS uses the Capacity Block. In the
following example output, a queue is associated with a compute node group that runs 4 instances
from an `active` Capacity Block. The nodes are in the `idle` Slurm state
(available for use and not yet allocated to any jobs).

```
$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
fanout up infinite 4 idle node-fanout-[1-4]
```

If the nodes are instead in `maint` state, you can run `scontrol show
 res` to see details about the Slurm reservation that controls this state. In the
following example output, the Capacity Block is `scheduled` with a future start
date.

```
$ scontrol show res
ReservationName=node-fanout-scheduled StartTime=2025-10-14T13:09:17 EndTime=2025-10-14T13:11:17 Duration=00:02:00
   Nodes=node-fanout-[1-4] NodeCnt=4 CoreCnt=16 Features=(null) PartitionName=(null) Flags=MAINT,SPEC_NODES
   TRES=cpu=16
   Users=root Groups=(null) Accounts=(null) Licenses=(null) State=ACTIVE BurstBuffer=(null)
   MaxStartDelay=(null)
   Comment=node-fanout Scheduled
```

**How can I tell if the errors I'm getting while launching capacity are because my Capacity
Block is shared?**

Check **Capacity Reservations** in the Amazon EC2 console to find how many
instances from the Capacity Block are actively provisioned. Check the tags of each instance to
find which service or cluster uses it. For example, all instances for AWS PCS have AWS PCS tags
such as `aws:pcs:cluster-id = pcs_l0mizqyk5o | aws:pcs:compute-node-group-id =
 pcs_ic7onkmfqk` that indicate which clusters and compute node groups the instance
belongs to. You can then check if the Capacity Block is at maximum capacity.

You use `scontrol show nodes` to check if a Capacity Block node in an AWS PCS
cluster is triggering `ReservationCapacityExceeded`:

```
[root@ip-172-16-10-54 ~]# scontrol show nodes test-node-8-gamma-cb-2
NodeName=test-8-gamma-cb-2 CoresPerSocket=1
   CPUAlloc=0 CPUEfctv=8 CPUTot=8 CPULoad=0.00
   AvailableFeatures=test-8-gamma-cb,gpu
   ActiveFeatures=test-8-gamma-cb,gpu
   Gres=gpu:H100:1
   NodeAddr=test-8-gamma-cb-2 NodeHostName=test-8-gamma-cb-2
   RealMemory=249036 AllocMem=0 FreeMem=N/A Sockets=8 Boards=1
   State=IDLE+CLOUD+POWERING_DOWN ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=my-q
   BootTime=None SlurmdStartTime=None
   LastBusyTime=Unknown ResumeAfterTime=None
   CfgTRES=cpu=8,mem=249036M,billing=8
   AllocTRES=
   CurrentWatts=0 AveWatts=0
   Reason=Failed to launch backing instance (Error Code: ReservationCapacityExceeded) [root@2025-08-28T15:15:33]
```

**When multiple compute node groups are attached to the same queue, how can I force a job to
run on Capacity Block-backed instances?**

You can use Slurm features and constraints to lock a job to a certain set of nodes. We
recommend that you don't set Slurm weights for each compute node group because that only works
with nodes that aren't in the `maint` state.
