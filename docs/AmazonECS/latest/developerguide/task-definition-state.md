# Amazon ECS task definition states

A task definition changes states when you create, deregister, or delete it. You can
view the task definition state in the console, or by using
`DescribeTaskDefinition`.

The following are the possible states for a task definition:

ACTIVE

A task definition is `ACTIVE` after it is registered with Amazon ECS. You can use
task definitions in the `ACTIVE` state to run tasks, or create
services.

INACTIVE

A task definition transitions from the `ACTIVE` state to the
`INACTIVE` state when you deregister a task definition. You can
retrieve an `INACTIVE` task definition by calling
`DescribeTaskDefinition`. You cannot run new tasks or create new
services with a task definition in the `INACTIVE` state. There is no
impact on existing services or tasks.

DELETE_IN_PROGRESS

A task definition transitions from the `INACTIVE` state to the
`DELETE_IN_PROGRESS` state after you submitted the task
definition for deletion. After the task definition is in the
`DELETE_IN_PROGRESS` state, Amazon ECS periodically verifies that
the target task definition is not being referenced by any active tasks or
deployments, and then deletes the task definition permanently. You cannot
run new tasks or create new services with a task definition in the
`DELETE_IN_PROGRESS` state. A task definition can be
submitted for deletion at any moment without impacting existing tasks and
services.

Task definitions that are in the `DELETE_IN_PROGRESS` state can be viewed in
the console and you can retrieve the task definition by calling
`DescribeTaskDefinition`.

When you delete all `INACTIVE` task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revision is in the `DELETE_IN_PROGRESS` state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.

If you use AWS Config to manage your task definitions, AWS Config charges you for all task
definition registrations. You are only charged for deregistering the latest
`ACTIVE` task definition. There is no charge for deleting a task definition.
For more information about pricing, see [AWS Config Pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

## Amazon ECS resources that can block a deletion

A task definition deletion request will not complete when there are any Amazon ECS resources that depend on the task definition revision. The following resources might prevent a task definition from being deleted:

- Amazon ECS standalone tasks - The task definition is required in order for the task to remain
  healthy.
- Amazon ECS service tasks - The task definition is required in order for the task to remain
  healthy.
- Amazon ECS service deployments and task sets - The task definition is required when a
  scaling event is initiated for an Amazon ECS deployment or task set.

If your task definition remains in the `DELETE_IN_PROGRESS` state, you can
use the console, or the AWS CLI to identify, and then stop the resources which block the
task definition deletion.

### Task definition deletion after the blocked resource is removed

The following rules apply after you remove the resources that block the task
definition deletion:

- Amazon ECS tasks - The task definition deletion can take up to 1 hour to
  complete after the task is stopped.
- Amazon ECS service deployments and task sets - The task definition deletion can take up
  to 24 hours to complete after the deployment or task set is deleted.
