

# Daemon auto repair
<a name="managed-daemons-auto-repair"></a>

A daemon can be critical or non-critical to instance health, which you control with the `critical` parameter when you create or update the daemon. The `critical` parameter defaults to `true`, so a daemon is critical unless you set `critical` to `false`.

For a critical daemon, if the daemon task stops or becomes unhealthy, Amazon ECS considers the instance impaired and automatically drains and replaces it. The daemon auto repair actions for a critical daemon are as follows:

1. Amazon ECS detects when a daemon task stops or becomes unhealthy.

1. Amazon ECS marks the instance as draining, which prevents it from accepting new application tasks.

1. Amazon ECS provisions a replacement instance and starts the daemon task on it.

1. After the daemon task reaches a healthy state, Amazon ECS schedules the application tasks from the draining instance onto the replacement.

1. Amazon ECS terminates the original instance.

For a non-critical daemon, the daemon task operates independently of container instance health. If the daemon task fails, stops, or becomes unhealthy, Amazon ECS keeps the container instance active. A non-critical daemon never blocks instance registration, so application tasks can be placed immediately even if the daemon fails to start.

**Important**  
Daemon health checks are optional but highly recommended. Without a health check, Amazon ECS can only detect failures when the daemon task stops.

You can monitor daemon health using the `DescribeContainerInstances` API or `DescribeTasks` API.

For a non-critical daemon, Amazon ECS keeps the instance active when the daemon task is not running. The following fields report how many instances are in that state:
+ `DescribeDaemon` returns `withoutDaemonCount` for each capacity provider, and `totalWithoutDaemonCount` for the revision across all capacity providers.
+ `DescribeDaemonDeployments` returns `withoutDaemonInstanceCount` for each capacity provider, and `totalWithoutDaemonInstanceCount` for the revision across all capacity providers.

**Note**  
The without-daemon counts are separate from the running counts. `DescribeDaemon` reports `runningCount` and `totalRunningCount`. `DescribeDaemonDeployments` reports `runningInstanceCount` and `totalRunningInstanceCount`. An instance appears in one set or the other, never both, so do not add the two sets together.