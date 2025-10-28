# Defer volume configuration to launch time in an

Amazon ECS task definition

To configure an Amazon EBS volume for attachment to your task, you must specify the mount
point configuration in your task definition and name the volume. You must also set
`configuredAtLaunch` to `true` because Amazon EBS volumes can't be
configured for attachment in the task definition. Instead, Amazon EBS volumes are configured
for attachment during deployment.

To register the task definition by using the AWS Command Line Interface (AWS CLI), save the template as a
JSON file, and then pass the file as an input for the `register-task-definition` command.

To create and register a task definition using the AWS Management Console, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").

The following task definition shows the syntax for the `mountPoints` and
`volumes` objects in the task definition. For more information about task
definition parameters, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md"). To use this example, replace the
`user input placeholders` with your own
information.

```
{
    "family": `"mytaskdef"`,
    "containerDefinitions": [
        {
            "name": "`nginx`",
            "image": "`public.ecr.aws/nginx/nginx:latest`",
            "networkMode": "awsvpc",
           "portMappings": [
                {
                    "name": "`nginx-80-tcp`",
                    "containerPort": 80,
                    "hostPort": 80,
                    "protocol": "tcp",
                    "appProtocol": "http"
                }
            ],
            "mountPoints": [
                {
                    "sourceVolume": "`myEBSVolume`",
                    "containerPath": "`/mount/ebs`",
                    "readOnly": `true`
                }
            ]
        }
    ],
    "volumes": [
        {
            "name": "`myEBSVolume`",
            "configuredAtLaunch": true
        }
    ],
    "requiresCompatibilities": [
        "FARGATE", "EC2"
    ],
    "cpu": "1024",
    "memory": "3072",
    "networkMode": "awsvpc"
}
```

```
{
    "family": `"mytaskdef"`,
     "memory": "4096",
     "cpu": "2048",
    "family": "windows-simple-iis-2019-core",
    "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
    "runtimePlatform": {"operatingSystemFamily": "WINDOWS_SERVER_2019_CORE"},
    "requiresCompatibilities": ["EC2"]
    "containerDefinitions": [
        {
             "command": ["New-Item -Path C:\\inetpub\\wwwroot\\index.html -Type file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>'; C:\\ServiceMonitor.exe w3svc"],
            "entryPoint": [
                "powershell",
                "-Command"
            ],
            "essential": true,
            "cpu": 2048,
            "memory": 4096,
            "image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
            "name": "sample_windows_app",
            "portMappings": [
                {
                    "hostPort": 443,
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "mountPoints": [
                {
                    "sourceVolume": "`myEBSVolume`",
                    "containerPath": "`drive:\ebs`",
                    "readOnly": `true`
                }
            ]
        }
    ],
    "volumes": [
        {
            "name": "`myEBSVolume`",
            "configuredAtLaunch": true
        }
    ],
    "requiresCompatibilities": [
        "FARGATE", "EC2"
    ],
    "cpu": "1024",
    "memory": "3072",
    "networkMode": "awsvpc"
}
```

`mountPoints`

Type: Object array

Required: No

The mount points for the data volumes in your container. This parameter maps to `Volumes` in the
create-container Docker API and
the `--volume` option to docker run.

Windows containers can mount whole directories on the same drive as
`$env:ProgramData`. Windows containers cannot mount
directories on a different drive, and mount points cannot be used across
drives. You must specify mount points to attach an Amazon EBS volume directly to an Amazon ECS task.

`sourceVolume`

Type: String

Required: Yes, when `mountPoints` are
used

The name of the volume to mount.

`containerPath`

Type: String

Required: Yes, when `mountPoints` are
used

The path in the container where the volume will be mounted.

`readOnly`

Type: Boolean

Required: No

If this value is `true`, the container has
read-only access to the volume. If this value is
`false`, then the container can write to the
volume. The default value is `false`.

For tasks that run on EC2 instances running the Windows operating system, leave the value as the default of `false`.

`name`

Type: String

Required: No

The name of the volume. Up to 255 letters (uppercase and lowercase),
numbers, hyphens (`-`), and underscores (`_`) are allowed. This name is referenced
in the `sourceVolume` parameter of the container definition
`mountPoints` object.

`configuredAtLaunch`

Type: Boolean

Required: Yes, when you want to use attach an EBS volume directly to a
task.

Specifies whether a volume is configurable at launch. When set to
`true`, you can configure the volume when you run a
standalone task, or when you create or update a service. When set to
`false`, you won't be able to provide another volume
configuration in the task definition. This parameter must be provided and
set to `true` to configure an Amazon EBS volume for attachment to a
task.
