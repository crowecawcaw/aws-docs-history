# Deregistering an Amazon ECS task definition revision

using the console

You can deregister the task definition revision so that it no longer displays in your
`ListTaskDefinition` API calls or in the console when you want to run a task
or update a service.

When you deregister a task definition revision, it is immediately marked as
`INACTIVE`. Existing tasks and services that reference an
`INACTIVE` task definition revision continue to run without disruption.
Existing services that reference an `INACTIVE` task definition revision can still
scale up or down by modifying the service's desired count.

You can't use an `INACTIVE` task definition revision to run new tasks or create
new services. You also can't update an existing service to reference an
`INACTIVE` task definition revision (even though there may be up to a
10-minute window following deregistration where these restrictions have not yet taken
effect).

###### Note

When you deregister all revisions in a task family, the task definition family is
moved to the `INACTIVE` list. Adding a new revision of an
`INACTIVE` task definition moves the task definition family back to the
`ACTIVE` list.

At this time, `INACTIVE` task definition revisions remain discoverable in
your account indefinitely. However, this behavior is subject to change in the future.
Therefore, you should not rely on `INACTIVE` task definition revisions
persisting beyond the lifecycle of any associated tasks and services.

## CloudFormation stacks

The following behavior applies to task definitions that were
created in the new Amazon ECS console before January 12, 2023.

When you create a task definition, the Amazon ECS console automatically creates a CloudFormation
stack that has a name that begins with `ECS-Console-V2-TaskDefinition-`. If you used the
AWS CLI or an AWS SDK to deregister the task definition, then you must manually delete the task
definition stack. For more information, see [Deleting a
stack](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the _CloudFormation User Guide_.

Task definitions created after January 12, 2023, do not have a CloudFormation stack
automatically created for them.

## Procedure

###### To deregister a new task definition (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, choose the region that contains your task
   definition.
3. In the navigation pane, choose **Task definitions**.
4. On the **Task definitions** page, choose the task definition
   family that contains one or more revisions that you want to deregister.
5. On the **task definition Name** page, select the revisions to
   delete, and then choose **Actions**,
   **Deregister**.
6. Verify the information in the **Deregister** window, and then
   choose **Deregister** to finish.
