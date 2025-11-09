# Slurm Workload Manager (`slurm`)

## Cluster capacity size and update

The capacity of the cluster is defined by the number of compute nodes the cluster
can scale. Compute nodes are backed by Amazon EC2 instances defined within compute
resources in the AWS ParallelCluster configuration
`(Scheduling/SlurmQueues/ComputeResources)`, and are organized into queues
`(Scheduling/SlurmQueues)` that map 1:1 to Slurm partitions.

Within a compute resource it’s possible to configure the minimum number of compute
nodes (instances) that must always be kept running in the cluster
(`MinCount`),
and the maximum number of instances the compute resource can scale to
([MaxCount3](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MaxCount "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MaxCount")).

At cluster creation time, or upon a cluster update, AWS ParallelCluster launches as
many Amazon EC2 instances as configured in `MinCount` for each compute resource
(`Scheduling/SlurmQueues/ ComputeResources`)
defined in the cluster. The instances
launched to cover the minimal amount of nodes for a compute resources in the cluster
are called **\*static
nodes**.\* Once started, static nodes are meant to be
persistent in the cluster and they are not terminated by the system, unless a
particular event or condition occurs. Such events include, for example, the failure
of Slurm or Amazon EC2 health checks and the change of the Slurm node status to DRAIN or
DOWN.

