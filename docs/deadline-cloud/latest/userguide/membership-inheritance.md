# Membership inheritance

Deadline Cloud uses a hierarchical membership model where permissions can be assigned at the farm, queue,
or fleet level. Understanding how membership inheritance works helps you configure access control
effectively.

Membership controls access to view and manage resources. Membership does not
affect where jobs run. For example, assigning a group to a fleet lets the group's
members see the fleet and its workers, but it does not route their jobs to that
fleet. The service schedules jobs based on queue–fleet associations and each
step's host requirements. For more information, see [Schedule
jobs in Deadline Cloud](../developerguide/build-jobs-scheduling.md "../developerguide/build-jobs-scheduling.md") in the _Deadline Cloud Developer Guide_.

## Farm-level membership

When you assign a user or group membership at the farm level, that membership applies to all
queues and fleets within the farm. Farm-level membership provides broad access and is useful for
users who need to work across multiple queues or fleets.

For example, if you assign a user as a Contributor at the farm level, that user can submit
jobs to any queue in the farm.

## Queue and fleet-level membership

You can assign membership at the queue or fleet level to grant access to specific
resources. Queue-level and fleet-level membership applies only to that resource.

For example, if you assign a user as a Manager on a specific queue, that user can edit jobs
and manage access only for that queue, not for other queues in the farm.

Users can have access to only a queue or fleet without having farm-level membership. In this
case, the user cannot see the farm in their farm list, but can submit jobs to and view only
the queues or fleets they have access to.

## Effective permissions

When a user has membership at multiple levels, Deadline Cloud applies the highest access level.
Lower-level assignments cannot reduce farm-level permissions. For example:

- A user with Viewer access at the farm level and Manager access on a specific queue
  has Manager permissions on that queue and Viewer permissions on all other queues.
- A user with Owner access at the farm level retains Owner permissions on any queue,
  even if that queue has a Viewer-level assignment.

###### Note

Users without any membership at the farm, queue, or fleet level cannot access those
resources, even if they are authenticated through IAM Identity Center.

For instructions on assigning membership to users and groups, see
[Assign permissions to users and groups](assign-permissions-procedure.md "assign-permissions-procedure.md").
