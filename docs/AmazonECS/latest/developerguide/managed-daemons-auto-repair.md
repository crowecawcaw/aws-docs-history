# Daemon auto repair

Amazon ECS treats all daemons as critical to instance health. If any daemon task stops or
becomes unhealthy, Amazon ECS considers the instance impaired and automatically drains and
replaces it. The daemon auto repair actions are as follows:

1. Amazon ECS detects when a daemon task stops or becomes unhealthy.
2. Amazon ECS marks the instance as draining, which prevents it from accepting new
   application tasks.
3. Amazon ECS provisions a replacement instance and starts the daemon task on it.
4. After the daemon task reaches a healthy state, Amazon ECS schedules the application
   tasks from the draining instance onto the replacement.
5. Amazon ECS terminates the original instance.

###### Important

Daemon health checks are optional but highly recommended. Without a health check,
Amazon ECS can only detect failures when the daemon task stops.

You can monitor daemon health using the `DescribeContainerInstances` API or
`DescribeTasks` API.
