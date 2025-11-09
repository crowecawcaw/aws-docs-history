# Use strategies to define Amazon ECS task

placement

For tasks that use the EC2 launch type, Amazon ECS must
determine where to place the task based on the requirements specified in the task
definition, such as CPU and memory. Similarly, when you scale down the task count, Amazon ECS
must determine which tasks to terminate. You can apply task placement strategies and
constraints to customize how Amazon ECS places and terminates tasks.

The default task placement strategies depend on whether you run tasks manually (standalone tasks) or within a service. For tasks running as part of an Amazon ECS service, the task placement strategy is `spread` using the `attribute:ecs.availability-zone`. There isn't a default task placement constraint for tasks not in services. For more
information, see [Schedule your containers on Amazon ECS](scheduling_tasks.md "scheduling_tasks.md").

###### Note

Task placement strategies are a best effort. Amazon ECS still attempts to place tasks
even when the most optimal placement option is unavailable. However, task placement
constraints are binding, and they can prevent task placement.

You can use task placement strategies and constraints together. For example, you can
use a task placement strategy and a task placement constraint to distribute tasks across
Availability Zones and bin pack tasks based on memory within each Availability Zone, but
only for G2 instances.

When Amazon ECS places tasks, it uses the following process to select container
instances:

1. Identify the container instances that satisfy the CPU, GPU, memory, and port
   requirements in the task definition.
2. Identify the container instances that satisfy the task placement
   constraints.
3. Identify the container instances that satisfy the task placement
   strategies.
4. Select the container instances for task placement.
   You specify task placement strategies in the service definition, or task definition using
   the `placementStrategy` parameter.

```
"placementStrategy": [
    {
        "field": "The field to apply the placement strategy against",
        "type": "The placement strategy to use"
    }
]
```

You can specify the strategies when you run a task ([RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md")), create a new service ( [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md")), or update an existing
service ([UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md")).

The following table describes the available types and fields.

| type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Valid field values                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `binpack` Tasks are placed on container instances so as<br>to leave the least amount of unused CPU or memory. This strategy<br>minimizes the number of container instances in use.<br>When this strategy is used and a scale-in action is taken, Amazon ECS<br>terminates tasks. It does this based on the amount of resources that are<br>left on the container instance after the task is terminated. The<br>container instance that has the most available resources left after task<br>termination has that task terminated.                                  | • cpu<br>• memory                                                                                                                                                                      |
| `random` Tasks are placed randomly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Not used                                                                                                                                                                               |
| `spread`Tasks are placed evenly based on the specified<br>value. Service tasks are spread based on the tasks from that<br>service. Standalone tasks are spread based on the tasks from the same task<br>group. For more information about task groups, see [Group related Amazon ECS tasks](task-groups.md "task-groups.md") . When the<br>`spread` strategy is used and a scale-in action is taken,<br>Amazon ECS selects tasks to terminate that maintain a balance across<br>Availability Zones. Within an Availability Zone, tasks are selected at<br>random. | • `instanceId` (or `host`, which has the<br>same effect)<br>• any platform or custom attribute that's applied to a container<br>instance, such as<br>`attribute:ecs.availability-zone` |

The task placement strategies can be updated for existing services as well. For more
information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

You can create a task placement strategy that uses multiple strategies by creating arrays of strategies in the order that you want them performed. For example, if you want to spread tasks across Availability Zones and then bin pack tasks based on memory within each
Availability Zone, specify the Availability Zone strategy followed by the memory strategy. For example strategies, see [Example Amazon ECS task placement strategies](strategy-examples.md "strategy-examples.md").
