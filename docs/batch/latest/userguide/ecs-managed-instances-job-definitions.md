# Job definitions on Amazon ECS Managed Instances

AWS Batch jobs on Amazon ECS Managed Instances use the `ecsProperties` job definition
format with a platform capability of `MANAGED_INSTANCES`. Amazon ECS Managed Instances
jobs do not support legacy `containerProperties`.

The following list describes job definition parameters that are specific to or restricted
for Amazon ECS Managed Instances jobs.

`platformCapabilities`

Must be specified as `MANAGED_INSTANCES`.

```
"platformCapabilities": [ "MANAGED_INSTANCES" ]
```

`type`

Must be specified as `container`.

```
"type": "container"
```

Parameters in `ecsProperties`

`networkMode`

Controls how the task's network is configured. This parameter only applies to Amazon ECS
Managed Instances job definitions. This parameter does not apply to Fargate or Amazon EC2
platform job definitions.

Valid values: `host`

When not specified, the default is `host`. With `host` mode,
the container shares the host instance's network stack directly, providing maximum network
bandwidth.

```
"networkMode": "host"
```

`runtimePlatform`

Specifies the operating system family and CPU architecture for the task. Use this
to run jobs on ARM64 (Graviton) instances. The valid value for
`operatingSystemFamily` is `LINUX` (default). The valid values for
`cpuArchitecture` are `X86_64` and `ARM64`.

```
"runtimePlatform": {
  "operatingSystemFamily": "LINUX",
  "cpuArchitecture": "ARM64"
}
```

`executionRoleArn`

The IAM role that grants the Amazon ECS container agent permission to make AWS API
calls on your behalf, such as pulling container images from Amazon ECR. For more information,
see [IAM Roles for Tasks](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the
_Amazon Elastic Container Service Developer Guide_.

`resourceRequirements`

Both memory and vCPU requirements must be specified in
`resourceRequirements`. Unlike Fargate, Amazon ECS Managed Instances does not
restrict which vCPU and memory combinations are valid — you can specify any values that
fit within the instance types available to your compute environment. GPU resources are
supported.

```
"resourceRequirements": [
  {"type": "MEMORY", "value": "8192"},
  {"type": "VCPU", "value": "4"},
  {"type": "GPU", "value": "1"}
]
```

Parameters supported on Amazon ECS Managed Instances but not Fargate

The following parameters are available for Amazon ECS Managed Instances jobs but are
blocked for Fargate:

- `privileged` — run the container with elevated privileges on the host
  instance.
- `resourceRequirements` type `GPU` — request NVIDIA GPU
  devices.
- `linuxParameters.devices` — expose host devices to the
  container.
- `linuxParameters.tmpfs` — mount RAM-backed tmpfs filesystems.
- `ulimits` — set resource limits (nofile, nproc, etc.) on the
  container.
- `volumes` with `host.sourcePath` — bind mount host paths
  into the container.

Parameters not supported on Amazon ECS Managed Instances

`fargatePlatformConfiguration`

Not applicable for Amazon ECS Managed Instances jobs.

Multi-node parallel (MNP) jobs

Amazon ECS Managed Instances does not support multi-node parallel jobs. Use Amazon EC2
managed compute environments for MNP workloads.

Parameters in `logConfiguration`

`logDriver`

Only `awslogs`, `splunk`, and `awsfirelens`
are supported for Amazon ECS Managed Instances jobs.
