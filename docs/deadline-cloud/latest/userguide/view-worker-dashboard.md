# View worker details in the worker

dashboard

The _worker dashboard_ provides details for the worker that
processes a task. You can see:

- Metadata, such as the instance type, for the worker
- The session actions that the worker performed
- Worker performance, including CPU, memory and disk usage
- A graph of the CPU, memory, and disk usage over time
- A graph of the disk speed over time
- The worker log for the task

###### To view the worker dashboard from a task

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md "view-a-job.md") to
   view a list of jobs.
2. Select a job from the **Jobs** list.
3. Select a step from the **Steps** list.
4. Select a task from the **Tasks** list.
5. In the task table, from the **Actions** menu,
   choose **View worker dashboard**.

###### To view the worker dashboard from fleet details

1. Follow the steps in [View queue and fleet details in Deadline Cloud](view-queue-and-fleet.md "view-queue-and-fleet.md") to view a fleet.
2. Select a **Worker** from the **Workers**
   list.
3. From the **Actions** menu, choose **View worker
   dashboard**.

## Use cases

### Detecting under-provisioned instances

When renders take longer than expected, the worker dashboard can help determine
if your instances are adequately sized for your workloads. While 100% vCPU utilization
is normal for many renderers, consistently high memory usage near maximum capacity
and elevated disk space utilization may indicate that your instances are
under-provisioned. In such cases, upgrading your fleet's instance configuration can
reduce render errors and significantly improve render times. However, it's important
to continue monitoring worker performance after upgrading to ensure you've found the
optimal balance - upgrading too aggressively can lead to unnecessary costs through
over-provisioning.

### Detecting over-provisioned instances

Even when tasks are completing successfully, there may be opportunities to optimize
your costs. The worker dashboard can reveal if you're paying for more compute power
than your workloads require. If you see that the worker has low average vCPU usage,
minimal memory utilization, and excess unused disk space, you can downsize the instance
configuration of your fleet.

### Troubleshooting failed tasks

When investigating failed tasks, the worker dashboard serves as a valuable diagnostic
tool. Pay particular attention to peak memory usage and disk space utilization - if
these metrics approach or reach 100%, they're likely the root cause of your task
failures. Such resource exhaustion indicates that your current instances lack the
capacity to handle your workloads effectively. In these cases, provisioning instances
with increased memory or disk space will help ensure successful task completion.

### Optimal instance utilization rate

**vCPU Utilization**

**Target range: 70–90%**

- **Below 70%**:
  Likely underutilizing compute resources, meaning you're paying for more
  CPU than your workload needs
- **70–90%**:
  Optimal range where you're efficiently using resources without hitting
  bottlenecks
- **Consistently at 100%**: Could indicate
  CPU bottlenecks that might slow down renders

Keep in mind that some render tasks will naturally be more CPU-intensive than others,
and 100% vCPU usage may not be an issue. Real-time visualization tasks might show more
consistent CPU utilization, while tasks with changing computational requirements might
have varying patterns.

**Memory Utilization**

**Target range: 70–85%**

- **Below 50%**:
  Potentially oversized instances for your workload
- **70–85%**:
  Optimal utilization with enough headroom for spikes
- **Above 90%**: Risk
  of performance degradation or out-of-memory errors

Memory requirements can vary significantly depending on scene complexity, texture
resolution, and simulation data. Monitoring memory trends over time is important to identify
if your workloads are growing in memory requirements.

**Disk Space Utilization**

**Target range: 60–80%**

- **Below 40%**:
  Likely over-provisioned storage
- **60–85%**:
  Good utilization with room for temporary files and caches
- **Above 85%**: Risk
  of running out of space during large renders

Remember that disk I/O performance can be just as important as capacity, especially for workloads
that read/write large texture or cache files during rendering.
