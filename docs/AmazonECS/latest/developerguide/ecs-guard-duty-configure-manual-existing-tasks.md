# Adding Runtime Monitoring to

existing Amazon ECS tasks

When you turn on Runtime Monitoring, all new standalone tasks, and new service deployments
in the cluster are protected automatically. In order to preserve the immutability
constraint, existing tasks are not affected.

## Prerequisites

- Turn on Runtime Monitoring. For more information, see [Turning on Runtime Monitoring for Amazon ECS](ecs-guard-duty-configure-manual-guard-duty.md "ecs-guard-duty-configure-manual-guard-duty.md").

## Procedure

- To immediately protect a task, you need
  to perform one of the following actions:
  - For standalone tasks, stop the tasks, and then start them. For more information, see [Stopping an Amazon ECS task](standalone-task-stop.md "standalone-task-stop.md") and [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md").
  - For tasks that are part of a service, update the service with the
    "force new deployment" option. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
