# Specifying a container restart policy in an Amazon ECS task definition

To specify a restart policy for a container in a task definition, within the container
definition, specify the `restartPolicy` object. For more information about
the `restartPolicy` object, see [Restart policy](task_definition_parameters.md#container_definition_restart_policy "task_definition_parameters.md#container_definition_restart_policy").

The following is a task definition using the Linux containers on Fargate that sets up a web server. The container definition includes the
`restartPolicy` object, with `enabled` set to true to enable a
restart policy for the container. The container must run for 180 seconds before it can
be restarted and will not be restarted if it exits with the exit code `0`,
which indicates success.

```
{
  "containerDefinitions": [
    {
      "command": [
        "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
      ],
      "entryPoint": ["sh", "-c"],
      "essential": true,
      "image": "public.ecr.aws/docker/library/httpd:2.4",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/fargate-task-definition",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "name": "sample-fargate-app",
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp"
        }
      ],
      **"restartPolicy": {
 "enabled": true,
 "ignoredExitCodes": `[0]`,
 "restartAttemptPeriod": `180`
 }**
    }
  ],
  "cpu": "256",
  "executionRoleArn": "arn:aws:iam::`012345678910`:role/ecsTaskExecutionRole",
  "family": "fargate-task-definition",
  "memory": "512",
  "networkMode": "awsvpc",
  "runtimePlatform": {
    "operatingSystemFamily": "LINUX"
  },
  "requiresCompatibilities": ["FARGATE"]
}

```

After you have registered a task definition with the `restartPolicy` object
in a container definition, you can run a task or create a service with that task
definition. For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md") and [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md "create-service-console-v2.md").
