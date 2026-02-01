# Membership inheritance

Deadline Cloud uses a hierarchical membership model where permissions can be assigned at the farm, queue,
or fleet level. Understanding how membership inheritance works helps you configure access control
effectively.

## Farm-level membership

When you assign a user or group membership at the farm level, that membership applies to all
queues and fleets within the farm. Farm-level membership provides broad access and is useful for
users who need to work across multiple queues or fleets.

For example, if you assign a user as a Contributor at the farm level, that user can submit
jobs to any queue in the farm.

## Queue and fleet-level membership

You can also assign membership at the queue or fleet level for more granular access control.
Queue-level and fleet-level membership only applies to that specific resource.

For example, if you assign a user as a Manager on a specific queue, that user can edit jobs
and manage access only for that queue, not for other queues in the farm.

Users can have access to only a queue or fleet without having farm-level membership. In this
case, the user cannot see the farm in their farm list, but can submit jobs to and view only
the queues or fleets they have access to.

## Effective permissions

When a user has membership at multiple levels, Deadline Cloud uses the highest access level. For example:

- A user with Viewer access at the farm level and Manager access on a specific queue
  has Manager permissions on that queue and Viewer permissions on all other queues.
- A user with Contributor access at the farm level and Owner access on a specific
  fleet has Owner permissions on that fleet and Contributor permissions elsewhere.

###### Note

Users without any membership at the farm, queue, or fleet level cannot access those
resources, even if they are authenticated through IAM Identity Center.

For instructions on assigning membership to users and groups, see
[Assign permissions to users and groups](assign-permissions-procedure.md "assign-permissions-procedure.md").
