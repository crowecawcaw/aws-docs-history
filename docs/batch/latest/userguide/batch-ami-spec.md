# Compute resource AMI specification

The basic AWS Batch compute resource AMI specification consists of the following:

Required

- A modern Linux distribution that's running at least version 3.10 of the Linux kernel on an
  HVM virtualization type AMI. Windows containers aren't supported.

###### Important

Multi-node parallel jobs can only run on compute resources that were launched on an Amazon Linux
instance with the `ecs-init` package installed. We recommend that you use the
default Amazon ECS optimized AMI when you create your compute environment. You can do this by not
specifying a custom AMI. For more information, see [Multi-node parallel jobs](multi-node-parallel-jobs.md "multi-node-parallel-jobs.md").

- The Amazon ECS container agent. We recommend that you use the latest version. For more
  information, see [Installing the Amazon ECS
  Container Agent](../../../AmazonECS/latest/developerguide/ecs-agent-install.md "../../../AmazonECS/latest/developerguide/ecs-agent-install.md") in the _Amazon Elastic Container Service Developer Guide_.
- The `awslogs` log driver must be specified as an available log driver with the
  `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable when the Amazon ECS container agent
  is started. For more information, see [Amazon ECS
  Container Agent Configuration](../../../AmazonECS/latest/developerguide/ecs-agent-config.md "../../../AmazonECS/latest/developerguide/ecs-agent-config.md") in the _Amazon Elastic Container Service Developer Guide_.
- A Docker daemon that's running at least version 1.9, and any Docker runtime dependencies.
  For more information, see [Check
  runtime dependencies](https://docs.docker.com/engine/installation/binaries/#check-runtime-dependencies "https://docs.docker.com/engine/installation/binaries/#check-runtime-dependencies") in the Docker documentation.

###### Note

We recommend the Docker version that ships with and is tested with the corresponding
Amazon ECS agent version that you're using. Amazon ECS provides a changelog for the Linux variant of the
Amazon ECS-optimized AMI on GitHub. For more information, see [Changelog](https://github.com/aws/amazon-ecs-ami/blob/main/CHANGELOG.md "https://github.com/aws/amazon-ecs-ami/blob/main/CHANGELOG.md").
Recommended

- An initialization and nanny process to run and monitor the Amazon ECS agent. The Amazon ECS
  optimized AMI uses the `ecs-init` upstart process, and other operating systems
  might use `systemd`. For more information and examples, see [Example container instance User Data
  Configuration Scripts](../../../AmazonECS/latest/developerguide/example_user_data_scripts.md "../../../AmazonECS/latest/developerguide/example_user_data_scripts.md") in the _Amazon Elastic Container Service Developer Guide_. For more
  information about `ecs-init`, see the [`ecs-init` project](https://github.com/aws/amazon-ecs-init "https://github.com/aws/amazon-ecs-init") on GitHub.
  At a minimum, managed compute environments require the Amazon ECS agent to start at boot. If the
  Amazon ECS agent isn't running on your compute resource, then it can't accept jobs from AWS Batch.
  The Amazon ECS optimized AMI is preconfigured with these requirements and recommendations. We
  recommend that you use the Amazon ECS optimized AMI or an Amazon Linux AMI with the `ecs-init`
  package that's installed for your compute resources. Choose another AMI if your application
  requires a specific operating system or a Docker version that's not yet available in those
  AMIs. For more information, see [Amazon ECS-Optimized AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md") in the _Amazon Elastic Container Service Developer Guide_.
