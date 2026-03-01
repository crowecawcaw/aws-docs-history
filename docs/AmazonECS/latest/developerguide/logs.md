# Viewing Amazon ECS container agent logs

Amazon ECS stores logs in the `/var/log/ecs` folder of your container
instances. There are logs available from the Amazon ECS container agent and from the
`ecs-init` service that controls the state of the agent (start/stop) on the
container instance. You can view these log files by connecting to a container instance using
SSH.

###### Note

If you are not sure how to collect all of the logs on your container instances, you
can use the Amazon ECS logs collector. For more information, see [Collecting container logs with Amazon ECS logs collector](ecs-logs-collector.md "ecs-logs-collector.md").

The `ecs-init` process stores logs at
`/var/log/ecs/ecs-init.log`.

The `ecs-init.log` file contains information about the container agent lifecycle
management, configuration, and bootstrapping.

You can use the following command to view the log files.

```
`cat /var/log/ecs/ecs-init.log`
```

Output:

```
2018-02-16T18:13:54Z [INFO] pre-start
2018-02-16T18:13:56Z [INFO] start
2018-02-16T18:13:56Z [INFO] No existing agent container to remove.
2018-02-16T18:13:56Z [INFO] Starting Amazon Elastic Container Service Agent
```

You can use the Amazon ECS logs collector for Windows. For more information, see [Amazon ECS Logs Collector For Windows](https://github.com/awslabs/aws-ecs-logs-collector-for-windows?tab=readme-ov-file#aws-ecs-logs-collector-for-windows "https://github.com/awslabs/aws-ecs-logs-collector-for-windows?tab=readme-ov-file#aws-ecs-logs-collector-for-windows") on Github.

1. Connect to your instance.
2. Open PowerShell and then run the following commands with administrative
   privileges. The commands download the script and collects the logs.

```
Invoke-WebRequest -OutFile ecs-logs-collector.ps1 https://raw.githubusercontent.com/awslabs/aws-ecs-logs-collector-for-windows/master/ecs-logs-collector.ps1
.\ecs-logs-collector.ps1
```

You can turn on debug logging for Amazon ECS agent and the Docker daemon. This option
allows the script to collect the logs before turning on debug mode. The script
restarts the Docker daemon and Amazon ECS agent, and then terminates all containers
running on the instance. Before running the following command, drain the container
instance and moving any important tasks to other container instances.

Run the following command to turn on logging.

```
.\ecs-logs-collector.ps1 -RunMode debug
```
