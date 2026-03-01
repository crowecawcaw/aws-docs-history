# Amazon ECS Availability Zone service rebalancing service event messages

The following are examples of service event messages you might see.

## service (`service-name`) is not AZ balanced with `number-tasks` tasks in `Availability Zone 1`, `number-tasks` in `Availability Zone 2`, and `number-tasks` in `Availability Zone 3`. AZ Rebalancing in progress.

The service scheduler sends a `service
 (`service-name`) is not AZ balanced` service
event when the number of tasks is not evenly spread across Availability Zones. There
is no action to take. This is an information event.

## service (`service-name`) is AZ balanced with `number-tasks` tasks in `Availability Zone 1`, `number-tasks` tasks in `Availability Zone 2`, and `number-tasks` tasks in `Availability Zone 3`.

The service scheduler sends a `service
 (`service-name`) is AZ balanced` service
event when Availability Zone service rebalancing completes. There is no action to
take. This is an information event.

## `service-name` has started `number-tasks` tasks in `Availability Zone` to AZ Rebalance: `task-ids`.

The service scheduler sends a
`service-name`/`task-set-name`
has started `number` tasks in `Availability
 Zone` service event when it starts tasks in an Availability Zone
because of service rebalancing. There is no action to take. This is an information
event.

## `service-name` has stopped `number-tasks` running tasks in `Availability Zone` due to AZ rebalancing: `task-id`.

The service scheduler sends a
`service-name`/`task-set-name`
has stopped `number` tasks in `Availability
 Zone` service event when it stops tasks in an Availability Zone
because of service rebalancing. There is no action to take. This is an information
event.

## service (`service-name`) is unable to place a task in `Availability Zone` because no container instance met all of its requirements.

The service scheduler sends a `service-name` is unable to
place a task in `Availability Zone` service event because
no container instance met all of its requirements. To address the issue, launch
instances in the Availability Zone.

## service (`service-name`) is unable to place a task in `Availability Zone`.

The service scheduler sends a `service-name` is unable to
place a task in `Availability Zone` service event when you
use the Fargate and there is no available capacity.

You can add additional subnets in the Availability Zone in the error message, or
contact Support to get additional capacity.

## service (`service-name`) was unable to AZ Rebalance because `task-set-name` was unable to scale in due to `reason`.

The service scheduler sends a `service-name` was unable
to AZ Rebalance because `task-set-name` was unable to scale
in due to `reason` service event when you use task scale-in
protection.

You can do one the following:

- Wait until the protection on the current tasks expire, enabling them to be
  terminated.
- Determine which tasks can be stopped and use the
  `UpdateTaskProtection` API with the
  `protectionEnabled` option set to `false` to unset
  protection for these tasks.
- Increase the desired task count of the service to more than the number of
  protected tasks.

## service (`service-name`) stopped AZ Rebalancing.

The service scheduler sends a `service-name` stopped AZ
Rebalancing service event when the Availability Zone rebalancing operation stopped. This is
an information event. Amazon ECS sends additional events which provide more
information.
