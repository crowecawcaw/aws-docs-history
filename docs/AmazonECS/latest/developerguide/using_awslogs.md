# Send Amazon ECS logs to CloudWatch

You can configure the containers in your tasks to send log information to CloudWatch Logs. If
you're using Fargate for your tasks, you can view the logs
from your containers. If you're using EC2, you can view
different logs from your containers in one convenient location, and it prevents your
container logs from taking up disk space on your container instances.

###### Note

The type of information that is logged by the containers in your task depends mostly
on their `ENTRYPOINT` command. By default, the logs that are captured show
the command output that you typically might see in an interactive terminal if you ran
the container locally, which are the `STDOUT` and `STDERR` I/O
streams. The `awslogs` log driver simply passes these logs from Docker to
CloudWatch Logs. For more information about how Docker logs are processed, including alternative
ways to capture different file data or streams, see [View logs for a container
or service](https://docs.docker.com/engine/logging/ "https://docs.docker.com/engine/logging/") in the Docker documentation.

To send system logs from your Amazon ECS container instances to CloudWatch Logs, see [Monitoring Log Files](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md") and [CloudWatch Logs
quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md") in the _Amazon CloudWatch Logs User Guide_.

## Fargate

If you're using Fargate for your tasks, you need to add
the required `logConfiguration` parameters to your task definition to turn on
the `awslogs` log driver. For more information, see [Example Amazon ECS task definition: Route logs to CloudWatch](specify-log-config.md "specify-log-config.md").

For Windows container on Fargate, perform one of the following options when any of your
task definition parameters have special characters such as, `& \ < > ^
 |`:

- Add an escape (`\`) with double quotes around the entire parameter
  string

Example

```
"awslogs-multiline-pattern": "\"^[|DEBUG|INFO|WARNING|ERROR\"",
```

- Add an escape (`^`) character around each special
  character

Example

```
"awslogs-multiline-pattern": "^^[^|DEBUG^|INFO^|WARNING^|ERROR",
```

## EC2

If you're using EC2 for your tasks and want to turn on
the `awslogs` log driver, your Amazon ECS container instances require at least
version 1.9.0 of the container agent. For information about how to check your agent
version and updating to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

###### Note

You must use either an Amazon ECS-optimized AMI or a custom AMI with at least
version `1.9.0-1` of the `ecs-init` package. When using a
custom AMI, you must specify that the `awslogs` logging driver is
available on the Amazon EC2 instance when you start the agent by using the following
environment variable in your **docker run** statement or environment
variable file.

```
ECS_AVAILABLE_LOGGING_DRIVERS=["json-file","`awslogs`"]
```

Your Amazon ECS container instances also require `logs:CreateLogStream` and
`logs:PutLogEvents` permission on the IAM role that you can launch your
container instances with. If you created your Amazon ECS container instance role before
`awslogs` log driver support was enabled in Amazon ECS, you might need to add
this permission. The `ecsTaskExecutionRole` is used when it's assigned to the
task and likely contains the correct permissions. For information about the task
execution role, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md"). If your container instances use the
managed IAM policy for container instances, your container instances likely have the
correct permissions. For information about the managed IAM policy for container
instances, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
