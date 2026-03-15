# Amazon ECS task definition differences for Amazon ECS Managed Instances

In order to use Amazon ECS Managed Instances, you must configure your task definition to use the
Amazon ECS Managed Instances launch type. There are additional considerations when using
Amazon ECS Managed Instances.

## Task definition parameters

Tasks that use Amazon ECS Managed Instances support most of the Amazon ECS task definition parameters
that are available. However, some parameters have specific behaviors or limitations when
used with Amazon ECS Managed Instances tasks.

The following task definition parameters are not valid in Amazon ECS Managed Instances
tasks:

- `disableNetworking`
- `dnsSearchDomains`
- `dnsServers`
- `dockerLabels`
- `dockerSecurityOptions`
- `dockerVolumeConfiguration`
- `ephemeralStorage`
- `extraHosts`
- `fsxWindowsFileServerVolumeConfiguration`
- `hostname`
- `inferenceAccelerator`
- `ipcMode`
- `links`
- `maxSwap`
- `proxyConfiguration`
- `sharedMemorySize`
- `sourcepath` volumes
- `swappiness`
- `tmpfs`

The following task definition parameters are valid in Amazon ECS Managed Instances tasks, but
have limitations that should be noted:

- `networkConfiguration` - Amazon ECS Managed Instances tasks use the
  `awsvpc` or `host` network mode.
- `placementConstraints` - The following constraint attributes are
  supported.
  - `ecs.subnet-id`
  - `ecs.availability-zone`
  - `ecs.instance-type`
  - `ecs.cpu-architecture`

- `requiresCompatibilities` - Must include
  `MANAGED_INSTANCES` to ensure the task definition is compatible
  with Amazon ECS Managed Instances.
- `resourceRequirement` - `InferenceAccelerator` is not
  supported.
- `operatingSystemFamily` - Amazon ECS Managed Instances use `LINUX`.

To ensure that your task definition validates for use with Amazon ECS Managed Instances, you can
specify the following when you register the task definition:

- In the AWS Management Console, for the **Requires Compatibilities** field,
  specify `MANAGED_INSTANCES`.
- In the AWS CLI, specify the `--requires-compatibilities`
  option.
- In the Amazon ECS API, specify the `requiresCompatibilities`
  flag.
