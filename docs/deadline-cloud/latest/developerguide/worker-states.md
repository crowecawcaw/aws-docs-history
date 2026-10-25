

# Worker states and lifecycle
<a name="worker-states"></a>

A *worker* is a host in a fleet that runs the tasks that make up your jobs. Each worker runs the Deadline Cloud worker agent, which connects the host to your farm. Every worker has a status, on both service-managed and customer-managed fleets. You can see the status in the worker status column of the Deadline Cloud monitor and in the `status` field that the [GetWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetWorker.html) and [ListWorkers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListWorkers.html) operations return. The status shows whether the worker is available for work, shutting down, or no longer connected. It also determines whether Deadline Cloud charges for the worker.

## Worker statuses
<a name="worker-states-definitions"></a>

The following table lists the worker statuses in lifecycle order.


| Status | Description | 
| --- | --- | 
| `CREATED` | The worker agent registered the worker, and Deadline Cloud acknowledged the registration. The worker isn't ready for work yet. | 
| `STARTED` | The worker is connected and ready to receive tasks. | 
| `IDLE` | The worker is connected, and Deadline Cloud has no tasks assigned to it. | 
| `RUNNING` | The worker is connected, and Deadline Cloud has assigned tasks to it. | 
| `STOPPING` | The worker is shutting down and doesn't accept new tasks. | 
| `STOPPED` | The worker isn't running tasks, won't receive new tasks, and no longer sends heartbeats. Deadline Cloud still knows about the worker. The host can be shut down. | 
| `NOT_RESPONDING` | Deadline Cloud stopped receiving heartbeats from the worker, for example after a lost connection or a host failure. | 
| `NOT_COMPATIBLE` | The worker's capabilities don't meet the worker requirements of the fleet. | 

The status determines whether Deadline Cloud charges for the worker. For the statuses that incur a charge, see [Charges for workers](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/cost-management.html#worker-charges) in the *Deadline Cloud User Guide*.

## What changes a worker's status
<a name="worker-states-transitions"></a>

The following diagram shows how a worker that runs the Deadline Cloud worker agent moves between statuses. The changes are the same on service-managed and customer-managed fleets. If you write your own worker agent, follow the same changes.

A new worker is registered with the `CREATED` status (1) and changes to `STARTED` when it's ready for work (2). While connected, it moves between `IDLE` and `RUNNING` as tasks are assigned (3). A connected worker changes to `STOPPING` when it starts to shut down (4), to `STOPPED` when it finishes shutting down (5), to `NOT_RESPONDING` when it stops sending heartbeats (6), and to `NOT_COMPATIBLE` when it no longer meets the fleet's requirements (7). A `STOPPING` or `NOT_COMPATIBLE` worker also changes to `STOPPED` (5), and a `CREATED` worker that stops sending heartbeats changes to `NOT_RESPONDING` (6). A `STOPPED` or `NOT_RESPONDING` worker returns to `STARTED` when the worker agent connects again (8, a dashed arrow). The diagram shows a `STOPPED` worker being deleted (9), which is the usual path. You can also delete a `CREATED` worker. Each number matches a row in the table that follows the diagram, which describes the cause of each change.

![State diagram of worker statuses with numbered arrows. Each number matches a row in the following table.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/worker-states-diagram.png)


In the diagram, the connected area holds `STARTED`, `IDLE`, and `RUNNING`. The not-connected area holds `STOPPED`, `NOT_RESPONDING`, and `NOT_COMPATIBLE`. `NOT_RESPONDING` and `NOT_COMPATIBLE` indicate a problem. `CREATED`, `STOPPING`, and the deleted state sit outside both areas.

The following table lists each change and its cause.


| Arrow | From | To | What causes the change | 
| --- | --- | --- | --- | 
| 1 | (none) | `CREATED` | The worker agent registers the worker with the [CreateWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateWorker.html) operation. | 
| 2 | `CREATED` | `STARTED` | The worker agent obtains its credentials and reports that it's ready for work. | 
| 3 | `STARTED`, `IDLE`, or `RUNNING` | `IDLE` or `RUNNING` | Deadline Cloud sets `RUNNING` when it assigns tasks to the worker and `IDLE` when no tasks are assigned. | 
| 4 | `STARTED`, `IDLE`, or `RUNNING` | `STOPPING` | The worker starts to shut down. Deadline Cloud asks the worker to stop, for example when the fleet scales in, or the worker agent starts a drain after an operating system stop signal or an Amazon EC2 Spot interruption. The worker stops accepting new tasks. | 
| 5 | `STARTED`, `IDLE`, `RUNNING`, `STOPPING`, or `NOT_COMPATIBLE` | `STOPPED` | The worker agent finishes shutting down and reports the new status with the [UpdateWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorker.html) operation. The worker agent also sets `STOPPED` when a host configuration script fails, and before it restarts a `NOT_COMPATIBLE` worker. You can also set the status to `STOPPED` yourself with `UpdateWorker`, for example to stop a stuck worker. | 
| 6 | `CREATED`, `STARTED`, `IDLE`, or `RUNNING` | `NOT_RESPONDING` | Deadline Cloud stops receiving heartbeats from the worker agent. | 
| 7 | `STARTED`, `IDLE`, or `RUNNING` | `NOT_COMPATIBLE` | You update the fleet, and the worker's capabilities no longer meet the fleet's worker requirements. | 
| 8 | `STOPPED` or `NOT_RESPONDING` | `STARTED` | The worker agent connects again, for example after you restart the agent or the host. A `NOT_COMPATIBLE` worker must change to `STOPPED` before it can change to `STARTED`. | 
| 9 | `CREATED` or `STOPPED` | Deleted | You or the worker agent delete the worker with the [DeleteWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteWorker.html) operation. Deadline Cloud no longer tracks a deleted worker. | 

For information about shutting down Amazon Elastic Compute Cloud (Amazon EC2) instances when their workers stop, see [Configure the Deadline Cloud worker agent](worker-host.md#worker-agent-config).