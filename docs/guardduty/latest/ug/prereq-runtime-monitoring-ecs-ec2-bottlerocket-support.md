# Prerequisites for ECS-EC2 Bottlerocket support

###### Important

This section applies only to _Bottlerocket ECS-optimized AMIs_
version `v1.62.1` and above, including the following variants:

- `bottlerocket-aws-ecs-2-x86_64` / `bottlerocket-aws-ecs-2-aarch64`
- `bottlerocket-aws-ecs-3-x86_64` / `bottlerocket-aws-ecs-3-aarch64`
- `bottlerocket-aws-ecs-2-nvidia` / `bottlerocket-aws-ecs-2-nvidia-fips`
- `bottlerocket-aws-ecs-3-nvidia` / `bottlerocket-aws-ecs-3-nvidia-fips`
  Runtime Monitoring extends GuardDuty's threat detection to your Bottlerocket Amazon EC2 instances in
  Amazon ECS clusters, using a security agent that runs as a host container to fit
  Bottlerocket's container-optimized design. To enable it, complete the prerequisites in
  this section. After these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

For more information about requirements and instructions, see [Managing GuardDuty security agent on Bottlerocket (Amazon ECS on Amazon EC2)](managing-gdu-agent-bottlerocket-ecs-ec2.md "managing-gdu-agent-bottlerocket-ecs-ec2.md").

###### Topics

- [Make EC2 instances SSM managed and configure instance permissions](#ssm-managed-prereq-bottlerocket "#ssm-managed-prereq-bottlerocket")
- [Validating architectural requirements](#validating-architecture-req-bottlerocket "#validating-architecture-req-bottlerocket")
- [Network connectivity requirements](#network-connectivity-prereq-bottlerocket "#network-connectivity-prereq-bottlerocket")
- [Validating your organization service control policy in a multi-account environment](#validate-organization-scp-bottlerocket "#validate-organization-scp-bottlerocket")
- [When using automated agent configuration](#runtime-bottlerocket-prereq-automated-agent-config "#runtime-bottlerocket-prereq-automated-agent-config")
- [CPU and memory limit for GuardDuty agent](#bottlerocket-prereq-cpu-memory-limits "#bottlerocket-prereq-cpu-memory-limits")
- [Next step](#next-step-after-prereq-bottlerocket "#next-step-after-prereq-bottlerocket")

## Make EC2 instances SSM managed and configure instance permissions

GuardDuty uses AWS Systems Manager (SSM) to deploy, install, and manage the security agent
on your Bottlerocket instances, running through the SSM agent in the Bottlerocket control
container.

In most cases, the permissions your instances already have for Bottlerocket also cover
GuardDuty. No additional policies are needed. The `AmazonEC2ContainerRegistryReadOnly`
policy that Bottlerocket uses to pull its control and admin container images also satisfies
GuardDuty's requirement to pull the agent container image. For more information, see the [Bottlerocket README](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#exploration "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#exploration").

The instance profile must include the following managed policies:

- `AmazonSSMManagedInstanceCore` – Required for the Bottlerocket control
  container to run the SSM agent. To manage your Amazon EC2 instances with Systems Manager, see [Setting up Systems Manager for
  Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_.
- `AmazonEC2ContainerRegistryReadOnly` – Required for pulling the
  GuardDuty agent container image from Amazon ECR. At minimum, the following permissions are
  required:

```
...
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
...
```

To further restrict the Amazon ECR permissions, you can add the Amazon ECR repository URI that hosts
the GuardDuty security agent for Amazon ECS-Amazon EC2 Bottlerocket. For more information, see [ECR repository for GuardDuty agent on ECS-EC2 Bottlerocket](ecs-ec2-bottlerocket-runtime-agent-ecr-image-uri.md "ecs-ec2-bottlerocket-runtime-agent-ecr-image-uri.md").

## Validating architectural requirements

The architecture of your instances determines how the GuardDuty security agent behaves.
Bottlerocket ECS-2 and ECS-3 variants meet these requirements out of the box. Confirm
the following before enabling Runtime Monitoring:

- Kernel support includes `eBPF`, `Tracepoints`, and
  `Kprobe`. Bottlerocket ECS-2 variants use kernel `6.1` and
  ECS-3 variants use kernel `6.12`. Both versions meet the kernel requirements
  for Runtime Monitoring. The `CONFIG_DEBUG_INFO_BTF=y` kernel option is enabled by
  default in Bottlerocket ECS-2 and ECS-3 kernels.
- For CPU architectures, Runtime Monitoring supports AMD64 (`x86_64`) and
  ARM64 (`aarch64`).

## Network connectivity requirements

GuardDuty hosts its security agent as a container image in Amazon ECR, so your instances need
network connectivity to Amazon ECR to pull it. Depending on your network configuration, choose
one of the following options:

**Option 1 - Using public network access (if available)**

If your Bottlerocket instances run in subnets with outbound internet access, no
additional network configuration is required.

**Option 2 - Using Amazon VPC endpoints (for private subnets)**

For Bottlerocket instances in private subnets, VPC endpoints provide the connectivity
the agent needs. Configure endpoints for Amazon ECR, Amazon S3, and Systems Manager so instances can
pull the agent image and communicate with Systems Manager for deployment.

For more information about configuring VPC endpoints, see [Create the
VPC endpoints for Amazon ECR](../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create "../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-vpc-create") in the _Amazon Elastic Container Registry User Guide_ and [Create
VPC endpoints](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md") in the _AWS Systems Manager User Guide_.

## Validating your organization service control policy in a multi-account environment

If you have set up a service control policy (SCP) to manage permissions in your
organization, validate that the permissions boundary allows the
`guardduty:SendSecurityTelemetry` action. GuardDuty requires this permission to support
Runtime Monitoring across different resource types.

If your account is a member account, contact the associated delegated administrator. For
information about managing SCPs for your organization, see [Service control policies
(SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").

## When using automated agent configuration

To use automated agent configuration, your AWS account must meet the
following prerequisites:

- When using inclusion tags with automated agent configuration, for GuardDuty to create an SSM
  association for a new instance, make sure that the new instance is SSM managed and shows up under
  **Fleet Manager** in the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/") console.
- When using exclusion tags with automated agent configuration:

  - Add the `GuardDutyManaged`:`false` tag to an Amazon EC2 instance
    before you launch it, and before you configure the GuardDuty automated agent for your
    account. After automated agent configuration is enabled, any instance that launches
    without an exclusion tag is covered automatically.
  - Enable **Allow tags in metadata** setting for your instances. This
    setting is required because GuardDuty needs to read the exclusion tag from the
    instance metadata service (IMDS) to determine whether it should exclude
    the instance from agent installation. For more information, see [Enable
    access to tags in instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS") in the _Amazon EC2 User Guide_.

## CPU and memory limit for GuardDuty agent

**CPU limit**

GuardDuty limits the security agent to 10 percent of the total vCPU capacity on the
instance. For example, on an instance with 4 vCPU cores, the agent can use at most
0.4 vCPU.

**Memory limit**

From the memory associated with your Amazon EC2 instance, there is a limit on the memory that the
GuardDuty security agent can use.

The following table shows the memory limit.

| Memory of the Amazon EC2 instance | Maximum memory for GuardDuty agent |
| --------------------------------- | ---------------------------------- |
| Less than 8 GB                    | 128 MB                             |
| 8 GB to less than 32 GB           | 256 MB                             |
| More than or equal to 32 GB       | 1 GB                               |

## Next step

Your next step is to configure Runtime Monitoring and manage the security agent
automatically.
