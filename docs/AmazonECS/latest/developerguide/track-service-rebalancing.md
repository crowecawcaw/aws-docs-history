

# Track Amazon ECS Availability Zone rebalancing
<a name="track-service-rebalancing"></a>

You can verify if Availability Zone rebalancing is enabled for a service in the console or by calling `describe-services`. The following example can be used to see the status with the CLI.

The response will be either `ENABLED` or `DISABLED`.

```
aws ecs describe-services \
    --services {{service-name}} \
    --cluster {{cluster-name}} \
    --query services[0].availabilityZoneRebalancing
```

## Service events
<a name="service-info-events"></a>

Amazon ECS sends service action events to help you understand the Availability Zone rebalancing lifecycle. 


| Event | Scenario | Type | Learn more | 
| --- | --- | --- | --- | 
| SERVICE\_REBALANCING\_STARTED | Amazon ECS starts an Availability Zone rebalancing operation | INFO | [service ({{service-name}}) is not AZ balanced with {{number-tasks}} tasks in {{Availability Zone 1}}, {{number-tasks}} in {{Availability Zone 2}}, and {{number-tasks}} in {{Availability Zone 3}}. AZ Rebalancing in progress.](service-rebalancing-event-messages-list.md#service-rebalancing-started) | 
| SERVICE\_REBALANCING\_COMPLETED | The Availability Zone rebalancing operation completes |  INFO | [service ({{service-name}}) is AZ balanced with {{number-tasks}} tasks in {{Availability Zone 1}}, {{number-tasks}} tasks in {{Availability Zone 2}}, and {{number-tasks}} tasks in {{Availability Zone 3}}.](service-rebalancing-event-messages-list.md#service-rebalancing-completed) | 
| TASKS\_STARTED | Amazon ECS successfully starts tasks as part of the Availability Zone rebalancing operation | INFO | [{{service-name}} has started {{number-tasks}} tasks in {{Availability Zone}} to AZ Rebalance: {{task-ids}}.](service-rebalancing-event-messages-list.md#service-rebalancing-tasks-started) | 
| TASKS\_STOPPED | Amazon ECS successfully stops tasks as part of the Availability Zone rebalancing operation | INFO | [{{service-name}} has stopped {{number-tasks}} running tasks in {{Availability Zone}} due to AZ rebalancing: {{task-id}}.](service-rebalancing-event-messages-list.md#service-rebalancing-tasks-stopped) | 
| SERVICE\_TASK\_PLACEMENT\_FAILURE | Amazon ECS failed to start a task as part of the Availability Zone rebalancing operation | ERROR | For EC2, see [service ({{service-name}}) is unable to place a task in {{Availability Zone}} because no container instance met all of its requirements.](service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure-instance)For the Fargate, see [service ({{service-name}}) is unable to place a task in {{Availability Zone}}.](service-rebalancing-event-messages-list.md#service-rebalancing-placement-failure) | 
| TASKSET\_SCALE\_IN\_FAILURE\_BY\_TASK\_PROTECTION | The Availability Zone rebalancing operation is blocked because task protection is in use. | INFO | [service ({{service-name}}) was unable to AZ Rebalance because {{task-set-name}} was unable to scale in due to {{reason}}.](service-rebalancing-event-messages-list.md#service-rebalancing-task-protection-failure) | 
| SERVICE\_REBALANCING\_STOPPED | The Availability Zone rebalancing operation stopped. Amazon ECS sends additional events which provide more information. | INFO | [service ({{service-name}}) stopped AZ Rebalancing.](service-rebalancing-event-messages-list.md#service-rebalancing-operation-stopped) | 

## Task state change events
<a name="task-state-change-events"></a>

Amazon ECS sends a task state change event (`START`) for each task that it starts as part of the rebalancing process.

Amazon ECS sends a task state change event (`STOPPED`) event for each task that it stops as part of the rebalancing process. The reason is set to `Availability-zone rebalancing initiated by (deployment ecs-svc/{{deployment-id}})`.

For more information about the events, see [Amazon ECS task state change events](ecs_task_events.md).