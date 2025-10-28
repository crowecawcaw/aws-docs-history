# Amazon ECS task definition differences for EC2 instances running Windows

Tasks that run on EC2 Windows instances don't support all of the Amazon ECS task
definition parameters that are available. Some parameters aren't supported at all,
and others behave differently.

The following task definition parameters aren't supported for Amazon EC2 Windows task
definitions:

- `containerDefinitions`
  - `disableNetworking`
  - `dnsServers`
  - `dnsSearchDomains`
  - `extraHosts`
  - `links`
  - `linuxParameters`
  - `privileged`
  - `readonlyRootFilesystem`
  - `user`
  - `ulimits`

- `volumes`
  - `dockerVolumeConfiguration`

- `cpu`

We recommend specifying container-level CPU for Windows containers.

- `memory`

We recommend specifying container-level memory for Windows containers.

- `proxyConfiguration`
- `ipcMode`
- `pidMode`
- `taskRoleArn`

The IAM roles for tasks on EC2 Windows instances features requires additional
configuration, but much of this configuration is similar to configuring
IAM roles for tasks on Linux container instances. For more information see
[Amazon EC2 Windows instance additional configuration](task-iam-roles.md#windows_task_IAM_roles "task-iam-roles.md#windows_task_IAM_roles").
