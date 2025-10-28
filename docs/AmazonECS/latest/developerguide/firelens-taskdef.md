# Example Amazon ECS task definition: Route logs to FireLens

To use custom log routing with FireLens, you must specify the following
in your task definition:

- A log router container that contains a FireLens configuration.
  We recommend that the container be marked as `essential`.
- One or more application containers that contain a log configuration specifying
  the `awsfirelens` log driver.
- A task IAM role Amazon Resource Name (ARN) that contains the permissions needed
  for the task to route the logs.
  When creating a new task definition using the AWS Management Console, there is a FireLens
  integration section that makes it easy to add a log router container. For more
  information, see [Creating an Amazon ECS task definition using the
  console](create-task-definition.md "create-task-definition.md").

Amazon ECS converts the log configuration and generates the Fluentd or Fluent Bit output
configuration. The output configuration is mounted in the log routing container at
`/fluent-bit/etc/fluent-bit.conf` for Fluent Bit and
`/fluentd/etc/fluent.conf` for Fluentd.

###### Important

FireLens listens on port `24224`. Therefore, to ensure
that the FireLens log router isn't reachable outside of the task, you must not allow
ingress traffic on port `24224` in the security group your task uses. For
tasks that use the `awsvpc` network mode, this is the security group
that's associated with the task. For tasks that use the `host` network
mode, this is the security group that's associated with the Amazon EC2 instance hosting
the task. For tasks that use the `bridge` network mode, don't create any
port mappings that use port `24224`.

By default, Amazon ECS adds additional fields in your log entries that help identify the source
of the logs.

- `ecs_cluster` – The name of the cluster that the task is part
  of.
- `ecs_task_arn` – The full Amazon Resource Name (ARN) of the task that the
  container is part of.
- `ecs_task_definition` – The task definition name and revision
  that the task is using.
- `ec2_instance_id` – The Amazon EC2 instance ID that the container is
  hosted on. This field is only valid for tasks using the EC2 launch
  type.
  You can set the `enable-ecs-log-metadata` to `false` if you do not
  want the metadata.

The following task definition example defines a log router container that uses Fluent
Bit to route its logs to CloudWatch Logs. It also defines an application container that uses a log
configuration to route logs to Amazon Data Firehose and sets the memory that's used to buffer
events to the 2 MiB.

###### Note

For more example task definitions, see [Amazon ECS FireLens
examples](https://github.com/aws-samples/amazon-ecs-firelens-examples "https://github.com/aws-samples/amazon-ecs-firelens-examples") on GitHub.

```
{
  "family": "firelens-example-firehose",
  "taskRoleArn": "arn:aws:iam::123456789012:role/ecs_task_iam_role",
  "containerDefinitions": [
    {
            "name": "log_router",
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
          "log-driver-buffer-limit": "1048576"
        }
      },
      "memoryReservation": 100
    }
  ]
}
```

The key-value pairs specified as options in the `logConfiguration` object
are used to generate the Fluentd or Fluent Bit output
configuration. The following is a code example from a Fluent Bit output
definition.

```
[OUTPUT]
    Name   firehose
    Match  app-firelens*
    region `us-west-2`
    delivery_stream `my-stream`
```

###### Note

FireLens manages the `match` configuration. You do not specify the `match`
configuration in your task definition.

## Use a custom configuration file

You can specify a custom configuration file. The configuration file format is the
native format for the log router that you're using. For more information, see [Fluentd Config File
Syntax](https://docs.fluentd.org/configuration/config-file "https://docs.fluentd.org/configuration/config-file") and [YAML Configuration](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/yaml "https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/yaml").

In your custom configuration file, for tasks using the `bridge` or
`awsvpc` network mode, don't set a Fluentd or Fluent Bit forward
input over TCP because FireLens adds it to the input
configuration.

Your FireLens configuration must contain the following options to
specify a custom configuration file:

`config-file-type`

The source location of the custom configuration file. The available
options are `s3` or `file`.

###### Note

Tasks that are hosted on AWS Fargate only support the
`file` configuration file type.

`config-file-value`

The source for the custom configuration file. If the `s3`
config file type is used, the config file value is the full ARN of the
Amazon S3 bucket and file. If the `file` config file type is used,
the config file value is the full path of the configuration file that
exists either in the container image or on a volume that's mounted in
the container.

###### Important

When using a custom configuration file, you must specify a
different path than the one FireLens uses. Amazon ECS
reserves the `/fluent-bit/etc/fluent-bit.conf` filepath
for Fluent Bit and `/fluentd/etc/fluent.conf` for
Fluentd.

The following example shows the syntax required when specifying a custom
configuration.

###### Important

To specify a custom configuration file that's hosted in Amazon S3, ensure you have
created a task execution IAM role with the proper permissions.

The following shows the syntax required when specifying a custom
configuration.

```
{
  "containerDefinitions": [
    {
      "essential": true,
      "image": "906394416424.dkr.ecr.`us-west-2`.amazonaws.com/aws-for-fluent-bit:stable",
      "name": "log_router",
      "firelensConfiguration": {
        "type": "fluentbit",
        "options": {
          "config-file-type": "`s3` | `file`",
          "config-file-value": "`arn:aws:s3:::`amzn-s3-demo-bucket`/fluent.conf` | `filepath`"
        }
      }
    }
  ]
}
```

###### Note

Tasks hosted on AWS Fargate only support the `file` configuration
file type.
