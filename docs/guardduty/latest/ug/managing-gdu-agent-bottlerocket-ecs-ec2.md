# Managing GuardDuty security agent on Bottlerocket (Amazon ECS on Amazon EC2)

###### Important

This page applies only to _Bottlerocket ECS-optimized AMIs_
version `v1.62.1` and later, including the following variants:

- `bottlerocket-aws-ecs-2-x86_64` / `bottlerocket-aws-ecs-2-aarch64`
- `bottlerocket-aws-ecs-3-x86_64` / `bottlerocket-aws-ecs-3-aarch64`
- `bottlerocket-aws-ecs-2-nvidia` / `bottlerocket-aws-ecs-2-nvidia-fips`
- `bottlerocket-aws-ecs-3-nvidia` / `bottlerocket-aws-ecs-3-nvidia-fips`
  For Bottlerocket instances in Amazon EKS clusters, Runtime Monitoring uses a different
  setup. See [Prerequisites for Amazon EKS cluster support](prereq-runtime-monitoring-eks-support.md "prereq-runtime-monitoring-eks-support.md").

This page explains how the GuardDuty security agent runs on Bottlerocket ECS-optimized AMIs
and how GuardDuty deploys it. On Bottlerocket, the agent runs as a
_host container_ rather than as an installed RPM or
Debian package. Bottlerocket is a container-optimized Linux OS with an
immutable root filesystem, so it doesn't use traditional package managers.
GuardDuty hosts the agent container image in an Amazon Elastic Container Registry (Amazon ECR) repository it manages,
and when you enable Runtime Monitoring with automated agent configuration, GuardDuty uses
AWS Systems Manager Distributor to deploy the agent host container for you.

## Prerequisites

Before you continue, make sure to follow all the [Prerequisites for ECS-EC2 Bottlerocket support](prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md "prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md").

## Enabling automated agent configuration

Bottlerocket ECS-EC2 instances use the same SSM document and automated agent
configuration as standard Amazon EC2 instances. To enable the GuardDuty automated agent
for your Bottlerocket instances, follow the steps in [Automated agent on Amazon EC2
resource](managing-gdu-agent-ec2-automated.md "managing-gdu-agent-ec2-automated.md"). This includes:

- Enabling GuardDuty agent in a multi-account environment.
- Enabling GuardDuty automated agent in a standalone account.

For additional prerequisites when using inclusion or exclusion tags, see [When using automated agent configuration](prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md#runtime-bottlerocket-prereq-automated-agent-config "prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md#runtime-bottlerocket-prereq-automated-agent-config").

## Verifying the agent

After enabling automated agent configuration, verify the agent is running on your
Bottlerocket instance:

1. Connect to your instance using SSM Session Manager.
2. Enter the admin container: `enter-admin-container`.
3. Check agent logs using one of the following:

   - `sheltie journalctl -u host-containers@amazon-guardduty-agent`
   - From a sheltie session (`sudo sheltie`): `ls /var/log/amzn-guardduty-agent/`.

For information about reviewing coverage statistics for your Amazon EC2 instances, see
[Reviewing coverage statistics](gdu-assess-coverage-ec2.md#review-coverage-statistics-ec2-runtime-monitoring "gdu-assess-coverage-ec2.md#review-coverage-statistics-ec2-runtime-monitoring").

If the coverage status appears as **Unhealthy**, see [Troubleshooting Bottlerocket ECS-EC2 runtime coverage issues](gdu-assess-coverage-bottlerocket-ecs-ec2.md#bottlerocket-ecs-ec2-coverage-issues-troubleshoot "gdu-assess-coverage-bottlerocket-ecs-ec2.md#bottlerocket-ecs-ec2-coverage-issues-troubleshoot").
