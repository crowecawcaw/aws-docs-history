# Track Amazon ECS Availability Zone rebalancing

You can verify if Availability Zone rebalancing is enabled for a service in the console or by
calling `describe-services`. The following example can be used to see the
status with the CLI.

The response will be either `ENABLED` or `DISABLED`.

```
aws ecs describe-services \
    --services `service-name` \
    --cluster `cluster-name` \
    --query services[0].availabilityZoneRebalancing
```

## Service events

Amazon ECS sends service action events to help you understand the Availability Zone rebalancing
lifecycle.

| Event                                         | Scenario                                                                                                                   | Type  | Learn more                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SERVICE_REBALANCING_STARTED`                 | Amazon ECS starts an Availability Zone rebalancing operation                                                               | INFO  | [service<br>(service-name) is not AZ balanced with<br>number-tasks tasks in Availability<br>Zone 1, number-tasks in<br>Availability Zone 2, and<br>number-tasks in Availability Zone<br>3. AZ Rebalancing in progress.](service-rebalancing-event-messages-list.md#service-rebalancing-started "service-rebalancing-event-messages-list.md#service-rebalancing-started")                                                                                                                                                                                                                                                    |
| `SERVICE_REBALANCING_COMPLETED`               | The Availability Zone rebalancing operation completes                                                                      | INFO  | [service<br>(service-name) is AZ balanced with<br>number-tasks tasks in Availability<br>Zone 1, number-tasks tasks in<br>Availability Zone 2, and<br>number-tasks tasks in Availability<br>Zone 3.](service-rebalancing-event-messages-list.md#service-rebalancing-completed "service-rebalancing-event-messages-list.md#service-rebalancing-completed")                                                                                                                                                                                                                                                                    |
| `TASKS_STARTED`                               | Amazon ECS successfully starts tasks as part of the<br>Availability Zone rebalancing operation                             | INFO  | [service-name has started<br>number-tasks tasks in Availability<br>Zone to AZ Rebalance:<br>task-ids.](service-rebalancing-event-messages-list.md#service-rebalancing-tasks-started "service-rebalancing-event-messages-list.md#service-rebalancing-tasks-started")                                                                                                                                                                                                                                                                                                                                                         |
| `TASKS_STOPPED`                               | Amazon ECS successfully stops tasks as part of the<br>Availability Zone rebalancing operation                              | INFO  | [service-name has stopped<br>number-tasks running tasks in<br>Availability Zone due to AZ rebalancing:<br>task-id.](service-rebalancing-event-messages-list.md#service-rebalancing-tasks-stopped "service-rebalancing-event-messages-list.md#service-rebalancing-tasks-stopped")                                                                                                                                                                                                                                                                                                                                            |
| `SERVICE_TASK_PLACEMENT_FAILURE`              | Amazon ECS failed to start a task as part of the Availability Zone rebalancing<br>operation                                | ERROR | For EC2, see [service<br>(service-name) is unable to place a task in<br>Availability Zone because no container instance<br>met all of its requirements.](service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure-instance "service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure-instance")<br>For the Fargate, see [service<br>(service-name) is unable to place a task in<br>Availability Zone.](service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure "service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure") |
| `TASKSET_SCALE_IN_FAILURE_BY_TASK_PROTECTION` | The Availability Zone rebalancing operation is blocked because task<br>protection is in use.                               | INFO  | [service<br>(service-name) was unable to AZ Rebalance because task-set-name was unable to scale in due to reason.](service-rebalancing-event-messages-list.md#service-rebalancing-task-protection-failure "service-rebalancing-event-messages-list.md#service-rebalancing-task-protection-failure")                                                                                                                                                                                                                                                                                                                         |
| `SERVICE_REBALANCING_STOPPED`                 | The Availability Zone rebalancing operation stopped. Amazon ECS sends<br>additional events which provide more information. | INFO  | [service<br>(service-name) stopped AZ Rebalancing.](service-rebalancing-event-messages-list.md#service-rebalancing-operation-stopped "service-rebalancing-event-messages-list.md#service-rebalancing-operation-stopped")                                                                                                                                                                                                                                                                                                                                                                                                    |

## Task state change events

Amazon ECS sends a task state change event (`START`) for each task that it
starts as part of the rebalancing process.

Amazon ECS sends a task state change event (`STOPPED`) event for each task
that it stops as part of the rebalancing process. The reason is set to
`Availability-zone rebalancing initiated by (deployment
 ecs-svc/`deployment-id`)`.

For more information about the events, see [Amazon ECS task state change events](ecs_task_events.md "ecs_task_events.md").
