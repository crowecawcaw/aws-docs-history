# Example Amazon ECS task definition: Route logs to CloudWatch

Before your containers can send logs to CloudWatch, you must specify the `awslogs` log
driver for containers in your task definition. For more information about the log parameters, see [Storage and logging](task_definition_parameters.md#container_definition_storage "task_definition_parameters.md#container_definition_storage")

The task definition JSON that follows has a `logConfiguration` object
specified for each container. One is for the WordPress container that sends logs to a
log group called `awslogs-wordpress`. The other is for a MySQL container that
sends logs to a log group that's called `awslogs-mysql`. Both containers use
the `awslogs-example` log stream prefix.

```
{
    "containerDefinitions": [
        {
            "name": "wordpress",
            "links": [
                "mysql"
            ],
            "image": "public.ecr.aws/docker/library/wordpress:latest",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 80,
                    "hostPort": 80
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-create-group": "true",
                    "awslogs-group": "`awslogs-wordpress`",
                    "awslogs-region": "`us-west-2`",
                    "awslogs-stream-prefix": "`awslogs-example`"
                }
            },
            "memory": 500,
            "cpu": 10
        },
        {
            "environment": [
                {
                    "name": "MYSQL_ROOT_PASSWORD",
                    "value": "password"
                }
            ],
            "name": "mysql",
            "image": "public.ecr.aws/docker/library/mysql:latest",
            "cpu": 10,
            "memory": 500,
            "essential": true,
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-create-group": "true",
                    "awslogs-group": "`awslogs-mysql`",
                    "awslogs-region": "`us-west-2`",
                    "awslogs-stream-prefix": "`awslogs-example`",
                    "mode": "non-blocking",
                    "max-buffer-size": "25m"
                }
            }
        }
    ],
    "family": "awslogs-example"
}
```

## Next steps

- You can optionally set a retention policy for the log group by using the CloudWatch AWS CLI or API.
  For more information, see [put-retention-policy](../../../cli/latest/reference/logs/put-retention-policy.md "../../../cli/latest/reference/logs/put-retention-policy.md") in the _AWS Command Line Interface
  Reference_.
- After you have registered a task definition with the `awslogs` log driver
  in a container definition log configuration, you can run a task or create a service with
  that task definition to start sending logs to CloudWatch Logs. For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md") and [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md "create-service-console-v2.md").
