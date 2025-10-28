# Example Amazon ECS task placement constraints

The following are task placement constraint examples.

This example uses the `memberOf` constraint to place tasks on t2 instances.
It can be specified with the following actions: [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"), [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md"), [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md"),
and [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md").

```
"placementConstraints": [
    {
        "expression": "attribute:ecs.instance-type =~ t2.*",
        "type": "memberOf"
    }
]
```

The example uses the `memberOf` constraint to place replica tasks on
instances with tasks in the daemon service `daemon-service` task group,
respecting any task placement strategies that are also specified. This constraint
ensures that the daemon service tasks get placed on the EC2 instance prior to the
replica service tasks.

Replace `daemon-service` with the name of the daemon service.

```
"placementConstraints": [
    {
        "expression": "task:group == service:`daemon-service`",
        "type": "memberOf"
    }
]
```

The example uses the `memberOf` constraint to place tasks on instances with
other tasks in the `databases` task group, respecting any task placement
strategies that are also specified. For more information about task groups, see [Group related Amazon ECS tasks](task-groups.md "task-groups.md") . It can be specified with the
following actions: [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"), [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md"), [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md"), and [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md").

```
"placementConstraints": [
    {
        "expression": "task:group == databases",
        "type": "memberOf"
    }
]
```

The `distinctInstance` constraint places each task in the group on a
different instance. It can be specified with the following actions: [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"), [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md"), and [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md")

Amazon ECS looks at the desired status of the tasks for the task placement. For example, if the desired status of the existing task is `STOPPED`, (but the last status isn’t), a new incoming task can be placed on the same instance despite the `distinctInstance` placement constraint. Therefore, you might see 2 tasks with last status of `RUNNING` on the same instance.

```
"placementConstraints": [
    {
        "type": "distinctInstance"
    }
]
```
