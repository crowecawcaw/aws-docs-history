# Configuring Amazon ECS logs for high

throughput

When you create a task definition, you can specify the number of log lines that are
buffered in memory by specifying the value in the `log-driver-buffer-limit`.
For more information, see [Fluentd logging
driver](https://docs.docker.com/engine/logging/drivers/fluentd/ "https://docs.docker.com/engine/logging/drivers/fluentd/") in the Docker documentation.

Use this option when there's high throughput, because Docker might run out of buffer
memory and discard buffer messages, so it can add new messages.

Consider the following when using FireLens for Amazon ECS with the buffer limit
option:

- This option is supported on EC2 and Fargate
  type with platform version `1.4.0` or later.
- The option is only valid when `logDriver` is set to
  `awsfirelens`.
- The default buffer limit is `1048576` log lines.
- The buffer limit must be greater than or equal to `0` and less than
  `536870912` log lines.
- The maximum amount of memory used for this buffer is the product of the size
  of each log line and the size of the buffer. For example, if the application’s
  log lines are on average `2` KiB, a buffer limit of 4096 would use at
  most `8` MiB. The total amount of memory allocated at the task level
  should be greater than the amount of memory that's allocated for all the
  containers in addition to the log driver memory buffer.
  When the `awsfirelens` log driver is specified in a task definition, the
  Amazon ECS container agent injects the following environment variables into the
  container:

`FLUENT_HOST`

The IP address that's assigned to the FireLens container.

###### Note

If you're using EC2 with the
`bridge` network mode, the `FLUENT_HOST`
environment variable in your application container can become inaccurate
after a restart of the FireLens log router container (the container with
the `firelensConfiguration` object in its container
definition). This is because `FLUENT_HOST` is a dynamic IP
address and can change after a restart. Logging directly from the
application container to the `FLUENT_HOST` IP address can
start failing after the address changes. For more information about
restarting individual containers, see [Restart individual containers in Amazon ECS tasks with
container restart policies](container-restart-policy.md "container-restart-policy.md").

`FLUENT_PORT`

The port that the Fluent Forward protocol is listening on.

You can use the `FLUENT_HOST` and `FLUENT_PORT` environment
variables to log directly to the log router from code instead of going through
`stdout`. For more information, see [fluent-logger-golang](https://github.com/fluent/fluent-logger-golang "https://github.com/fluent/fluent-logger-golang") on
GitHub.

The following shows the syntax for specifying the
`log-driver-buffer-limit`. Replace `my_service_` with the name of
your service:

```
{
    "containerDefinitions": [
        {
            "name": "`my_service_`log_router",
            "image": "public.ecr.aws/aws-observability/aws-for-fluent-bit:stable",
            "cpu": 0,
            "memoryReservation": 51,
            "portMappings": [],
            "essential": true,
            "environment": [],
            "mountPoints": [],
            "volumesFrom": [],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/ecs-aws-firelens-sidecar-container",
                    "mode": "non-blocking",
                    "awslogs-create-group": "true",
                    "max-buffer-size": "25m",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "firelens"
                },
                "secretOptions": []
            },
            "systemControls": [],
            "firelensConfiguration": {
                "type": "fluentbit"
            }
        },
        {
            "essential": true,
            "image": "public.ecr.aws/docker/library/httpd:latest",
            "name": "app",
            "logConfiguration": {
                "logDriver": "awsfirelens",
                "options": {
                    "Name": "firehose",
                    "region": "us-west-2",
                    "delivery_stream": "my-stream",
                    "log-driver-buffer-limit": "51200"
                }
            },
            "dependsOn": [
                {
                    "containerName": "log_router",
                    "condition": "START"
                }
            ],
            "memoryReservation": 100
        }
    ]
}
```
