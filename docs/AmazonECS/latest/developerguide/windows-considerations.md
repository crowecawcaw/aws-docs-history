# Windows containers on Fargate considerations for Amazon ECS

The following are the differences and considerations to know when you run Windows containers on AWS Fargate.

If you need to run tasks on Linux and Windows containers, then you need to create separate task definitions for each operating system.

AWS handles the operating system license management, so you do not need any
additional Microsoft Windows Server licenses.

Windows containers on AWS Fargate supports the following operating systems:

- Windows Server 2019 Full
- Windows Server 2019 Core
- Windows Server 2022 Full
- Windows Server 2022 Core
  Windows containers on AWS Fargate supports the awslogs driver. For more information, see [Send Amazon ECS logs to CloudWatch](using_awslogs.md "using_awslogs.md").

The following features are not supported on Windows containers on Fargate:

- Amazon FSx
- ENI trunking
- gMSAs for Windows Containers
- App Mesh service and proxy integration for tasks
- Firelens log router integration for tasks
- EFS volumes
- EBS volumes
- The following task definition parameters:
  - `maxSwap`
  - `swappiness`
  - `environmentFiles`

- The Fargate Spot capacity provider
- Image volumes

The Dockerfile `volume` option is ignored. Instead, use bind mounts in your task definition. For more information, see [Use bind mounts with Amazon ECS](bind-mounts.md "bind-mounts.md").

- The task-level CPU and memory parameters are ignored for Windows containers.
  We recommend specifying container-level resources for Windows containers.
- memory for task
- mermoryReservation on containers
- Restart policies on containers
- You can't update the platformFamily of a service.
