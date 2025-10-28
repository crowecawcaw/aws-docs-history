# Amazon ECS-optimized Bottlerocket AMIs

Bottlerocket is a Linux based open-source operating system
that is purpose built by AWS for running containers on virtual machines or bare metal
hosts. The Amazon ECS-optimized Bottlerocket AMI is secure and only includes the
minimum number of packages that's required to run containers. This improves resource usage,
reduces security attack surface, and helps lower management overhead. The
Bottlerocket AMI is also integrated with Amazon ECS to help reduce the
operational overhead involved in updating container instances in a cluster.

Bottlerocket differs from Amazon Linux in the following ways:

- Bottlerocket doesn't include a package manager, and its software
  can only be run as containers. Updates to Bottlerocket are both
  applied and can be rolled back in a single step, which reduces the likelihood of
  update errors.
- The primary mechanism to manage Bottlerocket hosts is with a
  container scheduler. Unlike Amazon Linux, logging into individual
  Bottlerocket instances is intended to be an infrequent operation
  for advanced debugging and troubleshooting purposes only.
  For more information about Bottlerocket, see the [documentation](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md") and [releases](https://github.com/bottlerocket-os/bottlerocket/releases "https://github.com/bottlerocket-os/bottlerocket/releases") on
  GitHub.

There are variants of the Amazon ECS-optimized Bottlerocket AMI for kernel 6.1
and kernel 5.10.

The following variants use kernel 6.1:

- `aws-ecs-2`
- `aws-ecs-2-nvidia`
  The following variants use kernel 5.10:

- `aws-ecs-1`
- `aws-ecs-1-nvidia`

For more information about the `aws-ecs-1-nvidia` variant, see
[Announcing NVIDIA GPU support for Bottlerocket on
Amazon ECS](https://aws.amazon.com/blogs/containers/announcing-nvidia-gpu-support-for-bottlerocket-on-amazon-ecs/ "https://aws.amazon.com/blogs/containers/announcing-nvidia-gpu-support-for-bottlerocket-on-amazon-ecs/").

## Considerations

Consider the following when using a Bottlerocket AMI with
Amazon ECS.

- Bottlerocket supports Amazon EC2 instances with `x86_64`
  and `arm64` processors. The Bottlerocket AMI isn't
  recommended for use with Amazon EC2 instances with an Inferentia chip.
- Bottlerocket images don't include an SSH server or a shell.
  However, you can use out-of-band management tools to gain SSH administrator
  access and perform bootstrapping.

For more information, see these sections in
the [bottlerocket
README.md](https://github.com/bottlerocket-os/bottlerocket "https://github.com/bottlerocket-os/bottlerocket") on GitHub:

    + [Exploration](https://github.com/bottlerocket-os/bottlerocket#exploration "https://github.com/bottlerocket-os/bottlerocket#exploration")
    + [Admin container](https://github.com/bottlerocket-os/bottlerocket#admin-container "https://github.com/bottlerocket-os/bottlerocket#admin-container")

- By default, Bottlerocket has a [control container](https://github.com/bottlerocket-os/bottlerocket-control-container "https://github.com/bottlerocket-os/bottlerocket-control-container") that's enabled. This container runs the [AWS Systems Manager agent](https://github.com/aws/amazon-ssm-agent "https://github.com/aws/amazon-ssm-agent") that
  you can use to run commands or start shell sessions on Amazon EC2
  Bottlerocket instances. For more information, see [Setting up Session Manager](../../../systems-manager/latest/userguide/session-manager-getting-started.md "../../../systems-manager/latest/userguide/session-manager-getting-started.md") in the
  _AWS Systems Manager User Guide_.

- Bottlerocket is optimized for container workloads and has a focus on security.
  Bottlerocket doesn't include a package manager and is immutable.

For information
about the security features and guidance, see [Security Features](https://github.com/bottlerocket-os/bottlerocket/blob/develop/SECURITY_FEATURES.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/SECURITY_FEATURES.md") and [Security Guidance](https://github.com/bottlerocket-os/bottlerocket/blob/develop/SECURITY_GUIDANCE.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/SECURITY_GUIDANCE.md") on GitHub.

- The `awsvpc` network mode is supported for Bottlerocket AMI
  version `1.1.0` or later.
- App Mesh in a task definition is supported for Bottlerocket AMI version
  `1.15.0` or later.
- The `initProcessEnabled` task definition parameter is supported for
  Bottlerocket AMI version `1.19.0` or later.
- The Bottlerocket AMIs also don't support the following services
  and features:
  - ECS Anywhere
  - Service Connect
  - Amazon EFS in encrypted mode
  - Amazon EFS in `awsvpc` network mode
  - Amazon EBS volumes can't be mounted
  - Elastic Inference Accelerator
