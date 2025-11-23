# Amazon ECS service throttle logic

The Amazon ECS service scheduler includes protective logic that throttles task launches when tasks repeatedly fail to start. This helps prevent unnecessary resource consumption and reduces costs.

When tasks in a service fail to transition from `PENDING` to `RUNNING` state and instead move directly to `STOPPED`, the scheduler:

- Incrementally increases the time between restart attempts
- Continues increasing delays up to a maximum of 27 minutes between attempts
- Generates a service event message to notify you of the issue

###### Note

The maximum delay period of 27 minutes may change in future updates.

When throttling is activated, you receive this service event message:

```
(service `service-name`) is unable to consistently start tasks successfully.
```

Important characteristics of the throttle logic:

- Services continue retry attempts indefinitely
- The only modification is the increased time between restarts
- There are no user-configurable parameters

## Resolving throttling issues

To resolve throttling, you can:

- Update the service to use a new task definition, which immediately returns the service to normal, non-throttled operation. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
- Address the underlying cause of the task failures.

Common causes of task failures that trigger throttling include:

- Insufficient cluster resources (ports, memory, or CPU)
  - Indicated by an [insufficient resource service event message](service-event-messages-list.md#service-event-messages-1 "service-event-messages-list.md#service-event-messages-1")

- Container image pull failures
  - Can be caused by invalid image names, tags, or insufficient permissions
  - Results in `CannotPullContainerError` in [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md")

- Insufficient disk space
  - Results in `CannotCreateContainerError` in [stopped task errors](stopped-task-errors.md "stopped-task-errors.md")
  - For resolution steps, see [Troubleshoot the Docker API error (500):
    devmapper in Amazon ECS](CannotCreateContainerError.md "CannotCreateContainerError.md")

###### Important

The following scenarios do NOT trigger throttle logic:

- Tasks that stop after reaching `RUNNING` state
- Tasks stopped due to failed ELB health checks
- Tasks where the container command exits with a non-zero code after reaching `RUNNING` state
