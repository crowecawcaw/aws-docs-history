# Viewing Amazon ECS stopped task errors

If you have trouble starting a task, your task might be stopping because of application or
configuration errors. For example, you run the task and the task displays a
`PENDING` status and then disappears.

If your task was created by an Amazon ECS service, the actions that Amazon ECS takes to maintain
the service are published in the service events. You can view the events in the AWS Management Console,
AWS CLI, AWS SDKs, the Amazon ECS API, or tools that use the SDKs and API. These events include
Amazon ECS stopping and replaces a task because the containers in the task have stopped running,
or have failed too many health checks from Elastic Load Balancing.

If your task ran on a container instance on Amazon EC2 or external computers, you can also
look at the logs of the container runtime and the Amazon ECS Agent. These logs are on the host
Amazon EC2 instance or external computer. For more information, see [Viewing Amazon ECS container agent logs](logs.md "logs.md").

## Procedure

Console

###### AWS Management Console

The following steps can be used to check stopped tasks for errors using
the console. In order to see stopped tasks, you must change the filter
option.

Stopped tasks only appear in the console for 1 hour.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose
   **Clusters**.
3. On the **Clusters** page, choose the
   cluster.
4. On the **Cluster :
   `name`** page, choose the
   **Tasks** tab.
5. Configure the filter to display stopped tasks. For **Filter
   desired status**, choose
   **Stopped**.

The **Stopped** option displays your stopped tasks
and **Any desired status** displays all of your
tasks. 6. Choose the stopped task to inspect. 7. In the row for your stopped task, in the **Last
Status** column, choose
**Stopped**.

A pop-up window displays the stopped reason.

AWS CLI

1. List the stopped tasks in a cluster. The output contains the Amazon Resource Name (ARN)
   of the task, which you need to describe the task.

```
`aws ecs list-tasks \
 --cluster `cluster_name` \
 --desired-status STOPPED \
 --region `region``
```

2. Describe the stopped task to retrieve the information. For more
   information, see [describe-tasks](../../../cli/latest/reference/ecs/describe-tasks.md "../../../cli/latest/reference/ecs/describe-tasks.md") in the _AWS Command Line Interface
   Reference_.

```
`aws ecs describe-tasks \
 --cluster cluster_name \
 --tasks arn:aws:ecs:`region`:`account_id`:task/`cluster_name`/`task_ID` \
 --region `region``
```

Use the following output parameters.

- `stopCode` - The stop code indicates why a task was
  stopped, for example ResourceInitializationError
- `StoppedReason` - The reason the task stopped.
- `reason` (in the `containers` structure) -
  The reason provide additional details about the stopped
  container.

## Next steps

View your stopped tasks so you can get information about the cause. For more
information, see [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md "stopped-task-error-codes.md").
