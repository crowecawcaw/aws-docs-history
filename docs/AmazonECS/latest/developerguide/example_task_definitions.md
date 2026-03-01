# Example Amazon ECS task definitions

You can copy the examples and snippets to
start creating your own task definitions.

You can copy the examples, and then paste them when you use the **Configure via
JSON** option in the console. Make sure to customize the examples, such as
using your account ID. You can include the snippets in your task definition JSON. For more
information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md") and [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md").

For more task definition examples, see [AWS Sample Task
Definitions](https://github.com/aws-samples/aws-containers-task-definitions "https://github.com/aws-samples/aws-containers-task-definitions") on GitHub.

###### Topics

- [Webserver](#example_task_definition-webserver "#example_task_definition-webserver")
- [splunk log driver](#example_task_definition-splunk "#example_task_definition-splunk")
- [fluentd log driver](#example_task_definition-fluentd "#example_task_definition-fluentd")
- [gelf log driver](#example_task_definition-gelf "#example_task_definition-gelf")
- [Workloads on external instances](#ecs-anywhere-runtask "#ecs-anywhere-runtask")
- [Amazon ECR image and task definition IAM role](#example_task_definition-iam "#example_task_definition-iam")
- [Entrypoint with command](#example_task_definition-ping "#example_task_definition-ping")
- [Container dependency](#example_task_definition-containerdependency "#example_task_definition-containerdependency")
- [Volumes in task definitions](#volume_sample_task_defs "#volume_sample_task_defs")
- [Windows sample task definitions](#windows_sample_task_defs "#windows_sample_task_defs")

## Webserver

The following is an example task definition using the Linux containers on
Fargate that sets up a web server:

```
{
   "containerDefinitions": [
      {
         "command": [
            "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
         ],
         "entryPoint": [
            "sh",
            "-c"
         ],
         "essential": true,
         "image": "public.ecr.aws/docker/library/httpd:2.4",
         "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
               "awslogs-group" : "/ecs/fargate-task-definition",
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
         ]
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
   "requiresCompatibilities": [
       "FARGATE"
    ]
}
```

The following is an example task definition using the Windows containers on
Fargate that sets up a web server:

```
{
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
                    "hostPort": 80,
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ]
        }
    ],
    "memory": "4096",
    "cpu": "2048",
    "networkMode": "awsvpc",
    "family": "windows-simple-iis-2019-core",
    "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
    "runtimePlatform": {"operatingSystemFamily": "WINDOWS_SERVER_2019_CORE"},
    "requiresCompatibilities": ["FARGATE"]
}
```

## `splunk` log driver

The following snippet demonstrates how to use the `splunk` log driver in a
task definition that sends the logs to a remote service. The Splunk token parameter is
specified as a secret option because it can be treated as sensitive data. For more
information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").

```
"containerDefinitions": [{
		"logConfiguration": {
			"logDriver": "splunk",
			"options": {
				"splunk-url": "`https://cloud.splunk.com:8080`",
				"tag": "`tag_name`",
			},
			"secretOptions": [{
				"name": "splunk-token",
				"valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`splunk-token-KnrBkD`"
}],
```

## `fluentd` log driver

The following snippet demonstrates how to use the `fluentd` log driver in a
task definition that sends the logs to a remote service. The
`fluentd-address` value is specified as a secret option as it may be
treated as sensitive data. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").

```
"containerDefinitions": [{
	"logConfiguration": {
		"logDriver": "fluentd",
		"options": {
			"tag": "`fluentd demo`"
		},
		"secretOptions": [{
			"name": "fluentd-address",
			"valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`fluentd-address-KnrBkD`"
		}]
	},
	"entryPoint": [],
	"portMappings": [{
             "hostPort": 80,
             "protocol": "tcp",
             "containerPort": 80
             },
             {
		"hostPort": 24224,
		"protocol": "tcp",
		"containerPort": 24224
	}]
}],
```

## `gelf` log driver

The following snippet demonstrates how to use the `gelf` log driver in a
task definition that sends the logs to a remote host running Logstash that takes Gelf
logs as an input. For more information, see [logConfiguration](task_definition_parameters.md#ContainerDefinition-logConfiguration "task_definition_parameters.md#ContainerDefinition-logConfiguration").

```
"containerDefinitions": [{
	"logConfiguration": {
		"logDriver": "gelf",
		"options": {
			"gelf-address": "`udp://logstash-service-address:5000`",
			"tag": "`gelf task demo`"
		}
	},
	"entryPoint": [],
	"portMappings": [{
			"hostPort": 5000,
			"protocol": "udp",
			"containerPort": 5000
		},
		{
			"hostPort": 5000,
			"protocol": "tcp",
			"containerPort": 5000
		}
	]
}],
```

## Workloads on external instances

When registering an Amazon ECS task definition, use the
`requiresCompatibilities` parameter and specify `EXTERNAL`
which validates that the task definition is compatible to use when running Amazon ECS
workloads on your external instances. If you use the console for registering a task
definition, you must use the JSON editor. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

###### Important

If your tasks require a task execution IAM role, make sure that it's specified
in the task definition.

When you deploy your workload, use the `EXTERNAL` launch type when creating
your service or running your standalone task.

The following is an example task definition.

Linux

```
{
	"requiresCompatibilities": [
		"EXTERNAL"
	],
	"containerDefinitions": [{
		"name": "nginx",
		"image": "public.ecr.aws/nginx/nginx:latest",
		"memory": 256,
		"cpu": 256,
		"essential": true,
		"portMappings": [{
			"containerPort": 80,
			"hostPort": 8080,
			"protocol": "tcp"
		}]
	}],
	"networkMode": "bridge",
	"family": "nginx"
}
```

Windows

```
{
	"requiresCompatibilities": [
		"EXTERNAL"
	],
	"containerDefinitions": [{
		"name": "windows-container",
		"image": "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019",
		"memory": 256,
		"cpu": 512,
		"essential": true,
		"portMappings": [{
			"containerPort": 80,
			"hostPort": 8080,
			"protocol": "tcp"
		}]
	}],
	"networkMode": "bridge",
	"family": "windows-container"
}
```

## Amazon ECR image and task definition IAM role

The following snippet uses an Amazon ECR image called `aws-nodejs-sample` with
the `v1` tag from the
`123456789012.dkr.ecr.us-west-2.amazonaws.com` registry. The container in
this task inherits IAM permissions from the
`arn:aws:iam::123456789012:role/AmazonECSTaskS3BucketRole` role. For more
information, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

```
{
    "containerDefinitions": [
        {
            "name": "sample-app",
            "image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/aws-nodejs-sample:v1",
            "memory": 200,
            "cpu": 10,
            "essential": true
        }
    ],
    "family": "example_task_3",
    "taskRoleArn": "arn:aws:iam::123456789012:role/AmazonECSTaskS3BucketRole"
}
```

## Entrypoint with command

The following snippet demonstrates the syntax for a Docker container that uses an
entry point and a command argument. This container pings `example.com` four
times and then exits.

```
{
    "containerDefinitions": [
        {
            "memory": 32,
            "essential": true,
            "entryPoint": ["ping"],
            "name": "alpine_ping",
            "readonlyRootFilesystem": true,
            "image": "alpine:3.4",
            "command": [
                "-c",
                "4",
                "example.com"
            ],
            "cpu": 16
        }
    ],
    "family": "example_task_2"
}
```

## Container dependency

This snippet demonstrates the syntax for a task definition with multiple containers
where container dependency is specified. In the following task definition, the
`envoy` container must reach a healthy status, determined by the required
container health check parameters, before the `app` container will start. For
more information, see [Container dependency](task_definition_parameters.md#container_definition_dependson "task_definition_parameters.md#container_definition_dependson").

```
{
  "family": "`appmesh-gateway`",
  "runtimePlatform": {
        "operatingSystemFamily": "LINUX"
  },
  "proxyConfiguration":{
      "type": "APPMESH",
      "containerName": "envoy",
      "properties": [
          {
              "name": "IgnoredUID",
              "value": "1337"
          },
          {
              "name": "ProxyIngressPort",
              "value": "15000"
          },
          {
              "name": "ProxyEgressPort",
              "value": "15001"
          },
          {
              "name": "AppPorts",
              "value": "`9080`"
          },
          {
              "name": "EgressIgnoredIPs",
              "value": "169.254.170.2,169.254.169.254"
          }
      ]
  },
  "containerDefinitions": [
    {
      "name": "app",
      "image": "`application_image`",
      "portMappings": [
        {
          "containerPort": `9080`,
          "hostPort": `9080`,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "dependsOn": [
        {
          "containerName": "envoy",
          "condition": "HEALTHY"
        }
      ]
    },
    {
      "name": "envoy",
      "image": "840364872350.dkr.ecr.`region-code`.amazonaws.com/aws-appmesh-envoy:v1.15.1.0-prod",
      "essential": true,
      "environment": [
        {
          "name": "APPMESH_VIRTUAL_NODE_NAME",
          "value": "mesh/`meshName`/virtualNode/`virtualNodeName`"
        },
        {
          "name": "ENVOY_LOG_LEVEL",
          "value": "info"
        }
      ],
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "echo hello"
        ],
        "interval": 5,
        "timeout": 2,
        "retries": 3
      }
    }
  ],
  "executionRoleArn": "arn:aws:iam::`123456789012`:role/`ecsTaskExecutionRole`",
  "networkMode": "awsvpc"
}
```

## Volumes in task definitions

Use the following to understand how to specify volumes in tasks.

- For information about how to configure an Amazon EBS volume, see [Specify Amazon EBS volume configuration at Amazon ECS deployment](configure-ebs-volume.md "configure-ebs-volume.md").
- For information about how to configure an Amazon EFS volume, see [Configuring Amazon EFS file systems for Amazon ECS using the console](tutorial-efs-volumes.md "tutorial-efs-volumes.md").
- For information about how to configure a FSx for Windows File Server volume, see [Learn how to configure FSx for Windows File Server file systems for Amazon ECS](tutorial-wfsx-volumes.md "tutorial-wfsx-volumes.md").
- For information about how to configure a Docker volume, see [Docker volume examples for Amazon ECS](docker-volume-examples.md "docker-volume-examples.md").
- For information about how to configure a bind mount, see [Bind mount examples for Amazon ECS](bind-mount-examples.md "bind-mount-examples.md").

## Windows sample task definitions

The following is a sample task definition to help you get started with Windows
containers on Amazon ECS.

###### Example Amazon ECS Console Sample Application for Windows

The following task definition is the Amazon ECS console sample application that is
produced in the first-run wizard for Amazon ECS; it has been ported to use the
`microsoft/iis` Windows container image.

```
{
  "family": "windows-simple-iis",
  "containerDefinitions": [
    {
      "name": "windows_sample_app",
      "image": "mcr.microsoft.com/windows/servercore/iis",
      "cpu": 1024,
      "entryPoint":["powershell", "-Command"],
      "command":["New-Item -Path C:\\inetpub\\wwwroot\\index.html -Type file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>'; C:\\ServiceMonitor.exe w3svc"],
      "portMappings": [
        {
          "protocol": "tcp",
          "containerPort": 80
        }
      ],
      "memory": 1024,
      "essential": true
    }
  ],
  "networkMode": "awsvpc",
  "memory": "1024",
  "cpu": "1024"
}
```
