# Adding Runtime Monitoring to existing Amazon ECS Fargate tasks

When you turn on Runtime Monitoring, all new standalone tasks, and new service deployments
in the cluster are protected automatically. In order to preserve the immutability
constraint, existing tasks are not affected.

## Prerequisites

1. Turn on Runtime Monitoring. For more information, see [Turning on Runtime Monitoring for Amazon ECS](ecs-guard-duty-configure-automatic-guard-duty.md "ecs-guard-duty-configure-automatic-guard-duty.md").
2. Fargate tasks must use a task execution role. This role grants the tasks
   permission to retrieve, update, and manage the GuardDuty security agent on your
   behalf. For more information see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

## Procedure

- To immediately protect a task, you need
  to perform one of the following actions:
  - For standalone tasks, stop the tasks, and then start them. For more information, see [Stopping an Amazon ECS task](standalone-task-stop.md "standalone-task-stop.md") and [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md")
  - For tasks that are part of a service, update the service with the
    "force new deployment" option. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
