# Fargate security

considerations for Amazon ECS

Each task has a dedicated infrastructure capacity because Fargate runs each
workload on an isolated virtual environment. Workloads that run on Fargate do not
share network interfaces, ephemeral storage, CPU, or memory with other tasks. You
can run multiple containers within a task including application containers and
sidecar containers, or simply sidecars. A _sidecar_
is a container that runs alongside an application container in an Amazon ECS task. While
the application container runs core application code, processes running in sidecars
can augment the application. Sidecars help you segregate application functions into
dedicated containers, making it easier for you to update parts of your
application.

Containers that are part of the same task share resources for Fargate launch
type because these containers will always run on the same host and share compute
resources. These containers also share the ephemeral storage provided by Fargate.
Linux containers in a task share network namespaces, including the IP address and
network ports. Inside a task, containers that belong to the task can
inter-communicate over localhost.

The runtime environment in Fargate prevents you from using certain controller
features that are supported on EC2 instances. Consider the following when you
architect workloads that run on Fargate:

- No privileged containers or access - Features such as privileged
  containers or access are currently unavailable on Fargate. This will
  affect uses cases such as running Docker in Docker.
- Limited access to Linux capabilities - The environment in which
  containers run on Fargate is locked down. Additional Linux capabilities,
  such as CAP_SYS_ADMIN and CAP_NET_ADMIN, are restricted to prevent a
  privilege escalation. Fargate supports adding the [CAP_SYS_PTRACE](task_definition_parameters.md#other_task_definition_params "task_definition_parameters.md#other_task_definition_params") Linux capability to tasks to allow observability
  and security tools deployed within the task to monitor the containerized
  application.
- No access to the underlying host - Neither customers nor AWS operators
  can connect to a host running customer workloads. You can use ECS exec to
  run commands in or get a shell to a container running on Fargate. You can
  use ECS exec to help collect diagnostic information for debugging. Fargate
  also prevents containers from accessing the underlying host’s resources,
  such as the file system, devices, networking, and container runtime.
- Networking - You can use security groups and network ACLs to control
  inbound and outbound traffic. Fargate tasks receive an IP address from the
  configured subnet in your VPC.
