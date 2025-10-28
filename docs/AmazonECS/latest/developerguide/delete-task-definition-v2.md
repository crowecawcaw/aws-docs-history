# Deleting an Amazon ECS task definition revision using the

console

When no longer need a specific task definition revision in Amazon ECS, you
can delete the task definition revision.

When you delete a task definition revision, it immediately transitions from the
`INACTIVE` to `DELETE_IN_PROGRESS`. Existing tasks and services
that reference a `DELETE_IN_PROGRESS` task definition revision continue to run
without disruption.

You can't use a `DELETE_IN_PROGRESS` task definition revision to run new tasks
or create new services. You also can't update an existing service to reference a
`DELETE_IN_PROGRESS` task definition revision.

When you delete all `INACTIVE` task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revision is in the `DELETE_IN_PROGRESS` state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.

## Amazon ECS resources that can block a

deletion

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

## Procedure

###### To delete task definitions (Amazon ECS console)

You must deregister a task definition revision before you delete it. For more
information, see [Deregistering an Amazon ECS task definition revision
using the console](deregister-task-definition-v2.md "deregister-task-definition-v2.md").

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, choose the region that contains your task
   definition.
3. In the navigation pane, choose **Task definitions**.
4. On the **Task definitions** page, choose the task definition
   family that contains one or more revisions that you want to delete.
5. On the **Task definition name** page, select the revisions to
   delete, and then choose **Actions**,
   **Delete**.

If **Delete** is unavailable, you must deregister the task
definition. 6. Verify the information in the **Delete** confirmation box, and
then choose **Delete** to finish.
