# Collecting container logs with Amazon ECS logs collector

###### Note

You can't use the Amazon ECS logs collector on Amazon ECS Managed Instances.

If you are unsure how to collect all of the various logs on your container instances,
you can use the Amazon ECS logs collector. It is available on GitHub for both [Linux](https://github.com/awslabs/ecs-logs-collector "https://github.com/awslabs/ecs-logs-collector") and [Windows](https://github.com/awslabs/aws-ecs-logs-collector-for-windows "https://github.com/awslabs/aws-ecs-logs-collector-for-windows").
The script collects general operating system logs as well as Docker and Amazon ECS container
agent logs, which can be helpful for troubleshooting AWS Support cases. It then compresses
and archives the collected information into a single file that can easily be shared for
diagnostic purposes. It also supports enabling debug mode for the Docker daemon and the
Amazon ECS container agent on Amazon Linux variants, such as the Amazon ECS-optimized AMI.

###### Note

On Amazon Linux Amazon ECS-optimized AMIs version 20250909 and later, the Amazon ECS logs collector is pre-installed at `/opt/amazon/ecs/ecs-logs-collector.sh` and ready to use without downloading from GitHub. For more information, see [ECS Logs Collector](https://github.com/aws/amazon-ecs-ami?tab=readme-ov-file#ecs-logs-collector "https://github.com/aws/amazon-ecs-ami?tab=readme-ov-file#ecs-logs-collector") in the ECS-optimized AMI documentation.

Currently, the Amazon ECS logs collector supports the following operating systems:

- Amazon Linux
- Red Hat Enterprise Linux
- Ubuntu
- Windows Server

###### To run the Amazon ECS logs collector for Linux (ECS-optimized AMI)

1. Connect to your container instance.
2. Run the script to collect the logs and create the archive.

###### Note

To enable the debug mode for the Docker daemon and the Amazon ECS container
agent, add the `--mode=enable-debug` option to the following
command. This might restart the Docker daemon, which kills all containers
that are running on the instance. Consider draining the container instance
and moving any important tasks to other container instances before enabling
debug mode. For more information, see [Draining Amazon ECS container instances](container-instance-draining.md "container-instance-draining.md").

```
`[ec2-user ~]$` `sudo /opt/amazon/ecs/ecs-logs-collector.sh`
```

After you have run the script, you can examine the collected logs in the
`collect` folder that the script created. The
`collect.tgz` file is a compressed archive of all of the logs,
which you can share with AWS Support for diagnostic help.

###### To download and run the Amazon ECS logs collector for Linux

1. Connect to your container instance.
2. Download the Amazon ECS logs collector script.

```
`curl -O https://raw.githubusercontent.com/awslabs/ecs-logs-collector/master/ecs-logs-collector.sh`
```

3. Run the script to collect the logs and create the archive.

```
`$` `sudo bash ./ecs-logs-collector.sh`
```

###### To download and run the Amazon ECS logs collector for Windows

1. Connect to your container instance. For more information, see [Connect to your Windows instance using RDP](../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/UserGuide/connecting_to_windows_instance.md") in the
   _Amazon EC2 User Guide_.
2. Download the Amazon ECS logs collector script using PowerShell.

```
`Invoke-WebRequest -OutFile ecs-logs-collector.ps1 https://raw.githubusercontent.com/awslabs/aws-ecs-logs-collector-for-windows/master/ecs-logs-collector.ps1`
```

3. Run the script to collect the logs and create the archive.

###### Note

To enable the debug mode for the Docker daemon and the Amazon ECS container
agent, add the `-RunMode debug` option to the following command.
This restarts the Docker daemon, which kills all containers that are running
on the instance. Consider draining the container instance and moving any
important tasks to other container instances before enabling debug mode. For
more information, see [Draining Amazon ECS container instances](container-instance-draining.md "container-instance-draining.md").

```
`.\ecs-logs-collector.ps1`
```

After you have run the script, you can examine the collected logs in the
`collect` folder that the script created. The
`collect.tgz` file is a compressed archive of all of the logs,
which you can share with AWS Support for diagnostic help.
