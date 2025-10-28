# Monitor workloads using Amazon ECS metadata

You can use the task and container metadata to troubleshoot your workloads and to make
configuration changes based on the runtime environment.

Metadata includes the following categories:

- Task-level attributes that provide information about where the task is running.
- Container-level attributes that provide the Docker ID, name, and image details.

This provides visibility into the container.

- Network settings such as IP addresses, subnets, and network mode.

This helps with network configuration and troubleshooting.

- Task status and health

This lets you know if the tasks are running.
You can view metadata by any of the following methods:

- Container metadata file

Beginning with version 1.15.0 of the Amazon ECS container agent, various container
metadata is available within your containers or the host container instance. By
enabling this feature, you can query the information about a task, container, and
container instance from within the container or the host container instance. The
metadata file is created on the host instance and mounted in the container as a
Docker volume and therefore is not available when a task is hosted on
AWS Fargate.

- Task metadata endpoint

The Amazon ECS container agent injects an environment variable into each container,
referred to as the _task metadata endpoint_ which provides
various task metadata and [Docker stats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats") to the container.

- Container introspection

The Amazon ECS container agent provides an API operation for gathering details about
the container instance on which the agent is running and the associated tasks
running on that instance.