The Amazon EC2 instances, in the range of `1` to `‘MaxCount -
 MinCount’` (`MaxCount`
_minus_ `MinCount)`, launched on-demand to deal with
the increased load of the cluster, are referred to as **_dynamic nodes_**. Their nature
is ephemeral, they are launched to serve pending jobs and are terminated once they
stay idle for a period of time defined by `Scheduling/SlurmSettings/ScaledownIdletime`
in the cluster configuration (default: 10 minutes).

Static nodes and dynamic node comply to the following naming schema:

- Static nodes
  `<Queue/Name>-st-<ComputeResource/Name>-<num>` where
  `<num> = 1..ComputeResource/MinCount`
- Dynamic nodes
  `<Queue/Name>-dy-<ComputeResource/Name>-<num>` where
  `<num> = 1..(ComputeResource/MaxCount -
ComputeResource/MinCount)`

For example given the following AWS ParallelCluster configuration:

```

Scheduling:
    Scheduler: Slurm
    SlurmQueues:
        - Name: queue1
            ComputeResources:
                - Name: c5xlarge
                    Instances:
                        - InstanceType: c5.xlarge
                        MinCount: 100
                        MaxCount: 150
```

The following nodes will be defined in Slurm

```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     50  idle~ queue1-dy-c5xlarge-[1-50]
queue1*      up   infinite    100   idle queue1-st-c5xlarge-[1-100]

```

When a compute resource has `MinCount == MaxCount`, all the
corresponding compute nodes will be static and all the instances will be launched at
cluster creation/update time and kept up and running. For example:

```

Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue1
      ComputeResources:
        - Name: c5xlarge
          Instances:
            - InstanceType: c5.xlarge
          MinCount: 100
          MaxCount: 100

```

```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite    100   idle queue1-st-c5xlarge-[1-100]

```

## Cluster capacity update

The update of the cluster capacity includes adding or removing queues, compute
resources or changing the `MinCount/MaxCount` of a compute resource.
Starting from AWS ParallelCluster version 3.9.0, reducing the size of a queue requires
the compute fleet to be stopped or [QueueUpdateStrategy](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy")
set to TERMINATE for before a cluster update to
take place. It’s not required to stop the compute fleet or to set [QueueUpdateStrategy](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy "Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy")
to TERMINATE when:

- Adding new queues to Scheduling/[SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues")
- Adding new compute resources `Scheduling/SlurmQueues/ComputeResources`
  to a queue
- Increasing the `MaxCount`
  of a compute resource
- Increasing MinCount of a compute resource and increasing MaxCount of the
  same compute resource of at least the same amount

## Considerations and limitations

This section is meant to outline any important factors, constraints, or
limitations that should be taken into account when resizing the cluster
capacity.

- When removing a queue from `Scheduling/SlurmQueues` all the compute nodes with name
  `<Queue/Name>-*` , both static and dynamic, will be
  removed from the Slurm configuration and the corresponding Amazon EC2 instances
  will be terminated.
- When removing a compute resource `Scheduling/SlurmQueues/ComputeResources`
  from a queue, all the compute nodes with name
  `<Queue/Name>-*-<ComputeResource/Name>-*` , both static
  and dynamic, will be removed from the Slurm configuration and the
  corresponding Amazon EC2 instances will be terminated.

When changing the `MinCount` parameter of a compute resource we can
distinguish two different scenarios, if `MaxCount` is kept equal to
`MinCount` (static capacity only), and if `MaxCount` is
greater than `MinCount` (mixed static and dynamic capacity).

### Capacity changes with static nodes only

- If `MinCount == MaxCount` , when increasing
  `MinCount` (and `MaxCount` ), the cluster will
  be configured by extending the number of static nodes to the new value
  of `MinCount`
  `<Queue/Name>-st-<ComputeResource/Name>-<new_MinCount>`
  and the system will keep trying to launch Amazon EC2 instances to fulfill the
  new required static capacity.
- If `MinCount == MaxCount` , when decreasing
  `MinCount` (and `MaxCount` ) of the amount N,
  the cluster will be configured by removing the last N static nodes
  `<Queue/Name>-st-<ComputeResource/Name>-<old_MinCount

* N>...<old_MinCount>]` and the system will terminate the
  corresponding Amazon EC2 instances.
  - Initial state `MinCount = MaxCount = 100`
  - ```

    ```

  $ sinfo
  PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
  queue1\* up infinite 100 idle queue1-st-c5xlarge-[1-100]

  ````
  + Update `-30` on `MinCount` and
   `MaxCount: MinCount = MaxCount = 70`
  + ```

  $ sinfo
  PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
  queue1*      up   infinite     70   idle queue1-st-c5xlarge-[1-70]

  ````

### Capacity changes with mixed nodes

If `MinCount < MaxCount`, when increasing `MinCount`
by an amount N (assuming `MaxCount` will be kept unchanged), the
cluster will be configured by extending the number static nodes to the new value
of `MinCount` ( `old_MinCount + N` ):
`<Queue/Name>-st-<ComputeResource/Name>-<old_MinCount +
 N>` and the system will keep trying to launch Amazon EC2 instances to fulfill
the new required static capacity. Moreover, to honor the `MaxCount`
capacity of the compute resource, the cluster configuration is updated by
_removing the last N dynamic nodes_:
`<Queue/Name>-dy-<ComputeResource/Name>-[<MaxCount -
 old_MinCount - N>...<MaxCount - old_MinCount>]` and the system will
terminate the corresponding Amazon EC2 instances.

- Initial state: `MinCount = 100; MaxCount = 150`
- ```

  ```

$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
queue1* up infinite 50 idle~ queue1-dy-c5xlarge-[1-50]
queue1* up infinite 100 idle queue1-st-c5xlarge-[1-100]

````
* Update +30 to `MinCount : MinCount = 130 (MaxCount =
 150)`
* ```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     20  idle~ queue1-dy-c5xlarge-[1-20]
queue1*      up   infinite    130   idle queue1-st-c5xlarge-[1-130]

````

If `MinCount < MaxCount`, when increasing `MinCount`
and `MaxCount` of the same amount N, the cluster will be configured
by extending the number static nodes to the new value of `MinCount` (
`old_MinCount + N` ):
`<Queue/Name>-st-<ComputeResource/Name>-<old_MinCount +
 N>` and the system will keep trying to launch Amazon EC2 instances to fulfill
the new required static capacity. Moreover, no changes will be done on the
number of dynamic nodes to honor the new

`MaxCount` value.

- Initial state: `MinCount = 100; MaxCount = 150`
- ```

  ```

$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
queue1* up infinite 50 idle~ queue1-dy-c5xlarge-[1-50]
queue1* up infinite 100 idle queue1-st-c5xlarge-[1-100]

````
* Update +30 to `MinCount : MinCount = 130 (MaxCount =
 180)`
* ```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     20  idle~ queue1-dy-c5xlarge-[1-50]
queue1*      up   infinite    130   idle queue1-st-c5xlarge-[1-130]

````

If `MinCount < MaxCount`, when decreasing `MinCount`
of the amount N (assuming `MaxCount` will be kept unchanged), the
cluster will be configured by removing the last N static nodes static nodes
`<Queue/Name>-st-<ComputeResource/Name>-[<old_MinCount -
 N>...<old_MinCount>`and the system will terminate the corresponding
Amazon EC2 instances. Moreover, to honor the `MaxCount` capacity of the
compute resource, the cluster configuration is updated by extending the number
of the dynamic nodes to fill the gap `MaxCount - new_MinCount:
 <Queue/Name>-dy-<ComputeResource/Name>-[1..<MazCount -
 new_MinCount>]` In this case, since those are dynamic nodes, no new
Amazon EC2 instances will be launched unless the scheduler has jobs in pending on the
new nodes.

- Initial state: `MinCount = 100; MaxCount = 150`
- ```

  ```

$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
queue1* up infinite 50 idle~ queue1-dy-c5xlarge-[1-50]
queue1* up infinite 100 idle queue1-st-c5xlarge-[1-100]

````
* Update -30 on `MinCount : MinCount = 70 (MaxCount =
 120)`
* ```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     80  idle~ queue1-dy-c5xlarge-[1-80]
queue1*      up   infinite     70   idle queue1-st-c5xlarge-[1-70]

````

If `MinCount < MaxCount`, when decreasing `MinCount`
and `MaxCount` of the same amount N, the cluster will be configured
by removing the last N static nodes
`<Queue/Name>-st-<ComputeResource/Name>-<old_MinCount -
 N>...<oldMinCount>]` and the system will terminate the
corresponding Amazon EC2 instances.

Moreover, no changes will be done on the number of dynamic nodes to honor the
new `MaxCount` value.

- Initial state: `MinCount = 100; MaxCount = 150`
- ```

  ```

$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
queue1* up infinite 50 idle~ queue1-dy-c5xlarge-[1-50]
queue1* up infinite 100 idle queue1-st-c5xlarge-[1-100]

````
* Update -30 on `MinCount : MinCount = 70 (MaxCount =
 120)`
* ```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     80  idle~ queue1-dy-c5xlarge-[1-50]
queue1*      up   infinite     70   idle queue1-st-c5xlarge-[1-70]

````

If `MinCount < MaxCount`, when decreasing `MaxCount`
of the amount N (assuming `MinCount` will be kept unchanged), the
cluster will be configured by removing the last N dynamic nodes
`<Queue/Name>-dy-<ComputeResource/Name>-<old_MaxCount -
 N...<oldMaxCount>]` and the system will terminate the corresponding
Amazon EC2 instances in the case they were running.No impact is expected on the static
nodes.

- Initial state: `MinCount = 100; MaxCount = 150`
- ```

  ```

$ sinfo
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
queue1* up infinite 50 idle~ queue1-dy-c5xlarge-[1-50]
queue1* up infinite 100 idle queue1-st-c5xlarge-[1-100]

````
* Update -30 on `MaxCount : MinCount = 100 (MaxCount =
 120)`
* ```

$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
queue1*      up   infinite     20  idle~ queue1-dy-c5xlarge-[1-20]
queue1*      up   infinite    100   idle queue1-st-c5xlarge-[1-100]

````

## Impacts on the Jobs

In all the cases where nodes are removed and Amazon EC2 instances terminated, a sbatch
job running on the removed nodes will be re-queued, unless there are no other nodes
satisfying the job requirements. In this last case, the job fails with status
NODE_FAIL and disappears from the queue and it must be
re-submitted manually.

If you are planning to perform a cluster resize update, you can prevent jobs to go
running in the nodes that are going to be removed during the planned update. This is
possible by setting the nodes to be removed in maintenance. Please be aware that
setting a node in maintenance would not impact jobs that are eventually already
running in the node.

Suppose that with the planned cluster resize update you are going to remove the
node `qeueu-st-computeresource-[9-10`]. You can create a Slurm
reservation with the following command

```
sudo -i scontrol create reservation ReservationName=maint_for_update user=root starttime=now duration=infinite flags=maint,ignore_jobs nodes=qeueu-st-computeresource-[9-10]
```

This will create a Slurm reservation named `maint_for_update` on the
nodes `qeueu-st-computeresource-[9-10]`. From the time when the
reservation is created, no more jobs can go running into the nodes
`qeueu-st-computeresource-[9-10]`. Please be aware that the
reservation will not prevent jobs to be eventually allocated on the nodes
`qeueu-st-computeresource-[9-10]`.

After the cluster resize update, if the Slurm reservation was set only on nodes
that were removed during the resize update, the maintenance reservation will be
automatically deleted. If instead you had created a Slurm reservation on nodes
that are still present after the cluster resize update, we may want to remove the
maintenance reservation on the nodes after the resize update is performed, by using
the following command

```
sudo -i scontrol delete ReservationName=maint_for_update
```

For additional details on Slurm reservation, see the official SchedMD doc [here](https://slurm.schedmd.com/reservations.html "https://slurm.schedmd.com/reservations.html").

## Cluster update process on capacity changes

Upon a scheduler configuration change, the following steps are executed during the
cluster update process:

- Stop AWS ParallelCluster `clustermgtd (supervisorctl stop
clustermgtd)`
- Generate updated Slurm partitions configuration from AWS ParallelCluster
  configuration
- Restart `slurmctld` (done through Chef service recipe)
- Check `slurmctld` status `(systemctl is-active --quiet
slurmctld.service)`
- Reload Slurm configuration `(scontrol reconfigure)`
- Start `clustermgtd (supervisorctl start clustermgtd)`

For information about Slurm, see [https://slurm.schedmd.com](https://slurm.schedmd.com "https://slurm.schedmd.com"). For downloads, see [https://github.com/SchedMD/slurm/tags](https://github.com/SchedMD/slurm/tags "https://github.com/SchedMD/slurm/tags"). For the source code, see [https://github.com/SchedMD/slurm](https://github.com/SchedMD/slurm "https://github.com/SchedMD/slurm").

## Supported cluster and SLURM versions

The following table lists the AWS ParallelCluster and Slurm versions that AWS
supports.

| AWS ParallelCluster version(s) | Supported Slurm version |
| ------------------------------ | ----------------------- |
| 3.13.0                         | 24.05.07                |
| 3.12.0                         | 23.11.10                |
| 3.11.0                         | 23.11.10                |
| 3.9.2, 3.9.3, 3.10.0           | 23.11.7                 |
| 3.9.0, 3.9.1                   | 23.11.4                 |
| 3.8.0                          | 23.02.7                 |
| 3.7.2                          | 23.02.6                 |
| 3.7.1                          | 23.02.5                 |
| 3.7.0                          | 23.02.4                 |
| 3.6.0, 3.6.1                   | 23.02.2                 |
| 3.5.0, 3.5.1                   | 22.05.8                 |
| 3.4.0, 3.4.1                   | 22.05.7                 |
| 3.3.0, 3.3.1                   | 22.05.5                 |
| 3.1.4, 3.1.5, 3.2.0, 3.2.1     | 21.08.8-2               |
| 3.1.2, 3.1.3                   | 21.08.6                 |
| 3.1.1                          | 21.08.5                 |
| 3.0.0                          | 20.11.8                 |

###### Topics

- [Configuration of multiple queues](configuration-of-multiple-queues-v3.md "configuration-of-multiple-queues-v3.md")
- [Slurm guide for multiple
  queue mode](multiple-queue-mode-slurm-user-guide-v3.md "multiple-queue-mode-slurm-user-guide-v3.md")
- [Slurm cluster protected mode](slurm-protected-mode-v3.md "slurm-protected-mode-v3.md")
- [Slurm cluster fast insufficient capacity fail-over](slurm-short-capacity-fail-mode-v3.md "slurm-short-capacity-fail-mode-v3.md")
- [Slurm memory-based scheduling](slurm-mem-based-scheduling-v3.md "slurm-mem-based-scheduling-v3.md")
- [Multiple instance type allocation with Slurm](slurm-multiple-instance-allocation-v3.md "slurm-multiple-instance-allocation-v3.md")
- [Cluster scaling for dynamic nodes](scheduler-node-allocation-v3.md "scheduler-node-allocation-v3.md")
- [Slurm accounting with AWS ParallelCluster](slurm-accounting-v3.md "slurm-accounting-v3.md")
- [Slurm configuration customization](slurm-configuration-settings-v3.md "slurm-configuration-settings-v3.md")
- [Slurmprolog and epilog](slurm-prolog-epilog-v3.md "slurm-prolog-epilog-v3.md")
- [Cluster capacity size and update](slurm-cluster-capacity-size-and-update.md "slurm-cluster-capacity-size-and-update.md")
