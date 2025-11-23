# Amazon ECS Linux container instance management

When you use EC2 instances for your Amazon ECS workloads, you are responsible for maintaining the instances

###### Management procedures

- [Launching a container instance](launch_container_instance.md "launch_container_instance.md")
- [Bootstrapping Linux container instances](bootstrap_container_instance.md "bootstrap_container_instance.md")
- [Configuring container instances to receive Spot Instance notices](spot-instance-draining-linux-container.md "spot-instance-draining-linux-container.md")
- [Running a script when you launch a container instance](start_task_at_launch.md "start_task_at_launch.md")
- [Increasing Amazon ECS Linux container instance network
  interfaces](container-instance-eni.md "container-instance-eni.md")
- [Reserving container instance memory](memory-management.md "memory-management.md")
- [Manage container instances remotely](ec2-run-command.md "ec2-run-command.md")
- [Using an HTTP proxy for Linux container instances](http_proxy_config.md "http_proxy_config.md")
- [Configuring pre-initialized instances for your Amazon EC2 Auto Scaling
  group](using-warm-pool.md "using-warm-pool.md")
- [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md")
  Each Amazon ECS container agent version supports a different feature set and provides bug
  fixes from previous versions. When possible, we always recommend using the latest version
  of the Amazon ECS container agent. To update your container agent to the latest version, see
  [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

To see which features and enhancements are included with each agent release, see [https://github.com/aws/amazon-ecs-agent/releases](https://github.com/aws/amazon-ecs-agent/releases "https://github.com/aws/amazon-ecs-agent/releases").

###### Important

The minimum Docker version for reliable metrics is Docker version `v20.10.13` and
newer, which is included in Amazon ECS-optimized AMI `20220607` and newer.

Amazon ECS agent versions `1.20.0` and newer have deprecated support for
Docker versions older than `18.01.0`.
